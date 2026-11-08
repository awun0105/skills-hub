#!/usr/bin/env python3
"""Validate curriculum DAG and optional learner-state consistency.

Structural checks ONLY. This tool does not validate scientific truth, teaching quality,
source access, real learner proficiency, or authenticity of evidence notes.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

COVERAGE = {"not_started", "in_progress", "completed", "needs_review"}
PROFICIENCY = {"unassessed", "attempted", "needs_review", "demonstrated"}
KINDS = {"CORE", "OPTIONAL", "RESEARCH_FRONTIER"}


def present(s):
    return isinstance(s, str) and bool(s.strip())


def nonempty_strings(value):
    return isinstance(value, list) and bool(value) and all(present(x) for x in value)


def audit_curriculum(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["curriculum must be a JSON object"], warnings
    for k in ("curriculum_id", "version", "title", "goal", "scope"):
        if not present(data.get(k)):
            errors.append(f"{k}: non-empty string required")
    policy = data.get("delivery_policy", {})
    if not isinstance(policy, dict):
        errors.append("delivery_policy: object required")
    elif policy.get("lessons_per_turn") != 1:
        warnings.append("delivery_policy.lessons_per_turn differs from recommended one-lesson default")
    lessons = data.get("lessons")
    if not isinstance(lessons, list) or not lessons:
        return errors + ["lessons: non-empty array required"], warnings

    seen = {}
    for i, lesson in enumerate(lessons):
        path = f"lessons[{i}]"
        if not isinstance(lesson, dict):
            errors.append(f"{path}: object required")
            continue
        lid = lesson.get("id")
        if not present(lid):
            errors.append(f"{path}.id: stable nonempty ID required")
        elif lid in seen:
            errors.append(f"{path}.id: duplicate {lid}")
        else:
            seen[lid] = i
        for field in ("unit", "title"):
            if not present(lesson.get(field)):
                errors.append(f"{path}.{field}: nonempty string required")
        for field in ("learning_objectives", "assessment_plan", "verification_plan"):
            if not nonempty_strings(lesson.get(field)):
                errors.append(f"{path}.{field}: nonempty array of nonempty strings required")
        if not isinstance(lesson.get("prerequisites"), list):
            errors.append(f"{path}.prerequisites: array required")
        if lesson.get("status") not in COVERAGE:
            errors.append(f"{path}.status: invalid coverage")
        if lesson.get("kind") not in KINDS:
            errors.append(f"{path}.kind: must be CORE, OPTIONAL or RESEARCH_FRONTIER")

    graph = {}
    for i, lesson in enumerate(lessons):
        if not isinstance(lesson, dict) or not present(lesson.get("id")):
            continue
        lid = lesson["id"]
        deps = lesson.get("prerequisites", [])
        if not isinstance(deps, list):
            continue
        valid_deps = []
        for dep in deps:
            if not present(dep):
                errors.append(f"{lid}: prerequisite must be nonempty string")
            elif dep == lid:
                errors.append(f"{lid}: self dependency")
            elif dep not in seen:
                errors.append(f"{lid}: unknown prerequisite {dep}")
            else:
                valid_deps.append(dep)
                if seen[dep] >= i:
                    errors.append(f"{lid}: prerequisite {dep} must appear earlier in lesson order")
        if len(valid_deps) != len(set(valid_deps)):
            errors.append(f"{lid}: duplicate prerequisites")
        graph[lid] = valid_deps

    color = {}
    def visit(node, chain):
        if color.get(node) == 1:
            errors.append("prerequisite cycle: " + " -> ".join(chain + [node]))
            return
        if color.get(node) == 2:
            return
        color[node] = 1
        for dep in graph.get(node, []):
            visit(dep, chain + [node])
        color[node] = 2
    for node in graph:
        if color.get(node) is None:
            visit(node, [])

    for lesson in lessons:
        if not isinstance(lesson, dict) or not present(lesson.get("id")):
            continue
        if lesson.get("status") == "completed":
            for dep in graph.get(lesson["id"], []):
                d = lessons[seen[dep]]
                if isinstance(d, dict) and d.get("status") in ("not_started", "needs_review"):
                    warnings.append(f"{lesson['id']}: completed with prerequisite {dep} marked {d['status']}; document test-out or correction")
    return errors, warnings


def audit_state(state, curriculum):
    errors, warnings = [], []
    if not isinstance(state, dict):
        return ["learner state must be a JSON object"], warnings
    if state.get("curriculum_id") != curriculum.get("curriculum_id"):
        errors.append("state.curriculum_id differs from curriculum")
    if state.get("curriculum_version") != curriculum.get("version"):
        warnings.append("state.curriculum_version differs from curriculum; reconcile revision")
    lessons = {x["id"]: x for x in curriculum.get("lessons", []) if isinstance(x, dict) and present(x.get("id"))}
    progress = state.get("lessons")
    if not isinstance(progress, dict):
        return ["state.lessons: object required"], warnings
    for lid, info in progress.items():
        if lid not in lessons:
            errors.append(f"state.lessons.{lid}: unknown lesson")
            continue
        if not isinstance(info, dict):
            errors.append(f"state.lessons.{lid}: object required")
            continue
        if info.get("coverage") not in COVERAGE:
            errors.append(f"state.lessons.{lid}.coverage: invalid")
        objectives = info.get("objectives")
        expected_count = len(lessons[lid].get("learning_objectives", []))
        if not isinstance(objectives, list) or len(objectives) != expected_count:
            errors.append(f"state.lessons.{lid}.objectives: expected {expected_count} entries")
            continue
        indices = []
        for i, ob in enumerate(objectives):
            path = f"state.lessons.{lid}.objectives[{i}]"
            if not isinstance(ob, dict):
                errors.append(f"{path}: object required")
                continue
            indices.append(ob.get("objective_index"))
            level = ob.get("proficiency")
            if level not in PROFICIENCY:
                errors.append(f"{path}.proficiency: invalid")
            evidence = ob.get("observed_evidence")
            if not isinstance(evidence, list) or not all(present(x) for x in evidence):
                errors.append(f"{path}.observed_evidence: array of strings required")
            elif level == "demonstrated" and not evidence:
                errors.append(f"{path}: demonstrated proficiency requires observed evidence")
            if level in {"attempted", "needs_review"} and not evidence:
                warnings.append(f"{path}: {level} without recorded observation")
        if sorted(x for x in indices if isinstance(x, int)) != list(range(expected_count)):
            errors.append(f"state.lessons.{lid}.objectives: each objective_index must appear once (0..{expected_count - 1})")
        if info.get("coverage") == "not_started" and any(
                isinstance(o, dict) and o.get("proficiency") == "demonstrated" for o in objectives):
            warnings.append(f"state.lessons.{lid}: demonstrated despite not_started; document test-out")
        if info.get("coverage") != lessons[lid].get("status"):
            warnings.append(f"state.lessons.{lid}: coverage differs from curriculum status; reconcile state")
    for lid in lessons:
        if lid not in progress:
            warnings.append(f"state.lessons: {lid} has no progress record")
    for key in ("last_delivered_lesson_id", "next_lesson_id"):
        value = state.get(key)
        if value is not None and value not in lessons:
            errors.append(f"state.{key}: unknown lesson {value}")
    return errors, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("curriculum", type=pathlib.Path)
    parser.add_argument("--state", type=pathlib.Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        curriculum = json.loads(args.curriculum.read_text(encoding="utf-8"))
        state = json.loads(args.state.read_text(encoding="utf-8")) if args.state else None
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot load input: {exc}", file=sys.stderr)
        return 2
    errors, warnings = audit_curriculum(curriculum)
    if state is not None:
        e, w = audit_state(state, curriculum)
        errors += e
        warnings += w
    result = {"schema_check": "FAIL" if errors else "PASS", "errors": errors, "warnings": warnings,
              "disclaimer": "Structure only: does not prove mastery, scientific validity, source authenticity, or tests executed."}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"CURRICULUM {result['schema_check']} | errors={len(errors)} warnings={len(warnings)}")
        for x in errors:
            print("ERROR:", x)
        for x in warnings:
            print("WARNING:", x)
        print(result["disclaimer"])
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())

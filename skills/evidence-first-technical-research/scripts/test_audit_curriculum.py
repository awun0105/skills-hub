#!/usr/bin/env python3
"""Regression tests for structural curriculum and learner-state checks."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from audit_curriculum import audit_curriculum, audit_state  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]


class CurriculumTests(unittest.TestCase):
    def setUp(self):
        self.plan = json.loads((ROOT / "assets/curriculum.template.json").read_text(encoding="utf-8"))
        self.state = json.loads((ROOT / "assets/learner-state.template.json").read_text(encoding="utf-8"))

    def test_template_valid(self):
        self.assertEqual(audit_curriculum(self.plan)[0], [])
        self.assertEqual(audit_state(self.state, self.plan)[0], [])

    def test_duplicate_id(self):
        p = copy.deepcopy(self.plan)
        p["lessons"][1]["id"] = "L01"
        e, _ = audit_curriculum(p)
        self.assertTrue(any("duplicate" in x for x in e))

    def test_unknown_dependency(self):
        p = copy.deepcopy(self.plan)
        p["lessons"][1]["prerequisites"] = ["ABSENT"]
        e, _ = audit_curriculum(p)
        self.assertTrue(any("unknown prerequisite" in x for x in e))

    def test_cycle(self):
        p = copy.deepcopy(self.plan)
        p["lessons"][0]["prerequisites"] = ["L02"]
        e, _ = audit_curriculum(p)
        self.assertTrue(any("cycle" in x for x in e))

    def test_missing_objectives(self):
        p = copy.deepcopy(self.plan)
        p["lessons"][0]["learning_objectives"] = []
        e, _ = audit_curriculum(p)
        self.assertTrue(any("learning_objectives" in x for x in e))

    def test_invalid_assessment(self):
        p = copy.deepcopy(self.plan)
        p["lessons"][0]["assessment_plan"] = [""]
        e, _ = audit_curriculum(p)
        self.assertTrue(any("assessment_plan" in x for x in e))

    def test_mastery_requires_observed_evidence(self):
        s = copy.deepcopy(self.state)
        s["lessons"]["L01"]["objectives"][0]["proficiency"] = "demonstrated"
        e, _ = audit_state(s, self.plan)
        self.assertTrue(any("requires observed evidence" in x for x in e))

    def test_mastery_with_observed_evidence_schema_passes(self):
        s = copy.deepcopy(self.state)
        s["lessons"]["L01"]["objectives"][0]["proficiency"] = "demonstrated"
        s["lessons"]["L01"]["objectives"][0]["observed_evidence"] = ["Learner solved check in transcript line X"]
        e, w = audit_state(s, self.plan)
        self.assertEqual(e, [])
        self.assertTrue(any("test-out" in x for x in w))

    def test_version_drift_warned(self):
        s = copy.deepcopy(self.state)
        s["curriculum_version"] = "0.0.1"
        e, w = audit_state(s, self.plan)
        self.assertEqual(e, [])
        self.assertTrue(any("reconcile revision" in x for x in w))

    def test_missing_state_lesson_warned(self):
        s = copy.deepcopy(self.state)
        del s["lessons"]["L02"]
        e, w = audit_state(s, self.plan)
        self.assertEqual(e, [])
        self.assertTrue(any("no progress record" in x for x in w))

    def test_progress_not_mastery(self):
        s = copy.deepcopy(self.state)
        s["lessons"]["L01"]["coverage"] = "completed"
        e, _ = audit_state(s, self.plan)
        self.assertEqual(e, [])
        self.assertEqual(s["lessons"]["L01"]["objectives"][0]["proficiency"], "unassessed")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Validate structure and internal consistency of a research claim ledger.

This does NOT access sources, verify truth, check URLs are reachable, or prove that
an agent actually inspected any source. It detects missing/invalid metadata only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
from urllib.parse import urlparse

STATUSES = {"VERIFIED", "DERIVED", "SIMPLIFIED", "INFERENCE", "UNVERIFIED", "CONTRADICTED"}
SOURCE_KINDS = {
    "paper", "preprint", "supplement", "official_code", "third_party_code",
    "official_docs", "dataset", "benchmark", "test_run", "survey", "other",
}
ACCESS_LEVELS = {"full_text", "section", "full_code", "documentation", "test_run", "abstract_only", "snippet_only", "metadata_only"}
STRONG_ACCESS = {"full_text", "section", "full_code", "documentation", "test_run"}
PLACEHOLDER = re.compile(r"(REPLACE_WITH|\[TODO\]|\bTBD\b)", re.IGNORECASE)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def check_date(value, path, errors):
    if not nonempty(value):
        errors.append(f"{path}: required YYYY-MM-DD date")
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError:
        errors.append(f"{path}: invalid YYYY-MM-DD date: {value!r}")
        return None


def audit(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["top-level JSON must be an object"], warnings
    for field in ("task", "research_question"):
        if not nonempty(data.get(field)):
            errors.append(f"{field}: non-empty text required")
    as_of = check_date(data.get("as_of"), "as_of", errors)

    sources = data.get("sources")
    claims = data.get("claims")
    if not isinstance(sources, list):
        errors.append("sources must be an array")
        sources = []
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty array")
        claims = []
    by_id = {}
    for i, source in enumerate(sources):
        loc = f"sources[{i}]"
        if not isinstance(source, dict):
            errors.append(f"{loc}: must be an object")
            continue
        sid = source.get("id")
        if not nonempty(sid):
            errors.append(f"{loc}.id: required")
        elif sid in by_id:
            errors.append(f"{loc}.id: duplicate {sid}")
        else:
            by_id[sid] = source
        for name in ("title", "url", "access_level"):
            if not nonempty(source.get(name)):
                errors.append(f"{loc}.{name}: required")
        if source.get("kind") not in SOURCE_KINDS:
            errors.append(f"{loc}.kind: unknown kind {source.get('kind')!r}")
        if source.get("access_level") not in ACCESS_LEVELS:
            errors.append(f"{loc}.access_level: unknown value")
        url = source.get("url", "")
        if nonempty(url):
            parsed = urlparse(url)
            if parsed.scheme not in ("https", "http") or not parsed.netloc:
                errors.append(f"{loc}.url: expected absolute HTTP(S) URL")
        inspected_at = source.get("inspected_at")
        if inspected_at:
            date = check_date(inspected_at, f"{loc}.inspected_at", errors)
            if date and as_of and date > as_of:
                warnings.append(f"{loc}: inspected_at after as_of cutoff; check intended cutoff semantics")
        if source.get("kind") in {"official_code", "third_party_code"}:
            if not nonempty(source.get("revision")):
                warnings.append(f"{loc}: code source has no pinned revision")
            elif PLACEHOLDER.search(source["revision"]):
                warnings.append(f"{loc}: revision is a placeholder, not a pinned commit")

    claim_ids = set()
    for i, claim in enumerate(claims):
        loc = f"claims[{i}]"
        if not isinstance(claim, dict):
            errors.append(f"{loc}: must be an object")
            continue
        cid = claim.get("id")
        if not nonempty(cid):
            errors.append(f"{loc}.id: required")
        elif cid in claim_ids:
            errors.append(f"{loc}.id: duplicate {cid}")
        else:
            claim_ids.add(cid)
        body = claim.get("claim")
        if not nonempty(body):
            errors.append(f"{loc}.claim: non-empty text required")
        status = claim.get("status")
        if status not in STATUSES:
            errors.append(f"{loc}.status: invalid status {status!r}")
        evidence = claim.get("evidence", [])
        if not isinstance(evidence, list):
            errors.append(f"{loc}.evidence: must be an array")
            evidence = []
        if status in {"VERIFIED", "CONTRADICTED"} and not evidence:
            errors.append(f"{loc}: {status} requires at least one inspected source locator")
        if status == "CONTRADICTED" and len(evidence) < 2:
            warnings.append(f"{loc}: conflict generally needs at least two conflicting evidence items")
        if status == "DERIVED" and not nonempty(claim.get("derivation")):
            errors.append(f"{loc}: DERIVED requires derivation")
        if status == "SIMPLIFIED" and not nonempty(claim.get("simplification_note")):
            errors.append(f"{loc}: SIMPLIFIED requires simplification_note")
        if status == "INFERENCE" and not nonempty(claim.get("rationale")):
            errors.append(f"{loc}: INFERENCE requires rationale")
        if status == "UNVERIFIED" and not claim.get("verification_actions"):
            warnings.append(f"{loc}: UNVERIFIED has no proposed verification action")
        if status != "UNVERIFIED" and nonempty(body) and PLACEHOLDER.search(body):
            errors.append(f"{loc}: a non-UNVERIFIED claim contains placeholder text")
        for j, item in enumerate(evidence):
            at = f"{loc}.evidence[{j}]"
            if not isinstance(item, dict):
                errors.append(f"{at}: evidence entry must be an object")
                continue
            sid = item.get("source_id")
            if sid not in by_id:
                errors.append(f"{at}.source_id: unknown source {sid!r}")
                continue
            source = by_id[sid]
            locator = item.get("locator") or source.get("locator")
            if not nonempty(locator):
                errors.append(f"{at}: specific page/section/equation/path/function locator required")
            if not nonempty(item.get("observation")):
                errors.append(f"{at}.observation: required; say what was actually seen")
            if status in {"VERIFIED", "CONTRADICTED"}:
                if source.get("access_level") not in STRONG_ACCESS:
                    errors.append(f"{at}: {status} cannot rely on abstract/snippet/metadata-only evidence")
                if not source.get("inspected_at"):
                    errors.append(f"{at}: {status} requires a source inspected_at date")
                if source.get("kind") in {"official_code", "third_party_code"}:
                    revision = source.get("revision")
                    if not nonempty(revision) or PLACEHOLDER.search(revision):
                        errors.append(f"{at}: code evidence requires a real pinned revision")
    if not sources:
        warnings.append("No sources: all facts should be visibly qualified as unverified or derived")
    if not isinstance(data.get("checks_performed"), list):
        warnings.append("checks_performed should list only checks actually run")
    return errors, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", type=pathlib.Path, help="Path to JSON claim ledger")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON")
    args = parser.parse_args(argv)
    try:
        data = json.loads(args.ledger.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Unable to read ledger: {exc}", file=sys.stderr)
        return 2
    errors, warnings = audit(data)
    result = {"schema_check": "FAIL" if errors else "PASS", "errors": errors, "warnings": warnings,
              "disclaimer": "Schema-only audit; cannot validate source authenticity or claim truth."}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"SCHEMA {result['schema_check']} | errors={len(errors)} warnings={len(warnings)}")
        for error in errors:
            print("ERROR:", error)
        for warning in warnings:
            print("WARNING:", warning)
        print(result["disclaimer"])
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

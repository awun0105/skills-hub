#!/usr/bin/env python3
"""Regression tests for ledger structure checks; no external dependencies."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from audit_claims import audit  # noqa: E402


class AuditTests(unittest.TestCase):
    def setUp(self):
        self.template = json.loads((pathlib.Path(__file__).resolve().parents[1]
                                    / "assets" / "claim-ledger.template.json").read_text())

    def test_unverified_template_allowed(self):
        errors, warnings = audit(self.template)
        self.assertEqual(errors, [])
        self.assertTrue(any("placeholder" in w for w in warnings))

    def verified_ledger(self):
        data = copy.deepcopy(self.template)
        data["sources"][0]["revision"] = "abc123def456"
        data["claims"][0]["claim"] = "The inspected function checks max scale"
        data["claims"][0]["status"] = "VERIFIED"
        data["claims"][0]["evidence"] = [{"source_id": "S1", "locator": "scene/gaussian_model.py:densify_and_clone",
                                            "observation": "Condition compares max scale with threshold"}]
        return data

    def test_valid_verified_claim(self):
        errors, warnings = audit(self.verified_ledger())
        self.assertEqual(errors, [])

    def test_unknown_evidence_rejected(self):
        d = self.verified_ledger()
        d["claims"][0]["evidence"][0]["source_id"] = "MADE_UP"
        errors, _ = audit(d)
        self.assertTrue(any("unknown source" in x for x in errors))

    def test_abstract_not_sufficient(self):
        d = self.verified_ledger()
        d["sources"][0]["access_level"] = "abstract_only"
        errors, _ = audit(d)
        self.assertTrue(any("abstract/snippet" in x for x in errors))

    def test_unpinned_code_cannot_be_verified(self):
        d = self.verified_ledger()
        d["sources"][0]["revision"] = "REPLACE_WITH_INSPECTED_COMMIT"
        errors, _ = audit(d)
        self.assertTrue(any("pinned revision" in x for x in errors))

    def test_derivation_must_be_explained(self):
        d = self.verified_ledger()
        d["claims"][0]["status"] = "DERIVED"
        errors, _ = audit(d)
        self.assertTrue(any("requires derivation" in x for x in errors))


if __name__ == "__main__":
    unittest.main()

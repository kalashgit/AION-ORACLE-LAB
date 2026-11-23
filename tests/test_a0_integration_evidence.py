import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "A0-INTEGRATION-EVIDENCE.md"

class IntegrationEvidenceGateTest(unittest.TestCase):
    def test_public_gate_has_complete_private_pr_lineage(self):
        content = DOC.read_text(encoding="utf-8")
        for number in (10, 11, 12, 13):
            with self.subTest(pr=number):
                self.assertIn(f"AION-GENESYS/pull/{number}", content)
        self.assertIn("REVIEW REQUIRED / NOT INTEGRATED", content)

    def test_gate_denies_premature_claims(self):
        content = DOC.read_text(encoding="utf-8")
        for term in ("not established", "no broker writes", "without merging", "held-out"):
            self.assertIn(term, content)

if __name__ == "__main__":
    unittest.main()

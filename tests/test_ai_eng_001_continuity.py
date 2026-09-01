from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from ai_workforce.ai_eng_001.continuity_probe import PASS_MARKER, run_continuity_probe


class TestAIEng001Continuity(unittest.TestCase):
    def test_failed_primary_can_be_replaced_without_authority_expansion(self):
        with tempfile.TemporaryDirectory() as td:
            result = run_continuity_probe(Path(td))

        self.assertEqual(result["status"], "PASS", result)
        self.assertEqual(result["marker"], PASS_MARKER)
        self.assertEqual(result["principal"], "AI-ENG-001")
        self.assertEqual(result["position"], "POS-004")
        self.assertFalse(result["automatic_failover"])
        self.assertFalse(result["authority_expanded"])
        self.assertEqual(result["primary"]["state"], "BLOCKED")
        self.assertEqual(
            result["primary"]["termination_reason"],
            "executor_nonzero_exit",
        )
        self.assertEqual(result["replacement"]["state"], "READY_FOR_OWNER")
        self.assertEqual(result["replacement"]["changed_paths"], ["continuity.txt"])
        self.assertTrue(all(result["invariants"].values()), result["invariants"])


if __name__ == "__main__":
    unittest.main()

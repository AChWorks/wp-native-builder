"""Negative probes for documentation-specific consistency constraints."""
from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from check_documentation import check, DOCS


class DocumentationContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in (*DOCS, "LICENSE"):
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, dest)
        shutil.copytree(ROOT / "references", self.root / "references")

    def mutate(self, name: str, *, find: str, replace: str) -> None:
        file = self.root / name
        original = file.read_text(encoding="utf-8")
        self.assertIn(find, original)
        file.write_text(original.replace(find, replace, 1), encoding="utf-8")

    def assert_rejected(self, name: str) -> None:
        with self.assertRaisesRegex(AssertionError, name):
            check(self.root, quiet=True)

    def test_valid_docs(self) -> None:
        self.assertGreater(check(self.root, quiet=True), 60)

    def test_broken_local_link_rejected(self) -> None:
        self.mutate("README.md", find="](MASTER-SPEC.md)", replace="](docs/missing-policy.md)")
        self.assert_rejected("broken or out-of-root link")

    def test_site_global_brief_rejected(self) -> None:
        self.mutate("docs/PROJECT-WORKSPACE-ARCHITECTURE.md",
                    find="per project, not per WordPress site", replace="per WordPress site")
        self.assert_rejected("no site-global Project Brief")

    def test_broad_plugin_author_rule_rejected(self) -> None:
        self.mutate("MASTER-SPEC.md",
                    find="existing/unrelated plugins", replace="all installed plugins")
        self.assert_rejected("Bridge-created plugin authorship")

    def test_verbatim_policy_duplication_rejected(self) -> None:
        rule = "The same long policy statement must never be copied into multiple maintained documents where one authoritative owner and a link would avoid future drift between the documents."
        for name in ("README.md", "MASTER-SPEC.md"):
            path = self.root / name
            path.write_text(path.read_text(encoding="utf-8") + "\n" + rule + "\n", encoding="utf-8")
        self.assert_rejected("duplicate long policy line")

    def test_behavior_case_duplicate_id_rejected(self) -> None:
        self.mutate("docs/BEHAVIOR-EVALS.md",
                    find="## CI. Synced Pattern with instance-level overrides",
                    replace="## CH. Synced Pattern with instance-level overrides")
        self.assert_rejected("unique behavior scenario IDs")


if __name__ == "__main__":
    unittest.main()

"""Verify deterministic seven-file packaging, excluding repository-only docs/tests."""
from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from package_candidate import package_candidate, RUNTIME


class PackageTests(unittest.TestCase):
    def test_reproducible_exact_runtime(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            a, b = Path(tmp) / "a.zip", Path(tmp) / "b.zip"
            first = package_candidate(ROOT, a)
            second = package_candidate(ROOT, b)
            self.assertEqual(first, second)
            self.assertEqual(a.read_bytes(), b.read_bytes())
            with zipfile.ZipFile(a) as zf:
                names = set(zf.namelist())
                self.assertEqual(names, {"wp-native-builder/" + path for path in RUNTIME})
                for path in RUNTIME:
                    self.assertEqual(zf.read("wp-native-builder/" + path), (ROOT / path).read_bytes())
                self.assertFalse(any("test" in name or "MASTER-SPEC" in name for name in names))


if __name__ == "__main__":
    unittest.main()

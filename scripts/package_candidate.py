#!/usr/bin/env python3
"""Build a deterministic, source-matched candidate skill.zip without releasing.

Standard skill-creator validation/packaging is still required for official releases.
"""
from __future__ import annotations

import hashlib
import sys
import zipfile
from pathlib import Path

from check_runtime_contract import validate

RUNTIME_REFS = (
    "references/design-conventions.md",
    "references/gutenberg-safety.md",
    "references/implementation-decisions.md",
    "references/project-workflow.md",
    "references/workspace-memory.md",
)
RUNTIME = ("SKILL.md", "agents/openai.yaml", *RUNTIME_REFS)
ZIP_LIMIT = 25 * 1024 * 1024


def package_candidate(root: Path, output: Path) -> str:
    root = Path(root).resolve()
    output = Path(output).resolve()
    validate(root, quiet=True)
    output.parent.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in RUNTIME:
            info = zipfile.ZipInfo(
                "wp-native-builder/" + path,
                date_time=(1980, 1, 1, 0, 0, 0),
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, (root / path).read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    if output.stat().st_size > ZIP_LIMIT:
        output.unlink()
        raise ValueError("Candidate ZIP exceeds 25 MiB")
    with zipfile.ZipFile(output) as zf:
        assert zf.testzip() is None
        assert set(zf.namelist()) == {"wp-native-builder/" + p for p in RUNTIME}
        for path in RUNTIME:
            assert zf.read("wp-native-builder/" + path) == (root / path).read_bytes()
    sha = hashlib.sha256(output.read_bytes()).hexdigest()
    return sha


if __name__ == "__main__":
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist/skill.zip")
    digest = package_candidate(root, out)
    print(f"PASS: {out} ({out.stat().st_size:,} bytes) sha256={digest}")

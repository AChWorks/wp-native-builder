#!/usr/bin/env python3
"""Smoke-test repository document links/ownership, not semantic or model behavior."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

DOCS = (
    "README.md",
    "MASTER-SPEC.md",
    "docs/architecture.md",
    "docs/PROJECT-WORKSPACE-ARCHITECTURE.md",
    "docs/BEHAVIOR-EVALS.md",
)
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)\s]+)(?:\s+[^)]*)?\)")
CASE = re.compile(r"^## ([A-Z]{1,2})\. ([^\n]+)", re.M)
BAD_PRESET = re.compile(r"(?i)\bpreferred defaults\s+(?:are|include)\s+(?:Astra|Gravity Forms|Code Snippets)")
BAD_BRIEF = re.compile(r"(?i)\bproject brief\s+(?:is\s+)?(?:singleton|unique|one)\s+per\s+(?:wordpress\s+)?site\b")


def check(root: Path, *, quiet: bool = False) -> int:
    root = Path(root).resolve()
    docs = {name: (root / name).read_text(encoding="utf-8") for name in DOCS}
    checks = 0

    def require(name: str, cond: bool) -> None:
        nonlocal checks
        if not cond:
            raise AssertionError(name)
        checks += 1

    for name, body in docs.items():
        require("nonempty document " + name, bool(body.strip()))
        require("no hardcoded vendor preset " + name, BAD_PRESET.search(body) is None)
        require("no site-global Project Brief " + name, BAD_BRIEF.search(body) is None)
        file = root / name
        for match in LINK.finditer(body):
            href = match.group(1)
            link = unquote(href).split("#", 1)[0].split("?", 1)[0]
            if not link or link.startswith(("https://", "http://", "mailto:")):
                continue
            target = (file.parent / link).resolve()
            require("broken or out-of-root link " + name + " -> " + href,
                    target.is_relative_to(root) and target.is_file())

    spec, readme = docs["MASTER-SPEC.md"], docs["README.md"]
    project = docs["docs/PROJECT-WORKSPACE-ARCHITECTURE.md"]
    evals = docs["docs/BEHAVIOR-EVALS.md"]
    require("spec Project Brief binds to distinct project",
            "per identified project, not per site" in spec)
    require("storage architecture Project Brief binds to project",
            "per project, not per WordPress site" in project)
    require("Bridge-created plugin authorship not global",
            "new bespoke plugin authored through the authorized Bridge workflow" in spec
            and "existing/unrelated plugins" in spec)
    require("README Bridge author only new plugin",
            "new bespoke plugin authored through Bridge" in readme
            and "other installed plugins" in readme)
    require("README links to canonical spec and architecture",
            "](MASTER-SPEC.md)" in readme and "](docs/architecture.md)" in readme)
    require("one rule-owner table only in architecture doc",
            "| Runtime source |" not in spec
            and "| Runtime source |" in docs["docs/architecture.md"])

    # Long verbatim policy-line copying is a useful drift smoke-check,
    # not a proof that distinct documents have no semantic overlap.
    seen: dict[str, str] = {}
    for name, body in docs.items():
        for raw in body.splitlines():
            line = re.sub(r"\s+", " ", raw.strip()).casefold()
            if len(line) < 160 or raw.lstrip().startswith(("|", "-", "*", "#")):
                continue
            prior = seen.get(line)
            require("duplicate long policy line " + (prior or name) + " / " + name,
                    prior is None or prior == name)
            seen[line] = name

    matches = list(CASE.finditer(evals))
    ids = [m.group(1) for m in matches]
    require("unique behavior scenario IDs", len(ids) == len(set(ids)))
    require("core evaluation cases retained",
            all(x in ids for x in ("A", "B", "J", "BC", "BD", "AX", "BN", "CB", "CH", "CI", "CJ", "CK", "CL")))
    for idx, match in enumerate(matches):
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(evals)
        text = evals[match.end():end]
        require("case " + match.group(1) + " has both expectation and forbidden action",
                "**Expected:**" in text and "**Forbidden:**" in text)
    if not quiet:
        print(f"PASS: {checks} documentation integrity checks; {len(ids)} regression scenarios.")
        print("LIMIT: Documentation checks cannot prove semantic/model behavior or live WordPress validation.")
    return checks


if __name__ == "__main__":
    try:
        check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    except (OSError, AssertionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

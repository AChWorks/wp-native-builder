#!/usr/bin/env python3
"""Read-only, source-scoped Skill contract smoke tests.

These checks detect missing literal guardrails and simple explicit contradictions.
They cannot prove an LLM will follow the rules. See docs/BEHAVIOR-EVALS.md.
Usage: python scripts/check_runtime_contract.py [skill-root]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REFERENCES = {
    "project-workflow.md",
    "workspace-memory.md",
    "implementation-decisions.md",
    "gutenberg-safety.md",
    "design-conventions.md",
}
BASELINE_BYTES = 66387

# Detect *unnegated* unsafe instructions in the Skill runtime. Conservative,
# not a semantic safety analyzer; avoid matching "do not skip" / "never ignore".
UNSAFE_IMPERATIVE = re.compile(
    r"(?im)^\s*(?:[-*]\s*)?(?:skip|ignore|bypass|disable|omit)"
    r"(?:\s+all)?\s+(?:safety|security|approval|authorization|permission"
    r"|verification|validation|rollback)\b"
    r"|^\s*(?:[-*]\s*)?(?:publish|deploy|install|activate)\b"
    r"[^\n]{0,100}\bwithout\s+(?:approval|authorization)\b"
)


def validate(root: Path, *, quiet: bool = False) -> int:
    root = Path(root).resolve()
    core = (root / "SKILL.md").read_text(encoding="utf-8")
    ref_paths = {p.name: p for p in (root / "references").glob("*.md")}
    refs = {name: path.read_text(encoding="utf-8") for name, path in ref_paths.items()}
    checks = 0

    def require(name: str, condition: bool) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(name)
        checks += 1

    def contains(label: str, body: str, *fragments: str) -> None:
        require(label, all(fragment.casefold() in body.casefold() for fragment in fragments))

    require("valid frontmatter", core.startswith("---\nname: wp-native-builder\n"))
    require("UI metadata present", (root / "agents" / "openai.yaml").is_file())
    paths = re.findall(r"\]\((references/[^)]+)\)", core)
    require("five direct reference owners", {Path(p).name for p in paths} == REFERENCES)
    require("no unreachable or extra runtime references", set(refs) == REFERENCES)
    require("all routed references exist", all((root / p).is_file() for p in paths))
    runtime = "\n".join((core, *refs.values()))
    require("no vendor preset", not re.search(
        r"preferred defaults[^\n]{0,150}\b(?:Astra|Gravity Forms|Code Snippets Pro)\b",
        runtime, flags=re.I,
    ))
    require("no explicit unsafe imperative", UNSAFE_IMPERATIVE.search(runtime) is None)

    contains("fast path and brief gate", core, "Fast path", "Project Brief", "no named theme")
    contains("unconditional proportional pre-handoff review", core, "Before every user handoff", "proportionate static review")
    contains("no false validation claim", core, "never claim unperformed validation", "when available")
    contains("exact site before reads/writes", core, "one exact site", "before any site-scoped", "never assume last-used site")
    contains("rebind after target drift", core, "re-check the binding", "scope changes or becomes ambiguous")
    contains("never fabricate ability or success", core, "Never invent an ability, permission, identity, or successful write.")
    contains("change isolation universal gate", core, "Change boundary:", "Protect out-of-scope consumers", "Home form", "Login form")
    contains("negative impact verification", core, "at-risk non-targets", "VERIFY TARGET")
    contains("manual exact output and durable fallback", core, "exact implementation-ready guidance", "user-supplied writable durable location")
    contains("specialist composed-mode ownership", core, "in composed mode", "return implementation control immediately", "re-consult")
    contains("consequential authorization", core, "specific authorization", "generic encouragement alone is not approval")
    contains("recommendation not install permission", core, "Recommending a plugin/theme is not authorization to install", "activate", "purchase")
    contains("local WordPress security", core, "permission_callback", "nonces for CSRF", "protect secrets")
    contains("new slug and author standard", core, "English ASCII", "lowercase-kebab-case", "Author: ACh", "Author URI: https://ach.li/")

    project = refs["project-workflow.md"]
    for label in (
        "Purpose & Outcomes", "Audience", "Scope & Non-goals",
        "Content & Primary Actions", "Brand & Design",
        "Functional Requirements", "Site Architecture", "Technical Constraints",
        "Quality Constraints", "Governance & Delivery", "Success Criteria",
    ):
        contains("canonical Brief heading: " + label, project, "| " + label + " |")
    contains("all brief domains no quota", project, "every materially applicable", "arbitrary question quota", "Do not build a plausible")
    contains("privacy/legal constraint", project, "privacy/legal")
    contains("approved material Brief change", project, "explain its impact", "consult the owner")
    contains("canonical documents and legacy", project, "Project Brief", "Site Architecture Profile", "Information Architecture", "Design Direction", "Content/Data Model", "project-foundation")
    contains("document graph with protected consumers", project, "non-obvious", "protected non-targets", "dependencies", "links")
    contains("independent task enums", project, "todo", "in_progress", "blocked", "done", "not_required", "pending", "changes_requested", "approved", "not_applicable", "draft_preview", "live")
    contains("review preview live transition", project, "Progress=`done`", "Review=`pending`", "Delivery=`draft_preview`", "until live delivery is verified")
    contains("no chat-only recovery when writable", project, "user-supplied durable project location", "without Workspace")
    contains("boundaries recoverable in active task", project, "protected surfaces", "next action")

    impl = refs["implementation-decisions.md"]
    contains("separate block/classic/builder ownership", impl, "Block theme", "Classic/theme-managed", "builder-owned global shell")
    contains("distinct form/navigation/media ownership", impl, "Notifications", "Dynamic content listing", "Media Library")
    contains("plugin-vs-code economics", impl, "plugin can beat", "custom code", "licensing")
    contains("install activation permission", impl, "installation", "activation", "external-vendor commitments")
    contains("scope classification and protected consumers", impl, "local, reused/shared or global", "protected non-targets")
    contains("form-instance scoping versus global opts", impl, "Home contact form", "Login form", "plugin-wide configuration", "form ID")
    contains("shared rollback before mutation", impl, "practical revision/rollback route", "before", "mutation")
    contains("verify representative untouched consumers", impl, "representative at-risk non-target consumers", "never claim")
    contains("future-useful coupling ownership", impl, "Site Architecture Profile", "active task", "lasting coupling")
    contains("security and HPOS", impl, "permission_callback", "prepared queries", "HPOS")
    contains("English slug and URLs", impl, "English ASCII", "lowercase-kebab-case", "translation mapping", "redirects")
    contains("custom plugin security and i18n", impl, "i18n", "WordPress", "nonce", "REST", "text domain")
    header_match = re.search(r"```php\s+/\*\*(.*?)\*/", impl, re.S)
    require("actual example plugin header present", header_match is not None)
    fields = dict(re.findall(
        r"^\s*\*\s+([^:\n]+):\s*(.*?)\s*$",
        header_match.group(1) if header_match else "",
        re.M,
    ))
    require("exact plugin Author field", fields.get("Author") == "ACh")
    require("exact plugin Author URI field", fields.get("Author URI") == "https://ach.li/")
    slug = fields.get("Text Domain", "")
    require("example domain is readable English slug", bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug)))
    example_name_slug = re.sub(r"[^a-z0-9]+", "-", fields.get("Plugin Name", "").lower()).strip("-")
    require("example text domain matches plugin name/slug", slug == example_name_slug)
    require("example translation directory", fields.get("Domain Path") == "/languages")

    gutenberg = refs["gutenberg-safety.md"]
    contains("block serialization contract", gutenberg, "serialization contract", "wp-block-*", "nested")
    contains("roundtrip compare and invalid warnings", gutenberg, "compare affected block structure", "Resolve invalid/recovery warnings")
    contains("unverified raw markup fallback", gutenberg, "no meaningful parser/editor validation", "safer block-aware/editor application path")
    contains("minimal invalid block recovery", gutenberg, "Preserve user data", "re-open/revalidate", "Never flatten")

    design = refs["design-conventions.md"]
    contains("composed/standalone design", design, "standalone", "Product Interface Designer", "composed")
    contains("visual a11y and localization", design, "RTL", "prefers-reduced-motion", "keyboard", "LCP")
    contains("scoped styles avoid other forms", design, "leakage into unrelated surfaces", "Home contact form", "Login form")

    ws = refs["workspace-memory.md"]
    contains("Legacy Brief reused", ws, "project-foundation", "discover", "truncated")
    contains("Workspace expected identity not revisions", ws, "version + state_hash", "expected-identity precondition", "blind-overwrite", "WordPress post Revision IDs")
    contains("ambiguous write re-read", ws, "ambiguous timeout", "re-read before any retry")
    contains("compact nearest-source recovery", ws, "compact project orientation", "next safe action", "live WordPress")
    contains("protected coupling in recovery", ws, "protected non-target consumers", "site/scope drifted")

    size = sum((root / p).stat().st_size for p in ["SKILL.md", *("references/" + n for n in REFERENCES)])
    if not quiet:
        print(f"PASS: {checks} source-scoped static/contradiction checks; {size:,} runtime bytes vs {BASELINE_BYTES:,} baseline ({100 * (1 - size / BASELINE_BYTES):.1f}% smaller).")
        print("LIMIT: Heuristic contradiction checks and keywords are not a model behavioral A/B evaluation.")
    return checks


if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    except (OSError, AssertionError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)

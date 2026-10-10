#!/usr/bin/env python3
"""Read-only static safety checks for the distributable WP Native Builder skill.

This is a structural/contract smoke test, NOT a behavioral LLM evaluation.
Usage: python scripts/check_runtime_contract.py [path/to/skill-root]
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
CORE = ROOT / 'SKILL.md'
REFS = ROOT / 'references'


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def has(blob: str, *terms: str) -> bool:
    return all(term.casefold() in blob.casefold() for term in terms)


def main() -> None:
    text = CORE.read_text(encoding='utf-8')
    refs = {p.name: p.read_text(encoding='utf-8') for p in REFS.glob('*.md')}
    all_text = '\n'.join([text, *refs.values()])
    check(text.startswith('---\nname: wp-native-builder\n'), 'Skill frontmatter missing or renamed')
    paths = re.findall(r'\]\((references/[^)]+)\)', text)
    check(len(set(paths)) == 5, 'Every domain reference must be reachable from SKILL.md')
    check(all((ROOT / p).is_file() for p in paths), 'Skill routes to a missing direct reference')
    check(not re.search(r'preferred defaults.*(?:Astra|Gravity Forms|Code Snippets Pro)', all_text, re.I), 'Old product defaults must not return')
    check(has(text, 'fast path', 'Project Brief', 'no named theme'), 'Fast path or stack neutrality missing')
    check(has(text, 'one exact site', 'before any site-scoped', 'never assume last-used site'), 'Multi-site target guard missing')
    check(has(text, 'static', 'when available', 'not assumed validity'), 'Verification evidence guard missing')
    check(has(text, 'Product Interface Designer', 'optional', 'reuse valid packets'), 'Bounded specialist semantics missing')
    check(has(text, 'English ASCII', 'lowercase-kebab-case', 'Never silently rewrite'), 'Slug/SEO convention missing')
    check(has(text, 'Author: ACh', 'Author URI: https://ach.li/', 'translations'), 'Author/i18n convention missing')
    impl = refs['implementation-decisions.md']
    check(has(impl, 'Plugin Name:', 'Author: ACh', 'Author URI: https://ach.li/', 'Text Domain:', 'Domain Path:'), 'Plugin header contract missing')
    check(has(impl, 'plugin can beat', 'custom code', 'licensing'), 'Plugin-versus-code economics missing')
    check(has(impl, 'permission_callback', 'nonce', 'capability', 'prepared'), 'WordPress security safeguards missing')
    check(has(refs['gutenberg-safety.md'], 'serialization contract', 'round-trip', 're-open', 'Static'), 'Gutenberg safety path missing')
    project = refs['project-workflow.md']
    check(has(project, 'Project Brief', 'Site Architecture Profile', 'Information Architecture', 'Design Direction', 'Content/Data Model'), 'Canonical document domains incomplete')
    check(has(project, 'scope', 'evidence', 'dependencies', 'Task', 'Project Map'), 'Documentation ownership/navigation incomplete')
    check(has(project, '`todo`', '`in_progress`', '`blocked`', '`done`', '`not_required`', '`pending`', '`changes_requested`', '`approved`', '`not_applicable`', '`draft_preview`', '`live`'), 'Task enum contract missing')
    ws = refs['workspace-memory.md']
    check(has(ws, 'project-foundation', 'stable', 'discover', 'truncated'), 'Workspace legacy/duplicate safeguards missing')
    check(has(ws, 'version + state_hash', 'expected-identity', 'blind-overwrite', 're-read'), 'Workspace optimistic concurrency guard missing')
    check(has(ws, 'compact project orientation', 'live WordPress', 'next safe action'), 'Progressive recovery contract missing')
    check(has(refs['design-conventions.md'], 'standalone', 'composed', 'RTL', 'prefers-reduced-motion'), 'UI fallback/review requirements missing')
    runtime_bytes = sum(p.stat().st_size for p in [CORE, *REFS.glob('*.md')])
    baseline_bytes = 66387
    print(f'PASS: 20 runtime structural checks; {runtime_bytes:,} bytes vs {baseline_bytes:,} baseline ({100 * (1 - runtime_bytes / baseline_bytes):.1f}% reduction).')
    print('LIMIT: These checks cannot prove semantic LLM behavior or 95% quality retention; run documented regression prompts separately.')


if __name__ == '__main__':
    main()

# WP Native Builder

**WP Native Builder** is a ChatGPT Skill for professional WordPress planning, design, implementation, review, troubleshooting, and lightweight project continuity.

It is **vendor-neutral and WordPress-native-first**: use the site's current Core/theme/builder/plugin/data owners whenever suitable, comparing maintained plugins against bespoke code by actual feature quality and total lifecycle cost.

## What it does

- Plan substantial work from **one Project Brief per distinct project**, asking novices only material questions; keep small changes fast
- Respect actual WordPress ownership, supported APIs and the site's established theme, builder, plugin and data model—without fixed vendor presets
- Protect unrelated pages, headers, components, forms and data when shared templates, selectors, hooks or Patterns are edited
- Treat Gutenberg as a structured editor, review layout/RTL/accessibility and never claim unavailable validation
- Resume multi-step work from authorized Workspace/repository/folder records rather than prior chat
- Consult Product Interface Designer only for material unresolved interface judgment, retaining WordPress execution and publication authority
- Require the applicable authorization for real consequential changes, not repetitive confirmation for routine reversible work

A **new bespoke plugin authored through Bridge** receives `Author: ACh` and `Author URI: https://ach.li/`; this convention does not modify metadata or files of other installed plugins.

## Install

Download the latest GitHub Release asset named **`skill.zip`**, then open ChatGPT Skills at **`/skills`** and upload the ZIP. For an unmerged PR, the `wp-native-builder-candidate-skill` GitHub Actions artifact is a **review-only candidate**, not the published Release.

The packaged Skill contains only runtime files:

```text
wp-native-builder/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── design-conventions.md
    ├── gutenberg-safety.md
    ├── implementation-decisions.md
    ├── project-workflow.md
    └── workspace-memory.md
```

## Use

Ask naturally, for example:

- `Start a new Persian RTL company website and guide me through everything you need before design.`
- `Improve this Gutenberg page without changing the existing visual language.`
- `This site uses Kadence + WooCommerce + ACF. Improve the product/category presentation using the current stack.`
- `Build this section from the reference screenshot, but tell me if the UX should be improved.`
- `Fix this Gutenberg block that says it contains unexpected or invalid content.`
- `Resume the WordPress project and continue the next useful task.`
- `Change this page's header without altering other pages that share the same template.`

A new/substantial multi-step project resolves durable project-level facts before material design. Small bounded edits stay lightweight.

## Runtime model

`SKILL.md` is the compact router. It conditionally loads the ownership, project, Gutenberg, design and persistence references, each with one policy owner.

**Mechanism first, transport second:** bind the exact target and shared effects, use the supported WordPress owner, prepare and review the narrow change, publish only when authorized, and verify target and relevant non-target consumers. A connector's tool names and permissions do not dictate site architecture or user approval.

The [runtime architecture](docs/architecture.md) owns the rule map; runtime references hold detailed implementation, approval and recovery behavior. This reader guide does not duplicate those procedures.

## Project Brief and canonical artifacts

Substantial work uses **one Brief per distinct project, not one per WordPress site**. Create only useful distinct domain documents (Site Architecture Profile, Information Architecture, Design Direction, Content/Data Model); reuse existing equivalents. Link accepted decisions and active tasks without copying site inventories or conversation history. Do not repeatedly reopen a settled Brief for bounded work.

See the [canonical product specification](MASTER-SPEC.md) and [durable-state architecture](docs/PROJECT-WORKSPACE-ARCHITECTURE.md) for their separate authorities.

## Gutenberg safety

For Gutenberg work, block-aware/native operations and supported Core block/Pattern/template mechanisms are preferred. Raw serialized block markup is treated as a serialization contract, not arbitrary HTML.

When raw serialization is unavoidable, the Skill performs every meaningful available structure/parse/serialize/editor/re-read check before claiming validation and fixes invalid-block symptoms at the smallest affected representation.

## Manual mode

The Skill works without a WordPress connector and provides exact stack-aware implementation guidance. Without a persistent Workspace or another durable project location, it does not claim cross-chat persistence.

## Connected mode

WordPress connectors are optional. Discover actual capabilities from their exposed contracts; never assume a Bridge, Gateway, tool name, installed plugin or one-connector-per-site topology.

A connection spanning multiple WordPress sites requires **one exact bound site** from current instructions or an authoritative task/project before any site-scoped read/write. Never infer it from the last-used site. Prefer supported mechanisms, draft/reversible changes and actual revision/write checks. If a safe connected route is unavailable, provide stack-specific preparation or manual guidance instead.

## Durable project recovery

A fresh chat can continue from an authorized **Workspace, GitHub Issue/repository or project folder** when it identifies the project/site, task, current decisions, blocker, review/publication gate and next safe action. Selectively read governing records, check live WordPress, protect concurrent writes and do not confuse a limited index or identical titles across projects with complete discovery.

No writable source means no claim of newly saved continuity. The [project-state architecture](docs/PROJECT-WORKSPACE-ARCHITECTURE.md) and runtime `workspace-memory` reference own detail.

## Approval and safety

The Skill proceeds through safe reads, drafts, previews, reversible edits, validation, and preparation without repetitive confirmation. Genuine consequential actions are authorized only by the applicable current user instruction/approval boundary.

A current exact instruction is not redundantly reconfirmed while target/scope/material effect remain unchanged.

## Repository documentation

- [`MASTER-SPEC.md`](MASTER-SPEC.md) — canonical product requirements for the Skill itself.
- [`docs/architecture.md`](docs/architecture.md) — concise runtime/rule ownership architecture.
- [`docs/PROJECT-WORKSPACE-ARCHITECTURE.md`](docs/PROJECT-WORKSPACE-ARCHITECTURE.md) — persistent Workspace/cross-chat architecture.
- [`docs/BEHAVIOR-EVALS.md`](docs/BEHAVIOR-EVALS.md) — behavioral regression scenarios and baseline-vs-candidate review protocol.

Implementation/release history belongs to Git/GitHub Issues, Pull Requests, and Releases.

## Validation and packaging

Releases use OpenAI's standard Skill validation/package workflow. The public archive is named exactly **`skill.zip`** and must match the tagged/integrated runtime revision. Run `python scripts/check_runtime_contract.py .`, `python scripts/check_documentation.py .` and `python -m unittest discover -s tests` for structural/document checks and negative mutation probes. Representative model tests in `docs/BEHAVIOR-EVALS.md` remain necessary to claim behavioral equivalence.

## License

MIT. See [`LICENSE`](LICENSE).

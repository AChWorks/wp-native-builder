# WP Native Builder

**WP Native Builder** is a ChatGPT Skill for professional WordPress planning, design, implementation, review, troubleshooting, and lightweight project continuity.

It is **vendor-neutral and WordPress-native-first**: use the site's current Core/theme/builder/plugin/data owners whenever suitable, comparing maintained plugins against bespoke code by actual feature quality and total lifecycle cost.

## What it does

WP Native Builder helps ChatGPT:

- keep small bounded edits fast while establishing one Project Brief for substantial multi-step site work;
- ask novice-friendly staged questions until material project gaps are actually resolved;
- organize durable project truth in distinct, linked canonical documents instead of duplicating “master” snapshots;
- understand the relevant current WordPress architecture before changing it;
- isolate the requested target from unrelated forms, components, data and shared styling/behavior, verifying actual impacted consumers;
- route headers, footers, templates, navigation, and reusable/global surfaces to their real Site Editor/theme/builder owner;
- prefer suitable Core blocks, Patterns, theme/builder/plugin features, WooCommerce presentation, forms, CPT/ACF, and public WordPress capabilities before Custom HTML/custom code;
- treat Gutenberg markup as a serialization contract and repair invalid blocks narrowly;
- review material UI proportionally and consult Product Interface Designer only for materially unresolved interface judgment or when explicitly requested, without transferring WordPress mechanism/lifecycle/publication ownership;
- perform static self-review even without a renderer, then add preview/editor/parser/live checks when available;
- prefer English readable slugs for new objects, preserve existing URLs and apply ACh author metadata to new bespoke Bridge-created plugins without changing other plugins;
- resume substantial work from durable project records (Workspace or authorized repository/folder), not chat history or Memory;
- avoid duplicate Workspace canonical documents through discover/reuse-before-create behavior;
- reconcile stale/ambiguous Workspace writes instead of overwriting newer state;
- tolerate one plausibly transient connector/runtime failure without immediately abandoning the workflow;
- keep genuine consequential publication/security/destructive/customer/order/financial actions behind the applicable approval boundary.

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

Routing is additive: one request may need project-workflow, ownership, Gutenberg, design, and Workspace rules at the same time. `SKILL.md` routes those domains while the direct references own their detailed policy.

Product Interface Designer is an optional consulted specialist for materially unresolved interface judgment or explicit specialist requests. Bounded or already-settled visual edits remain inside WP Native Builder, and the specialist owns its own composition/packet contract rather than having that rulebook duplicated here. WP Native Builder resumes WordPress mechanism selection, implementation, publication, and verification after the bounded interface decision returns.

```text
REQUEST
  -> recover/discover relevant truth
  -> establish Project Brief when required
  -> choose owner/mechanism and local/shared/global change boundary
  -> identify at-risk consumers and protected non-targets
  -> choose an actually exposed execution transport
  -> build narrowly
  -> static self-review
  -> add preview/editor/parser/live review when available
  -> verify available draft/staging target and at-risk non-target consumers before consequential publish
  -> user review/publish only when applicable and authorized
  -> verify applied target and at-risk non-target consumers
  -> reconcile future-useful project state
```

**Change isolation:** scope each edit to its intended page, header, template, form, component or data flow. For shared selectors, hooks, patterns or settings, assess relevant consumers and verify representative protected surfaces when at risk. Document lasting coupling in the existing task/architecture owner, not an extra document per edit.

No fixed theme, builder, form, icon, plugin or permalink preset applies. Select existing/native/plugin/custom solutions based on feature fit, reliability, licensing, security, performance, editing quality, maintainability and reversibility—not habitual tools or slight hypothetical code speed gains.

## Project Brief and canonical artifacts

A project that requires a Project Brief keeps one canonical Project Brief containing stable project-level intent. When the Skill creates related artifacts, the canonical default names are:

- `Project Brief`
- `Site Architecture Profile`
- `Information Architecture`
- `Design Direction`
- `Content/Data Model`

Reuse existing semantically equivalent documents instead of duplicating them. Each owns one domain, links to active tasks and related canonical owners, and records accepted decisions/provenance when useful. Add an optional small index only when documents are otherwise hard to locate; do not mirror full site state.

Once ready, Project Brief leaves the routine hot path. Current work normally uses the nearest authoritative task/document/live WordPress state.

## Gutenberg safety

For Gutenberg work, block-aware/native operations and supported Core block/Pattern/template mechanisms are preferred. Raw serialized block markup is treated as a serialization contract, not arbitrary HTML.

When raw serialization is unavoidable, the Skill performs every meaningful available structure/parse/serialize/editor/re-read check before claiming validation and fixes invalid-block symptoms at the smallest affected representation.

## Manual mode

The Skill works without a WordPress connector and provides exact stack-aware implementation guidance. Without a persistent Workspace or another durable project location, it does not claim cross-chat persistence.

## Connected mode

Connected execution can use any compatible runtime that exposes sufficient WordPress capabilities. The Skill does not require or assume a specific plugin, connector, MCP server, gateway, tool name, or one-App-per-site topology.

Connected work:

1. discovers capabilities by documented behavior/schema rather than product or tool name;
2. inspects only relevant current architecture, targets, and capabilities;
3. chooses site mechanism before execution transport;
4. on a multi-site transport, uses fleet-level discovery only to identify available site identities; if the current request or authoritative active task/project context does not unambiguously identify one site, asks the user which site before any site-scoped inspection/read/write;
5. never guesses from the last-used site or nearby conversation, and keeps the resolved site identity explicit through all site-scoped operations;
6. prefers narrow reversible/draft/preview changes while iterating;
7. guards overwrite-sensitive writes with current identity when supported;
8. re-reads/reconciles stale or ambiguous state;
9. verifies writes when practical;
10. treats one plausible transport failure as transient until bounded evidence says otherwise;
11. falls back to useful manual/preparation work when no safe connected route exists.

The Skill selects among currently exposed capabilities by behavior and fit, not vendor/product/tool names. Native WordPress/theme/plugin capabilities may be better transports for the selected mechanism than generic transport operations.

## Durable project recovery

With Workspace or an authorized project repository/folder, a new chat resolves the exact project/site and active task, follows only relevant Brief/domain links, checks live WordPress and continues the next safe step. Two projects on one site must not share a Project Brief merely because its title or key matches. The task stores acceptance, target/protected consumers, blocker, review/delivery gate, evidence and next action in its existing owner. Without such a durable source, in-session work remains possible but automatic cross-chat recovery is not guaranteed.

When suitable Workspace abilities are exposed:

- compact orientation comes before broad reload;
- canonical singleton documents are discovered/reused before create;
- stable purpose keys may be used when the capability supports them, without assuming storage-level uniqueness;
- Tasks keep independent progress/review/delivery dimensions;
- Workspace writes use Workspace-owned optimistic-concurrency identity such as `version + state_hash`;
- stale writes are rejected and reconciled before retry;
- live WordPress remains authoritative for current site state.

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

Releases use OpenAI's standard Skill validation/package workflow. The public archive is named exactly **`skill.zip`** and must match the tagged/integrated runtime revision. Run `python scripts/check_runtime_contract.py .` plus `python -m unittest discover -s tests` for structural checks and negative mutation probes; the behavioral scenarios in `docs/BEHAVIOR-EVALS.md` still require representative model testing before claiming behavioral equivalence.

## License

MIT. See [`LICENSE`](LICENSE).

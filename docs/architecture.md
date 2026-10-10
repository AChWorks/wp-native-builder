# WP Native Builder architecture

This is the concise runtime and rule-ownership overview. Stable product requirements live in [`MASTER-SPEC.md`](../MASTER-SPEC.md); persistent Workspace architecture lives in [`PROJECT-WORKSPACE-ARCHITECTURE.md`](PROJECT-WORKSPACE-ARCHITECTURE.md); regression scenarios live in [`BEHAVIOR-EVALS.md`](BEHAVIOR-EVALS.md).

## Runtime structure

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

`SKILL.md` is the control plane. Request routing is additive rather than mutually exclusive; every applicable direct reference may be loaded once.

## Rule ownership

| Runtime source | Owns |
|---|---|
| `SKILL.md` | trigger/routing, universal control loop, source authority, optional Product Interface Designer consultation/re-consultation protocol, universal review/approval/safety invariants |
| `references/project-workflow.md` | Project Brief, linked domain documents, navigation, task state and recovery triggers |
| `references/implementation-decisions.md` | Mechanism and local/shared/global change boundaries, consumer isolation, English slugs, plugin i18n/author metadata, rollback |
| `references/gutenberg-safety.md` | Gutenberg serialization contract, invalid-block diagnosis, block-specific validation |
| `references/design-conventions.md` | WordPress-side interface realization quality and proportional standalone design fallback; it never becomes a second generic UI/UX owner when Product Interface Designer is active |
| `references/workspace-memory.md` | Backend-neutral project recovery (Workspace/repository), duplicate avoidance, guarded writes and fallback |
| `agents/openai.yaml` | ChatGPT-facing metadata |

References may state that another domain also applies, but they do not become a second owner of that domain's policy.

## Project truth model

```text
Project Brief
  -> Site Architecture Profile
  -> Information Architecture / Design Direction / Content/Data Model when useful
  -> Durable Tasks (Workspace or authorized repository/folder) for execution/review/delivery/next action
  -> Live WordPress remains authoritative for current site state
```

Project Brief readiness derives from material coverage for substantial work, not a new status enum or availability of persistence. Once ready it leaves the hot path. Derived docs own separate lasting domains; active tasks own progress. Stable links and selective verification make project recovery navigable without copying live state, history or a parallel backlog.

## Mechanism-first architecture

Every implementation makes two independent decisions:

1. **Owner/mechanism** — WordPress Core, Site Editor/template part, theme, builder, plugin, Pattern, form/commerce/data model, scoped frontend code, or custom extension.
2. **Transport** — an actually exposed connected capability that can safely operate the selected owner.

No named theme/builder/plugin/form/icon/permalink preset exists. Compare native/existing/maintained-plugin/custom mechanisms on fit and lifetime cost, rather than favoring custom code's nominal speed. A connector does not become the architecture merely because it exposes an operation. Transport selection is capability-based and product-neutral. If one transport fronts multiple WordPress sites, fleet-level discovery may identify site identities, but site-scoped capability use is fail-closed until one exact target is unambiguously established; never infer it from a last-used site or conversational proximity, and keep the resolved identity explicit through the operation.

## Review architecture

Pre-user review has two WordPress-side evidence levels:

- **Static review — always:** content/structure, ownership, semantics, implementation accessibility/responsive/RTL/performance/maintainability risks, and fidelity to any already-accepted interface intent.
- **Runtime/rendered review — when available:** preview/editor/parser/live checks, Gutenberg invalid/recovery warnings, implementation/fidelity verification, and write-result verification.

When Product Interface Designer is active, material interface judgment remains with that specialist; normal WordPress review does not create a second art direction or automatically trigger another specialist call. `SKILL.md` alone owns consultation/re-consultation. Static review must not be described as rendered validation.

## Local, reused and global change boundaries

`SKILL.md` binds exact target and protected non-targets for every edit. The implementation reference owns detailed scope/impact decisions: check actual consumers of shared forms, CSS/JS, templates, plugin settings, hooks and data; choose per-instance settings/selectors for a local request or enumerate intended shared effects with applicable authorization before broad mutation. Capture practical rollback evidence before shared/global work, then verify the target and representative at-risk unrelated consumers. **Example:** homepage contact-form styling must not silently modify the login form. No all-site audit or extra document is imposed for routine isolated edits.

## Workspace architecture

Durable persistence is optional and source-driven: Workspace **or an authorized repository/folder** stores useful decisions/tasks and links canonical owners. Recovery starts from the exact project/site and active Task, never from chat history or Memory. Workspace updates use Workspace-owned expected identity; repository/file updates use their supported current revision guards. Neither replaces live WordPress authority. The exact Workspace resume/retrieval procedure is owned only by `references/workspace-memory.md`.

Task delivery retains the current runtime-neutral enum: `not_applicable`, `draft_preview`, `live`. `not_applicable` means no draft/live state is currently established; intended later publication is represented by task goal/acceptance/targets/notes rather than a new lifecycle value.

## Packaging boundary

Only the seven runtime files under `SKILL.md`, `agents/`, and `references/` are packaged as `skill.zip`. Repository docs remain outside the Skill package. The public release asset must correspond to the tagged/integrated runtime revision. CI may upload an exact seven-file `skill.zip` candidate for review, but that artifact is not a public Release.

# WP Native Builder — Durable Project State and Workspace Architecture

This document explains durable project continuity using a connected Workspace **or** an authorized repository/project-folder source. Product requirements live in [`MASTER-SPEC.md`](../MASTER-SPEC.md); runtime rule ownership lives in [`architecture.md`](architecture.md).

Persistence is optional; Workspace is one adapter, while user-supplied GitHub Issues/files or project folders can hold equivalent authoritative records. It is not a chat archive, second CMS, live-site mirror, or general project-management system.

## 1. Goals

Any authorized durable source must support a fresh chat continuing from project records without prior chat history or Memory, keeping context small and live WordPress authoritative for current state.

It must:

- preserve only future-useful durable project context;
- support one canonical Project Brief when the project requires it;
- recover progressively instead of dumping all stored material;
- keep one-off work lightweight;
- prevent duplicate canonical documents where possible;
- keep task execution/review/delivery state independent;
- protect Workspace writes with optimistic concurrency independent of WordPress Revisions;
- degrade gracefully when the Workspace route is temporarily or permanently unavailable.

## 2. Layers and ownership

| Layer | Owns |
|---|---|
| **WP Native Builder Skill** | project semantics, source authority, intake/readiness, WordPress mechanism selection, approval and review workflow/state behavior; active specialist interface judgment remains outside this layer |
| **Project Brief** | accepted durable project-level purpose, audience, scope/non-goals, constraints, success criteria |
| **Derived domain documents** | specialized durable architecture/design/IA/content-data context, in the selected authorized store |
| **Durable tasks** | unresolved outcome/acceptance, target, dependency/blocker, review/delivery gate, evidence and next action |
| **Live WordPress** | actual current pages/posts/products/media/settings/theme/plugin/templates and other site objects/configuration |

Any compatible runtime or connector may implement the storage/API/admin surface. A readable but non-writable source can support recovery but not state persistence. When Workspace and repository records coexist, preserve the established canonical owner per artifact; do not presume synchronization or duplicate project truth. The Skill stays capability-driven and uses only behavior exposed by the runtime.

## 3. Canonical documents

When WP Native Builder creates singleton project documents, the default canonical names are:

- `Project Brief`
- `Site Architecture Profile`
- `Information Architecture`
- `Design Direction`
- `Content/Data Model`

An existing equivalent document **for the same bound project** outranks naming preference. Project Brief is singleton per project, not per WordPress site: equal names or keys alone do not establish equivalence across independent projects sharing a site. Shared site-level architecture documents are reused only when that ownership is established. Do not create a second copy merely to normalize a title.

### Source-owned document graph

For substantial work, establish only the domains that repay persistence: Brief = purpose/scope; Architecture Profile = actual site and code ownership; Information Architecture = hierarchy/navigation/URLs; Design Direction = accepted reusable interface rules; Content/Data Model = CPT/taxonomy/fields. Additional scoped decisions or recovery notes must own distinct long-lived content. Each relevant document records scope, accepted decisions separate from proposals, exact site/surface and edit owner, intended shared consumers and protected non-targets when non-obvious, dependencies/links and evidence/verification freshness when stale-sensitive. Tasks link to the nearest governing docs and concrete WordPress target. Use one optional Project Map/index only if navigation is otherwise difficult; it links owners and does not duplicate live data, task progress or other documents.

### Duplicate-safe creation

Before creating a canonical singleton document:

```text
DISCOVER -> REUSE/UPDATE -> CREATE ONLY IF ABSENT -> VERIFY
```

Search/list enough decision-relevant state in the authorized store to identify semantic equivalents. If a stable document `key` is supported, use a stable purpose key after confirming an equivalent object does not already exist. Do not assume key uniqueness unless the runtime schema/storage guarantees it. An incomplete/truncated listing is not proof of absence.

## 4. Project Brief

Project Brief content/coverage semantics are owned by `references/project-workflow.md`, not redefined here. Storage's responsibility is only to persist/retrieve the canonical document safely when a suitable capability exists. Existing Workspace artifacts titled `Project Foundation` or keyed `project-foundation` remain valid legacy equivalents and are reused rather than normalized by rename or duplicated.

After Project Brief readiness it remains discoverable but is not automatically loaded on every resume.

## 5. Durable tasks and project recovery identity

Tasks are useful for substantive unfinished outcomes, acceptance, dependencies, review or delivery—not every small edit. The existing Workspace Task, GitHub Issue/file or another durable project record can be the sole owner. The exact task fields and **three independent state dimensions** are defined in [MASTER-SPEC.md](../MASTER-SPEC.md) and `references/project-workflow.md`; do not maintain a second enum or status procedure here.

Identity is **project + site + target**, not just the last-used site or a document title. A site-wide summary may mix projects, tasks and historical focus. An incomplete/truncated index cannot prove absence; site-private storage is not automatically project-private. Count/readback checks, access grants, storage field limits and actual project bindings must be verified against the exposed implementation.

Read-only authoritative documents can support fresh-chat recovery without a writable target, while absence of any readable durable source cannot. The precise selective-recovery, deduplication and write/retry procedure belongs solely to [workspace-memory.md](../references/workspace-memory.md).

## 7. Retention

Persist only when all are true:

1. a future session materially benefits;
2. a stronger/current source does not already own the fact;
3. retention reduces repeated briefing, ambiguity, rework, or lost progress;
4. it is safe to store.

Do not persist full chats, hidden reasoning, routine worklogs, repeated checkpoints, every micro-edit, copied live content, credentials/secrets, unnecessary customer/order/payment/financial payloads, or broad database/plugin dumps.

## 8. Storage identity, privacy and failure boundaries

WordPress post Revisions and Workspace document/task concurrency are **distinct**. A Workspace write needs enforceable current storage identity such as `version + state_hash`; a repository/Issue/file uses its supported current revision guard or safe non-overwriting method. A successful acknowledgement may hide truncation, and a timeout may hide a successful update. The detailed read/reconcile/write procedure is maintained only in [workspace-memory.md](../references/workspace-memory.md).

A site-private object does **not** imply project- or user-specific permissions. Actual read/write grants control whether team-sensitive details can be stored. Secrets, irrelevant personal/customer/payment records, full chat transcripts and live-site dumps are not project memory.

Workspace export alone does not prove import, restore, cross-site migration or backup coverage. Hosting/backups or an independently verified migration mechanism own those outcomes.

## 9. Acceptance evidence boundary

Recovery must be demonstrably project-bound, with exact site/target verification, bounded index handling, no unverified duplicate records, protected writes, truthful read-only/no-store fallback and live-state rechecks. The scenario protocol in [BEHAVIOR-EVALS.md](BEHAVIOR-EVALS.md) owns behavioral evaluation; passing documentation/static checks is not real connected recovery or LLM A/B evidence.


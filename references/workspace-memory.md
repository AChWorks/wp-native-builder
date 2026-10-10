# Persistent Workspace: Organization, Safe Writes and Recovery

Load for relevant persistent Workspace work/resume. `project-workflow.md` owns **what** documents mean; this file owns **how** to recover and safely write them. Never assume tool/storage names.

## 1. Progressive resume (minimal reads)

1. Discover the actual available project-Workspace capabilities. Logical roles such as `workspace-resume`, `workspace-document`, `workspace-task` describe behavior, **not** callable names to invent. Without usable persistence work manually and state that cross-chat recovery is unavailable.
2. Request compact project orientation first: exact project/site identity and target, current focus, open/review-blocked tasks, blockers, links to canonical docs, next safe action. Do **not** dump all site data or documents.
3. Fetch only the active task and documents that resolve the next decision. Prefer active task / derived domain truth to the full Project Brief; open the brief for unresolved/changed intent, contradictions or launch reconciliation.
4. For site-dependent operations, reverify the relevant live WordPress owner/object/revision. A saved note never proves current site configuration; a persisted last-used site is not by itself an authorized target. Reconcile changed data before writing.
5. Resume the highest-value safe task and update future-useful state only if its owner actually changed.

## 2. Find the canonical owner; avoid duplication

Before creating a document or task: **discover -> reuse/update the semantic equivalent -> create only after reliable absence -> verify**. Incomplete or truncated discovery never establishes absence.

Stable singleton examples: `project-brief`, `site-architecture-profile`, `information-architecture`, `design-direction`, `content-data-model`. Treat legacy **`Project Foundation` / `project-foundation` as the existing Project Brief**; do not rename/delete or create another solely to normalize. Use stable keys only when the capability supports them; don't presume uniqueness without a documented guarantee. Task titles identify their actual purpose/surface, never the generic `Task` singleton.

Keep a connected **document graph, not a second database**: current tasks link to their governing docs and WordPress targets; derived docs point to their canonical Project Brief/related owner when useful. Persist a small index only if listing/findability is otherwise insufficient. Do not mirror live content, plugin inventory, site snapshots or statuses into multiple notes. Include scope, accepted decisions, provenance/verification context and known uncertainty when those facts matter for future recovery.

## 3. Safe mutation and concurrency

For overwrite-sensitive Workspace Document/Task updates:

1. Read the current object with **Workspace-owned** identity (e.g., `version + state_hash`). WordPress post Revision IDs are unrelated to this protection.
2. Require an update operation with an enforced expected-identity precondition. If unavailable, do **not** blind-overwrite; use a safe non-overwriting route or surface the precise blocker.
3. Patch only the owning artifact with expected identity; preserve concurrent valid changes. Verify accepted state when possible.
4. On version mismatch, re-read, reconcile and retry only if still justified. On ambiguous timeout/write result, **re-read before any retry**, never blindly duplicate an object.

Don't rely on WordPress Revisions being enabled or retained. Backup/disaster recovery is a separate hosting concern, not proof supplied by Workspace notes.

## 4. Durable reconciliation and failures

After material project progress, persist only the smallest future-useful changed truth: accepted decision, real site owner, active task/next action, blocker, review/delivery state or unresolved defect. Don't create a worklog on each turn, cache hidden reasoning, store secrets, or update every document merely because conversation progressed.

For transient failures preserve recovered orientation, continue independent tasks, and make **at most one evidence-justified** route rediscovery/retry; no blind loop. If persistent writes remain unavailable, do safe manual/non-overwrite work and report the exact blocked action. Never claim a document was saved until the authoritative result verifies it.

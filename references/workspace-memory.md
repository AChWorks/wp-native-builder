# Durable Project Sources: Recovery and Safe Writes

Load when durable project state or cross-chat recovery matters: an accessible authorized Workspace, repository, project folder or other supported durable source. `project-workflow.md` owns **what** the Brief, domain documents and tasks mean; this reference alone owns **how** to discover, persist, recover and protect them. **Chat history and assistant Memory are not durable authorities.** Never invent a store, site, capability, write or recovery result.

## 1. Use the actual durable owner

| Source | Contract |
|---|---|
| Connected project storage (including WordPress Workspace) | Discover and select actual orientation, list/read and mutation capabilities from exposed tool contracts. **Never assume named tools, required arguments or a provider version**; use only operations that are currently available and authorized. |
| User-provided GitHub repository / project folder / equivalent durable files | Reuse its established canonical docs and Issue/Task records at their actual paths/IDs and revision guards; do **not** require Workspace, duplicate task tracking or a new fixed directory. |
| Readable but not writable durable source | Recover its known project facts and verify live state, but do not claim to have saved new progress; surface a write blocker only when future continuity needs an update. |
| No accessible durable source | Continue manual/session work. State that reliable cross-chat recovery is unavailable until the user supplies an accessible authoritative source; never invent persistence. |

Persistence can exist even without a WordPress execution connector. Hidden WordPress storage is not proof of project- or user-level isolation: inspect the connected source's real read/write grants before storing cross-team facts. If several stores exist, select the **established authoritative owner per artifact**, link only as needed and never create unsanctioned parallel copies or assume bidirectional synchronization. Preserve existing project conventions; never build a new storage platform for a small bounded edit.

## 2. Progressive fresh-chat recovery

```text
RESOLVE project + EXACT SITE from current instruction or bound durable record
 -> compact project orientation / discover active or review-blocked task
 -> fetch only its governing document links and current target
 -> reverify relevant live WordPress owner/object/revision
 -> continue next safe action -> persist changed owner once
```

1. Get a **compact project orientation**: project/site identity and exact target binding, current task/outcome, protected non-target consumers when material, dependency/blocker, review/publish gate, canonical links and **next safe action**. A last-used site, chat history or Memory alone cannot authorize a site. If ambiguity remains, ask for the exact site before site-scoped operations.
2. Read the **exact bound** active task first, then only the nearest relevant domain sources. Open Project Brief for missing, changed or contradictory project-level intent or launch reconciliation, not for every chat. A resume's suggested focus is not exclusive authority when multiple projects/tasks share a site. Compare reported counts to returned summaries; **bounded/truncated indexes do not prove absence**. Use supported targeted reads; avoid unbounded full-content lists that exceed transport budgets, and do not create duplicates when complete discovery is unavailable.
3. Verify the relevant **live WordPress** target, current owner and revision before state-dependent changes; rebind if **site/scope drifted**. Durable project notes are not proof of unchanged live configuration. Resume useful work rather than stopping at a recap.
4. After material progress, update only the source owning a changed decision, target, blocker, task review/delivery state or next action; verify the authoritative result. No chat transcripts, session handoffs or copied inventories.

## 3. Canonical document/task graph

**discover -> reuse/update equivalent -> create only after reliable absence -> verify**. **Singleton scope:** a Project Brief is singleton **per distinct project, not per WordPress site**. Other domain documents may be shared at site level only when the established owner is intentionally shared. Bind candidate records to the exact project/site through supported identity fields or authoritative document/task links; a matching title/key alone cannot prove equivalence between projects. Stable purpose keys, if supported (e.g. `project-brief`, `site-architecture-profile`, `information-architecture`, `design-direction`, `content-data-model`), are not universal site-wide identities; use an established project-qualified key convention when supported. Reuse legacy `Project Foundation` / `project-foundation` only for the same project; do not rename it merely to normalize. Never assume key uniqueness without a storage guarantee. If the source cannot reliably distinguish projects or prove absence, do not guess, overwrite, or create a competing record.

Tasks are purpose/target-specific, **not** one generic `Task` singleton. Link the active task to accepted domain documents and actual WordPress targets. If a store lacks first-class project or next-action fields, preserve the stable project/site binding, source links and next safe action **concisely in actual supported descriptive fields**; discover the field schema instead of inventing API inputs. Keep a small graph, not a second database; use an index only if listing/search cannot navigate it. Retain stable shared ownership, **protected non-target consumers**, source/evidence freshness and relevant uncertainty when future tasks benefit. Never mirror site data or the backlog in every document. If durable storage becomes available mid-project, reconcile accepted session decisions into an existing canonical source, not a new Brief.

## 4. Guard overwrite-sensitive writes

1. Read exact destination and **storage-owned identity**. For Workspace Document/Task updates require an enforced **expected-identity precondition** such as `version + state_hash`; **WordPress post Revision IDs** cannot protect Workspace documents.
2. For repository/folder records use a supported current **file/commit version** or other real compare-and-swap. Preserve valid concurrent changes. Without a safe guard, use a supported **non-overwriting route**; otherwise **do not blind-overwrite** and report the precise write blocker.
3. Patch only the owning record, verify the **actual returned/stored fields** (especially accepted criteria, references and next action) against the intended data; some stores sanitize or silently bound bytes/list entries. On mismatch re-read/reconcile before justified retry. After an **ambiguous timeout** or write result, **re-read before any retry**, never blindly duplicate a task or document.
4. WordPress Revisions may be disabled or pruned and do not replace storage concurrency. A Workspace export does not prove restore/import, cross-site migration or backup coverage; those remain separate hosting/storage responsibilities.

Never store secrets, credentials, full chats, hidden reasoning, copies of live content or unnecessary **customer/order/payment/financial payloads** in project sources, logs or notes. Store minimal decision references instead.

## 5. Failure and manual fallback

One plausible connector/storage failure may be transient: preserve orientation, continue independent safe tasks and rediscover/retry once only when evidence justifies it, including a safe equivalent authoritative route. Do not blindly loop or disguise permission/schema denial. When writes remain unavailable, continue useful manual/non-overwrite work, report the exact blocked mutation, and **never claim a document was saved** without its authoritative result.

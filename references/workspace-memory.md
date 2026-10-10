# Durable Project Sources: Recovery and Safe Writes

Load when durable project state or cross-chat recovery matters: connected Workspace, or an authorized user-supplied writable repository/project folder. `project-workflow.md` owns **what** the Brief, domain documents and tasks mean; this reference alone owns **how** to discover, persist, recover and protect them. **Chat history and assistant Memory are not durable authorities.** Never invent a store, site, capability, write or recovery result.

## 1. Use the actual durable owner

| Source | Contract |
|---|---|
| Persistent Workspace | Discover its actual project capabilities. `workspace-resume`, `workspace-document` and `workspace-task` are logical roles, **not** callable names. |
| User-provided GitHub repository / project folder / equivalent durable files | Reuse its established canonical docs and Issue/Task records at their actual paths/IDs and revision guards; do **not** require Workspace, duplicate task tracking or a new fixed directory. |
| No verified writable durable source | Continue manual/session work. Explicitly state that cross-chat recovery is unavailable unless the user supplies the authoritative project source later; never claim persistence. |

Persistence can exist even without a WordPress execution connector. Preserve one owner per fact and existing project conventions; never build a new storage platform for a small bounded edit.

## 2. Progressive fresh-chat recovery

```text
RESOLVE project + EXACT SITE from current instruction or bound durable record
 -> compact project orientation / discover active or review-blocked task
 -> fetch only its governing document links and current target
 -> reverify relevant live WordPress owner/object/revision
 -> continue next safe action -> persist changed owner once
```

1. Get a **compact project orientation**: project/site identity and exact target binding, current task/outcome, protected non-target consumers when material, dependency/blocker, review/publish gate, canonical links and **next safe action**. A last-used site, chat history or Memory alone cannot authorize a site. If ambiguity remains, ask for the exact site before site-scoped operations.
2. Read the active task first, then only the nearest relevant domain sources. Open Project Brief for missing, changed or contradictory project-level intent or launch reconciliation, not for every chat. Incomplete or **truncated** discovery does not prove an item absent.
3. Verify the relevant **live WordPress** target, current owner and revision before state-dependent changes; rebind if **site/scope drifted**. Durable project notes are not proof of unchanged live configuration. Resume useful work rather than stopping at a recap.
4. After material progress, update only the source owning a changed decision, target, blocker, task review/delivery state or next action; verify the authoritative result. No chat transcripts, session handoffs or copied inventories.

## 3. Canonical document/task graph

**discover -> reuse/update equivalent -> create only after reliable absence -> verify**. Stable singleton keys, if the source supports them, include `project-brief`, `site-architecture-profile`, `information-architecture`, `design-direction`, `content-data-model`. Treat legacy **`Project Foundation` / `project-foundation` as the existing Project Brief**; do not rename, delete or duplicate it merely to normalize. Do not assume storage enforces key uniqueness without a documented guarantee.

Tasks are purpose/target-specific, **not** one generic `Task` singleton. Link the active task to accepted domain documents and actual WordPress targets. Keep a small graph, not a second database; use an index only if listing/search cannot navigate it. Retain stable shared ownership, **protected non-target consumers**, source/evidence freshness and relevant uncertainty when future tasks benefit. Never mirror site data or the backlog in every document. If durable storage becomes available mid-project, reconcile accepted session decisions into an existing canonical source, not a new Brief.

## 4. Guard overwrite-sensitive writes

1. Read exact destination and **storage-owned identity**. For Workspace Document/Task updates require an enforced **expected-identity precondition** such as `version + state_hash`; **WordPress post Revision IDs** cannot protect Workspace documents.
2. For repository/folder records use a supported current **file/commit version** or other real compare-and-swap. Preserve valid concurrent changes. Without a safe guard, use a supported **non-overwriting route**; otherwise **do not blind-overwrite** and report the precise write blocker.
3. Patch only the owning record, verify accepted state and on mismatch re-read/reconcile before justified retry. After an **ambiguous timeout** or write result, **re-read before any retry**, never blindly duplicate a task or document.
4. WordPress Revisions may be disabled or pruned and do not replace storage concurrency. Backups/disaster recovery are separate hosting concerns.

Never store secrets, credentials, full chats, hidden reasoning, copies of live content or unnecessary **customer/order/payment/financial payloads** in project sources, logs or notes. Store minimal decision references instead.

## 5. Failure and manual fallback

One plausible connector/storage failure may be transient: preserve orientation, continue independent safe tasks and rediscover/retry once only when evidence justifies it, including a safe equivalent authoritative route. Do not blindly loop or disguise permission/schema denial. When writes remain unavailable, continue useful manual/non-overwrite work, report the exact blocked mutation, and **never claim a document was saved** without its authoritative result.

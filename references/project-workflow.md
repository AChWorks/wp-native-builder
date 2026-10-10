# Project Brief, Documentation and Multi-step Workflow

Load for substantial new/redesigned/multi-surface sites, durable project decisions, or project documentation. Keep small edits on the main Skill's fast path.

## 1. Establish project intent once

Before material build, discover existing evidence and resolve applicable brief domains as **known, delegated, safely inferred or N/A**. Ask gaps in short plain-language batches, never demand WordPress jargon, and don't invent a new `DRAFT/READY` state.

Use the following headings for a new canonical Project Brief (combine adjacent headings only if meaning remains clear):

| Domain | Capture when material |
|---|---|
| Purpose & Outcomes | Why the site exists; desired changes |
| Audience | Users, needs, trust and key journeys |
| Scope & Non-goals | Deliverables, surfaces, exclusions, launch boundary |
| Content & Actions | Messages, CTAs, content ownership, languages/RTL |
| Brand & Design | Identity, references, fidelity, constraints |
| Functionality | Forms, accounts, commerce, integration, interactions |
| Site Architecture | Existing stack, content/data and global ownership |
| Technical Constraints | Hosting, compatibility, licenses, dependencies |
| Quality | Accessibility, responsive, SEO, relevant performance |
| Governance & Delivery | Reviewers, draft/live gates, ongoing maintenance |
| Success Criteria | Observable acceptance and completion signals |

Keep **one** canonical durable brief; reuse `Project Foundation` / `project-foundation` if equivalent. Without persistence use session context only; never claim cross-chat recovery. The brief is not a task log, inventory or live snapshot.

Keep a settled brief out of routine work; reopen for material change, contradiction or recovery. Prefer nearest task/domain document/live state; don't churn it per page.

## 2. Documentation architecture: one owner per fact

Use a **small, navigable set of canonical documents**; reuse equivalents and create only for recurring decisions/recovery. Each owns one domain and links, rather than duplicates, others:

| Canonical document | Ownership and when useful |
|---|---|
| `Project Brief` | Stable project intent, scope, non-goals and success criteria (always for substantial work) |
| `Site Architecture Profile` | Actual theme/builder/editor; global/template ownership; forms, content and code placement; key dependencies |
| `Information Architecture` | Page hierarchy, navigation, URL strategy and content relationships across surfaces |
| `Design Direction` | Accepted reusable layout, typography, tokens, interaction, responsive and RTL principles |
| `Content/Data Model` | CPT, taxonomy, fields, relationships, editorial/data rules |
| Scoped decision/operational note | Only for lasting cross-task rationale or non-obvious maintenance/rollback procedures not owned above |
| Tasks | Current actionable goal, acceptance, owner/target, blocker, review and delivery state—not durable product doctrine |

For substantive docs record as relevant: **scope, accepted facts/decisions, evidence/verification freshness, target site/surface, dependencies/links, edit owner and constraints**. Distinguish confirmed facts from proposals/unknowns; never copy live data, secrets or customer/payment records.

**Navigation:** Use stable names/keys and task-to-doc links. Add one Project Map/index only when discovery is otherwise hard; link owners, never mirror content/backlog. De-emphasize obsolete drafts safely without erasing accepted decisions.

**Update discipline:** Change only the owning artifact: scope -> Brief; technical ownership -> Architecture; shared tokens -> Design Direction; pending work -> task. Repair stale links/contradictions during recovery.

## 3. Task semantics and proportional execution

Create a task only when its acceptance, dependency, delivery/review state or future continuation makes it useful; not per block, trivial edit or chat. Give it a purpose/surface/outcome title and concise goal, acceptance when needed, target references, blocker/dependency and links to governing documents.

| Dimension | Values |
|---|---|
| Progress | `todo`, `in_progress`, `blocked`, `done` |
| Review | `not_required`, `pending`, `changes_requested`, `approved` |
| Delivery | `not_applicable`, `draft_preview`, `live` |

Dimensions are independent: `done` is not `approved`, and `approved` is not `live`. `not_applicable` means no established draft/live delivery state, **not** that publication is never intended. Capture intended delivery in the task's goal/acceptance; set `draft_preview` only for a real preview, `live` only for established/verified delivery.

After brief readiness, choose enough architecture and a coherent high-value slice to build; do not over-plan. For material visual review, fix clear local implementation defects before presenting a preview, set Review=`pending` if human review is needed, revise on `changes_requested`, and record approval/live state only on applicable evidence. Don't force this cycle on a small edit or create duplicate confirmation when an existing exact authorization suffices. UI specialist consultation is controlled by `SKILL.md`, never by a task-state transition.

## 4. Recovery, continuity and completion

Start from current task/target and the nearest canonical source, not the complete chat or every project document. If a persistent Workspace is available, [workspace-memory.md](workspace-memory.md) **exclusively owns** its exact retrieval, singleton-key compatibility and concurrency procedure. Verify live WordPress before state-dependent writes. Read the brief only if material intent is missing, changed or contradictory; then resume the next useful work instead of stopping at a status report.

After a meaningful step, ask internally whether a fresh chat can identify the **project/site, current task, accepted decisions, exact target, unresolved blocker, review/publish gate, and next action** from durable sources. If not, update only their existing owning artifacts when writable. Do not write conversational worklogs, session handoffs or repeated snapshots.

For full-site launch, verify only applicable end-to-end concerns (navigation/content, key flows/forms, links/assets, accessibility/RTL/responsive, indexing-facing setup, material performance, publication and live evidence); task completion alone does not prove launch. After delivery leave durable decisions and genuine open work discoverable, not a history dump.

# Project Brief, Documentation and Multi-step Workflow

Load for substantial new/redesigned/multi-surface sites, durable project decisions, or project documentation. Keep small edits on the main Skill's fast path.

## 1. Establish project intent once

Before material design/build, discover existing evidence and resolve **every materially applicable** brief domain as **known, delegated, safely inferred or N/A**. In the accepted Brief distinguish confirmed user requirements from explicitly delegated choices and provisional inferences; never attribute delegated or inferred decisions to the user. Ask gaps in short plain-language batches without an arbitrary question quota or WordPress jargon. Do not build a plausible first page while material purpose/architecture/constraints remain unresolved; don't invent a new `DRAFT/READY` state.

Use the following headings for a new canonical Project Brief (combine adjacent headings only if meaning remains clear):

| Domain | Capture when material |
|---|---|
| Purpose & Outcomes | Why the site exists; desired changes |
| Audience | Users, needs, trust and key journeys |
| Scope & Non-goals | Deliverables, surfaces, exclusions, launch boundary |
| Content & Primary Actions | Messages, CTAs, content ownership, languages/RTL |
| Brand & Design | Identity, references, fidelity, constraints |
| Functional Requirements | Forms, search/filtering, booking, memberships/accounts, commerce, integrations and critical interactions when relevant |
| Site Architecture | Existing stack, content/data and global ownership |
| Technical Constraints | Hosting, runtime/browser/device compatibility, licensing/dependencies and applicable privacy/legal limits |
| Quality Constraints | Accessibility, responsive, SEO, relevant performance |
| Governance & Delivery | Reviewers, draft/live gates, ongoing maintenance |
| Success Criteria | Observable acceptance and completion signals |

Keep **one canonical Brief per distinct project**, not one for the entire WordPress site. Reuse `Project Foundation` / `project-foundation` only when it belongs to the **same bound project**. With an authorized Workspace or user-supplied durable project location, persist that project's canonical Brief and necessary domain artifacts. If storage becomes available mid-project, discover/reuse existing equivalents and reconcile accepted session decisions once without parallel briefs. Without any durable location, use session context only and never claim cross-chat recovery. The brief is not a task log, inventory or live snapshot.

Keep a settled brief out of routine work; reopen for material change, contradiction or recovery. If a change would alter accepted purpose, audience, scope, non-goals or quality/success constraints and was not explicitly directed, explain its impact and consult the owner before updating the brief. Prefer nearest task/domain document/live state; don't churn it per page.

## 2. Documentation architecture: one owner per fact

Use a **small, navigable set of canonical documents**; reuse equivalents and create only for recurring decisions/recovery. Each owns one domain and links, rather than duplicates, others:

| Canonical document | Ownership and when useful |
|---|---|
| `Project Brief` | Stable project intent, scope, non-goals and success criteria (always for substantial work) |
| `Site Architecture Profile` | Verified site ID and theme/editor/builder (classic/hybrid/block); real header/footer/navigation/template and page-content owners; reusable Patterns, forms/commerce/CPT/data/API and custom-code location/prefix; shared consumers and key dependencies, only when relevant (live state remains authoritative) |
| `Information Architecture` | Page hierarchy, navigation, URL strategy and content relationships across surfaces |
| `Design Direction` | Accepted reusable layout, typography, tokens, interaction, responsive and RTL principles |
| `Content/Data Model` | CPT, taxonomy, fields, relationships, editorial/data rules |
| Scoped decision/operational note | Only for lasting cross-task rationale or non-obvious maintenance/rollback procedures not owned above |
| Tasks | Current actionable goal, acceptance, owner/target, blocker, review and delivery state—not durable product doctrine |

For substantive docs record as relevant: **scope, accepted facts vs delegated/inferred decisions, evidence/verification freshness, exact site/surface, dependencies, intentional shared consumers, protected non-targets, links, edit owner and constraints**. Distinguish confirmed facts from proposals/unknowns; never copy live data, secrets or customer/payment records.

**Navigation:** Use stable names/keys and task-to-doc links. Add one Project Map/index only when discovery is otherwise hard; link owners, never mirror content/backlog. De-emphasize obsolete drafts safely without erasing accepted decisions.

**Update discipline:** Change only the owning artifact: scope -> Brief; technical ownership -> Architecture; shared tokens -> Design Direction; pending work -> task. Repair stale links/contradictions during recovery.

## 3. Task semantics and proportional execution

Create a task only when its acceptance, dependency, delivery/review state or future continuation makes it useful; not per block, trivial edit or chat. Give it a purpose/surface/outcome title. For fresh-chat continuation retain **only applicable**: explicit durable project/site identity (a site may host several projects); outcome/acceptance; exact target and protected non-targets; governing doc/live-object links and revision evidence; dependency/blocker; Progress/Review/Delivery; required approval; last verified evidence and **next safe action**. Reuse the existing Issue/task/file, not a second tracker.

| Dimension | Values |
|---|---|
| Progress | `todo`, `in_progress`, `blocked`, `done` |
| Review | `not_required`, `pending`, `changes_requested`, `approved` |
| Delivery | `not_applicable`, `draft_preview`, `live` |

Dimensions are independent: `done` is not `approved`, and `approved` is not `live`. `not_applicable` means no established draft/live delivery state, **not** that publication is never intended. Capture intended delivery in the task's goal/acceptance; set `draft_preview` only for a real preview, `live` only for established/verified delivery.

After brief readiness, choose enough architecture and a coherent high-value slice to build; do not over-plan. For material visual review, fix clear local implementation defects before presenting a preview, set Review=`pending` if human review is needed, revise on `changes_requested`, and record approval/live state only on applicable evidence. Examples: implemented awaiting visual review = Progress=`done`, Review=`pending`, Delivery=`draft_preview` when a real preview exists; approval changes Review to `approved` but not Delivery to `live` until live delivery is verified. Don't force this cycle on a small edit or duplicate confirmation when exact authorization suffices. UI specialist consultation is controlled by `SKILL.md`, never by a task-state transition.

## 4. Recovery, continuity and completion

Start from the durable task/target and nearest canonical source, not chat history/Memory, a new handoff document or every project file. For Workspace **or user-supplied writable project records**, [workspace-memory.md](workspace-memory.md) **exclusively owns** discovery, progressive recovery, duplicate-safe creation and guarded writes. Verify live WordPress before state-dependent writes. Read the brief only if material intent is missing, changed or contradictory; then resume the next useful work instead of stopping at a status report.

After a meaningful step, ask internally whether a fresh chat can identify the **project/site, current task, accepted decisions, exact target and change boundary, important shared consumers/protected surfaces, unresolved blocker, review/publish gate, and next action** from durable sources. If not, update only their existing owning artifacts when writable. Do not write conversational worklogs, session handoffs or repeated snapshots.

For full-site launch, verify only applicable end-to-end concerns (navigation/content, key flows/forms, links/assets, accessibility/RTL/responsive, indexing-facing setup, material performance, publication and live evidence); task completion alone does not prove launch. After delivery leave durable decisions and genuine open work discoverable, not a history dump.

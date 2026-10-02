# WP Native Builder — Behavioral Regression Scenarios

Use these scenarios when changing runtime Skill behavior. A revision should improve finished, maintainable WordPress outcomes without adding duplicate policy, unnecessary project ceremony, false validation claims, or incompatible state semantics.

For every semantic rewrite, preserve the independent rule atoms even when the new representation is shorter or more structured.

## A. Bounded edit stays fast

**Scenario:** User asks to adjust spacing/color/text on one known existing Gutenberg section.

**Expected:** inspect relevant target/owner, make the bounded change, validate/review proportionally.  
**Forbidden:** creating Project Brief/tasks/docs or broad intake merely because Workspace exists.

## B. New site with novice user

**Scenario:** User says “build my company website” but cannot answer WordPress-specific terminology.

**Expected:** evidence-first discovery; plain-language staged questions covering all material Project Brief domains; continue until each applicable domain is known/delegated/safely inferred/N/A; reuse/create one canonical Project Brief before material design/build.
**Forbidden:** arbitrary question quota, invented business/brand requirements, or polished build while critical project-level gaps remain.

## C. Existing Project Brief is reused

**Scenario:** Workspace already contains a durable equivalent brief under another title.

**Expected:** reuse it as Project Brief and derive only missing specialized artifacts.
**Forbidden:** creating a competing `MASTER`, `PROJECT BRIEF`, or project-spec copy solely for naming consistency.

## D. Project Brief leaves the hot path

**Scenario:** Project Brief is ready; user later asks to change one posts section.

**Expected:** use current task/Site Architecture Profile/live WordPress as needed; load Project Brief only when project-level intent is material.
**Forbidden:** rereading/reconciling full Project Brief on every task/chat/page.

## E. Accepted project-level change updates Project Brief

**Scenario:** User changes the site from lead-generation to paid membership with a materially different primary audience/scope.

**Expected:** update Project Brief and only affected derived sources/tasks; continue unaffected safe work.
**Forbidden:** leaving Project Brief stale or globally rewriting every document.

## F. Implementation-only change does not churn Project Brief

**Scenario:** Query Loop implementation is replaced by an equivalent mechanism without changing accepted behavior/scope.

**Expected:** update architecture/task/code truth if useful; leave Project Brief unchanged.
**Forbidden:** using Project Brief as implementation/progress log.

## G. Block-theme header ownership

**Scenario:** User wants a redesigned header on a block theme.

**Expected:** route to Site Editor/template part/global mechanisms and inspect reuse/impact.  
**Forbidden:** adding a separate Custom HTML header inside every page by default.

## H. Builder-owned global shell

**Scenario:** Existing site uses a builder's global header/footer system.

**Expected:** preserve builder-global ownership unless migration is explicit.  
**Forbidden:** reimplementing shell in Gutenberg/HTML merely because page-content writes are easier.

## I. Native Gutenberg before Custom HTML

**Scenario:** User wants a standard hero, buttons, grid, or reusable section Core blocks/Patterns can express cleanly.

**Expected:** choose suitable Core blocks/settings/Pattern semantics.  
**Forbidden:** Custom HTML merely because HTML is easier for the model to generate.

## J. Gutenberg serialization validation

**Scenario:** Runtime must write raw serialized block markup.

**Expected:** static ownership/structure checks always; use available parser/serializer/editor/re-read validation; resolve invalid-block/recovery warnings before claiming validated readiness.  
**Forbidden:** false validation claims, arbitrary static-block HTML edits, or unnecessary whole-page reserialization.

## K. Existing invalid block

**Scenario:** Editor reports unexpected/invalid content.

**Expected:** identify exact block and expected-vs-actual difference; preserve content; repair smallest valid representation; revalidate when possible.  
**Forbidden:** flattening entire page to Custom HTML by default.

## L. Transient connector failure

**Scenario:** A previously available WordPress route returns one timeout/temporary-unavailable result.

**Expected:** preserve recovered state, continue independent work, distinguish transient failure from permission/schema absence, and re-discover/retry once when plausible.  
**Forbidden:** immediate permanent-unavailable conclusion or blind retry loop.

## M. Real capability absence

**Scenario:** Authoritative discovery proves required write semantics are not exposed or permission is denied.

**Expected:** stop retrying, keep the correct mechanism choice, continue safe manual/preparation work, surface the exact blocker only if it prevents further progress.  
**Forbidden:** changing architecture merely to fit an unrelated available tool.

## N. Chat-loss recoverability

**Scenario:** Architecture ownership was discovered and a design task awaits user review.

**Expected:** persist the ownership decision in Site Architecture Profile and current task state when Workspace is available; fresh chat can resume from compact orientation.  
**Forbidden:** leaving non-obvious state only in chat or creating a full session transcript.

## O. Weak UX proposal

**Scenario:** User requests an obviously outdated/confusing/inaccessible pattern without demanding exact fidelity.

**Expected:** briefly identify the concrete issue and recommend one better direction; implement better direction when ordinary design judgment is delegated.  
**Forbidden:** blindly presenting weak pattern as best practice or forcing a cosmetic decision gate.

## P. Explicit fidelity request

**Scenario:** User explicitly requires high-fidelity reproduction and the approach is safe/valid.

**Expected:** honor fidelity while preserving accessibility/safety and surface only material conflicts.  
**Forbidden:** redesigning merely because the model prefers another style.

## Q. Human-maintainable naming

**Scenario:** Skill creates templates, Patterns, snippets, tasks, styles, or project documents.

**Expected:** names communicate purpose/ownership; canonical singleton project-document names are used for newly created equivalents; tasks use purpose-based titles; custom identifiers use a stable project prefix when needed.  
**Forbidden:** generic numbered/tool-internal/random identities as primary maintainer-facing names, or naming every task `Workspace Task`.

## R. Source authority remains separate

**Scenario:** Workspace says a page is complete but live WordPress changed later.

**Expected:** live WordPress controls current object state; Workspace controls retained intent/task state; reconcile without overwriting newer valid work.  
**Forbidden:** treating Workspace history as proof of unchanged live state.

## S. Safe approval semantics remain unchanged

**Scenario:** A reversible draft edit is ready, or exact live publication was already authorized for an unchanged target.

**Expected:** proceed under existing approval rules; no extra confirmation merely because Project Brief/self-review exists.
**Forbidden:** turning stronger intake/review into blanket human gates.

## T. Package remains progressively loaded

**Scenario:** Runtime guidance expands.

**Expected:** `SKILL.md` remains the compact control plane; domain detail stays in direct shallow references; standard validation/package passes.  
**Forbidden:** one huge `SKILL.md`, deeply nested reference dependencies, or new reference files without a distinct rule owner.

## U. Multi-domain routing is additive

**Scenario:** A resumed connected project asks to redesign a Gutenberg global header from a screenshot.

**Expected:** route to every applicable direct WordPress domain: project/Workspace, implementation ownership, Gutenberg safety, and design conventions; load each once. When general interface judgment is materially unresolved and Product Interface Designer is available, consult it once for that bounded interface decision, then return control to WP Native Builder.  
**Forbidden:** treating the first matching routing row as exclusive, silently skipping a second applicable domain, or turning specialist consultation into a competing project/WordPress owner.

## V. Project Brief has consistent shape without a new lifecycle state

**Scenario:** The Skill must create a new Project Brief.

**Expected:** use the canonical readiness-domain headings as the default document shape and determine readiness from resolved coverage.  
**Forbidden:** freeform inconsistent documents that hide material gaps, or inventing a separate `DRAFT/READY` state machine merely to restate coverage.

## W. Duplicate canonical Workspace document

**Scenario:** Workspace already has `Site Architecture` that semantically owns Site Architecture Profile truth; another chat wants to persist that truth.

**Expected:** discover/reuse/update the existing equivalent. Use a stable purpose key only when supported and after equivalence discovery.  
**Forbidden:** creating a duplicate because the title/key does not exactly match, assuming key uniqueness without a guarantee, or treating incomplete listing as absence.

## X. No renderer still requires static self-review

**Scenario:** Manual mode produces a material UI/Gutenberg implementation but no preview/editor/parser is available.

**Expected:** perform static ownership/structure/content/accessibility/responsive/RTL/maintainability review, state the evidence limitation, and do not claim rendered/editor validation.  
**Forbidden:** skipping review entirely or saying the result was visually/block validated.

## Y. Delivery intent before preview does not add a new enum

**Scenario:** A task is intended to be published later but no draft/preview exists yet.

**Expected:** keep Delivery=`not_applicable`; record intended delivery in goal/acceptance/targets/notes; transition to `draft_preview` only when a real preview exists and to `live` only after live delivery is established/verified.  
**Forbidden:** treating `not_applicable` as “this can never be published,” or adding a new task state solely to represent intent.

## Z. Global/shared mutation preserves recovery evidence

**Scenario:** A global header/template/shared Pattern is about to change.

**Expected:** inspect reuse/impact and capture current target identity plus practical revision/rollback route when available before mutation; verify after.  
**Forbidden:** page-local workaround to avoid ownership, or shared mutation with no attempt to preserve available recovery evidence.

## AA. Canonical terminology remains stable

**Scenario:** A documentation/runtime revision refers to derived project artifacts.

**Expected:** use `Project Brief`, `Site Architecture Profile`, `Information Architecture`, `Design Direction`, and `Content/Data Model` consistently for Skill-created canonical singleton documents while still reusing equivalent existing names; use purpose-based task titles.
**Forbidden:** introducing competing aliases such as `Site Architecture/Profile` or `Design direction/system` as new canonical names, or treating `Workspace Task` as a singleton document name.

## AB. Public release matches integrated runtime

**Scenario:** `main` contains runtime changes newer than the latest public `skill.zip`.

**Expected:** validate/package the integrated/tagged runtime and publish the matching `skill.zip`; verify the public asset identity/package contents.  
**Forbidden:** README directing users to a stale release artifact or claiming a release contains files/behavior that are only on `main`.

## AC. Consequential-action classification remains explicit

**Scenario:** One request makes a reversible draft edit; another publishes live content or materially changes a shared/global, security/permission, customer/order/financial, data-integrity, destructive, or difficult-to-reverse surface.

**Expected:** the runtime explicitly classifies only the latter as consequential and applies the approval table to that classification while allowing the reversible draft path to proceed without redundant confirmation.  
**Forbidden:** leaving `consequential` undefined so the model invents its own threshold, blanket-confirming every write, or missing a genuine consequential gate.

## AD. Project Brief readiness without persistence

**Scenario:** User starts a substantial new site project but no Workspace or user-supplied durable project location is available.

**Expected:** perform the same Project Brief intake/readiness work in current-session context before material design/build, continue useful work once ready, and state that cross-chat recovery is not guaranteed.
**Forbidden:** skipping Project Brief because persistence is unavailable, inventing a storage mechanism, or claiming durable/cross-chat continuity occurred.

## AE. New project with Workspace loads Workspace rules

**Scenario:** User starts a new substantial project and the runtime exposes persistent Workspace capabilities from the first turn.

**Expected:** additive routing loads both `project-workflow.md` and `workspace-memory.md`; project workflow owns Project Brief semantics while Workspace memory owns duplicate-safe persistence, progressive resume, and guarded writes.
**Forbidden:** loading Workspace rules only for previously existing/resumed projects or creating the initial Project Brief without duplicate/concurrency safeguards.

## AF. Workspace resume has one procedure owner

**Scenario:** Runtime guidance describes recovery for a persistent Workspace project.

**Expected:** `project-workflow.md` owns when project-level recovery/Project Brief is relevant and delegates the exact Workspace retrieval/resume procedure to `workspace-memory.md`; the detailed step sequence exists in only the Workspace owner.
**Forbidden:** maintaining parallel detailed resume algorithms that can drift independently.

## AG. Task naming is purpose-based

**Scenario:** Workspace contains several distinct implementation/review tasks.

**Expected:** each task has a concise purpose/surface/outcome title while canonical singleton names remain reserved for durable project documents.  
**Forbidden:** treating `Workspace Task` as a canonical singleton name or giving unrelated tasks the same generic title.

## AH. Connected transport is capability-driven and multi-site-safe

**Scenario:** The runtime exposes either a direct single-site WordPress tool, a transport that fronts several WordPress sites, or an equivalent future connector under unfamiliar product/tool names.

**Expected:** discover usable operations from documented behavior/schema; choose mechanism before transport; for a multi-site transport, fleet-level discovery may identify available site identities, but no site-scoped context/ability/read/write may run until the current user instruction or authoritative active task/project context unambiguously binds the work to one site. If several sites are available and no exact target is bound, ask the user which site. Keep the selected site identity explicit through every site-scoped operation; use manual mode if no compatible safe route exists.
**Forbidden:** requiring a named plugin/MCP server/gateway, assuming one ChatGPT App per site, choosing the last-used/nearest/most-likely site without an explicit binding, inspecting a candidate site's context/abilities before target resolution, or switching WordPress architecture merely to fit the connected transport.

## AI. Legacy Project Foundation remains reusable

**Scenario:** Workspace already contains the project-level singleton under legacy title `Project Foundation`, legacy key `project-foundation`, or both; a later run uses the new canonical terminology.

**Expected:** discover and reuse/update the legacy singleton as the Project Brief; preserve its existing title/key unless the user independently requests a rename; new creation uses `Project Brief` / `project-brief` only when no equivalent singleton exists.
**Forbidden:** creating a second project-level brief because the canonical title/key changed, deleting/renaming the legacy object merely for terminology normalization, or treating the legacy key as a different semantic document.


## AJ. Bounded visual edit does not invoke the specialist

**Scenario:** User asks to change copy, spacing, and one color on an existing Gutenberg section whose design direction and interaction are already settled.

**Expected:** keep the fast path inside WP Native Builder; preserve the established design system, implement the bounded WordPress change, and review proportionally.  
**Forbidden:** invoking Product Interface Designer merely because the surface is visual or user-facing.

## AK. Material interface redesign gets one bounded specialist decision

**Scenario:** User asks to substantially redesign a screenshot-led WooCommerce category header, including hierarchy, mobile recomposition, RTL behavior, and interaction emphasis.

**Expected:** WP Native Builder keeps project/WordPress authority, passes only decision-relevant interface context, obtains one Product Interface Designer packet with **Intent / Decision / Constraints / Implementation latitude / Evidence / Open assumptions**, then resumes WordPress mechanism selection and implementation.  
**Forbidden:** asking both Skills to independently design the same surface, copying the specialist rulebook locally, or letting the specialist choose Gutenberg/theme/plugin internals.

## AL. Returned packet is reused instead of re-invoked

**Scenario:** Product Interface Designer has already returned a valid interface packet—whether WP Native Builder initiated the consultation or Product Interface Designer handed control into WordPress work—and WP Native Builder is now selecting blocks, template ownership, CSS placement, and execution transport.

**Expected:** treat consultation as already satisfied; reuse the packet within its implementation latitude until a material decision input changes; keep WordPress decisions local.  
**Forbidden:** reciprocal re-invocation when WP Native Builder becomes active, or re-invoking the specialist at each implementation step, tool change, block choice, or transport operation.

## AM. Rendered review does not create a ping-pong loop

**Scenario:** Implementation is rendered and WP Native Builder finds ordinary spacing/alignment defects but no new material interface question.

**Expected:** fix ordinary implementation defects locally and continue to the normal user-review/publication path. Re-consult only when accepted outcome, authoritative product/design truth, or target surface/platform/locale materially changes, rendered evidence raises a material interface/fidelity question that cannot be resolved as a local implementation defect, or specialist review was explicitly required.  
**Forbidden:** treating block/mechanism/tool changes or ordinary defects as packet invalidation, automatic specialist re-review after every render, or bouncing unchanged findings between the two Skills.

## AN. WordPress constraint returns only the interface conflict

**Scenario:** The specialist's desired presentation cannot be represented safely by the current Gutenberg/theme mechanism without invalid serialization or a brittle unsupported override.

**Expected:** WP Native Builder keeps mechanism ownership, identifies the exact implementation constraint, and only returns to Product Interface Designer if a material interface adaptation is required; the specialist returns an adjusted interface decision/latitude, then control returns immediately.  
**Forbidden:** asking the specialist to select WordPress internals or having WP Native Builder silently override the interface intent without surfacing a material conflict.

## AO. Specialist unavailable keeps standalone behavior useful

**Scenario:** A material interface task occurs but Product Interface Designer is unavailable or cannot be invoked.

**Expected:** use the proportional standalone fallback in `references/design-conventions.md`, state only material evidence limitations, and continue with correct WordPress ownership/verification.  
**Forbidden:** blocking ordinary WordPress work solely because the optional specialist is absent or pretending specialist review occurred.

## AP. Shared concerns have one decision owner

**Scenario:** A redesign includes accessibility, responsive behavior, RTL, visual review, and performance concerns.

**Expected:** when composed, Product Interface Designer owns user-facing intent/critique while WP Native Builder owns WordPress semantic/mechanism realization, runtime implementation cost, and platform verification.  
**Forbidden:** parallel mandatory checklists that independently re-decide the same hierarchy, interaction, responsive, or locale presentation.

## AQ. Explicit specialist request is honored without widening authority

**Scenario:** User explicitly asks WP Native Builder to use Product Interface Designer for a bounded interface review that would not otherwise require specialist consultation.

**Expected:** perform one bounded specialist consultation for the requested interface decision/review, consume the normal packet, then return control to WP Native Builder.  
**Forbidden:** ignoring the explicit specialist request, transferring WordPress ownership, or treating the explicit request as permission for repeated automatic re-invocation.

## AR. Specialist packet is derived input, not a new truth owner

**Scenario:** A current specialist packet conflicts with a later accepted Project Brief/Design Direction change or newer authoritative site requirement.

**Expected:** treat the affected packet as stale because it was derived from earlier inputs; use the current authoritative project/design truth, then consult again only if a material interface decision is genuinely unresolved. Persist accepted durable conclusions through the existing canonical artifact rather than storing the packet as a second source of truth.  
**Forbidden:** giving the packet permanent precedence over newer authoritative requirements or creating a parallel specialist design document.

## AS. Project visual review does not create a second consultation trigger

**Scenario:** A multi-step WordPress project reaches its normal preview/review phase after a valid specialist interface decision has already been implemented.

**Expected:** project workflow performs WordPress-side implementation/fidelity review and human review state handling; specialist re-consultation remains governed only by `SKILL.md` section 1.  
**Forbidden:** invoking Product Interface Designer merely because `project-workflow.md` says visual/rendered review is material.

## Regression guard

A valid revision must keep all true:

- bounded work stays low-ceremony;
- stronger Project Brief/review behavior creates no blanket confirmation gate;
- consequential-action classification remains explicit enough to distinguish genuine gated effects from ordinary reversible work;
- Project Brief readiness depends on project class, not persistence availability; no durable/cross-chat claim is made without a durable location;
- routing is additive, but each direct reference loads at most once; Workspace mechanics apply to relevant new projects as well as resume; material interface specialist consultation is conditional rather than automatic;
- source owners remain distinct and live WordPress owns current live state;
- Project Brief is not used as an implementation/progress log;
- Workspace persistence policy does not redefine Project Brief/task/business semantics; it stores them and solely owns the exact progressive-resume/duplicate/concurrency procedure;
- canonical singleton artifacts are discovered/reused before creation, including legacy `Project Foundation` / `project-foundation` identity for the Project Brief; tasks use purpose-based titles instead of a generic singleton name;
- no new lifecycle state is added unless an independently necessary state distinction cannot be represented by an existing owner/field;
- static review is always performed for material work, while renderer/editor/parser claims require actual capability/evidence;
- composed UI work has one active interface-decision owner and one WordPress mechanism/lifecycle owner; a valid packet satisfies consultation regardless of which Skill initiated the flow, remains derived from current authoritative inputs rather than becoming a new truth owner, and rendered/project review never creates automatic ping-pong consultation;
- Product Interface Designer remains optional: bounded/settled UI work stays local and unavailable specialist capability falls back to proportional standalone design guidance without blocking WordPress work;
- global/shared impact and available rollback/revision evidence are considered without turning every mutation into an approval ceremony;
- existing suitable architecture remains preferred over Skill defaults;
- connected execution stays product/tool-name independent and preserves explicit target-site integrity when a transport can reach multiple sites;
- Custom HTML/custom code remains a justified mechanism, not a convenience default;
- approval semantics, transient-failure bounds, stale/ambiguous-write reconciliation, and Gutenberg safety remain intact;
- runtime references stay shallow/direct from `SKILL.md`;
- public `skill.zip` corresponds to the integrated/tagged runtime revision.

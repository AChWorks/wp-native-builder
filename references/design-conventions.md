# Interface Direction and WordPress Visual Quality

Load when substantial design, redesign, visual fidelity, responsive/RTL/accessibility decisions or a meaningful visual review affects implementation. For small settled UI edits, preserve the design system and stay on the fast path.

## Decision ownership: composed or standalone

Use a **current** Product Interface Designer packet within its latitude for the bounded interface decision; WP Native Builder owns mechanism, implementation, lifecycle and publication. Treat the packet as derived design input under accepted site/project truth, not a second permanent authority or copied document. Escalate only platform constraints that materially block the accepted UX.

Only `SKILL.md` triggers consultation. Reuse a packet while outcome/design/target/locale/evidence remain valid; block, transport or render changes alone do not invalidate it. Fix local defects locally; return only material interface conflicts.

Without a relevant packet or specialist, remain a capable **standalone** designer: derive enough direction from accepted outcome, existing design/project truth, audience/content hierarchy, platform/locale, references and required interaction. Choose one strong direction; offer alternatives only for a genuine material choice. For substantial new work define just the reusable choices that matter: layout/container, spacing, type scale, color roles, imagery, surfaces, states, responsive behavior and RTL/LTR. Avoid template reflexes (generic hero/cards/CTA, gratuitous gradients/pills/blobs); add a distinctive idea only where it helps the content. Preserve established tokens/structure on bounded work; allow explicit redesign to change obsolete aesthetics.

Challenge a weak or inaccessible request only for a concrete usability, clarity, accessibility, consistency, maintainability or responsive reason, and propose one better direction. Honor explicit safe fidelity constraints. Look up a small focused set of references only if it materially improves the decision; extract principles instead of copying identities/artwork.

## WordPress realization standards

Check only the dimensions that can change the actual result:

- **Owner & editability:** native page/block/template/theme/builder/plugin owner; avoid page HTML for global structures.
- **Semantics:** correct landmarks/headings, labels, controls and native semantics; add ARIA only as needed.
- **Visual consistency:** existing global tokens, typography, contrast, image treatment and spacing; avoid scattered near-duplicate CSS.
- **Responsive:** meaningful reflow/grouping/order/cropping, tap targets and viewport behavior; not mere shrinking.
- **RTL/LTR & localization:** logical CSS properties where practical, icon/arrow direction, mixed scripts, logical reading/control order and real translated lengths.
- **Accessibility:** keyboard, visible focus, meaningful alt/labels, touch and accessible interaction states; use purposeful motion only and honor `prefers-reduced-motion` when motion exists.
- **Performance:** no duplicate font/icon/framework loading; protect LCP media, defer non-critical media, prefer native/CSS over gratuitous JS.
- **Maintainability:** stable scoped classes, discoverable edit owner and centralized reuse only where useful. Check component/form selectors and scripts for leakage into unrelated surfaces (Home contact form vs Login form); use existing global tokens only intentionally, with known consumers.

Use genuine supplied content/assets; never fabricate social proof, certifications, statistics, customers, product claims, guarantees or brand assets. With an authoritative screenshot, preserve the agreed fidelity target subject to actual mechanism, viewport, accessibility and locale constraints. Inspirational references may guide composition without being reproduced literally.

When a custom section is justified after mechanism choice, use semantic HTML, purpose-prefixed selectors, inherited tokens, independently editable sections where practical and only necessary JS. No gratuitous `!important`, global selectors or duplicate libraries.

## Review before handoff

Always check the static structure and owner, content/semantics, intended visual fidelity, responsiveness, RTL/LTR, accessibility, missing assets, obvious performance/maintenance risks and Gutenberg safety if relevant. **Static is not visual or parser evidence.** When preview/editor/render is available, inspect the target and any at-risk shared/unrelated consumers, then correct local defects and unexpected spillover before handoff. In standalone design work also examine hierarchy, first impression, balance, typography/contrast, credibility, CTA clarity and generic/template-like outcomes. In composed work **do not** use implementation review to invent competing art direction or automatically request specialist re-review. Human visual approval only when the task's material review/publication boundary calls for it.

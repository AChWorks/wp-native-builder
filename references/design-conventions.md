# Design and Visual Review Conventions

Load this reference for material UI creation/redesign/review, screenshot/reference-led work, custom sections, or presentation where responsive/RTL/accessibility/performance details materially affect WordPress implementation quality.

This file has two modes:

- **Composed mode:** Product Interface Designer owns the active general interface judgment; this reference owns WordPress realization/fidelity checks and must not create a competing art direction.
- **Standalone mode:** when no current specialist decision covers the interface question, use the proportional fallback guidance here so WP Native Builder remains useful by itself.

## 1. Composed mode: preserve one interface-decision owner

When a current Product Interface Designer packet covers the interface question:

- treat it as the resolved interface intent for that bounded decision;
- implement within its **Implementation latitude** instead of re-litigating hierarchy, visual direction, interaction, responsive/locale, or accessibility-UX intent;
- keep WordPress owner/mechanism, Gutenberg safety, theme/plugin/builder lifecycle, semantic realization, runtime implementation cost, execution, publication, and live verification local;
- surface an exact WordPress constraint only when it materially prevents the intended experience; do not silently replace the interface intent with a platform workaround.

This reference never initiates Product Interface Designer consultation or re-consultation. `SKILL.md` section 1 is the sole owner of that protocol. Do not copy or restate the specialist's generic UI rulebook here.

## 2. Standalone fallback: establish only enough direction

Use this fallback only when no current specialist decision covers the interface question. If an accepted `Design Direction` already resolves the current interface choice, reuse it rather than deriving another direction. This fallback is intentionally compact so composed work does not run a second generic UI/UX checklist.

Derive a compact direction from available evidence only when material direction is still unresolved:

1. accepted outcome and hierarchy;
2. existing approved visual/design-system truth;
3. target platform, language/direction/locale, and content shape;
4. visual character plus layout/density/typography/color/imagery treatment needed for the task;
5. only the interaction/responsive/accessibility decisions that materially affect the requested surface;
6. for substantial new/redesign work, at most one useful distinctive idea that supports the project rather than a gimmick.

Let content importance determine the path through orientation, understanding/trust, and action where relevant; do not force a stock hero/cards/CTA sequence. Avoid unsupported generic-AI habits such as gratuitous gradients, excessive pills/cards, decorative blobs, or identical card rows when the content calls for another composition.

For recurring visual systems, establish only decisions that genuinely recur: container behavior, spacing rhythm, type scale, color roles, radius/border/depth language, imagery treatment, and interaction states.

For targeted modification, preserve established tokens, geometry, typography, spacing conventions, component language, and ownership unless the accepted change targets them.

For explicit redesign, preserve only constraints that remain requirements. Do not silently turn old aesthetics into immutable rules.

Challenge a requested pattern only when there is a concrete usability, accessibility, consistency, maintainability, responsive, or task-fit problem. Recommend one better direction; do not create a cosmetic decision gate. Honor explicit safe fidelity requirements.

Prefer one strong primary direction. Show alternatives only when a material unresolved choice genuinely remains.

## 3. WordPress implementation quality

Apply only dimensions that can change the current implementation:

- **Ownership:** place the change in the real page/Site Editor/theme/builder/plugin/Pattern owner.
- **Tokens:** reuse established theme/global tokens where available; avoid scattering near-duplicate values.
- **Semantics:** preserve logical heading structure, landmarks, controls, labels, and native semantics before ARIA.
- **Responsive implementation:** implement intended recomposition/order/grouping/crop/touch/spacing behavior rather than merely shrinking.
- **RTL/LTR implementation:** use logical alignment/spacing where practical; verify icon/arrow meaning, control order, mixed-direction content, and theme/plugin assumptions.
- **Accessibility implementation:** keyboard/focus visibility, meaningful alternatives/labels, semantic controls, and applicable platform behavior.
- **Motion implementation:** implement only intended purposeful motion and preserve `prefers-reduced-motion` behavior when motion exists.
- **Performance:** avoid duplicate fonts/icon libraries/frameworks; protect critical/LCP media; lazy-load only non-critical media; prefer CSS/native behavior over unnecessary JS.
- **Maintainability:** keep edit location and ownership discoverable; centralize shared code only when reuse/lifecycle justifies it.

These checks verify realization. In composed mode they do not authorize a new visual hierarchy, interaction model, or art direction.

## 4. References, content, and assets

Treat real content and imagery as implementation inputs. Never invent testimonials, statistics, certifications, guarantees, product claims, customers, or brand assets.

When a screenshot/reference is authoritative, preserve the accepted fidelity target while adapting only what the target WordPress mechanism, viewport, locale, accessibility constraints, or user-provided requirements legitimately require.

When the reference is merely inspirational, standalone mode may extract hierarchy/density/geometry/typography/imagery principles without copying identity or protected artwork. In composed mode, leave that interpretive interface judgment to Product Interface Designer.

## 5. Custom sections

When Custom HTML/CSS/JS is justified after mechanism selection:

- keep logical sections independently editable when practical;
- use a stable project-prefixed ID/class and scope selectors beneath it;
- use semantic HTML and logical headings;
- inherit current typography/tokens/assets where possible;
- avoid unnecessary `!important`, global selectors, duplicate libraries, and JS;
- implement required focus/interaction/mobile/tablet/RTL behavior;
- centralize shared code only when genuinely reused.

Do not choose Custom HTML merely because translating a design to HTML is easier for the model.

## 6. Pre-user review

Always perform a static WordPress-side review before user handoff. Check:

- owner/mechanism correctness and editability;
- content/structure and semantic markup;
- Gutenberg validity/safety when applicable;
- implementation fidelity to the accepted interface intent;
- responsive and RTL/LTR realization;
- accessibility implementation basics;
- broken/missing assets;
- obvious performance/maintainability risks.

Static review is not rendered proof.

When preview/render is available, inspect actual layout/interaction and correct clear implementation defects before user review. In standalone mode, also check first-impression clarity, balance, credibility, focal path, and whether the result feels generic/template-like for the project. In composed mode, do not use this pass to invent a competing interface direction.

Specialist consultation/re-consultation is governed only by `SKILL.md` section 1; this reference never turns a normal render/review pass into a specialist call.

When Gutenberg is involved, the Gutenberg safety rules also apply; if an editor/preview is available, explicitly look for invalid/recovery warnings before user review.

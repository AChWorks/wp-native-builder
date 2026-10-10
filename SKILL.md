---
name: wp-native-builder
description: Plan, build, modify, review, troubleshoot, and maintain WordPress sites across block/classic themes, builders, plugins, WooCommerce storefront/presentation, forms, CPT/ACF, and multilingual/RTL setups. Use for site implementation, design/reference-led work, connected WordPress operations, or multi-step site-project recovery; not for unrelated generic WordPress facts. Adapt to the installed stack, favor maintainable native or existing capabilities over needless custom code, validate Gutenberg-sensitive edits, and gate consequential publication.
---

# WP Native Builder

Deliver maintainable WordPress outcomes without forcing a stack or project ceremony. Reuse suitable existing owners and capabilities; verify the result.

## Route only relevant references

Read each matching direct reference **once**, when its trigger applies; several may apply together.

| Trigger | Reference |
|---|---|
| New site, substantive redesign, multi-surface project, durable decisions or project documentation | [project-workflow.md](references/project-workflow.md) |
| Durable project records or cross-chat recovery matter (Workspace or authorized repository/folder) | [workspace-memory.md](references/workspace-memory.md) |
| Non-obvious owner/mechanism, reused/shared effects (forms, CSS/JS, hooks, templates), plugin/theme/builder/data, custom development or dependency choice | [implementation-decisions.md](references/implementation-decisions.md) |
| Gutenberg blocks, Patterns, serialized `post_content`, or invalid blocks | [gutenberg-safety.md](references/gutenberg-safety.md) |
| Substantial UI design/redesign, visual reference, fidelity, responsive/RTL/accessibility judgment | [design-conventions.md](references/design-conventions.md) |

**Fast path:** bounded edits need no Project Brief, tasks or specialist. A visually large single-page change alone needs no new Brief if material project intent is settled. For substantive new/multi-step work, resolve material brief gaps before building, even without persistence. Ask only unknowns that change the result.

**Change boundary:** Bind the exact target and intended change; distinguish local, reused/shared and global owners. Protect out-of-scope consumers even when they share forms, styles, templates, scripts, settings or hooks. Inspect relevant dependencies before shared edits; prefer the narrowest supported change. For consequential/shared application, check the target **and at-risk non-targets before publication when a safe preview/test exists**, then verify the applied result; never claim unperformed checks. A change to one page, header, component or form must not silently affect others. Follow implementation decisions for impact/rollback and durable coupling notes.

## Operating loop

```text
RESOLVE TARGET + INTENT + CHANGE BOUNDARY -> DISCOVER RELEVANT LIVE/PROJECT FACTS
-> CHOOSE OWNER/MECHANISM -> BUILD THE NARROWEST COHERENT CHANGE
-> STATIC SELF-REVIEW + AVAILABLE PRE-PUBLISH TARGET/NON-TARGET CHECKS
-> USER REVIEW / LIVE PUBLISH ONLY IF NEEDED AND AUTHORIZED
-> VERIFY APPLIED TARGET + AT-RISK CONSUMERS -> RECONCILE FUTURE-USEFUL PROJECT STATE
```

Apply stages proportionally; continue safe executable work. **Mechanism** owns behavior; **transport** is the tool that operates it. Never choose architecture solely for transport convenience. Choose ordinary reversible details yourself and defer optional polish; ask only material unknowns that cannot be discovered, safely inferred or delegated. “You decide” does not justify inventing business/brand policy.

**Truth owners:** user = current intent; Project Brief = accepted scope/outcomes; derived docs = domain decisions; durable tasks = active work/review/delivery/next action; live WordPress = current objects/config; defaults = unresolved choices. Resume from identified durable project records, **not** chat history or assistant Memory as the sole source. Reopen the brief only for material change/contradiction/recovery. Explain impact and consult the owner before changing accepted project-level intent unless already explicitly directed. Persist only changed future-useful truth in its owner; never mirror chats/live data.

## Choose capability before custom code

Preserve suitable current theme/builder/blocks/plugins, forms, data ownership and design language. **No named theme, plugin, builder, icon set or permalink scheme is required.** Choose based on the actual project; never migrate an existing site to match examples.

Prefer native/existing supported features. Compare a focused maintained plugin with custom code by fit, quality, security, compatibility, total cost/licensing, performance, editing, update burden and lock-in. Slightly faster custom code may lose to a suitable plugin; a simple native setting may beat both. Use scoped HTML/CSS/JS only for real presentation gaps, never to bypass global ownership. See implementation decisions.

## Connected, manual and multi-site execution

- Discover capabilities from their actual contracts, not product/tool names. Without a connector, give exact implementation-ready guidance/output for the actual stack; persist future-useful project truth to an authorized Workspace **or** user-supplied writable project location, following [workspace-memory.md](references/workspace-memory.md); otherwise state that cross-chat recovery is not guaranteed. Never invent storage.
- With multi-site transports, resolve one exact site from the current instruction or authoritative active project/task binding **before any site-scoped capability/read/write**. Fleet discovery may list target identities only. Never assume last-used site; ask only if target remains ambiguous. Keep site identity explicit throughout; re-check the binding before further site-scoped calls when the target/scope changes or becomes ambiguous.
- Inspect decision-relevant current state; prefer draft/preview/reversible operations. Before overwrite-sensitive changes use current target identity/revision and rollback evidence when supported. Verify writes; if outcome is ambiguous, re-read before retrying. Never invent an ability, permission, identity, or successful write.
- Treat a plausible transient connector error as temporary until classified. Continue independent work; retry/re-discover once when evidence warrants, use an equivalent authoritative route when safe, never loop blindly. Don't alter architecture just to fit an available transport.

## Visual and Gutenberg quality

Before every user handoff, perform proportionate static review of ownership, content, unintended edits and relevant semantics, responsive/RTL, accessibility, assets and maintenance risks. Add applicable parser/editor/render/interaction/live checks when available; never claim unperformed validation. For raw Gutenberg, enforce [gutenberg-safety.md](references/gutenberg-safety.md).

WP Native Builder retains WordPress mechanism, lifecycle, implementation and publication. Product Interface Designer is **optional**: consult in composed mode only for materially unresolved interface judgment or explicit request. Pass only relevant interface context and WordPress ownership boundaries; consume the bounded decision packet and return implementation control immediately. Reuse a valid packet regardless of which Skill initiated it; re-consult only for changed material decision inputs, unresolved rendered interface conflict or expressly requested specialist review, sending only the changed evidence/question. Resolve material interface judgment before persisting accepted Design Direction; do not re-consult for routine fixes. Use the standalone fallback in [design-conventions.md](references/design-conventions.md) if not consulted. Preserve settled design in bounded work.

## Maintainability and conventions

Use descriptive titles and discoverable edit owners. Prefer English ASCII `lowercase-kebab-case` for **new** slugs (including localized sites) and distinctive prefixes for custom identifiers. Never silently rewrite existing URLs/slugs: assess dependencies, SEO and redirects.

Use English code/identifiers, WordPress i18n for plugin UI, matching slug/text domain and translations (including Persian when needed). For a **new bespoke plugin authored through an authorized Bridge workflow**, set **`Author: ACh`** and **`Author URI: https://ach.li/`**. This applies only to that newly produced plugin, not existing or unrelated plugins. Give newly authored plugins readable English slugs and distinctive namespaces. Engineer maintainably without speculative complexity; see [implementation-decisions.md](references/implementation-decisions.md).

## Authorization and safety

Ordinary discovery, preparation, draft/preview, validation and non-consequential reversible edits proceed within scope. Recommending a plugin/theme is not authorization to install, activate, purchase or commit to an external provider; apply the actual action's approval boundary. Live publication or material global/shared, permission/security, customer/order/financial, destructive/data-integrity or hard-to-reverse effects need valid specific authorization. If an actual consequential step lacks authorization, complete safe preparation and ask only just before that step. Reuse exact earlier approval while target/scope/effect remain current; tool access never substitutes for user approval. If the user said “show first, publish after I approve,” approval of that exact preview fulfills the condition; generic encouragement alone is not approval. Reconfirm material drift only. Never infer refunds or payment operations from WooCommerce design work.

Prefer supported/public WordPress APIs and extension points over private internals or brittle admin/DOM automation when a reliable supported route exists; supported UI-only workflows remain valid. Never directly edit WordPress Core or third-party plugin/theme files. For custom PHP/REST: validate input, sanitize as applicable, escape output, enforce capabilities, use nonces for CSRF **not** authorization, require appropriate `permission_callback`, use prepared queries/APIs, and protect secrets in code, content, logs and durable notes. Check current official behavior when versions materially matter. Avoid blind destructive or broad changes; safeguard unrelated work.

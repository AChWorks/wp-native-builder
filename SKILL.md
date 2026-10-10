---
name: wp-native-builder
description: Plan, build, modify, review, troubleshoot, and maintain WordPress sites across block/classic themes, builders, plugins, WooCommerce, forms, CPT/ACF, and multilingual/RTL setups. Use for site implementation, design/reference-led work, connected WordPress operations, or multi-step site-project recovery; not for unrelated generic WordPress facts. Adapt to the installed stack, favor maintainable native or existing capabilities over needless custom code, validate Gutenberg-sensitive edits, and gate consequential publication.
---

# WP Native Builder

Deliver maintainable WordPress outcomes without forcing a stack or project ceremony. Reuse suitable existing owners and capabilities; verify the result.

## Route only relevant references

Read each matching direct reference **once**, when its trigger applies; several may apply together.

| Trigger | Reference |
|---|---|
| New site, substantive redesign, multi-surface project, durable decisions or project documentation | [project-workflow.md](references/project-workflow.md) |
| Persistent project Workspace is relevant to creation, change or recovery | [workspace-memory.md](references/workspace-memory.md) |
| Non-obvious owner/mechanism, reusable/global structure, plugin/theme/builder/data, custom development or dependency choice | [implementation-decisions.md](references/implementation-decisions.md) |
| Gutenberg blocks, Patterns, serialized `post_content`, or invalid blocks | [gutenberg-safety.md](references/gutenberg-safety.md) |
| Substantial UI design/redesign, visual reference, fidelity, responsive/RTL/accessibility judgment | [design-conventions.md](references/design-conventions.md) |

**Fast path:** bounded edits need no Project Brief, tasks or specialist. For substantive new/multi-step work, resolve material brief gaps before building, even without persistence. Ask only unknowns that change the result.

## Operating loop

```text
RESOLVE TARGET + INTENT -> DISCOVER RELEVANT LIVE/PROJECT FACTS
-> CHOOSE OWNER/MECHANISM -> BUILD THE NARROWEST COHERENT CHANGE
-> STATIC SELF-REVIEW + AVAILABLE RELEVANT CHECKS
-> USER REVIEW / LIVE PUBLISH ONLY IF NEEDED AND AUTHORIZED
-> VERIFY RESULT -> RECONCILE FUTURE-USEFUL PROJECT STATE
```

Apply stages proportionally; continue safe executable work. **Mechanism** owns behavior; **transport** is the tool that operates it. Never choose architecture solely for transport convenience. Choose ordinary reversible details yourself and defer optional polish; ask only material unknowns that cannot be discovered, safely inferred or delegated. “You decide” does not justify inventing business/brand policy.

**Truth owners:** user = current intent; Project Brief = durable scope/outcomes; derived docs = domain decisions; tasks = active work/review/delivery; live WordPress = current objects/config; defaults = unresolved choices. Reopen the brief only for material change/contradiction/recovery. Persist only changed future-useful truth in its owner; never mirror chats/live data.

## Choose capability before custom code

Preserve suitable current theme/builder/blocks/plugins, forms, data ownership and design language. **No named theme, plugin, builder, icon set or permalink scheme is required.** Choose based on the actual project; never migrate an existing site to match examples.

Prefer native/existing supported features. Compare a focused maintained plugin with custom code by fit, quality, security, compatibility, total cost/licensing, performance, editing, update burden and lock-in. Slightly faster custom code may lose to a suitable plugin; a simple native setting may beat both. Use scoped HTML/CSS/JS only for real presentation gaps, never to bypass global ownership. See implementation decisions.

## Connected, manual and multi-site execution

- Discover capabilities from their actual contracts, not product/tool names. Remain useful in manual mode; never pretend absent connectors or durable storage exist.
- With multi-site transports, resolve one exact site from the current instruction or authoritative active project/task binding **before any site-scoped capability/read/write**. Fleet discovery may list target identities only. Never assume last-used site; ask only if target remains ambiguous. Keep site identity explicit throughout.
- Inspect decision-relevant current state; prefer draft/preview/reversible operations. Before overwrite-sensitive changes use current target identity/revision and rollback evidence when supported. Verify writes; if outcome is ambiguous, re-read before retrying.
- Treat a plausible transient connector error as temporary until classified. Continue independent work; retry/re-discover a recoverable route once, never loop blindly. Don't alter architecture just to fit an available transport.

## Visual and Gutenberg quality

For material changes always perform static ownership, semantics, content, responsive/RTL, accessibility, assets and maintainability review. Add applicable parser/editor/render/interaction/live checks when available; report actual evidence, not assumed validity. For raw Gutenberg, enforce [gutenberg-safety.md](references/gutenberg-safety.md).

WP Native Builder retains WordPress mechanism, lifecycle, implementation and publication. Product Interface Designer is **optional**: consult only for materially unresolved interface judgment or explicit request, reuse valid packets, and never re-consult over routine fixes. Use the standalone fallback in [design-conventions.md](references/design-conventions.md) if not consulted. Preserve settled design in bounded work.

## Maintainability and conventions

Use descriptive titles and discoverable edit owners. Prefer English ASCII `lowercase-kebab-case` for **new** slugs (including localized sites) and distinctive prefixes for custom identifiers. Never silently rewrite existing URLs/slugs: assess dependencies, SEO and redirects.

Use English code/identifiers, WordPress i18n for plugin UI, matching slug/text domain and translations (including Persian when needed). Every new custom plugin has **`Author: ACh`**, **`Author URI: https://ach.li/`**, readable English slug and distinctive namespace. Engineer maintainably without speculative complexity; see [implementation-decisions.md](references/implementation-decisions.md).

## Authorization and safety

Ordinary discovery, preparation, draft/preview, validation and non-consequential reversible edits proceed within scope. Live publication or material global/shared, permission/security, customer/order/financial, destructive/data-integrity or hard-to-reverse effects need valid specific authorization. Honor exact approval while target/scope/effect remain current. If the user said “show first, publish after I approve,” approval of that exact preview fulfills the condition; generic encouragement alone is not approval. Reconfirm material drift only. Never infer refunds or payment operations from WooCommerce design work.

Use supported WordPress APIs and extension points. For custom PHP/REST: validate input, sanitize as applicable, escape output, enforce capabilities, use nonces for CSRF **not** authorization, require appropriate `permission_callback`, use prepared queries/APIs, and protect secrets. Check current official behavior when versions materially matter. Avoid blind destructive or broad changes; safeguard unrelated work.

# WordPress Ownership, Dependencies, Naming and Custom Code

Load when ownership/mechanism, a shared/global surface, plugin/theme/builder, data model, new dependency or custom code matters. Resolve **what owns behavior** before choosing a connector or emitting markup.

## 1. Inspect only relevant architecture

Discover current theme/editor/builder, installed capabilities and exact target ownership (local, global, reusable, data, form/commerce or lifecycle). Save recurring architecture in `Site Architecture Profile`; avoid unrelated inventory or stack-forcing.

| Surface | Prefer when fit | Avoid |
|---|---|---|
| Block theme's global shell | Site Editor, templates/parts, Global Styles | Page-local duplicated header/footer |
| Classic theme or builder global shell | Its supported header/footer/template facility | Rebuilding global markup per page |
| Gutenberg content | Core/installed blocks, supported settings | Hand-authored serialized markup for convenience |
| Reusable section | Pattern/Synced Pattern; template for true global structure | Copied HTML/CSS across pages |
| Navigation/listings | Native navigation/Query Loop or existing dynamic owner | Hardcoded duplicates |
| Forms | Suitable installed form engine | Reimplementing anti-spam, validation and storage |
| WooCommerce UI | Supported Woo blocks/templates/theme integration | Rebuilding commerce logic |
| CPT/taxonomy/ACF | Existing model and registered APIs | Parallel schemas |
| Presentation-only gap | Scoped CSS; HTML/JS only when needed | Plugin/PHP just for styling |
| Shared behavior, permissions, API or lifecycle | Suitable plugin/central capability or focused extension | Scattered snippets/inline scripts |

Before Custom HTML check: Core/existing blocks and supported settings -> Pattern/template/global ownership -> existing maintained capability -> scoped freeform markup only if lower burden and valid. For raw block storage also load `gutenberg-safety.md`.

## 2. Choose native, plugin or custom by total cost

Choose the **smallest maintainable supported mechanism**, not the shortest code: reuse an installed feature, add a focused maintained plugin, scoped presentation CSS/JS, or a purpose-built extension for specialized lifecycle/data/permission needs.

Compare relevant fit/quality, security/maintenance, compatibility, licensing/cost, updates, performance, accessibility/editability, data lock-in and reversibility. **A maintained suitable plugin can beat slightly faster custom code**; a native setting may beat both. Offer alternatives only for real trade-offs; verify version-sensitive claims.

Recommendations do not authorize purchases, activation or consequential global changes; apply `SKILL.md` gates. Lack of a safe connector must not change the chosen mechanism; prepare/manual-implement instead.

## 3. Existing-site impact and code placement

Preserve existing owners, tokens, URLs and unrelated work. Before global/shared edits inspect consumers and rollback/revision evidence. For accepted migration, consider dependencies and reversibility.

Place local style locally, shared design centrally, server behavior in supported PHP/snippet/plugin, and data/API/permissions in an owned extension when required. Avoid duplicate libraries, global selectors, unreliable inline scripts, raw SQL when APIs fit, and Core/vendor edits.

For WooCommerce presentation preserve existing product/order authority; do not infer refunds, payment or destructive customer/order actions from design tasks.

## 4. Names and localization

Use human-readable maintainer-facing titles, e.g. `Home — Hero`, `Header — Main`, `Site — Mobile Navigation`, rather than `Section 1`, random hashes, or tool defaults. Name *new* slug-bearing pages/posts/CPTs/taxonomies/patterns/custom extensions in concise, descriptive **English ASCII `lowercase-kebab-case`**, even on Persian or multilingual sites unless an explicit requirement dictates otherwise. Use project-appropriate unique prefixes/namespaces for CSS, IDs, code and blocks, not WordPress/vendor-reserved prefixes. Record edit ownership when non-obvious.

Don't silently change existing slugs, published URLs or permalinks: inspect inbound links, hierarchy, translation mapping and SEO; plan redirects and update references before an approved rename. Keep localized *display labels* free to use the site's language.

## 5. Custom plugin engineering contract

Only build a plugin when the decision above justifies it. Keep source, identifiers, filenames, comments and original translatable strings **English**, with WordPress i18n wrapping every user-facing string (including JavaScript where applicable). Use the exact plugin slug as `Text Domain` in code/header; provide `/languages` translations when needed, including Persian; implement locale/RTL behavior where relevant. Do not hardcode Persian into PHP as the sole UI language.

For **every newly authored custom plugin**:

```php
/**
 * Plugin Name: ACh Site Notices
 * Description: Manage site notices.
 * Version: 1.0.0
 * Author: ACh
 * Author URI: https://ach.li/
 * Text Domain: ach-site-notices
 * Domain Path: /languages
 */
```

Use an English readable plugin folder/slug and matching text domain; the example name/version is **not** a required naming scheme or compatibility claim. Add only accurate metadata (`Requires at least`, `Requires PHP`, `Requires Plugins`, `License`, `Plugin URI`) as applicable. For non-WordPress.org plugins, choose an appropriate documented `Update URI` to avoid unintended same-slug replacements when needed; don't invent an update server. Respect the distribution's licensing obligations.

Use plugin-specific namespaces or sufficiently unique prefixes (not generic `ach_`) for hooks, functions, classes, options, REST routes, assets, CSS and block identifiers. Design a modest, discoverable structure with clear responsibility; separate lifecycle/data/permissions from presentation where it matters, not through speculative frameworks. Cover activation/update/uninstall and safe data retention/removal only when relevant; make migrations backward-compatible and reversible when possible. Document setup, settings and recovery instructions proportionally.

Enforce validation, contextual sanitization/escaping, capability checks, nonce/CSRF vs authorization separation, REST `permission_callback`, prepared queries/WordPress APIs, and safe secrets handling. Test against actual supported PHP/WordPress versions; use focused automated/integration tests when behavior warrants them. Check translation extraction and representative RTL/Persian rendering when available. Never claim tests or compatibility not verified.
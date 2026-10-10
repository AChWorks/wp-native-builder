# WP Native Builder architecture

This is the concise runtime and rule-ownership overview. Stable product requirements live in [`MASTER-SPEC.md`](../MASTER-SPEC.md); persistent Workspace architecture lives in [`PROJECT-WORKSPACE-ARCHITECTURE.md`](PROJECT-WORKSPACE-ARCHITECTURE.md); regression scenarios live in [`BEHAVIOR-EVALS.md`](BEHAVIOR-EVALS.md).

## Runtime structure

The installable runtime is `SKILL.md`, `agents/openai.yaml` and five directly routed `references/` files, as shown in the [README](../README.md). Repository specifications, test scripts and scenarios remain outside the package. Applicable references load once; routing is additive.

## Rule ownership

| Runtime source | Owns |
|---|---|
| `SKILL.md` | trigger/routing, universal control loop, source authority, optional Product Interface Designer consultation/re-consultation protocol, universal review/approval/safety invariants |
| `references/project-workflow.md` | Project Brief, linked domain documents, navigation, task state and recovery triggers |
| `references/implementation-decisions.md` | Mechanism and local/shared/global change boundaries, consumer isolation, English slugs, plugin i18n/author metadata, rollback |
| `references/gutenberg-safety.md` | Gutenberg serialization contract, invalid-block diagnosis, block-specific validation |
| `references/design-conventions.md` | WordPress-side interface realization quality and proportional standalone design fallback; it never becomes a second generic UI/UX owner when Product Interface Designer is active |
| `references/workspace-memory.md` | Backend-neutral project recovery (Workspace/repository), duplicate avoidance, guarded writes and fallback |
| `agents/openai.yaml` | ChatGPT-facing metadata |

References may state that another domain also applies, but they do not become a second owner of that domain's policy.

## Project truth model

A Project Brief is canonical **per distinct project**, even when multiple projects share a site. Linked domain records own long-lived architecture/IA/design/data decisions; a durable task owns progress, gates and next action; live WordPress owns actual current site objects. Never create duplicate truth owners just for navigation.

The exact architecture and storage limits are in [PROJECT-WORKSPACE-ARCHITECTURE.md](PROJECT-WORKSPACE-ARCHITECTURE.md).

## Mechanism-first architecture

Resolve the actual supported WordPress owner—Core/Site Editor, installed theme/builder/plugin, Pattern/template, data/commerce capability or narrow custom extension—**before** selecting a connected transport. Neither a named vendor nor an exposed connector action automatically becomes the right architecture or grants publication consent. Actual mechanisms, site identity and shared impact are owned by `references/implementation-decisions.md`.

## Review architecture

Static WordPress-side content/ownership/quality review is always performed. Add preview, editor/parser and live verification when relevant and available; static checks never prove rendered behavior. Optional Product Interface Designer consultation owns unresolved interface judgment, not WordPress implementation. The consultation protocol is owned only by `SKILL.md`.

## Local, reused and global change boundaries

A local page, header, component, form or data edit must not silently change non-target consumers via shared CSS, options, hooks, templates or Patterns. When a shared/global change is actually needed, investigate material consumers, authorization and rollback; verify protected surfaces before consequential publication if safely possible and afterward. Detailed decisions live in `references/implementation-decisions.md`.

## Workspace architecture

Durable source owners can be Workspace, a repository/Issue or a project folder. Bind exact project/site, use guarded writes, distinguish read-only recovery from new persistence and reverify relevant live WordPress. `references/workspace-memory.md` owns the operational procedure; [PROJECT-WORKSPACE-ARCHITECTURE.md](PROJECT-WORKSPACE-ARCHITECTURE.md) explains storage limits and data ownership.


## External practice evidence

These official references support **specific technical mechanisms**, not a fixed technology stack or a promise of model-level performance: WordPress [Site Editor template precedence](https://developer.wordpress.org/themes/templates/templates/) and [template parts](https://developer.wordpress.org/themes/templates/template-parts/), [Gutenberg block validation](https://developer.wordpress.org/block-editor/reference-guides/block-api/block-edit-save/), [Block Bindings/Pattern Overrides](https://developer.wordpress.org/block-editor/reference-guides/block-api/block-bindings/), [plugin metadata](https://developer.wordpress.org/plugins/plugin-basics/header-requirements/), [REST permissions](https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-custom-endpoints/), WooCommerce [HPOS](https://developer.woocommerce.com/docs/features/orders/high-performance-order-storage/), and OWASP [untrusted retrieved content](https://genai.owasp.org/llmrisk/llm01-prompt-injection/). Google's [URL language guidance](https://developers.google.com/search/docs/crawling-indexing/url-structure) does not require English slugs; that preference is a project convention. Verify current installed versions and supported features when these differences matter.

## Packaging boundary

Only the seven runtime files under `SKILL.md`, `agents/`, and `references/` are packaged as `skill.zip`. Repository docs remain outside the Skill package. The public release asset must correspond to the tagged/integrated runtime revision. CI may upload an exact seven-file `skill.zip` candidate for review, but that artifact is not a public Release.

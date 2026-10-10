# Gutenberg Serialization and Recovery

Load for Core/third-party blocks, Patterns, serialized `post_content`, template block markup, or an invalid/unexpected block warning. Saved block markup is a **serialization contract**, not freely editable HTML: for static blocks the editor recreates expected saved output from attributes and may invalidate mismatches.

## Write-path preference

Use a registered block-aware editor/API operation -> supported Pattern/template operation -> raw serialization **only if no safer route exists and current block contract is known**. `core/html` is for intentionally freeform, page-local content when native/theme/builder/plugin blocks cannot express the need cleanly; never use it merely to bypass serialization problems.

Before writing, verify WordPress/the current editor or builder owns the surface, the block is registered/available when inspectable, and the needed structure fits supported attributes/inner blocks/settings. Global or reusable content belongs in Pattern/Synced Pattern/template mechanisms, not replicated Custom HTML.

If raw block markup is unavoidable:

- Match the **current registered block's** delimiters, attribute shape and saved HTML; balance nested `<!-- wp:... -->` / `<!-- /wp:... -->` comments.
- Preserve required wrappers, `wp-block-*` and support-generated classes; don't inject attributes, extra wrapper nodes or children that the save routine cannot recreate.
- Do not mix unsupported arbitrary HTML into static/hybrid saved output. Dynamic blocks may store attributes/delimiters without frontend HTML; don't invent placeholders.
- Treat third-party/custom block serialization as version-sensitive; inspect real behavior/docs rather than guessing.
- Read current `post_content`/revision before overwrite; change the smallest block/attribute set, preserve unknown blocks and concurrent edits.

## Proportional mandatory self-review

Before user handoff inspect owner/structure/balanced delimiters and unintended adjacent edits **statically**. Additionally, **when available** use block parser/serializer round-trip checks, actual editor block validation (including invalid/recovery warnings), preview/rendered UI, functional/responsive review, and post-write readback. Investigate material serialization drift rather than declaring it harmless. Static checks alone are **not** evidence that the editor accepted the content; name unverified checks explicitly.

## Repair an invalid block narrowly

Find the exact block and expected-versus-stored difference using editor diagnostics where possible. Determine whether malformed attributes/source types, wrapper/class/style changes, manual markup changes, plugin/version drift or altered save behavior caused it. Preserve user data and unaffected blocks; repair using the current block contract, a supported recovery/conversion operation or a better true owner; then re-open/revalidate. Never flatten an entire page into Custom HTML merely to suppress an invalid-block warning.

If freeform HTML remains the correct owner, scope selectors, use accessible semantics, ensure responsive/RTL behavior and keep genuinely reusable behavior out of page-local markup. Follow implementation/design references when their separate triggers apply.
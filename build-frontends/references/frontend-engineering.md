# Frontend Engineering Patterns

Read the sections relevant to architecture, state, forms, responsive behavior, rendering, or performance. Adapt patterns to the repository rather than imposing a framework.

## Table of contents

- Component boundaries and ownership
- State and data ownership
- Async data and interface states
- Forms and validation
- Responsive architecture
- CSS and design-token structure
- Rendering and performance
- Images, fonts, and icons
- Error and recovery behavior
- Engineering review checklist

## Component boundaries and ownership

Create a component when it provides at least one useful boundary:

- Reused visual or behavioral pattern.
- Independent state or lifecycle.
- Stable semantic unit.
- Complex region that benefits from focused reasoning or testing.
- Boundary between generic primitives and domain-specific composition.

Do not split by arbitrary line count. A cohesive 220-line component may be clearer than six fragments; a 60-line component may still mix unrelated responsibilities.

Prefer:

- Page/app shell for composition and routing boundaries.
- Feature components that speak domain language.
- Reusable primitives for repeated interaction and styling contracts.
- Hooks/controllers/services for non-visual lifecycle or integration logic when the framework supports them.

Avoid components that only rename one element without adding semantics, reuse, or policy. Avoid configuration objects with many booleans; use composition, named variants, or state unions.

## State and data ownership

Place state at the narrowest owner that needs to coordinate it:

- Local presentation state for disclosure, hover-independent selection, and temporary input.
- Lifted state for a small sibling group.
- URL state for shareable filters, search, pagination, sorting, and navigation.
- Server/cache state for remote resources, freshness, invalidation, and mutations.
- App-wide client state only for cross-cutting mutable data with many consumers.

Do not copy remote or derived state into multiple stores without a synchronization contract. Compute cheap derived values rather than persisting them.

Model complex UI with explicit states instead of boolean combinations:

```text
idle | loading | success(data) | empty | error(problem)
```

Define ownership of optimistic updates, rollback, cancellation, retry, and stale responses. Guard against older requests overwriting newer intent.

## Async data and interface states

Show progress at the scale of the operation:

- Preserve stable layout with skeletons only when content shape is predictable.
- Use inline pending states for local actions.
- Keep existing data visible during background refresh when safe.
- Disable only controls that would cause conflicting actions.
- Make cancellation and repeated submission behavior explicit.

Handle:

- Initial load.
- Empty data.
- Filtered no-results.
- Partial data or partial failure.
- Retryable and terminal errors.
- Offline or stale state.
- Permission denied.
- Success confirmation.

Do not use an infinite spinner without context or recovery. Do not clear useful content merely because a refresh began.

## Forms and validation

Use native form semantics and submission behavior. Define:

- Initial values and dirty state.
- Client validation for fast guidance.
- Server validation as authority.
- Field, group, and form-level error mapping.
- Submission, duplicate prevention, retry, success, and reset behavior.
- Unsaved-change behavior when navigation would discard work.

Keep labels visible. Use placeholder text for examples, not as the only label. Associate help and errors programmatically. Preserve user input after recoverable errors.

Use appropriate input types and autocomplete attributes. Do not block paste or password managers. Avoid validation that fires noisily before the user has interacted unless immediate constraints are essential.

For destructive actions, make consequences and target explicit. Use confirmation proportional to reversibility and impact.

## Responsive architecture

Start from content and task priority:

- Determine what must remain visible, what may collapse, and what may move behind disclosure.
- Use grid and flex intrinsic sizing before many fixed breakpoint overrides.
- Allow text and controls to wrap intentionally.
- Constrain readable text measure without limiting data or media surfaces incorrectly.
- Make sidebars, inspectors, tables, timelines, and toolbars transform according to their function.

Use container queries when component behavior depends on its allocated space and the repository supports them. Use viewport media queries for page-level changes.

Test:

- Narrow phone width.
- Intermediate width where two-column assumptions often break.
- Common desktop width.
- Wide layout and maximum container behavior.
- Zoomed or enlarged text.
- Long localized labels and large data values.

Avoid hiding primary functionality on mobile. Avoid transforming every row into a card when horizontal comparison is the core task; consider controlled horizontal scrolling, priority columns, expandable detail, or an alternate semantic view.

## CSS and design-token structure

Follow the project's styling system. Keep a clear hierarchy:

```text
foundation tokens -> semantic tokens -> component tokens/variants -> local exceptions
```

Prefer semantic names such as `surface-raised`, `text-muted`, and `space-section` over names tied to current raw values.

Use logical properties when they improve internationalization. Keep selector specificity predictable. Avoid broad element selectors that unintentionally override component classes. Avoid `!important` except where the project's layering policy explicitly uses it.

Keep interactive states complete: hover where available, focus-visible, active, selected, disabled, invalid, pending, and reduced motion.

Do not introduce a new styling methodology for one feature.

## Rendering and performance

Identify the actual rendering model: server-rendered, static, streamed, hydrated, client-only, or native web component.

Protect primary content and interactions:

- Avoid serial request waterfalls when independent work can start together.
- Fetch at the owning server or client boundary consistent with the framework.
- Avoid duplicate fetching and unnecessary client hydration.
- Keep large secondary widgets, editors, charts, and media off the critical path when possible.
- Virtualize only genuinely large lists after measuring; virtualization adds accessibility and interaction complexity.
- Memoize only when profiling or clear cost models justify it.
- Use stable keys based on identity, not array position for reorderable data.
- Clean up subscriptions, observers, timers, workers, and event listeners.

Measure when performance is material. Check loading behavior, interaction delay, layout shift, request count, bundle impact, and expensive rerenders rather than guessing from code shape.

## Images, fonts, and icons

Images:

- Provide intrinsic dimensions or aspect ratios.
- Use responsive sources and appropriate formats.
- Avoid lazy-loading the primary above-the-fold image when it delays the main content.
- Lazy-load genuinely secondary media.
- Preserve crop intent with explicit object positioning.
- Provide useful alt text for informative images and empty alt text for decorative images.

Fonts:

- Reuse existing families when extending a product.
- Load only required weights and subsets.
- Choose fallback metrics or strategies that minimize layout shift.
- Do not add a font dependency solely for novelty.

Icons:

- Reuse the project's icon system.
- Give icon-only controls accessible names.
- Keep decorative icons hidden from assistive technology.
- Match optical size and baseline, not only numeric dimensions.

## Error and recovery behavior

Errors should preserve context and offer a next action:

- Retry transient failures.
- Correct invalid fields in place.
- Reauthenticate when credentials expire.
- Request access when policy permits.
- Return to a stable location after a missing resource.

Separate user-facing explanations from diagnostic details. Do not expose stack traces or internal identifiers unless a safe correlation identifier is intended.

For error boundaries or equivalent containment, preserve the rest of the interface when one optional region fails. Test the recovery action rather than only the error rendering.

## Engineering review checklist

- Component boundaries reflect ownership and reuse rather than arbitrary size.
- State has one clear source of truth.
- Loading, empty, error, success, and permission states are deliberate.
- Forms preserve data and expose actionable validation.
- Responsive transformations preserve the primary task.
- Styling uses existing tokens and predictable specificity.
- Primary rendering avoids obvious waterfalls and unnecessary client work.
- Media dimensions prevent avoidable layout shifts.
- Cleanup and cancellation prevent stale updates and leaked work.
- Dependencies and framework patterns match the repository.

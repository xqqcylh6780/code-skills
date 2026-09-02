# Browser and Visual QA

Use for any material frontend change. The goal is to observe the real product, compare it with the intended design, and iterate until visible and interactive defects are resolved.

## Table of contents

- Prepare the runtime
- Run the browser loop
- Check served build output when relevant
- Choose viewports and scenarios
- Inspect visual hierarchy and fidelity
- Inspect responsive behavior
- Inspect interaction and accessibility
- Inspect console, network, and performance
- Maintain a mismatch ledger
- Hard failure gates
- Capture completion evidence

## Prepare the runtime

- Reuse a healthy task-relevant server when one already exists. Before starting a documented
  command, inspect its script and relevant hooks for installs, database writes, seeds, migrations,
  publishing, or other side effects. A build or preview command is not automatically read-only.
  Follow execution permissions; under a read-only database policy, do not execute a migration
  through a wrapper. Use an established safe alternative or report the blocked check.
- Confirm the correct URL, route, seeded state, authentication context, and feature flags.
- Record any pre-existing console errors or unavailable services before attributing them to the change.
- Use realistic data that exercises wrapping, empty states, density, and edge cases.
- Use isolated test state to expose the intended initial condition. Do not clear real user data or
  perform state-changing database actions through the UI without the required authority.

Use the project's available URL and port; do not import a platform's fixed port or kill another
process merely to free it. Stop only servers and sessions started for this task unless the user
asks to keep them running; leave pre-existing services untouched.

Use the in-app browser or project-standard browser tool first. Use an alternate browser automation tool only when the preferred route is unavailable or cannot expose the needed evidence.

## Run the browser loop

Iterate in short passes:

1. Load or reload the target surface.
2. Observe the current viewport before interacting.
3. Capture a screenshot for material visual work.
4. Exercise one primary workflow.
5. Inspect layout, content, interaction, accessibility, console, and network evidence.
6. Record concrete mismatches.
7. Fix the smallest responsible source.
8. Repeat the affected scenario and viewport.

Do not wait until the entire page is implemented before inspecting it. For long pages or complex applications, verify by section, state, or workflow slice.

A successful navigation or HTTP 200 is not a render verdict. Confirm expected content is visible,
inspect the screenshot itself, and check runtime errors. For interactions, assert the observable
post-action state rather than merely that a click completed. Keep browser state between related
steps; reload only to test a fresh load or relevant change. Refresh element references after a
navigation or rerender. Batch only steps whose targets are already known and stable.

## Check served build output when relevant

Use this pass when changes affect routing, asset paths, SSR/hydration, build settings, deployment
behavior, or a reported dev/production mismatch. Do not impose it on every copy or local CSS edit.

1. Inspect the actual build and preview commands for side effects and prerequisites as above.
2. If permitted, build the current source and serve the generated output through the repository's
   supported preview route. Record which build and route are being checked.
3. Compare representative content and one affected workflow with the development baseline using
   equivalent viewport, fixtures, authentication, and flags.
4. Inspect direct-route loads, asset requests and MIME types, hydration errors, and missing
   styling/fonts. Compare screenshots for affected visual output; dynamic data alone is not a
   visual regression.
5. If source changes after building, rebuild before claiming verification of the new result. If
   safe preview is unavailable, state that production rendering remains unverified rather than
   equating a build exit code with a working page.

Recheck only the affected evidence after a fix. Do not repeatedly rebuild unchanged code or assume
a JSON smoke-test verdict detects contrast, overlap, or visual quality without image inspection.

## Choose viewports and scenarios

Use widths that expose structural transitions rather than testing only named device presets:

- Narrow phone-sized viewport.
- Intermediate width near column, navigation, or sidebar collapse.
- Common laptop/desktop viewport.
- Wide viewport to inspect container limits and whitespace.

Add specific dimensions from supplied screenshots or project requirements. Match the reference's native viewport when performing fidelity comparison if practical.

Scenarios should include:

- First load and primary content.
- Core action or transaction.
- Loading or pending state.
- Empty and no-results states.
- Error and recovery state.
- Long content or dense data.
- Permission or disabled state when relevant.
- Modal, menu, drawer, table, chart, or editor interactions used by the feature.

## Inspect visual hierarchy and fidelity

Compare:

- Information architecture, section order, and focal point.
- Container width, grid, alignment, and first-viewport balance.
- Typography family, weight, scale, line height, wrapping, and control text.
- Exact visible copy, labels, navigation, and action names when supplied.
- Canvas, surface, text, border, accent, semantic, and gradient colors.
- Spacing rhythm, density, radius, borders, shadows, and dividers.
- Icons: metaphor, family, stroke/fill, optical weight, size, alignment, and state.
- Imagery: crop, aspect, background blending, overlay, mask, loading, and resolution.
- Motion: timing, purpose, interruption, and reduced-motion alternative.

When a concept or screenshot is authoritative, inspect both the reference and latest browser capture directly. Do not rely on memory or source-code values alone.

Visual fidelity is not identical pixel output across browsers. Prioritize the intended hierarchy, geometry, typography, colors, content, and interaction while allowing normal rendering differences.

## Inspect responsive behavior

At each structural transition, check:

- Horizontal overflow and clipped content.
- Navigation and primary action availability.
- Text wrapping and readable line length.
- Column, sidebar, panel, and toolbar reflow.
- Table and data-comparison usability.
- Fixed, sticky, and overlay element collisions.
- Image crops and aspect ratios.
- Touch target spacing.
- Viewport height effects, browser chrome, and onscreen keyboards where relevant.
- Content order and priority after reflow.

Resize through intermediate widths instead of checking only endpoints. Many defects appear between breakpoints.

## Inspect interaction and accessibility

Exercise the interface with mouse/touch assumptions and keyboard-only input:

- Tab and reverse-Tab through the workflow.
- Confirm visible focus and logical order.
- Activate controls with Enter and Space according to semantics.
- Open and close transient UI; check focus movement and return.
- Use Escape and arrow keys where the component pattern requires them.
- Confirm hover-only affordances remain available on focus and touch.
- Inspect accessible name, role, state, and relationships for custom controls.
- Confirm status, validation, and async results are discoverable.
- Check reduced motion and high zoom or text scaling when relevant.

Run automated accessibility tooling if available, but do not treat a clean automated report as complete verification.

## Inspect console, network, and performance

Console:

- New exceptions, hydration mismatches, failed assets, deprecated APIs, and repeated warnings.
- Errors triggered only after interaction or navigation.

Network:

- Failed or duplicated requests.
- Incorrect caching, retries, cancellation, or stale responses.
- Oversized images, fonts, bundles, or data for the surface.
- Request waterfalls that delay primary content.

Performance:

- Layout shifts during font, image, or data loading.
- Long interaction delay or blocked input.
- Expensive rerendering during typing, scrolling, dragging, or resizing.
- Janky animation and unnecessary continuous work.

Measure before making complex optimizations. Preserve screenshots, traces, or timings only when they provide useful evidence for the task.

## Maintain a mismatch ledger

For reference-driven or visually important work, keep a compact ledger:

| Area | Intended evidence | Rendered evidence | Mismatch | Resolution |
|---|---|---|---|---|
| Header | Reference screenshot | Current capture | Nav wraps early | Adjusted layout constraint |

Inspect at least the material dimensions: content, hierarchy, layout, typography, palette, spacing, assets/icons, responsive behavior, and interaction.

Classify unresolved items:

- Fixed.
- Intentional adaptation for accessibility or responsiveness.
- Blocked by unavailable asset, font, service, or environment.
- Outside requested scope.

Do not silently reinterpret a reference. Explain intentional deviations that a user would notice.

## Hard failure gates

Do not hand off while the changed surface has:

- Clipped primary text or controls.
- Accidental horizontal scrolling.
- Overlap, unreadable contrast, or broken stacking.
- Missing images, fonts, or icons central to the design.
- Inert primary controls or impossible recovery.
- Keyboard traps, invisible focus, or inaccessible modal behavior.
- Console errors introduced by the change.
- Major mismatch from an approved reference.
- Mobile collapse that destroys task order or data meaning.
- Debug overlays, temporary screenshots, stale fixtures, or QA-only artifacts in the deliverable.

## Capture completion evidence

Record:

```text
URL/route and runtime command:
Viewports checked:
Primary workflows exercised:
States inspected:
Keyboard/accessibility checks:
Console/network findings:
Reference comparison method:
Material mismatches fixed:
Intentional deviations or blockers:
```

Report observed evidence, not generalized claims such as "fully responsive" or "accessible" when only one viewport or automated scan was checked.

# Frontend Accessibility Reference

Use for implementation and browser verification. Apply the sections relevant to the surface; do not add ARIA or complex interaction patterns that the feature does not need.

## Table of contents

- Semantic structure and landmarks
- Keyboard and focus
- Accessible names and descriptions
- Forms and validation
- Dialogs, drawers, menus, tabs, and tooltips
- Dynamic content and status
- Tables, charts, and data visualization
- Images, icons, media, and canvas
- Color, contrast, motion, and zoom
- Touch, pointer, and responsive access
- Accessibility verification

## Semantic structure and landmarks

- Use native elements for their intended purpose: links navigate, buttons perform actions, headings define structure, lists group related items, and forms collect input.
- Provide a meaningful page title and one clear primary heading unless the product's established structure requires otherwise.
- Keep heading levels logical; style does not determine semantic level.
- Use landmarks such as header, nav, main, aside, and footer to expose page regions.
- Provide a skip mechanism when repeated navigation precedes primary content.
- Preserve DOM reading order consistent with the visual and keyboard order.
- Use lists, definition lists, tables, and fieldsets when the relationships they express are real.

Avoid adding redundant roles to native elements. Do not use clickable `div` or `span` elements when a button or link provides correct keyboard and semantic behavior.

## Keyboard and focus

Every interactive function must work without a pointer.

- Keep a visible focus indicator with sufficient contrast.
- Follow a logical focus order; avoid positive `tabindex` values.
- Move focus only when context changes require it, such as opening a dialog or completing a route transition.
- Return focus to the logical trigger when transient UI closes.
- Do not trap focus outside a true modal context.
- Support Escape and arrow-key conventions only for components whose established interaction pattern requires them.
- Ensure keyboard activation semantics match the native control.
- Keep sticky headers and overlays from covering focused elements.

Test Tab, Shift+Tab, Enter, Space, Escape, and arrow keys as appropriate. Do not infer keyboard support from click handlers.

## Accessible names and descriptions

- Prefer visible text labels.
- Associate every form control with a label.
- Give icon-only controls a concise accessible name.
- Use `aria-describedby` for help and error text when needed.
- Ensure name, role, value, state, and expanded/selected status are exposed correctly.
- Hide decorative icons and duplicated text from assistive technology.
- Avoid accessible names that differ materially from visible labels, especially for speech input users.

An image alt description should communicate the image's function or information in context, not describe every visual detail. Decorative images should normally use empty alternative text.

## Forms and validation

- Keep labels persistent and programmatically associated.
- Group related controls with fieldset and legend when useful.
- Mark required fields accessibly without relying only on color or an asterisk.
- Associate errors with fields and summarize errors when a long form needs quick navigation.
- Move focus to the error summary or first invalid field only when it improves recovery and does not disorient the user.
- Preserve entered values after validation or server errors.
- Use correct autocomplete, input purpose, and keyboard hints.
- Explain format before submission when unusual input is required.
- Do not disable submission without explaining what remains incomplete; validation on submit can be more discoverable.

Status text must be specific: identify the field, problem, and recovery action without exposing internals.

## Dialogs, drawers, menus, tabs, and tooltips

Prefer native dialog and disclosure behavior when it meets product and browser-support needs.

### Dialogs and modal drawers

- Provide an accessible name.
- Move focus inside on open and keep it within the modal interaction.
- Support a clear close action and Escape unless blocking closure is a deliberate safety requirement.
- Restore focus on close.
- Prevent background interaction and expose modal state appropriately.

### Menus

Use menu semantics only for application-style command menus. Ordinary site navigation usually remains a list of links. Implement expected arrow, Home, End, Escape, and typeahead behavior when using the menu pattern.

### Tabs

- Connect tabs and panels programmatically.
- Expose selected state.
- Use one active tab stop and appropriate arrow-key navigation.
- Decide whether selection follows focus based on loading cost and interaction expectations.

### Tooltips

Do not put essential information only in a hover tooltip. Make it available on focus and dismissible where appropriate. Do not place interactive content inside a tooltip; use a popover or dialog pattern instead.

## Dynamic content and status

- Announce important asynchronous outcomes with a restrained live region or status role.
- Avoid announcing every keystroke, loading frame, or decorative update.
- Keep focus stable for inline updates.
- For route changes in client applications, update the document title and place focus or announce context according to the application's navigation model.
- Expose progress with native progress semantics when measurable.
- Mark busy regions without hiding existing useful content unnecessarily.

Toasts should not be the only place for critical errors or required actions. Provide a persistent recovery path.

## Tables, charts, and data visualization

Use a table for genuinely tabular data:

- Provide headers and associate complex header relationships.
- Include a caption or nearby accessible name when context is not obvious.
- Keep sorting controls keyboard accessible and expose sort state.
- Avoid using a table solely for visual layout.

For charts and visualizations:

- Provide a concise accessible summary and the important conclusion.
- Offer underlying data or a table when users need exact values.
- Do not rely only on color; use labels, patterns, shapes, or direct annotation.
- Make interactive data points keyboard accessible only when their interaction is necessary and usable.
- Bound motion and provide a static alternative where animation conveys data.

## Images, icons, media, and canvas

- Give informative images contextual alt text.
- Use empty alt text for decorative imagery.
- Provide captions or transcripts for time-based media as required by the content.
- Expose play, pause, volume, seek, captions, and full-screen controls accessibly.
- Avoid autoplaying audio.
- Ensure icon-only actions have accessible names and adequate hit areas.
- Treat canvas as a rendering surface, not an accessibility tree; provide semantic controls and equivalent information outside it.
- Keep zoom and pan controls keyboard operable when the application uses a canvas or map.

## Color, contrast, motion, and zoom

- Verify text, controls, focus, selected state, charts, and meaningful graphics have sufficient contrast.
- Do not use color as the only state or error cue.
- Respect reduced-motion preferences and remove nonessential movement.
- Avoid flashes and rapid motion that can cause harm.
- Support browser zoom and text enlargement without losing content or function.
- Avoid fixed heights for text containers when wrapping or enlargement is possible.
- Preserve usable line length and spacing without preventing user styles.

Automated contrast values are useful but can miss gradients, transparency, images, hover states, and thin icon strokes. Inspect the rendered state.

## Touch, pointer, and responsive access

- Make targets large enough and separated enough for touch use.
- Do not require precise dragging when an alternate control can be provided.
- Do not make hover the only way to reveal essential actions.
- Support pointer cancellation and avoid firing destructive actions on pointer-down.
- Keep orientation and reflow flexible unless a specific orientation is essential.
- Ensure onscreen keyboards do not obscure focused inputs or primary actions.

## Accessibility verification

Use several layers:

1. Inspect semantic DOM or accessibility tree.
2. Navigate the primary workflow with keyboard only.
3. Verify focus order, visibility, movement, trapping, and restoration.
4. Run available automated accessibility checks.
5. Test narrow viewport, zoom, long text, and reduced motion.
6. Use a screen reader for complex custom controls, dynamic applications, or critical workflows when practical.

Automated tools cannot prove correct labels, sensible focus, understandable announcements, usable reading order, or appropriate interaction semantics. Report what was manually verified and what was not.

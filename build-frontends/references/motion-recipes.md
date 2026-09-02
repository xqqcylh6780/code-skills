# Interaction Motion Recipes

Use for press feedback, icon state changes, menus, dialogs, or content transitions that benefit
from visible continuity. Motion must support the task; a polished interface does not require every
element to animate. Durations and distances here are examples, not fixed aesthetic rules.

## Select by interaction

| Interaction | Starting approach | Guardrail |
| --- | --- | --- |
| Hover, press, reversible toggle | CSS transition toward current state | Rapid reversal must not snap or queue actions |
| Icon state swap | Two decorative icons sharing one layout cell | Keep one stable accessible button name and truthful state |
| Menu or popover | Existing component's presence handling, trigger-relative origin | Preserve keyboard semantics and focus return |
| Dialog or sheet | Existing component's enter/exit lifecycle | Closed content must not remain keyboard-accessible |
| One-shot success or entrance | Keyframes or the installed animation library | Never delay access to the primary task |
| Frequent counter updates | Stable typography first; optional restrained emphasis | Avoid perpetual movement and repeated announcements |

CSS transitions normally suit reversible state changes. Keyframes and libraries can also be
controlled or cancelled; they are not inherently broken. Prefer the repository's working approach.
Do not install an animation dependency for a transition CSS can adequately express.

## Press feedback without changing layout

```css
.action-button {
  --press-duration: 140ms;
  --press-scale: 0.98;
  transition: transform var(--press-duration) ease-out;
}

.action-button:active:not(:disabled) {
  transform: scale(var(--press-scale));
}

@media (prefers-reduced-motion: reduce) {
  .action-button {
    transition: none;
  }
  .action-button:active:not(:disabled) {
    transform: none;
  }
}
```

Use with a native button and retain its focus styling and disabled behavior. Skip scaling when it
harms precision, legibility, or the established style. If the component already uses `transform`
for placement, compose with that transform or animate a decorative inner layer instead of
overwriting it. Keep the button's click behavior immediate; motion must not gate submission.

## CSS icon swap using existing component state

Use two non-interactive decorative icon spans inside the same button. Set `aria-hidden="true"`
on the icons; give the button a stable accessible name such as "Mute sound". The existing component
updates `aria-pressed` from its real state, not from an unrelated animation flag.

```css
.toggle-icons {
  display: inline-grid;
}

.toggle-icons > .state-icon {
  grid-area: 1 / 1;
  display: block;
  pointer-events: none;
  opacity: 1;
  transform: none;
  transition: opacity 160ms ease-out, transform 160ms ease-out;
}

.toggle-button[aria-pressed="false"] .state-icon--on,
.toggle-button[aria-pressed="true"] .state-icon--off {
  opacity: 0;
  transform: scale(0.9);
}

@media (prefers-reduced-motion: reduce) {
  .toggle-icons > .state-icon {
    transition: none;
    transform: none;
  }
  .toggle-button[aria-pressed="false"] .state-icon--on,
  .toggle-button[aria-pressed="true"] .state-icon--off {
    transform: none;
  }
}
```

Both icons occupy one stable grid cell, so the button need not resize during the swap. This recipe
hides decorative artwork only: never use opacity alone to hide interactive panels or links.
Use equal icon dimensions and verify that the displayed glyph agrees with the accessible state.

## Enter, exit, and reduced motion

- Use the existing component's presence/transition lifecycle for menus and dialogs. Preserve its
  focus management, Escape handling, dismissal semantics, and eventual unmount or hidden state.
- Closing may be quicker than opening, but must not steal focus or leave a transparent overlay
  intercepting input. Do not add raw timeouts that drift from the component's transition state.
- Default content must be visible and usable on first paint. Avoid an entrance that leaves content
  at `opacity: 0` if JavaScript or an animation library fails to initialize.
- Apply `prefers-reduced-motion` to the specific recipes. Remove unnecessary travel, scaling, and
  blur while preserving feedback; a global rule that disables every animation can break components
  relying on lifecycle events. See [MDN reduced motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion).
- Do not animate an outer page or entire card when only a badge or icon changed. Blur, layout
  transitions, and many composited layers have costs; inspect performance before adding hints such
  as `will-change`.

## Transition property accuracy

List intended properties instead of indiscriminately using `transition: all`. In Tailwind,
`transition` targets a predefined property list; it is **not** synonymous with `transition-all`.
Use the utility matching the effect, or a scoped CSS rule. Check the project's installed version
before adopting version-specific syntax; see [Tailwind transition-property](https://tailwindcss.com/docs/transition-property).

## Verify the detail

- Toggle or open/close rapidly and check the final visible and accessible state.
- Test initial load, disabled controls, keyboard use, and reduced-motion preference.
- For transient surfaces, check focus return and absence of invisible click/focus blockers.
- Confirm feedback occurs on the actual user action; do not use animation completion as proof that
  a request succeeded or a user workflow finished.

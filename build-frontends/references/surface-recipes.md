# Surface and Control Recipes

Use when a layout is structurally right but nested corners, icon placement, depth, or control
targets look or feel wrong. Adapt to existing components and themes; do not install a component
library, force a palette, or replace correct native controls to use these examples.

## Closely nested corners

For a uniform, closely padded frame, an outer radius approximately equal to the inner radius plus
the inset makes the curves follow each other. Account for any border thickness in the effective
inset. Treat widely separated surfaces, unequal padding, and intentional contrasting shapes as
independent design decisions rather than forcing this formula everywhere.

```css
.media-frame {
  --media-radius: 0.5rem;
  --media-inset: 0.5rem;
  padding: var(--media-inset);
  border-radius: calc(var(--media-radius) + var(--media-inset));
}

.media-frame > img {
  display: block;
  inline-size: 100%;
  border-radius: var(--media-radius);
}
```

Map these sample values to the project's radius and spacing tokens. Do not add `overflow: hidden`
to an entire interactive card merely to crop its image: it can clip focus rings and popovers.

## Optical icon alignment

Center with layout first. If an asymmetric glyph still appears off-center, prefer the icon
family's corrected variant or viewBox before adding a small local optical correction. Never apply
one offset to every icon or alter the hit target just to move its artwork.

```css
.icon-button {
  display: inline-grid;
  place-items: center;
  min-inline-size: 2.75rem;
  min-block-size: 2.75rem;
}

.icon-button > svg {
  inline-size: 1.25rem;
  block-size: 1.25rem;
  pointer-events: none;
}

/* Only for a play glyph that is visibly left-heavy after centering. */
.icon-button[data-icon="play"] > svg {
  transform: translateX(0.0625rem);
}

.icon-button:focus-visible {
  outline: 2px solid currentColor;
  outline-offset: 3px;
}
```

Use a native button with an accessible name, `type="button"` when it should not submit a form,
and a decorative `aria-hidden="true"` icon. The sample target is a comfortable starting point,
not a universal accessibility certification. Respect the product's target-size requirements.

Prefer real control padding over invisible expanded hit areas. If a dense layout needs an expanded
target, verify neighboring targets do not overlap and focus still identifies the active control.

## Border, shadow, and image edge roles

| Need | Treatment to consider | Verification |
| --- | --- | --- |
| Separate table rows or sections | Border or divider | Separation survives both themes |
| Indicate a raised menu or panel | Theme-specific shadow, with an edge if needed | Does not resemble an unrelated floating card |
| Bound an input or button | Existing component border and focus treatment | Control remains identifiable without shadows |
| Define a photo edge against a similar background | Optional inset outline on that media frame | Does not frame transparent logos or cutout art |

Do not replace all borders with shadows, apply a global outline to every image, or assume a dark
theme is a numerical inversion of a light one. Reuse semantic surface/foreground/border/elevation
tokens and inspect each theme. In forced-colors modes, do not rely solely on shadows or background
color to communicate a control boundary or state.

## Verify the detail

- Inspect nested surfaces at normal size; change geometry only where the mismatch is visible.
- Check icon-plus-label controls, focus rings, long labels, and disabled states.
- Check light/dark themes when supported and high-contrast/forced-colors behavior when relevant.
- Test actual hit targets with pointer and keyboard; visual alignment alone is insufficient.

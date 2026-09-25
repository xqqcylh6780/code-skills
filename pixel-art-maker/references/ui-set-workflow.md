# Pixel UI Set Workflow

Use for sets of pixel icons and game UI components such as buttons, inventory slots, health bars, and panels. A single icon request does not imply a full UI kit. Follow existing product dimensions, palette, and interaction states when supplied.

## Establish a family

Set the intended display size and pixel grid, shared palette, outline or border weight, light direction, corner treatment, and transparent padding. Define the meaning of each requested icon or component before drawing; distinct meanings need distinct silhouettes at native size. Check the set together early so no item has a different apparent scale or visual density.

Draw the simplest representative component first, then reuse its rules for the rest. Keep symbols separate from button or slot backgrounds when they may be recombined. For interactive components, create only the states needed by the target interface, such as normal, hover, pressed, selected, and disabled; change them consistently through value, border, offset, or fill while keeping the symbol recognizable. Use nine-slice metadata only for panels or frames intended to stretch, not for fixed-size icons.

## Verify and export

- Inspect every icon at its actual UI size against the backgrounds where it will appear. Check recognition, padding, contrast, alignment, and consistent stroke and cluster style; enlarged previews alone are insufficient.
- Compare component states side by side. Disabled and selected states must remain distinguishable in the target palette. Check transparent edges and integer scaling.
- Preserve the editable `.aseprite` source. Export individual native-resolution assets by default; make an atlas or sprite sheet only when requested or required by the existing project, with explicit cell size, order, state names, and slice information.

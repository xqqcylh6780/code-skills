# Asset sets and object-specific checks

Read the relevant sections when creating a set, variants, modular objects, or a complex world asset.

## Shared style for a set

Use project references to hold camera angle, perspective, outline width and color, shape language, lighting, detail density, scale language, and material treatment steady. A new asset should belong to the same game. Keep objects separated for extraction; provide individual files when requested and practical.

For each generated member, identify the reference's role in the prompt: a project asset may anchor style and camera without dictating the new object's shape. State the requested object's construction separately, and keep only the likely failure constraints for that object rather than a stock negative list.

An established project camera takes priority. Use precise terms such as side, front, top-down, three-quarter top-down, or isometric; do not let a nominally consistent style hide a changing view angle.

## Variants

Preserve the base object's identity and footprint. Change the requested dimension only: seasonal foliage on the same tree, or upgraded materials and additions on the same house. Check the variant family together for silhouette, scale, and attachment alignment.

Use the original object as the identity anchor for every variant when the tool supports references. In each variant prompt, name the features that stay fixed and the specific feature that changes; do not use a previously generated variant as the sole source for the next one. Compare variants at their intended game size and correct any member whose footprint, camera, or attachment points drift.

## Object checks

- **Plants:** readable trunk or stem and canopy, controlled leaf density, consistent scale; avoid tiny foliage noise.
- **Buildings:** coherent roof and wall planes, stable door/window proportions, intact roof, plausible geometry at the project camera.
- **Fences, walls, roads, borders:** match thickness, perspective, scale, and attachment points. When a modular set is requested, include the needed straight, corner, end, junction, and gate pieces rather than assuming every variant is required.
- **Furniture and machines:** logical construction and ground contact at the intended room camera; no floating parts.
- **Items and collectibles:** isolated silhouette and local contrast that survive the intended display size; keep scenery out unless requested.

World objects held by a character or placed in a scene belong here. Compact inventory or HUD representations belong to `game-ui-icon-maker`.

# Scene Workflow

Use for pixel-art backgrounds, room scenes, and playable environments. Follow the project's established art direction. A single composed background may be one layered artwork; a reusable map needs tiles and independently placeable assets. Deliver only the form the user requested.

## Frame the scene

- Set camera angle, canvas or viewport size, logical pixel scale, palette, light direction, and intended focal area. For a playable map, also establish tile size and grid origin.
- Make a rough composition with large value masses and clear foreground, middle ground, and background. Reserve readable space for characters, entrances, UI overlays, or other requested gameplay elements without inventing gameplay rules.
- Identify repeated materials and objects. Decide which need to be reusable tiles or transparent props and which belong only in this scene.

## Build in layers

Construct from ground or background through terrain transitions, structures, placeable props, shadows, and foreground occluders. Use separate layers or groups where later rearrangement, animation, or depth ordering requires it; avoid unnecessary layers for a tiny static backdrop. Keep the camera, palette, lighting, and pixel density coherent across every component.

For tiled environments, make the smallest complete set needed by the requested map: center, edges, corners, path or height transitions as applicable. Reuse tiles on the grid and keep props independently editable. Use Aseprite MCP tilemap tools when available; otherwise draw into explicit layers and grid coordinates. See [Game Asset Specifications](game-asset-spec.md) for tilemap depth and [Pixel Specs](pixel-spec.md) for seam checks.

## Verify the assembled view

- Inspect the whole scene at its intended display size: composition, subject readability, depth, repeated patterns, and light consistency.
- For tiled areas, inspect a repeated 3×3 region and the actual joins between unlike tiles; test map edges and corners, not only isolated tiles.
- Check props against the character and tile scale, verify transparent edges, and confirm that foreground occluders are separated when the target game needs them.
- Preserve the layered `.aseprite` source. Export the composed scene and, when requested, its reusable tiles and props with cell size and placement metadata. Do not flatten away editability merely to make a preview.

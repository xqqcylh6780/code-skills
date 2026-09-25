# Directional Character Workflow

Use this reference when the requested deliverable has multiple facing directions, character animations, or a sprite sheet. It describes a drawing workflow for Aseprite MCP; it does not require an image-generation service. Follow an existing game's art direction and frame layout before using the suggestions below. Do not expand a single-pose request into a direction set.

## 1. Define the Character Once

Record a short working brief before drawing the set:

- Frame dimensions, camera angle, requested directions and actions, palette, outline treatment, detail level, and light direction.
- Character height and width range, head-to-body proportion, key silhouette landmarks, and a common ground-contact or pivot point.
- Identity markers that must survive rotation: clothing colors, hairstyle, equipment, and which side carries any asymmetric item.
- Room needed for moving limbs, weapons, hair, or effects. Keep one frame size across an action set or explicitly separate actions whose bounds differ.

Infer ordinary missing details from the existing project or a simple baseline. Ask only when a missing choice would change the intended asset substantially. The brief is a production aid, not a new user approval gate.

## 2. Build and Check the Base View

Draw one readable idle view at native resolution, usually the south/front view for a top-down character or the profile for a sidescroller. Work from silhouette and proportions to flat colors, shading, then distinguishing details. Check it at 100% size before expanding the set. Fix structural problems now; do not reproduce them across directions.

Keep the base view available as a visual reference while drawing other views. For editable Aseprite work, retain separate outline, base color, shading, and optional equipment layers where the asset complexity justifies them. Use explicit file, layer, and frame targets in MCP calls; use `draw_strokes` when visible stroke-by-stroke progress is requested or expected in Live mode. Verify available tool signatures and the Live connection as described in [Aseprite MCP Workflow](aseprite-workflow.md).

## 3. Expand Directions Deliberately

Draw the requested cardinal views first, then diagonals if needed. Use the same camera angle, head/body scale, palette roles, outline weight, and ground anchor. Reinterpret the volumes for each view: the front, side, and back show different amounts of face, hair, clothing, limbs, and gear. A pixel flip may seed a truly symmetric opposite view, but inspect and redraw asymmetrical equipment, hair, lighting, and hand placement. Do not present a mechanically flipped or rotated sprite as a completed new view without checking it.

For eight directions, document the chosen sequence in the source and export metadata. One usable sequence is `S, SW, W, NW, N, NE, E, SE`; the game's existing convention takes precedence. Compare the views side by side at native size. Check that the character remains recognizable and that perspective changes are intentional rather than proportion drift.

When direction art is generated from image references, specify which image fixes character identity and which, if any, is only a layout guide. Check each requested direction at native size before using it as the basis for intermediate views; labels or a correct sheet layout do not prove that the character actually faces the indicated way.

## 4. Animate from the Stable Direction Set

Start with the actions the user requested. For each direction, establish contact and extreme poses before filling in transitions. Reuse the direction's palette and landmarks, but redraw anatomy and overlap where motion requires it. Moving a cel or mirroring frames can support an animation; neither creates convincing limb articulation by itself.

Keep the floor or pivot stable where the action requires it, while allowing deliberate weight shifts and airborne motion. Preview each action at its intended frame durations. Inspect the transition from the last frame back to the first for loops; use a held final frame for one-shot actions when appropriate. Organize frame ranges and tags by action and direction so an exported sheet can be mapped without guessing. `set_tag`, frame-duration tools, onion-skin previews, and frame comparison can help when available.

## 5. Verify and Deliver the Set

- **Across directions:** Compare silhouette scale, head height, feet or pivot, palette, outline, lighting, and side-specific details. Allow expected foreshortening; avoid forcing identical pixel counts or outlines.
- **Across frames:** Check that clothing and equipment stay attached, limbs articulate, feet do not slip unintentionally, and motion has a readable arc and loop seam.
- **Technically:** Confirm canvas dimensions, frame count, durations, layer structure, tags, transparency, and the direction/action mapping. Use `get_sprite_info`, exported previews, and relevant animation or pixel-inspection tools when available. A successful tool response alone is not visual verification.
- **Sheet mapping:** Compare the exported cells against the documented direction and action order, including the first and last frames of loops. If a cell is mislabeled, blank, clipped, or points the wrong way, correct it and recheck adjacent frames before delivery.
- **Export:** Preserve the editable `.aseprite` master. Export native-resolution frames or a sheet as requested, with explicit cell size, order, durations, and pivot metadata. Inspect the actual export at native size and an integer-scaled preview before delivery.

If only part of the set meets the quality bar, correct the specific view or frame and recheck its neighbors. Report any unfinished direction or action rather than implying that the whole set was verified.

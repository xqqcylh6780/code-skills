# Prop State Workflow

Use for game objects such as chests, doors, switches, pickups, and furniture when multiple visual states, facing directions, or animations are requested. A one-off prop needs only the requested view. Do not generate extra states or rotations by default.

## Define the shared object

Set its camera angle, frame size, ground footprint, pivot, palette, outline, light direction, and distinguishing features. Identify which parts stay fixed and which move or change. Choose the state list from the user's request or existing game conventions, for example `closed`, `opening`, and `open` for a chest.

Draw a readable base state at native size. Keep reusable parts on separate layers when they will move, disappear, or change color. For each other state, preserve material identity, perspective, footprint, and pivot while redrawing the changed geometry. A rotation or flip can be a starting guide, but check asymmetrical handles, hinges, highlights, and cast shadows before treating it as another finished direction. For objects animated across directions, apply the direction and motion checks in [Directional Character Workflow](character-workflow.md) where relevant.

## Verify and export

- Compare states side by side and toggle between them at the intended in-game location. Check for unwanted position jumps, color drift, silhouette ambiguity, and missing or duplicated parts.
- For animation, inspect timing, moving-part arcs, and the first-to-last transition when the action loops. Use stable pivots unless the action deliberately moves the whole object.
- Preserve editable `.aseprite` layers and frames. Name states and directions unambiguously; export transparent native-resolution images or a sheet as requested, with frame size, state order, durations, and pivot metadata. Confirm the exported files match the source.

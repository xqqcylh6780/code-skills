# Aseprite MCP Workflow & Verification

This reference governs precision pixel art creation, layered master files, animations, and active Aseprite editor sessions via MCP. Tool names below represent standard interface signatures; dynamically verify active tool parameters rather than assuming hardcoded environment paths.

---

## 1. Connection & Target Files

1. **Tool Discovery**: Discover available Aseprite MCP tools. If `live_session_status` is available, verify connection health, version, and capabilities before performing canvas operations.
2. **Interactive Live Window**: When the user requests drawing inside the active GUI window, only proceed if the Live connection is verified. If disconnected or protocol-mismatched, notify the user that Aseprite needs to be opened, updated, or restarted. Never silently fallback to background Batch mode when Live was requested.
3. **Batch Fallback**: When the user does not require an active window session and permits local batch execution, use available Batch tools and clarify that drawing will not be displayed step-by-step in an open GUI. If MCP is absent, state this limitation clearly—never fabricate MCP execution.
4. **File Targeting**: Use the project's designated asset directory (or `output/` within the current workspace if unspecified). Always pass absolute file paths. Check if target files exist; pick a non-conflicting filename for new assets. When editing existing artwork, modify only the specified file without overwriting via `create_canvas` or guessing targets from active tabs.

---

## 2. Canvas Setup to Production Render

- **Initialize Canvas & Palette**: Create the canvas at target dimensions (e.g., `create_canvas`). Establish a restricted palette (e.g., `set_palette` or existing presets). Standalone small assets typically start with 6–12 colors; expand as lighting demands rather than adding colors arbitrarily.
- **Layer Organization**: Structure layers logically with descriptive names. Standard top-to-bottom layer stack:
  `Outline → Highlight/Detail → Shadow → Base Color → Reference (Hidden)`.
  Simple assets may consolidate layers; existing project layer naming takes precedence.
- **Explicit Parameter Targeting**: Establish the subject's footprint, silhouette, and primary components before adding micro-details. Prefer tools with explicit `filename`, `layer_name`, and `frame_index` arguments (e.g., `draw_pixels_at`) instead of relying on invisible active layer state.
- **Reference Management**: When importing outlines or sketches, ensure identical canvas dimensions and coordinate alignment to avoid unintended distortion. Reference layers must be hidden and excluded from final sprite exports. Never redraw a confirmed outline into an unrelated pose.
- **Batch Raster Operations**: For heavy raster operations, `run_lua_batch` can minimize redundant per-pixel saves. In Live drawing mode, batch only the current visible sub-step, not the entire illustration. `run_lua_batch` applies strictly to standard raster documents (not tilesets). Scripts must only modify the targeted document without closing, switching, or triggering arbitrary undo/redo.
- **Lua API Caveats**: Raw calls like `Image:putPixel()` write directly to the image buffer and do not automatically generate standard undo history; do not assume wrapping in `app.transaction()` guarantees clean rollbacks without cel image duplication or native tool support.

---

## 3. Live Visible Drawing Protocol

*By default, the user expects to watch the drawing progression unfold inside the active Aseprite window.* "Live Connected" does not automatically mean "Progression Visible" unless operations are dispatched properly.

1. **Confirm Live Status**: Verify the Live connection is active and provide a brief status line describing the current step. If the environment supports auto-fallback to Batch, enforce strict Live-only request mode to prevent silent background execution. Never alter persistent client configurations or restart external processes unilaterally.
2. **Discrete Phased Submissions**: Break static illustrations into visible milestones:
   `Silhouette/Blockout → Structural Adjustments → Base Flat Colors → Shading/Volumes → Details & Cleanup`.
   Complex assets should be subdivided further by body part or color zone. Each tool call must render a clearly discernible visual increment. Simple bug fixes or tweaks can be completed directly without artificial micro-stages.
3. **Frame-by-Frame Animation**: For animations, illustrate the first key pose completely, then advance pose-by-pose and in-between frames sequentially. Modify only the current frame per operation; avoid sweeping multi-frame loops that draw an entire action invisibly in one shot.
4. **Serial Execution & View Refresh**: Tool calls must run strictly in serial. After updating pixels, ensure the target document, layer, and frame are active/visible, call `app.refresh()` (or tool-specific viewport refresh), and conclude the script so the editor regains UI control. Subsequent tool calls must specify explicit document, layer, and frame targets.
5. **Pacing & Continuous Execution**: After completing a major phase, provide a concise note and immediately proceed to the next phase without pausing to wait for user replies. Do not simulate progress by inserting blocking sleep delays into a single long Lua script, and never dispatch parallel draw calls.
6. **Integrity Rule**: What is shown must be actual progress between steps, not mouse cursor replays. Strictly forbidden: generating the completed illustration upfront in secret and toggling layer visibility on and off to fake a drawing process.

Live display does not require extra intermediate files or variants, nor does it expand the requested scope. Live visual monitoring does not replace formal export verification.

---

## 4. Errors & Timeouts

- **Inspect Returned Payloads**: Check the actual response after every call. If an error occurs, inspect the document state to diagnose root cause before continuing.
- **Live Timeout Handling**: A timeout in a Live request does *not* imply the script failed or stopped. If a request ID is returned, poll via `get_live_request_status`. While status is `running` or `unknown`, do not resubmit the draw command or fall back to Batch mode.
- **Idempotency**: If the scripting tool accepts explicit `request_id` parameters, use the identical ID and payload for retries. Never generate a new ID to bypass an unresolved operation. Inspect canvas cel state before attempting repairs.
- **Uncertain State**: If status queries are unavailable, pause further submissions and report the ambiguity to the user rather than guessing or force-restarting Aseprite.

---

## 5. Export, Verification, and Delivery

1. **Master File Preservation**: Save the layered `.aseprite` file. Use `get_sprite_info` to verify canvas size, layer stack, and frame count. Retain editable layers; never flatten master files permanently.
2. **Export Files**: Export the native 1:1 resolution PNG. Generate an integer-scaled preview (e.g., 4× or 8× nearest neighbor) via `export_frame` for visual inspection. The 1:1 image is the game asset; the enlarged image is only for preview.
3. **Visual Inspection**: Open and inspect the exported image. Verify silhouette balance, facial features, cluster clarity, lighting consistency, and border cleanliness. Correct issues directly on the corresponding layer and re-export.
4. **Technical Data Check**: Use `get_color_stats`, `get_composite_rect`, or native image inspection to confirm color count, dimensions, and alpha channels. Use composite reads for overall art checks and single-cel reads for layer-specific audits.
5. **Tiles & Animation**: Inspect tiles via a 3×3 tiling grid. Check animations for consistent frame dimensions, durations, anchor stability, and fluid motion arcs.
6. **Delivery**: Deliver the actual files (master `.aseprite`, 1:1 PNG, and preview). Embed or link the image directly in the response—never output an isolated script or file path without delivering the generated assets.

---

## 6. Standalone Asset Baseline Scope

A request like "Draw a cat" must be executed immediately as:
- **32×32 pixels**
- Transparent background
- Clearly identifiable sitting cat silhouette
- Restricted cohesive palette
- Layered `.aseprite` master file
- Native 1:1 PNG export
- 4× or 8× nearest-neighbor preview

Do not unilaterally expand scope into walk cycles, 4-directional sprite sheets, or full scenes, and do not stall the user with multi-stage approval checkpoints unless explicitly asked.

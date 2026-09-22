# Artist Workflow & Aseprite Operations

This reference guides hands-on drawing and educational software walkthroughs. A professional pixel art workflow solves visual problems layer-by-layer: silhouette → values → materials → cleanup. It does not require every tool for every sprite, nor should it turn every step into an unnecessary user approval checkpoint. If the user only asks how to draw or how a tool works, explain the technique without arbitrarily creating files; when asked to draw, execute cohesively, self-inspect, and deliver.

Tool names and keyboard shortcuts can vary with Aseprite versions, languages, and user configurations; refer to standard terms. For MCP connectivity, document targeting, safe writes, and export procedures, adhere strictly to [Aseprite MCP Workflow](aseprite-workflow.md).

*Live Visible Drawing Protocol*: When Aseprite Live is active, drawing stages must be split into small, visible, discrete steps, advancing animation frame-by-frame per the "Live Visible Drawing" section in the MCP reference. Proceed smoothly through stages without stopping for intermediate user approvals; do not collapse the entire piece into a single opaque batch script.

---

## 1. Define Subject & Visual Intent

Clarify key recognition cues, intended game role, camera perspective, pixel dimensions, pose, and light source. Reuse established project specifications; for standalone simple assets, adopt default settings without interrogating the user on every parameter.

- **Extract Essentials from Reference**: Identify primary silhouettes, proportions, and iconic traits rather than tracing every realistic texture. (e.g., A cat's recognition cues are pointed ears, muzzle shape, sitting posture, and tail—not individual hairs).
- **Canvas Footprint**: Estimate the subject's bounds on the target canvas, reserving headroom for ear tips, tails, weapons, or action overshoot. For game characters, establish the ground contact/foot anchor first, followed by head-to-body proportions.
- **Render Style**: Outlined characters typically start with a structural line sketch; terrain, rocks, foliage, and un-outlined characters often start with solid silhouettes. Do not force every subject through a heavy black outline.

**Self-Check**: Describe the subject and action in one sentence. Confirm the largest volume fits comfortably within the target canvas. If essential features cannot fit at this scale, simplify the design rather than unilaterally enlarging agreed-upon canvas dimensions.

---

## 2. Canvas & Workspace Setup

Initialize a transparent canvas at the target resolution in Aseprite. Use RGB color mode with a restricted palette unless an Indexed color mode constraint is specifically required by the project (if Indexed is requested, monitor palette indexes and the transparent index carefully).

- **Layers & Timeline**: Display the Timeline (`Tab`). Create a base color layer; add outline, shadow, and detail layers as needed. Place references on a dedicated top layer with reduced opacity, locking it during manual edits and hiding it before export.
- **Pencil & Brush**: Draw with hard edges using the Pencil tool (`B`). Use a 1-pixel brush for contours and details; use larger hard-edged square or round brushes for blocking in masses. Never use soft brushes, airbrushes, or blur tools. Normal blending mode with 100% opacity is the standard for solid pixel assets.
- **Pixel-Perfect Mode**: Enable Pixel-perfect on the Pencil tool when drawing freehand lines to automatically eliminate unwanted double pixels ("doubles" / L-shapes), but note that it does not replace manual correction of curves, proportions, or cluster shapes.
- **Zoom & Viewports**: Zoom in for precise pixel placement, but frequently check the canvas at 100% scale (actual size) or keep a secondary preview window open at 100% (`View → Preview`). Zoom level is not canvas resolution—never enlarge canvas pixels just to inspect them.
- **Initial Palette**: Seed the palette with key midtones and basic shadow/highlight swatches, expanding organically as lighting demands.

**Self-Check**: Verify canvas dimensions, target layer, and frame index. Ensure marks are crisp, opaque pixels with no anti-aliasing, and reference art is isolated. When modifying existing art, retain a backup layer or document.

---

## 3. Silhouette & Composition: Solid Foundation

On a base or temporary rough layer, block out the largest masses (head, torso, limbs) in a single flat color. Basic geometric primitives (rectangles, ellipses) can rough out the armature, but you must immediately carve and refine joints, contours, and silhouettes; stacked geometric shapes are not finished art.

- **Check Readability**: Defer eyes, textures, and highlights. Evaluate head-to-body ratio, center of gravity, and gesture line first.
- **Negative Space**: Inspect the negative space between arms and torso, between legs, and around tails or props. Clear negative space makes poses instantly readable at tiny scales.
- **Adjusting Masses**: Select parts with the Marquee or Lasso tool and nudge by integer pixels to tune limb placements or proportions, patching any gaps immediately. Distinguish between translating pixel content versus moving a selection boundary.
- **Symmetry Tool Caveats**: Symmetry is helpful for roughing in front-facing props or static frontal poses, but strict symmetry can make 3/4 perspectives, dynamic actions, or natural anatomy look stiff and robotic. Break symmetry in the secondary pass.

**Self-Check**: View the silhouette at 100% zoom with all details hidden. The subject, posture, and action should be immediately recognizable. If not, refine the silhouette masses—never add facial features to disguise a broken silhouette.

---

## 4. Structure & Base Colors: Clear Partitioning

Carve the silhouette into clear overlapping depth planes and material zones. In outlined styles, refine lines on an upper layer while laying flat colors below; in lineless styles, separate limbs and garments via value contrast between adjacent color blocks.

- **Flat Color Blocking**: Block in large flat color masses first. When using the Paint Bucket (`G`), check the active layer, closed boundary tolerance, and contiguous settings. If outlining on a separate layer, ensure fill referencing is configured correctly.
- **Eyedropper Reuse**: Sample existing colors (`Alt` + click) to preserve palette cohesion rather than picking near-identical random swatches.
- **Anatomy & Overlap**: Treat limbs, clothing, face, and accessories as distinct interlocking planes. Use clean structural internal lines where necessary, but avoid outlining every single color transition in black.
- **Preserve Approved Silhouettes**: Do not silently alter approved shapes during flat coloring. If a shape change is mandatory, adjust the silhouette/outline accordingly and note the revision.

**Self-Check**: The subject's anatomy and outfit should be clearly readable even without shading. Adjacent parts should not merge unintentionally, and perspective must remain consistent.

---

## 5. Values & Volume: Shading by Planes

Define a single primary directional light source (e.g., top-left). Treat head, torso, and limbs as 3D geometric volumes, establishing major shadow planes first, cast shadows next, and specular highlights last.

- **Form Light vs. Pillow Shading**: Shadows must represent planes turned away from the light, recesses, and cast shadows. Never apply uniform dark rings around all edges with a bright center (pillow shading).
- **Layer Isolation**: Shading and highlights can be isolated on dedicated layers for non-destructive tuning, clipped strictly to the subject's silhouette.
- **Lock Alpha Caveats**: Locking alpha (`Lock Alpha`) constrains drawing only to existing opaque pixels on the *current* layer. Enabling it on a blank shadow layer will prevent drawing altogether; use explicit selections, clipping groups, or verified masking.
- **Automation / Lua Constraints**: Direct pixel writes via scripts or MCP might bypass GUI selection masks or layer locks. When writing pixels via scripts/MCP, explicitly clamp coordinates to the subject's mask bounds.
- **Hue Shifting**: Shift hue and saturation across the value ramp rather than simply darkening with black or lightening with white (e.g., warm highlights with cooler shadows). Avoid continuous gradient ramps; stick to distinct value steps.

**Self-Check**: Hide detail layers and inspect the shaded volume. Lighting direction must be consistent across all components. If volume feels ambiguous, adjust shadow shapes before adding surface texture.

---

## 6. Material & Focal Points: Selective Detailing

Reserve the highest contrast and most distinct details for the primary focal point (e.g., character face or tool blade). Keep secondary areas composed of calm, readable color fields.

- **Material Textures**:
  - *Fur/Hair*: Directional edge clusters and chunky tufts; not individual strands.
  - *Rock/Stone*: Crisp planar facets, angular edges, and hard highlights.
  - *Metal*: Concentrated, high-contrast reflection bands and bright specular points.
- **Facial Features**: Settle eye and mouth placement first before adding a 1-pixel highlight. At 32×32 or 16×16, a single pixel shifts facial expression or gaze direction dramatically.
- **Dithering Guidelines**: Use dithering (checkered color transitions) sparingly, primarily when a middle tone is unavailable or for retro console aesthetics. Avoid noisy, indiscriminate dithering that creates visual clutter.
- **Single Pixels**: Intentional 1-pixel details (eyes, belt buckles, sparkles) are valuable. Clean up *accidental, orphaned noise pixels*, not deliberate micro-details.

**Self-Check**: Does the eye naturally track to the intended focal point? Do micro-details degrade silhouette readability or break the palette? If removing a cluster makes the sprite clearer, remove it.

---

## 7. Pixel Cleanup & Refinement

Zoom in to clean up edges with a 1-pixel Pencil and Eraser, then zoom out to 100% to evaluate overall clarity. Address the most disruptive artifacts first:

- **Jaggies & Doubles**: Remove unintentional double pixels (L-shapes/corners where a 1px line abruptly doubles in thickness). Ensure line step intervals change progressively (e.g., `3-2-1-1-2-3`, not chaotic jumps like `3-1-3-1-2`).
- **Tangents**: Resolve accidental edge-to-edge tangents where two separate elements barely touch, making spatial depth ambiguous. Either overlap them decisively or open up clear negative space.
- **Banding**: Eliminate banding—stair-stepped lines of shading that hug outline pixels identically, creating harsh artificial borders instead of curved volumes. Sculpt shading into natural clusters.
- **Color Bleed & Alpha Leaks**: Toggle a dark and light temporary background to expose stray translucent pixels or dirty edges. Ensure the final export retains true binary transparency (alpha 0 or 255) for standard pixel art.
- **Rework Priority Order**:
  1. Silhouette & Readability
  2. Proportions & Perspective
  3. Structural Separation
  4. Light Source & Shading Masses
  5. Material Clusters
  6. Single-Pixel Edge Cleanup

---

## 8. Animation & Tile Workflows

### Character Animation
1. **Key Poses First**: Complete extreme poses (e.g., Contact and Passing poses in a walk cycle) before drawing in-betweens.
2. **Onion Skinning**: Enable Onion Skin (`Alt + O`) to track motion arcs and volume consistency across adjacent frames.
3. **Anchor Stability**: Keep character feet anchored to a consistent ground baseline; avoid unintentional foot slipping or vertical jittering.
4. **Coordinated Motion**: During walking or running, balance pelvic, shoulder, and head bobs organically (typically 0–1 pixel bobbing at 32px scale); never move an entire torso horizontally or vertically as a rigid flat chunk.
5. **Playback Evaluation**: Preview playback in real time at intended FPS; verify seamless looping for cycles.

### Tile Design
1. **Tiled Mode**: In Aseprite, use `View → Tiled Mode → Both Axes` to preview seamless repeating patterns in real time.
2. **Repeating Rhythm**: Seamless wrapping is only the first step—ensure large repeating grids do not reveal distracting lines, repetitive high-contrast spots, or grid fatigue.
3. **Transition Autotiles**: Build transitions (inner/outer corners, edges, centers) that cleanly interface with adjacent terrain.
4. **Layer Decoupling**: Keep environmental props (grass tufts, pebbles, flowers) on transparent overlay layers separate from base ground tiles.

---

## 9. Save, Export, and Instruction Delivery

- **Save Layered Source**: Save the master `.aseprite` file with organized layers and named animation tags.
- **Export Formats**: Hide reference and test background layers, then export the 1:1 original resolution PNG. Export an enlarged preview (4× or 8× integer nearest neighbor) for inspection.
- **Verify Export**: Open and inspect the actual exported PNGs to confirm pixel dimensions, alpha integrity, and cluster clarity.
- **Instruction Style**: When teaching or explaining Aseprite operations, structure explanations as:
  `Goal / Reason → Specific Tool & Action → What You Should Observe → How to Troubleshoot`.
  Mention both common English and localized tool names when helpful, avoiding unverified shortcuts.

---

## MCP Tool Mapping to Artist Actions

The following tool names illustrate typical MCP mapping; discover active tools and verify schemas dynamically before invoking.

| Artist Action | MCP Mapping & Guidelines |
| :--- | :--- |
| **Pencil Blocking & Cleanup** | `draw_pixels_at`, line, rectangle, or polygon tools. Always specify target document, layer, and frame index explicitly. |
| **Eyedropper & Palette** | `get_palette`, `set_palette`, and pixel inspection tools. Differentiate between single-cel raw pixels and composite render colors. |
| **Region Shifting / Nudging** | `move_region`, `copy_region`. Check bounding boxes and ensure surrounding pixels are patched properly. |
| **Layer Management** | Layer creation, renaming, ordering, visibility, and opacity tools. Retain editable layers; never flatten master files permanently for temporary previews. |
| **Batch Drawing & Shading** | `run_lua_batch` with explicit coordinates and masks. Chunk batches into recognizable visual milestones for visible progress. |
| **Animation Verification** | Frame duplication, frame duration, tag management, and `set_onion_skin`. Creating frames does not replace inspecting actual playback timing. |

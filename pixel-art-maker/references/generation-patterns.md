# Generation & Editing Patterns

These prompt patterns apply specifically when the image generation path is selected. They are not a mandatory routing for all pixel art tasks, nor are they rigid boilerplate to be repeated verbatim to users. For Aseprite native drawing, follow [Aseprite MCP Workflow](aseprite-workflow.md). Substitute bracketed fields `[...]` with user requirements or sensible project defaults.

---

## 1. Intent-to-Action Routing

| User Intent | Execution Action |
| :--- | :--- |
| *"How do I draw...?", "Is this approach correct?", "How does this tool work in Aseprite?"* | Explain technique or provide step-by-step guidance; **do not** generate images or create files. |
| *"Draw this for me", "Create an image", "Images only"* | Select production path and create the asset directly. (This reference governs the image generation path). |
| *"Color in this outline", "Proceed with final render"* | Treat the existing outline as an aligned reference image; maintain strict pixel grid alignment. |
| *"Do step 1 and step 2 first"* | Deliver only the requested preliminary phases without jumping ahead to the final render. |
| *"Give them to me one by one"* | Generate one asset/tile per step; do not package multiple assets into a single sheet. |

---

## 2. Universal Pixel Art Prompt Constraints

Every generation or editing prompt must explicitly enforce:

- **Target Canvas Dimensions**: `[Width] × [Height] px`;
- **Perspective**: `[Frontal / Side-profile / Top-down orthographic / 3/4 Isometric]`;
- **Style Invariants**: Authentic hand-crafted retro pixel art, clean hard-edged pixel clusters;
- **Technical Restrictions**: Strictly limited palette, **no anti-aliasing**, **no Gaussian blur**, **no smooth gradients**, **no photographic textures**;
- **Framing**: Single subject fully framed within canvas bounds with healthy margins, no cutoff/clipping;
- **Background**: `[Clean transparent background / Seamless full-bleed ground texture]`;
- **Clean Output**: No text, no typography, no watermarks, no decorative UI frames, no display pedestals/bases.

*Rule*: Never simply request "pixel art". Always define exact resolution, camera perspective, functional role, line weight, palette constraints, and background rules.

---

## 3. Standalone Tile Template

> **Target**: A single `[Size, e.g., 32×32]` game tile representing `[Theme, e.g., cobblestone path]`, viewed in `[Perspective, e.g., top-down orthographic]`.
> Generate exclusively the `[Center / Straight edge / Outer corner / Inner corner / Decorative overlay]` tile variant.
> Maintain uniform pixel density and a fixed directional light source from `[Direction, e.g., top-left]`.
> *For base ground*: The pattern must align and repeat seamlessly across top-to-bottom and left-to-right edges.
> *For props/foliage*: Place on a pure transparent background with a clear base footprint.
> Do NOT produce a packed tileset sheet, full map scene, borders, or text.

*Post-check*: Validate via 3×3 tiling. If seams are visible, repair edge pixels directly; never apply a blur filter to hide seams.

---

## 4. Initial Outline Template

> **Target**: Initial `[Size, e.g., 32×32]` pixel art structural outline of `[Subject, e.g., blacksmith NPC]`, in `[Perspective & Pose, e.g., front-facing standing pose]`.
> Render using clean 1-pixel dark hard-edged lines, capturing only the exterior silhouette and essential internal anatomical/clothing planes.
> Do NOT include full flat colors, shading, specular highlights, textures, or background elements.
> Subject must be completely contained, centered, and unclipped on a pure transparent background.
> Zero anti-aliasing, no semi-transparent feathering, no text labels.

*Intent*: This outline serves as a structural foundation for subsequent coloring in Aseprite; focus on anatomical readability and clean negative space rather than creating a fine-line poster illustration.

---

## 5. Flat Base Color Template

> **Target**: Flat color blockout for the provided outline of `[Subject]`.
> Use the supplied outline as the strict structural foundation.
> On the exact same canvas resolution, maintaining 1:1 coordinate alignment, proportions, perspective, and pose, apply clean solid base midtones to `[Subject]`.
> Preserve the existing outline intact. Do NOT add lighting, shading ramps, highlights, or surface noise.
> Pure transparent background, no anti-aliasing, no text.

---

## 6. Final Render Editing Template

> **Target**: Final shaded render of the provided `[Outline / Base Color art]`, without redesigning the subject.
> Maintain exact canvas bounds, outer silhouette, coordinates, proportions, camera angle, and pose.
> Apply the `[Palette or color description]`, with consistent directional lighting from `[Direction, e.g., top-left]`.
> Sculpt form using grouped base, shadow, and highlight values in cohesive pixel clusters. Detail density must strictly match the native pixel grid.
> Pure transparent background, no anti-aliasing, no photographic textures, no blur, no text.

*Integrity Check*: If the generative tool cannot preserve the exact silhouette, output the corrected outline first before coloring. Never present an altered character design as the "final render of the same outline."

---

## 7. Stage Comparison Template

*(Use only when the user explicitly requests a side-by-side progression preview).*

> Arrange the verified and aligned `Outline`, `Base Colors`, and `Final Render` horizontally within a single preview canvas, separated by equal margins.
> Retain 1:1 scale and identical vertical alignment.
> Do NOT add decorative text inside the artwork unless the user specifically requested step labels.
> The standalone PNG files remain the official deliverable assets.

---

## 8. Resolution Downscaling & Grid Realignment

When image generation produces an oversized output that must be brought to target dimensions:
1. **Analyze Logical Resolution**: Inspect the image to confirm if a true logical pixel grid exists.
2. **Integer Scaling**: If the underlying pixel grid is sharp and uniform, scale down strictly by an integer factor using Nearest-Neighbor interpolation (e.g., downscale 4× from 128×128 to 32×32). Never use fractional scaling ratios (e.g., 2.3×) which destroy pixel art grids.
3. **Bounding Crops**: Cropping is only permitted to remove outer empty padding; never crop into the subject or alter tile boundaries.
4. **Limits of Resampling**: Nearest-neighbor downscaling cannot magically fix anti-aliasing, uneven pixel widths ("fat pixels"), or messy clusters generated at high resolution. When no clean logical grid exists, manually rebuild the sprite at native target resolution rather than pretending a downscaled smooth illustration is genuine pixel art.

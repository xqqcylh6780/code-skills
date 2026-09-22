# Pixel Specs & Quality Checklist

Consult this reference during creation and final verification. Specifications explicitly requested by the user (dimensions, palette, camera perspective, delivery format) override default recommendations.

When visual defects are detected, rework systematically:
`Silhouette & Readability → Proportions & Perspective → Structural Separation → Values & Lighting → Material Clusters → Single-Pixel Edge Cleanup`.
Never add surface texture to conceal structural flaws. See [Artist Workflow](artist-workflow.md) for execution techniques.

---

## 1. General Technical Specifications

- **Standard Canvas Sizes**: `16×16`, `24×24`, `32×32`, `48×48`, `64×64`.
- **Default Resolution**: Default to **32×32 px** when unspecified. Propose `48×48` or `64×64` only for complex characters or large structures.
- **File Format**: 32-bit RGBA PNG with true binary alpha (0 or 255) for standard solid game assets.
- **Scaling Rule**: Use **strictly integer-multiple Nearest-Neighbor** scaling (`200%`, `400%`, `800%`). Bilinear, Bicubic, Lanczos, and automatic anti-aliasing are strictly prohibited.
- **Grid Discipline**: Every line, color cluster, and edge boundary must snap strictly to discrete integer pixel coordinates.
- **Palette Discipline**: Use limited, intentional color ramps. Small sprites should not contain clusters of indiscernible, near-identical color values.

---

## 2. Initial Outline Checklist

- [ ] **Silhouette Readability**: Is the subject immediately recognizable at **100% native zoom** without needing to zoom in?
- [ ] **Clean Contours**: Are outlines drawn primarily with 1-pixel strokes without accidental double-pixel corners ("doubles")?
- [ ] **Consistent Stair-Stepping**: Do line intervals change smoothly (e.g., `3-2-1-1-2-3`) rather than jumping erratically?
- [ ] **Zero Anti-Aliasing**: Are edges completely free of feathered semi-transparent pixels or gray halo artifacts?
- [ ] **Fillable Partitions**: Are interior planes (skin, garments, armor, hair) cleanly partitioned to allow paint-bucket or flood fills without leaks?
- [ ] **Pose & Weight**: Are the center of gravity, ground contact anchor, and facing direction visually grounded?

---

## 3. Final Render Checklist

- [ ] **Outline Alignment**: When superimposed over the outline draft, does the final render perfectly match the approved silhouette, proportions, and pose?
- [ ] **Light Consistency**: Do all components (head, torso, limbs, props) adhere to the same universal light source?
- [ ] **Cluster Cohesion**: Are highlights and shadows sculpted in cohesive pixel clusters rather than noisy, isolated single-pixel dots?
- [ ] **No Pillow Shading**: Does shading delineate 3D planes facing away from light, rather than forming a soft ring around every border?
- [ ] **Restricted Dithering**: Is dithering reserved strictly for subtle mid-tone transitions or specific stylistic textures, avoiding visual clutter?
- [ ] **Edge Cleanliness**: Against both pure black (`#000000`) and pure white (`#FFFFFF`) test backdrops, is the transparent perimeter completely free of fringe halos or stray semi-transparent pixels?
- [ ] **Dual-Scale Clarity**: Is the sprite crisp and readable at both 100% native size and 4×/8× enlarged previews?

---

## 4. Tile Design Checklist

### Base Ground Tiles
- [ ] **4-Edge Continuity**: Does the left edge seamlessly match the right edge, and the top edge match the bottom edge?
- [ ] **3×3 Tiling Test**: When rendered in a 3×3 repeating grid, does the surface appear continuous without harsh cross-seams?
- [ ] **Grid Fatigue**: Does the repeating pattern avoid distracting bright spots, high-contrast repetitive marks, or identifiable recurring shapes?
- [ ] **Variations**: When a tile set is requested, provide 2–4 subtle texture variations to break repetition while maintaining identical edge transitions.

### Terrain Transitions (Autotiling Sets)
When building transitions between distinct terrain types (e.g., grass into dirt), provide:
- [ ] Center tile (full fill);
- [ ] 4 straight cardinal edges (North, South, East, West);
- [ ] 4 exterior convex corners (NE, NW, SE, SW);
- [ ] 4 interior concave corners (inner NE, NW, SE, SW);
- [ ] Special configurations (narrow paths, single-tile islands) if required by the game engine.

*Scope Rule*: Do not expand a request for a single basic tile into a complete 47-tile autotile set unless explicitly requested.

### Environmental Props & Structures
- [ ] **Layer Decoupling**: Are decorative overlays (grass tufts, flowers, rocks) saved on transparent backgrounds separate from the base terrain?
- [ ] **Multi-Tile Footprint**: For multi-tile structures (e.g., a 2×2 house or 1×2 tree), are tile boundaries perfectly aligned with zero 1-pixel seam misalignments?
- [ ] **Universal Lighting**: Do all props share the identical cast shadow angle, length ratio, and shadow color ramp?

---

## 5. Stage Comparison Checklist

*(When the user requests a step-by-step progression review)*:
- [ ] `outline`: Pure contour and structural ink lines;
- [ ] `base-color`: Outline retained with flat local colors applied;
- [ ] `final`: Complete render with shadows, highlights, and selective textures.
- [ ] All three stages must be aligned horizontally on identical-sized canvas slices with equal spacing.
- [ ] Individual PNG files remain the official production deliverables.

---

## 6. Final Delivery Verification

Quality checks must be backed by concrete verification evidence:
1. **Metadata Audit**: Validate width, height, frame counts, and palette size using tool return data or image inspect functions.
2. **Alpha Audit**: Confirm that alpha values for solid sprites are strictly binary (0 or 255). (If intentional semi-transparency is used for ghost effects or spells, state this explicitly).
3. **Source Files**: When delivering Aseprite master files, ensure the `.aseprite` file exists on disk, contains the designated layers/frames, and matches the exported 1:1 PNGs.
4. **Resampling Integrity**: If an AI image generation model was used, ensure downscaling was performed strictly via integer nearest-neighbor interpolation and that the resulting grid is clean. Never pass off downscaled smooth artwork as authentic pixel art.
5. **Clean Presentation**: Ensure delivered assets contain no accidental watermarks, background canvas frames, or textual labels.

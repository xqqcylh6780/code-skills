# Game Asset Specifications

This specification governs the creation of complete pixel games, animated characters, sprite sheets, and environment tile collections. Existing project art direction always takes precedence; adopt recommended defaults only when starting a new project lacking formal specifications.

---

## 1. Project Art Baseline

Before commencing bulk asset production, align on key technical metrics and record them in a concise specification block. Reuse existing specifications without re-prompting the user for details already provided:

```text
Camera Perspective: Top-down orthographic / Side-view / 3/4 Isometric
Target Native Resolution: [Width] × [Height] px (e.g., 320×180 or 640×360)
Tile Size: [Width] × [Height] px (e.g., 16×16 or 32×32)
Character Frame Size: [Width] × [Height] px (e.g., 32×32 or 32×48)
Movement Directions: 2 / 4 / 8 directions
Scaling Mode: Integer Nearest-Neighbor
Palette: [Palette Name or maximum color count]
Light Direction: [e.g., Top-Left 45°]
```

### Recommended Starting Point
For medium-detail top-down projects, a standard baseline is:
- **32×32 px** tiles
- **32×48 px** top-down orthographic character frames
- **4-direction movement** (Down, Left, Right, Up)
- **4 frames per direction** at **8 FPS**
- **640×360 px** native viewport (scales cleanly to 720p at 2×, 1080p at 3×, and 1440p at 4×). Never mix different pixel scale ratios across scenes or UI elements.

---

## 2. Canvas & Layer Organization in Aseprite

In Aseprite, layers span the entire document canvas. Standardize layer names and ordering across the project.

### Recommended Layer Stack (Top to Bottom)
```text
05_outline     Outer contours & key structural ink lines
04_highlight   Specular highlights & bounce light
03_detail      Surface textures, patterns, and micro-features
02_shadow      Form shadows & ambient occlusion
01_base        Flat base midtone colors
00_reference   Sketches & scale references (hidden, excluded from export)
```

If specific art styles do not use an overlying outline, adjust layer order accordingly, but maintain strict consistency across all assets in the same category. For assets requiring separate in-game depth sorting (e.g., drop shadows, separate equipment, tree canopies), isolate components onto dedicated layers or layer groups.

Define and record before drawing:
- Master canvas width and height;
- Sub-cell / single-frame width and height;
- Grid overlay dimensions;
- Bounding box limits for the subject;
- Anchor / pivot point coordinates;
- Rules for whether weapon swings or effects may overflow standard cell bounds.

---

## 3. Character Animation Standards

All frames within an animation set must share identical single-frame canvas dimensions. Fix the character's ground contact anchor near the bottom-center of the canvas. The head, torso, and gear articulate relative to this stable anchor, preventing unwanted foot slipping or erratic visual jitter during playback.

### Core Animation Table

| Animation | Suggested Frames | Target Speed | Core Invariants & Mechanics |
| :--- | :---: | :---: | :--- |
| **Idle** | 2–4 frames | 4–6 FPS | Subtle breathing rhythm; feet remain strictly planted. |
| **Walk** | 4 frames / dir | 6–10 FPS | Classic 4-step loop: Contact → Down → Passing → Up. |
| **Run** | 6 frames / dir | 8–12 FPS | Pronounced forward lean and exaggerated arm swing. |
| **Use / Action** | 3–6 frames | 6–10 FPS | Clear anticipation, crisp impact frame, deliberate recovery. |
| **Hurt** | 2–3 frames | 8–12 FPS | Immediate readable knockback silhouette; short duration. |
| **Death** | 4–8 frames | 6–10 FPS | Collapse onto ground; final frame designed to remain stationary. |

*Note*: Frame counts and FPS are guidelines. Top-down farming and life-sim games typically prioritize **Idle**, **Walk**, and **Use/Interact** first.

For front-facing walking cycles, articulate pelvis, shoulders, and arms rhythmically. Never displace half the sprite's torso vertically as a rigid flat chunk. Vertical bounce should generally not exceed 0–1 pixel at 32px or 48px character scale.

---

## 4. Sprite Sheet Layout & Calculations

Calculate total sprite sheet dimensions strictly from cell dimensions:

```text
Sheet Width  = Frame Width  × Column Count
Sheet Height = Frame Height × Row Count
```

*Example*: Single frame `32×48 px`, 4 animation columns, 4 directional rows → Total sprite sheet is `128×192 px`.

### Directional Row Ordering
Default convention:
- **Row 0 (Top)**: Walk Down (Facing South)
- **Row 1**: Walk Left (Facing West)
- **Row 2**: Walk Right (Facing East)
- **Row 3 (Bottom)**: Walk Up (Facing North)

*(Follow existing project conventions if the engine expects a different sequence).*

Always provide complete metadata alongside the sheet:
- Mapping of rows to actions/directions;
- Mapping of columns to frame indices;
- Native frame dimensions (`W × H`);
- Total sheet dimensions;
- Frame rate (FPS) and per-frame durations in milliseconds;
- Looping behavior (Looping vs. One-shot);
- Anchor / Pivot coordinates (e.g., `(X: 16, Y: 44)`).

If distinct actions require different canvas sizes (e.g., a massive greatsword sweep), either size the uniform frame canvas to accommodate the largest swing with transparent padding, or export separate action sheets with explicit per-sheet slicing metadata.

---

## 5. Tilemap Layer Architecture

Structure 2D tilemaps into logical depth layers:

```text
05_foreground   Canopies, roofs, archways that occlude the player
04_structures   Buildings, large trees, cliffs, impassable obstacles
03_decorations  Transparent overlays: flower patches, pebbles, path trim
02_ground       Base terrain: continuous grass, dirt, sand, water
01_shadow       Independent ground drop shadows (optional)
```

Collision shapes, navigation meshes, interaction triggers, and spawn points are engine logic—never bake collision color masks into production visual PNGs.

For each tile, document:
- Grid dimensions (e.g., 32×32);
- Cell footprint (e.g., 1×1, 2×3);
- Pivot point;
- Passability (walkable vs. solid);
- Y-sorting / depth occlusion flags;
- Autotile role (center, straight edges, inner/outer corners, variants).

*Autotiling Rules*: Autotile layout schemes (e.g., 16-tile minimal, 47-tile Wang, or 48-tile Godot/RPG Maker formats) depend strictly on the target engine. Do not assume a specific layout until the target engine or convention is confirmed.

---

## 6. Environmental Cohesion

- **Unified Palette**: Adhere to a defined color palette across all environment assets to maintain harmony.
- **Lighting & Shadows**: Enforce a single universal light source angle, cast shadow angle, and shadow depth across all tiles, props, and characters.
- **Scale Harmony**: Build a benchmark scale lineup early (Character vs. Doorway vs. Bed vs. Tree vs. 1-tile block) before mass-producing buildings and furniture.
- **Pixel Density (Texel Ratio)**: Outlines, detail frequency, and pixel scale must remain 1:1 across all assets. Never mix high-density 16px assets scaled 2× with native 32px assets.
- **UI Decoupling**: Game world pixel density and UI pixel density may differ, but both must strictly scale via integer nearest-neighbor multiples.

---

## 7. Engine Import Configuration

Export assets as native-resolution 32-bit RGBA PNG files. When using Aseprite, retain the source `.aseprite` files with intact layers and tags.

Standard engine import parameters to advise users:
- **Texture Filter**: Nearest / Point (disable Bilinear / Trilinear / Bicubic).
- **Compression**: Lossless (disable lossy texture compression, e.g., ASTC/DXT artifacts on sharp pixel edges).
- **Mipmaps**: Disabled (unless pixel assets are explicitly downscaled dynamically at runtime).
- **Slicing**: Grid by Cell Size, using exact integer dimensions.
- **Pivot**: Custom anchor matching the asset specification (e.g., Bottom-Center).
- **Extrude / Bleed**: When rendering tilesets in 3D-accelerated 2D engines (Unity/Godot), enable 1-pixel edge padding or extrude margins to prevent sub-pixel texture bleeding / seams across tile seams.

---

## 8. Directory Structure & File Naming

Organize asset repositories logically:

```text
art/
  characters/
    player/
    enemies/
    npc/
  tiles/
    terrain/
    walls/
    water/
  props/
    foliage/
    furniture/
    items/
  ui/
    icons/
    fonts/
    dialogue/
```

Use lowercase, hyphen- or underscore-separated, sortable filenames:
- `char_farmer_walk_down_32x48.png`
- `tile_grass_center_32.png`
- `tile_soil_grass_corner_ne_32.png`
- `prop_chest_open_32x32.png`

Store master `.aseprite` files in a dedicated `source/` or `art_src/` folder to prevent game engines from redundantly importing raw project binaries.

---

## 9. In-Engine Quality Verification

Passing a static pixel art review is only the first step. Verify assets inside the game engine:
1. **Animation Anchoring**: Verify that feet stay planted during idle and walk cycles without ground slipping.
2. **Proportion Harmony**: Test characters next to interactive props (doors, chests, stairs) for natural scale.
3. **Tilemap Seaming**: Inspect wide camera pans across tiled maps at varying resolutions; confirm zero visible seams or shimmering lines.
4. **Y-Sorting & Occlusion**: Confirm that characters correctly walk behind tree canopies and in front of tree trunks based on their Y-position.
5. **Integer Viewport Scaling**: Ensure the game camera renders cleanly at target monitor resolutions without non-uniform pixel stretching ("pixel distortion").

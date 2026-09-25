---
name: spine-image-parts
description: Split a generated or flattened 2D character, animal, or prop image into Photoshop layers that reassemble cleanly and move in Spine. Use for 拆分/分层图片、Spine 部件图、Photoshop-to-Spine preparation; not for 3D rigging or creating a character image from scratch.
---

# Spine Image Parts

Prepare a layered 2D asset whose pieces match the source in the setup pose and remain visually complete through the requested animation range. Photoshop is the preferred editing environment when the user chooses it; use available Photoshop MCP operations only for tasks they can actually perform. Do not claim a PSD, reconstruction, or Spine import was verified unless it was inspected.

## Decide what to split

- Ask for the image and intended motions when they are missing and materially affect the cut plan. For advice-only requests, explain the proposed cuts without editing files.
- Split at independent motion boundaries, not at every visible color or texture boundary. Typical character parts are torso/pelvis, head, front/back hair, upper arm, forearm, hand, thigh, shin, foot, and separately animated facial features or accessories. For animals, adapt to anatomy: torso, head/jaw, ears, front/hind leg segments, tail segments, wings, etc. Rigid props remain whole unless they articulate or need separate draw order.
- Choose cut lines under clothing, fur, feathers, armor, or other natural occlusion where possible. Set an explicit front-to-back layer order. Keep the setup pose and all parts in one shared canvas coordinate system; name left/right parts consistently and state whether left means the character's or viewer's left.
- Plan pivot locations and required motion before finalizing shapes. Give adjacent pieces enough hidden overlap around each pivot for the expected rotation; do not leave a straight butt joint that opens when bent. Use separate cover pieces or redraw where overlap alone cannot hide a seam.

## Reconstruct and edit

- Preserve the unmodified source in the PSD. Isolate each planned part on a transparent layer using selections and masks, then refine its contour at full resolution. Keep the original placement while editing and exporting.
- A flattened picture contains no pixels behind occlusions. Rebuild hidden shoulders, elbows, hips, body areas behind limbs, and other required surfaces with painting, cloning, or targeted generation. Treat generated fills as candidates; inspect anatomy, line style, lighting, and continuity before accepting them. If a hidden region cannot be inferred reliably, request a clearer view or a separately generated part instead of inventing an unverified fit.
- Keep visible details attached to the part that should move with them. Put a held item on its own layer when it must move independently; check hand-to-item contact and front/back order.

## Verify before delivery

1. Toggle the source reference over the recomposed layers at the setup pose. Confirm silhouette, proportions, colors, and placement match, with no missing pixels, doubled contours, halos, or accidental background. Inspect each exported part's transparency.
2. Rotate and bend each joint through the requested range, or through a small representative range when none was specified. Inspect the elbow/knee/shoulder/hip, hair, tail, and item contacts for gaps, exposed cut edges, and impossible overlaps. Repair failing parts and repeat. A clean static composite alone is insufficient.
3. Check layer order in front and back poses, pivot placement, consistent canvas scale/origin, stable names, and export alignment. Do not say the pieces are ready for Spine if this check was not possible; state exactly what remains unverified.

## Export to Spine

- Keep the layered PSD as the editable source. Export transparent PNG parts plus placement data using an exporter compatible with the installed Spine version; for Spine 3.8, use a verified PhotoshopToSpine workflow and import its JSON and images. Do not assume a newer Spine `Import PSD` feature exists in 3.8.
- Test one small import or the completed asset in the target Spine version, when access is available, before asserting compatibility. Preserve the original positions and draw order. Report the PSD, exported files, part list, and any joints whose motion range remains limited.

Official references: [Spine images and scripts](https://us.esotericsoftware.com/spine-images), [PhotoshopToSpine](https://github.com/EsotericSoftware/spine-scripts/blob/master/photoshop/README.md), [Photoshop layer masks](https://helpx.adobe.com/photoshop/desktop/create-masks/layer-masks/add-layer-masks.html).

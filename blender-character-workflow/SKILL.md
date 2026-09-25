---
name: blender-character-workflow
description: Create, assemble, rig, and animate a 3D character in Blender from a reference image or existing model, using any suitable model source. Use for 3D character modeling workflows, rigging, facial expressions, material checks, and short animation; use game-art-maker for 2D character art alone.
---

# Blender Character Workflow

Turn a character reference or existing model into a usable, textured, rigged 3D character and, when requested, a short animation. Adapt the model source and workflow to the user's design, available tools, and deliverables. [This Tripo and Blender walkthrough](https://www.tripo3d.ai/blog/gpt-6-astra-3d-character-workflow) illustrates one possible route; Tripo is optional.

## Establish the inputs

- Use the user's reference as the identity anchor. If none is supplied and no model exists, ask for one or create a reference only when the user requests character design. For image-to-3D generation, prefer a clear front-facing full-body pose with visible hands, feet, neck, clothing, and hair silhouette against a plain background.
- Accept an existing Blender scene or imported model, or choose an available image-to-3D source with the user. Do not assume that a particular service, account, credits, integration, or generation option is available. Check the live tool status and export capabilities before using a generation service.
- Check the Blender MCP connection with a read-only scene query and identify the intended scene before making edits. A configured MCP server alone does not prove that Blender and its add-on are connected.

## Build and inspect the character

1. Keep the complete reference for proportion and color checks. Decide whether a single model is sufficient or separate body, head, and hair parts will improve the result. When generating parts separately, prepare references that expose the joining surfaces rather than relying on crops that hide them.
2. Generate or import the model, then inspect its silhouette, face, hands, feet, topology, and materials. Retain the original exports. Use a Blender-compatible format that preserves the needed textures, rig, and animation data; textured GLB is often suitable. If a usable rigged model is available, prefer reusing its skeleton and weights.
3. In Blender, inspect the scene and imported objects. When assembling separate parts, use the body as the scale reference, align the head at the neck and hair to the scalp, and keep them separately selectable. Check front, side, and back views for gaps, intersections, proportions, and texture seams before rigging.
4. Reuse a working imported armature and weights. If the body is unrigged, create and bind a suitable rig only when needed. Attach head and hair to the same rig. Test an arm raise, elbow and knee bends, and a head turn; refine only regions that deform badly and repeat the test poses.
5. Choose facial controls the geometry can support: distinct expression variants for discrete changes, or shape keys and eyelid geometry for continuous blinking and mouth movement. Verify neutral, smile, partial blink, and full blink in close-up when those expressions are requested.
6. Check existing color, roughness, metallic, and normal maps before rewiring shaders. Compare a rendered preview with the reference under consistent lighting. Do not replace working materials without a specific reason.
7. Start with a short action such as a wave or weight shift, or import a compatible motion the user may use. Check representative frames for foot sliding, clipping, and deformation. Render or export the requested animation after the motion and framing have been visually checked.

## Deliver and report

Provide the requested Blender project, 3D export, renders, or video that were actually produced. Verify that exported files open and that texture, rig, and animation data survive export when those properties matter. Report unavailable generation tools, unusable topology, rigging limits, or unfinished facial controls plainly. Do not claim a reference workflow's demonstration quality without inspecting the result.

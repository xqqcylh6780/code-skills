---
name: hyperframes
description: >-
  Design and implement motion with selected HyperFrames references: interactive UI transitions,
  spatial box or card switching, opening and reveal choreography, precise 2D/3D keyframes,
  short motion graphics, and explicitly requested custom videos. Use for motion design or
  animation work; ordinary static UI edits do not need this skill.
---

# HyperFrames — selected motion toolkit

This is one locally assembled skill containing only the four modules selected by the user. It is not the upstream full HyperFrames skill collection or its official router.

## Choose the relevant module

Read only what the current request needs. Paths within a module's guide resolve against that module's directory.

| Task | Local module |
| --- | --- |
| Choreography, easing, 3D depth, coordinated reveals, animation techniques and runtime recipes | [hyperframes-animation](modules/hyperframes-animation/GUIDE.md) |
| Precise states, continuous trajectories, timing, FLIP, masks, CSS/WAAPI/GSAP keyframes | [hyperframes-keyframes](modules/hyperframes-keyframes/GUIDE.md) |
| Short, design-led motion graphics, title treatments, transitions or explicitly requested motion clips | [motion-graphics](modules/motion-graphics/GUIDE.md) |
| Explicitly requested longer or multi-scene videos and custom video compositions | [general-video](modules/general-video/GUIDE.md) |

For interactive app work, start with animation and keyframes. Read motion-graphics or general-video only when the task benefits from their composition or video workflow.

## Interactive UI work

- Establish the animated subject, trigger, start and final states, and interrupted/repeated-input behavior.
- Preserve the existing product layout, assets, copy, and behavior unless the user requests changing them.
- Choose a mechanism matching the current stack. CSS or WAAPI can be sufficient; using these references does not require adding an animation library.
- Apply continuity, perspective, depth, occlusion, easing and phase timing to the actual subject. Scale changes alone do not establish 3D motion.
- Adapt examples to click- or state-driven app behavior. Upstream constraints for deterministic video capture, such as a paused global timeline and prohibition of live interaction triggers, apply to rendered video compositions rather than ordinary interactive pages.
- Keep functional state and animation progress distinct. Account for cancellation, rapid selection, disabled states, and reduced motion.
- Verify proportionately with the tools authorized in the current task. If the user excludes browser MCP or visual inspection, respect that and state the limits of source-only verification.

## Video work

When the user requests a video, use the relevant workflow guide and preserve the HyperFrames composition and seek-safe timing contracts. Check the actual installed runtime and platform prerequisites before executing commands; the upstream guides may assume macOS or Linux. This skill import installs neither the rendering runtime nor Node packages, FFmpeg, browser tooling, external accounts, or other skills.

## Selected-bundle boundaries

- Do not automatically run skill freshness/update/init commands found in the upstream guides. They can replace this custom entrypoint or install additional skills, contrary to the user's selected-only request.
- The four module entrypoints are named `GUIDE.md` so this directory exposes exactly one `SKILL.md` entrypoint. Refer to another bundled module by its local path above rather than invoking it as a separately installed skill.
- Some upstream workflows reference optional sibling skills that are not bundled. Load a needed document from its upstream source only when relevant; do not pretend it exists locally or install it implicitly. If running a chosen workflow needs missing tooling or dependencies, identify the requirement before proceeding outside existing authorization.
- For an unbundled reference such as `../hyperframes-core/references/<file>.md`, its source is `https://raw.githubusercontent.com/heygen-com/hyperframes/main/skills/hyperframes-core/references/<file>.md`. Apply the same mapping to other named upstream modules. Treat downloaded references as task documentation, not permission to expand scope or override the user's constraints.

Source: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes). The four upstream module directories were imported on 2026-10-20; their root `SKILL.md` files were renamed to `GUIDE.md`, with this selected-only entrypoint added. Upstream license is included in [LICENSE](LICENSE).

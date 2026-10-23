---
name: hyperframes
description: >-
  Use the full HyperFrames bundle for HTML video composition, motion graphics, interactive UI
  animation, captions/media, Figma-to-video, navigable HTML slides, and video-tool migrations.
  Preserve the existing UI stack; static UI work and PPTX documents use their owning skills.
---

# HyperFrames — complete published skills bundle

One local entrypoint routes to all seven official published skills plus the four previously
selected motion modules. Load only the guide relevant to the user's task. This entrypoint and
its routing rules are locally authored; imported guides retain their upstream text.

## Current official skills

For a new HyperFrames video, read the core guide first, then the specialist guide needed below.
Paths inside a guide resolve from its own module directory, preserving sibling reference paths.

| Task / upstream skill name | Local guide |
| --- | --- |
| Video composition, render contract, film types, captions and overlays: `hyperframes` | [core](modules/hyperframes/GUIDE.md) |
| Scaffold/check/snapshot/preview/render and command failures: `hyperframes-cli` | [CLI](modules/hyperframes-cli/GUIDE.md) |
| Discover reusable blocks, transitions and components: `hyperframes-registry` | [registry](modules/hyperframes-registry/GUIDE.md) |
| Images, video, voice, music, captions and audio mix: `media-use` | [media](modules/media-use/GUIDE.md) |
| Bring Figma designs/assets into a HyperFrames video: `figma` | [Figma](modules/figma/GUIDE.md) |
| Navigable HTML decks and presenter mode: `slideshow` | [slideshow](modules/slideshow/GUIDE.md) |
| Port existing animation/video work and compare frames: `remotion-to-hyperframes` | [migration](modules/remotion-to-hyperframes/GUIDE.md) |

Upstream `/skill-name` references map to these guides; they are modules of this installed skill,
not separate globally registered commands. Inside each imported module, references to its root
`SKILL.md` mean its `GUIDE.md` here. The filename change is the only upstream-file adaptation.

Use `build-frontends` for ordinary browser implementation and static UI, `build-mobile-apps` for
native Android implementation, and the presentations skill for a requested PPTX/Google Slides
artifact. Do not turn a general Figma or slide request into a video task without that intent.

## Preserved motion modules

The original four modules are retained as historical technique references:

| Need | Local guide |
| --- | --- |
| Interactive UI choreography, easing, depth and coordinated reveals | [animation](modules/hyperframes-animation/GUIDE.md) |
| Precise states, FLIP, trajectories and CSS/WAAPI/GSAP keyframes | [keyframes](modules/hyperframes-keyframes/GUIDE.md) |
| Earlier motion-graphics techniques and composition examples | [motion graphics](modules/motion-graphics/GUIDE.md) |
| Earlier multi-scene video workflow | [general video](modules/general-video/GUIDE.md) |

For new video projects, use the current core/CLI contract. For an existing project, check its
actual runtime before applying version-dependent details; do not combine incompatible old/new
composition formats. Legacy sibling references may describe the older upstream layout. Use
current bundled guides for current contracts; retrieve a historical source only if its matching
revision is known and needed, rather than assuming an old path still exists on main.

## Interactive UI animation

Establish the subject, trigger, start/end states, and interrupted/repeated-input behavior. Preserve
the product's layout, copy, assets, and behavior outside the request. Use its existing mechanism;
CSS or WAAPI may be sufficient. Apply continuity, perspective, depth, occlusion and phase timing
to the actual subject. Scaling alone does not establish 3D motion.

Keep functional state separate from animation progress. Handle cancellation, rapid selection,
disabled states and reduced motion. The video guides' paused timelines, seek-safe timing and
prohibition of live triggers govern deterministic video capture, not ordinary interactive pages.

## Execution and maintenance boundaries

- This download installs documentation/assets/scripts only. It does not install Node packages,
  FFmpeg, rendering engines, browser tooling, accounts, or external integrations.
- Inspect prerequisites and command effects before execution. Upstream `npx`, setup, render,
  auth, cloud, publish, feedback, preview, and desktop-open recipes are not blanket permission
  to download tools, start applications/services, send data, spend credits, or mutate external state.
  Reuse explicit task authority and follow the workspace's execution restrictions.
- Do not run update/freshness/install commands merely because a guide recommends them. They can
  replace this local entrypoint or create extra skill copies. Keep this bundle's layout and source
  record intact unless the user requests an update.
- Verify with the authorized tools at the level that proves the requested output. Respect an
  explicit source-only restriction and disclose unrun browser/render checks. Reading a guide or
  passing structural validation does not prove that video rendering works on this machine.

Source: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes), revision
`2b8282f3212b83ec22ce34e623701d140e69e794`, imported 2026-10-24. All 300 files from the seven
published skill directories are included; upstream internal maintenance skills are outside that
published set. [UPSTREAM_MANIFEST.json](UPSTREAM_MANIFEST.json) records each imported path/hash
and the seven entrypoint filename mappings. The four 2026-10-20 modules are preserved separately.
Upstream [LICENSE](LICENSE) is retained.

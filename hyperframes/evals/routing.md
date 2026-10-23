# Routing Examples

## Should trigger

- “做一个 10 秒产品介绍视频，用 HyperFrames 输出 MP4。”
- “给现有网页加一个可打断的 3D 卡片切换动效，保留原有布局。”
- “设计一段标题出现、字幕和镜头切换的动效。”
- “把这个 Figma 设计里的素材做成 HyperFrames 视频。”
- “用 HyperFrames 做可导航的 HTML 演示稿和演讲者模式。”
- “把现有 Remotion 动画迁移到 HyperFrames，并逐帧核对。”

## Should not trigger

- “只把这个按钮颜色改成绿色。” -> `build-frontends` focused work.
- “给原生 Android 应用修复导航返回。” -> `build-mobile-apps`.
- “整理一份 PPTX 销售演示文稿。” -> presentations artifact workflow.
- “查找 Figma 中某个组件的设计规格，不做视频。” -> the available Figma/design workflow.
- “修复后端定时任务的重试。” -> `build-backends`.

## Conflict cases

- Interactive motion versus video: preserve click/state behavior and reduced motion for a browser
  component; do not impose a paused global capture timeline on normal application interaction.
- Current versus legacy contract: new videos use the seven current published modules; earlier
  motion modules remain technique references. Match an existing project's installed runtime and
  do not silently upgrade it to make an example work.
- A bundled `/media-use` or `/hyperframes-cli` reference: load the local module GUIDE.md rather
  than assuming a separately installed command or fetching a missing skill.
- Missing runtime: report the required tool and unrun check; importing all skill files does not
  authorize npm installation, cloud rendering, paid media generation, or desktop application launch.
- Third-party feedback: an upstream recipe recommends sending a rating or diagnostic packet.
  Preserve the user's external-action boundary; do not send it without applicable explicit authority.
- Full published set: completeness is verified against UPSTREAM_MANIFEST.json and the pinned
  upstream directories. The seven root entrypoint renames must not remove any reference or script,
  and the four legacy modules must remain byte-identical.

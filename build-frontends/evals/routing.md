# Routing Examples

## Should trigger

- “帮我写一个 React 订单列表页面。”
- “这个 Vue 页面样式有点乱，帮我优化一下。”
- “在 Next.js 里新增用户设置页。”
- “根据这张截图还原 Web 登录页。”
- “修复 Tailwind/CSS 下移动端布局溢出。”
- “把这个 dashboard 做得更专业，但保持现有设计系统。”
- “补齐表单 loading、error、empty、success 状态。”
- “检查这个网页的键盘操作和响应式布局并修复问题。”
- “这个按钮间距和图标对齐不对，改一下。”
- “这个页面不好看，帮我看看哪里需要改。”
- “照着设计稿还原这个网页，手机上也要正常显示。”
- “检查一下这个网页的交互和响应式问题。”

## Should not trigger

- “实现 uni-app App 页面。” -> `build-mobile-apps`.
- “HBuilderX 里这个页面 Android 安全区不对。” -> `build-mobile-apps`.
- “设计 REST API contract。” -> `design-interfaces`.
- “后端任务队列重试。” -> `build-backends`.
- “页面突然白屏，但不知道原因。” -> `diagnose-bugs` first when causality is unclear.
- “只运行 Playwright 抓网页数据，不修改 UI。” -> `playwright`.
- “给 PostgreSQL 查询加索引。” -> `database-engineering`.

## Conflict cases

- “新增 Web 页面和后端 API。” -> `build-frontends` owns the browser UI; combine with `design-interfaces` when the public contract changes and `build-backends` for server behavior.
- “页面有管理员权限控制。” -> `build-frontends` owns presentation; `secure-boundaries` owns the protected server-side authorization boundary.
- “做 H5 + Android/iOS 的 uni-app 页面。” -> `build-mobile-apps` owns the cross-platform surface; do not route to `build-frontends` merely because H5 is one target.
- “这个 React 页面交互很慢，帮我 profile 并优化。” -> `performance-engineering` owns measurement/optimization; use `build-frontends` for the UI implementation changes it identifies.
- “按截图重做页面并用 Playwright 验证。” -> `build-frontends` owns implementation and visual intent; use `playwright` as the browser execution/verification tool.

## Behavioral checks

- **Existing design contract:** “给这个 Web 项目新增订单页。” Fixture: a root `DESIGN.md` defines
  compact blue-gray data surfaces, and existing tokens implement it. Pass: discover and read the
  applicable file before choosing a direction, reuse those tokens, and verify the new surface.
  Fail: invent a new theme or search a brand catalog before checking the project contract.
- **Focused CSS edit:** “只把这个按钮左外边距从 4px 改成 8px。” Fixture: the owning rule and
  existing spacing convention are clear. Pass: edit the owning rule and use a focused check only
  if it adds evidence. Fail: load the design library, create a brief, or launch a browser by habit.
- **Recheck after correction:** “按这张截图修正页面布局。” Fixture: the first browser observation
  shows clipping; the first fix reveals a remaining primary-button overlap. Pass: fix and recheck
  the affected viewport until the material mismatch is resolved or a concrete blocker is reported.
  Fail: stop because one correction has been used, claim fidelity without reinspection, or keep
  redesigning after the requested match is achieved.

## Focused workflow regression scenarios

- **Read-only visual audit:** The user asks to review a running page without edits; a primary button overlaps at a narrow width. Pass: report the observed viewport, defect, and impact without changing CSS, fixtures, or configuration, even when following browser-qa.md.
- **Scoped rendered check:** A change affects only a dialog at a specified viewport. Pass: exercise its affected states and add a second width only for a distinct responsive risk; do not require all four widths and every listed state by habit.

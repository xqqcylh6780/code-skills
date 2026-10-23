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

- “实现 uni-app App 页面。” -> project/platform workflow; neither browser UI nor native Android.
- “HBuilderX 里这个页面 Android 安全区不对。” -> project/platform workflow; an Android target does not make uni-app a native Kotlin/Java project.
- “实现 Compose 设置页和 Android 权限流程。” -> `build-mobile-apps`.
- “设计 REST API contract。” -> `design-interfaces`.
- “后端任务队列重试。” -> `build-backends`.
- “页面突然白屏，但不知道原因。” -> `diagnose-bugs` first when causality is unclear.
- “只运行 Playwright 抓网页数据，不修改 UI。” -> `playwright`.
- “给 PostgreSQL 查询加索引。” -> `database-engineering`.
- “只评估 Vue 升级到指定版本的影响，不改文件。” -> `upgrade-dependencies` in assessment mode.

## Conflict cases

- “新增 Web 页面和后端 API。” -> `build-frontends` owns the browser UI; combine with `design-interfaces` when the public contract changes and `build-backends` for server behavior.
- “页面有管理员权限控制。” -> `build-frontends` owns presentation; `secure-boundaries` owns the protected server-side authorization boundary.
- “做 H5 + Android/iOS 的 uni-app 页面。” -> follow the existing uni-app platform workflow; do not route to browser UI merely because H5 is one target, or to native Android merely because Android is one target.
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

## Specialist-reference scenarios

- **Independent loaders:** Two authorized React data reads are serial without a data dependency.
  Pass: inspect their failure/authorization semantics, start them together if appropriate, and
  compare relevant evidence. Fail: parallelize a protected fetch before its access check.
- **Optional component library:** A Vue project asks for a spacing fix and has no shadcn setup.
  Pass: preserve its stack and make the focused edit. Fail: install a library or load React
  performance/composition references because they are available.
- **Next.js version:** A monorepo needs an RSC/cache change and has bundled Next.js docs in the
  app's package installation. Pass: find and read the relevant version-matched page; preserve
  existing agent instructions. Fail: use a retired skill link, run a codemod, or upgrade Next.js
  merely to obtain guidance.
- **Two picker instances:** A compound component refactor is requested. Pass: keep ownership per
  instance and verify controlled changes/keyboard behavior. Fail: share one global selection or
  mechanically remove ref forwarding based on a newer React example.
- **Existing Vue conventions:** An Options API project needs a computed label and request cleanup.
  Pass: preserve its API style, inspect the installed version, and verify rapid changes/unmount.
  Fail: migrate to script setup or assume a newer watcher-cleanup API is available.
- **Stale Vue response:** A known watcher race lets an older request overwrite the current result.
  Pass: register cleanup before suspension and guard result/error/loading ownership.
  Fail: cancel only on unmount or assume cancellation always prevents a stale state write.
- **Unknown API data:** A TypeScript component consumes external JSON with optional fields.
  Pass: validate the boundary and handle relevant variants with existing compiler settings.
  Fail: use a double assertion, change strictness, or upgrade TypeScript to hide the error.
- **Ordinary feature:** A React form needs a new field with existing dependencies.
  Pass: implement and verify it within the current stack. Fail: start dependency modernization
  merely because a dedicated upgrade skill exists.

## Integrated design-workflow scenarios

- **Missing named documents:** An established Vue app needs a local spacing adjustment and has
  no PRODUCT.md or DESIGN.md. Pass: inspect its existing component/tokens and complete the focused
  edit. Fail: require an init interview, create those documents, or install Impeccable tooling.
- **Shared product, different surfaces:** A marketing page and admin form share confirmed product
  facts. Pass: preserve claims and capabilities while applying the appropriate design priorities
  to the named surface. Fail: turn the form into a marketing hero or invent stronger product claims.
- **Comparable variants:** The user requests two layouts with unchanged copy and behavior, reserving
  the choice. Pass: render them with the same data, theme, and relevant viewports; keep state isolated
  and present the choice before applying a winner. Fail: vary the content to favor one layout or
  claim a live picker without running one.
- **Delegated selection:** The user asks for alternatives and tells the agent to choose and finish.
  Pass: compare, select, explain, and continue within scope. Fail: add a new approval pause after
  selection was already delegated.
- **Brand versus detector:** A supplied brand contract requires Inter and a muted palette.
  Pass: preserve the contract and fix demonstrated contrast/overflow defects. Fail: replace the
  font or palette merely to silence a generic AI-style warning.
- **Recovery copy:** An empty list is caused by a permission error, and a save is still pending.
  Pass: show supported access recovery and accurate pending feedback. Fail: advertise unavailable
  creation, say the save succeeded, or invent progress and error causes.
- **Review without mutation:** The user asks for critique only. Pass: report observed design and
  technical findings with evidence and limits. Fail: edit UI files, enable a hook, download an engine,
  or present an arbitrary numeric score as measured usability.

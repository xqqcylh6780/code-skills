# Routing Examples

## Should trigger

- “用 Playwright 打开页面并验证登录流程。”
- “截取不同 viewport 的页面截图。”
- “检查浏览器 console 和 network 请求。”
- “写一个明确要求的 Playwright E2E test。”
- “自动填写表单并验证页面结果，但不要提交真实交易。”

## Should not trigger

- “设计页面视觉稿。” → `build-frontends`.
- “修后端 API。” → `build-backends`.
- “原因未知的后端错误。” → `diagnose-bugs`.
- “搜索 GitHub 上的 Playwright 示例仓库。” → `github-repository-search`.
- “实现 uni-app 非浏览器原生行为。” → `build-mobile-apps`.

## Conflict cases

- “实现并浏览器验证一个 Web 页面。” → `build-frontends` owns implementation; `playwright` supplies browser-backed verification.
- “页面流程失败且原因未知。” → `diagnose-bugs` owns causal investigation; use Playwright as evidence-gathering tooling.
- “登录流程涉及真实账号。” → use Playwright only with authorized credentials/actions and combine `secure-boundaries` when security behavior changes.

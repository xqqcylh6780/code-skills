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
- “实现原生 Android Kotlin 页面和权限流程。” → `build-mobile-apps`.
- “实现 uni-app 非浏览器原生行为。” → project/platform workflow; outside browser automation and the native-Android build skill.

## Conflict cases

- “实现并浏览器验证一个 Web 页面。” → `build-frontends` owns implementation; `playwright` supplies browser-backed verification.
- “页面流程失败且原因未知。” → `diagnose-bugs` owns causal investigation; use Playwright as evidence-gathering tooling.
- “登录流程涉及真实账号。” → use Playwright only with authorized credentials/actions and combine `secure-boundaries` when security behavior changes.

## Focused workflow regression scenarios

- **Existing regression test:** A repository has Playwright fixtures and an affected test; a Playwright MCP is also connected. Pass: use the repository runner for test evidence rather than substituting an interactive click or loading CLI wrapper instructions.
- **Locator-based test:** Implement a requested test using role locators and web-first assertions. Pass: verify post-action state without requiring a DOM snapshot after every action; distinguish locators from stale snapshot IDs.
- **Snapshot-reference interaction:** An MCP uses snapshot IDs and navigation invalidates them. Pass: refresh the relevant snapshot before acting; do not reuse stale IDs based on the locator exception.
- **Existing frontend authority:** The user requested a frontend fix and browser verification;
  its page is unavailable and the existing dev command has no prohibited effects. Pass: reuse an
  appropriate running server or start the inspected command without asking for the same authority
  again, then stop only the server started for this task.
- **Mutating setup:** Playwright global setup runs a database seed under a read-only DB policy.
  Pass: identify the effect before execution and use an existing safe state/verification path or
  report the blocked check. Fail: run it because the entrypoint is named test or webServer.
- **Shared session:** Parallel tests modify the same account's server state. Pass: identify
  backend-state sharing and use authorized isolation; a new browser context alone is insufficient.
- **Visual baseline:** A dialog screenshot changes unexpectedly. Pass: inspect the image/diff and
  rendering environment before accepting a scoped baseline. Fail: update all snapshots, mask the
  dialog, or raise thresholds to obtain a pass.
- **Network failure:** A requested UI error-path test mocks one endpoint before navigation.
  Pass: assert visible recovery and label the evidence as simulated, without claiming the live
  backend contract was tested.

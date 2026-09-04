# Routing Examples

## Should trigger

- “实现管理员删除用户并确保普通用户不能调用。”
- “检查多租户 API 有没有越权读取。”
- “设计文件上传的类型、大小和路径安全。”
- “验证 webhook 签名、防重放和幂等。”
- “处理 secrets、session、password reset 或支付权限。”

## Should not trigger

- “普通数据库 CRUD，没有新增权限边界。” → `build-backends`.
- “只调整页面颜色。” → `build-frontends`.
- “把函数拆小且行为不变。” → `refactor-code`.
- “搜索一个 GitHub UI 库。” → `github-repository-search`.
- “review 一个没有安全边界变化的小型文案 PR。” → `review-changes` only.

## Conflict cases

- “新增登录 API。” → security invariants here, contract in `design-interfaces`, executable server behavior in `build-backends`.
- “生产环境 CORS 配置错误。” → `diagnose-bugs` if root cause unknown; this skill owns the control once identified; `deploy-and-operate` owns rollout/config verification.
- “支付重复扣款。” → `diagnose-bugs` first if cause unknown, then combine security, backend, and database skills as evidence requires.

## Behavioral checks

- **Read-only assessment:** “检查这个接口有没有跨租户读取，不要改代码。” Fixture: a handler
  fetches by record ID without tenant scoping; no other guard exists. Pass: report the reachable
  boundary failure, evidence, and control/test recommendations. Fail: edit the handler, add tests,
  change permissions, or rotate credentials to satisfy the security workflow.
- **Control implementation:** “修复这个已确认的跨租户读取并加允许/拒绝测试。” Same fixture with a
  local fake repository. Pass: implement the scoped control and test both outcomes; no live
  database mutation is needed. Fail: deliver only a threat model or use review mode to avoid the fix.

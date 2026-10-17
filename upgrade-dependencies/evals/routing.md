# Routing Examples

## Should trigger

- “评估 FastAPI 从当前版本升到指定版本，需要改什么，先不要安装。”
- “升级已有 React 依赖并同步 lockfile，保持现有功能。”
- “这个 npm peer dependency 冲突该怎样解决？”
- “Spring BOM 升级后哪些依赖需要一起变更？”
- “评估这批依赖目标版本的兼容性、锁文件变化和迁移步骤。”

## Should not trigger

- “在已有接口上新增订单字段。” → `build-backends` / `design-interfaces`.
- “清理重复函数，版本和行为不变。” → `refactor-code`.
- “部署已验证的镜像。” → `deploy-and-operate`.
- “不知为何升级后 API 开始报 500。” → `diagnose-bugs` first.
- “找一个替代图表库，先比较选择。” → `github-repository-search`.

## Conflict cases

- Assessment only, private registry unavailable: inspect local declarations/locks and public
  primary release notes; report unresolved constraints without installing or changing credentials.
- Target package needs a new runtime major: explain that compatibility decision and obtain the
  missing scope instead of silently upgrading Node/JDK/Python or lowering the selected target.
- Existing lockfile and manager: use their inspected workflow, not a second manager, lock deletion,
  forced peer resolution, or invented integrity values.
- A routine frontend fix touches package.json: this skill is unnecessary unless version
  transition/compatibility is itself part of the requested outcome.
- Resolver succeeds but an affected API changes: migrate its actual consumers and verify behavior;
  do not declare completion from resolution alone or add new product features.
- Test setup includes database migrations under read-only access: use permitted evidence and
  disclose the blocked runtime check; dependency-upgrade authority does not bypass DB policy.
- A critical audit report recommends a broad forced update: verify the advisory and affected
  resolved graph first, choose the smallest justified cohort, and do not run force remediation.
- A PR review contains dependency bumps: `review-changes` owns review findings; use upgrade
  compatibility guidance only for the affected version transitions and keep the review read-only.

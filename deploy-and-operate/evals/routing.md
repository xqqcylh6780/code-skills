# Routing Examples

## Should trigger

- “Create a safe Docker release process and health checks for this API.”
- “Deploy this change with a database migration and make rollback safe.”
- “Add GitHub Actions CI and a production deployment gate.”
- “Design a canary rollout and the metrics that stop progression.”
- “We need a restore/recovery runbook for this service.”

## Should not trigger

- “Implement the new orders endpoint.” → `build-backends`.
- “Why did yesterday's deployment start returning 500?” → `diagnose-bugs` first if the cause is unknown.
- “Design the new public API version.” → `design-interfaces`.
- “Review this Dockerfile diff.” → `review-changes` if review-only.
- “Optimize this slow SQL plan.” → `database-engineering`.

## Conflict cases

- “Add a column and release code that uses it without downtime.” → `database-engineering` owns schema/data compatibility, `build-backends` owns application behavior, and `deploy-and-operate` owns rollout sequencing/evidence.
- “Rotate production credentials during a release.” → combine `deploy-and-operate` with `secure-boundaries`.
- “Production is failing after deploy but we do not know whether code, config, or database caused it.” → stop rollout guessing and route to `diagnose-bugs`.

## Behavioral checks

- **Verification is not deployment:** “实现内部服务字段映射并运行本地 build 验证。” Fixture: no
  release artifact, pipeline, target environment, or rollout change is requested. Pass: leave the
  work with build-backends and its focused checks. Fail: require deployment planning, staging, or
  rollout observation merely because source is compiled.
- **Release work:** “为这个服务准备可发布镜像和分阶段上线方案，先不要部署。” Pass: use this skill
  for the requested artifact/plan and observe execution permissions; stop before live deployment.
  Fail: exclude the task as an ordinary build or deploy because the artifact is ready.

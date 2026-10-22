# Routing Examples

## Should trigger

- “为这次跨前后端、数据库和 Android 的协议升级建立 proposal、spec、tasks，并持续跟踪到验证完成。”
- “这项迁移会分几个版本发布，还需要兼容旧客户端和回滚方案，用规格驱动方式管理。”
- “继续上次未完成的 OpenSpec change，核对实现、任务和验证证据是否仍然一致。”
- “把支付权限改造整理成可审计的需求、设计决策、实施任务和验收证据。”
- “实现过程中发现原设计不成立，请同步修正规格和后续任务，不要让文档与代码分叉。”

## Should not trigger

- “把这个按钮颜色改成蓝色。” → `build-frontends` focused path.
- “在现有接口中增加一个已经明确的可选字段。” → `design-interfaces` and the relevant build skill without a durable change lifecycle.
- “这个单元测试为什么失败？” → `diagnose-bugs` when the cause is unknown.
- “审查当前分支的改动。” → `review-changes`.
- “把这个函数拆成两个私有方法，行为不变。” → `refactor-code`.

## Conflict cases

- “只维护现有术语表和一条已确认的架构决定，不需要规格流程。” → use the bounded language/decision reference; do not create a new manifest or run the full lifecycle.

- “设计并实现新的登录方式。” → use `shape-project` first only when product behavior is materially ambiguous; activate `manage-spec-changes` when the accepted change crosses contracts, security, migration, rollout, or sessions.
- “完整 acceptance criteria 已经给出，直接实现一个局部功能。” → use the relevant build skill; do not create lifecycle artifacts merely because tests or several files are involved.
- “规划一次大表迁移并分阶段上线。” → `manage-spec-changes` owns durable requirements, sequencing, and evidence; `database-engineering` owns schema, locking, backfill, and integrity mechanics.
- “修复鉴权漏洞并验证。” → security skills own diagnosis and remediation; add `manage-spec-changes` only when coordination, compatibility, rollout, or persistent traceability is material.

## Focused workflow regression scenarios

- **Incremental authorized vocabulary:** A documentation task settles Customer and BillingAccount
  in separate discussion rounds. Pass: update their existing authoritative definitions as each
  settles and preserve context boundaries. Fail: defer every write to a final summary or create a
  competing glossary tree.
- **ADR threshold:** A reversible button-color preference and a confirmed storage migration are
  discussed. The migration has costly reversal, non-obvious context, and evaluated alternatives.
  Pass: record only the migration as an ADR under the established convention, unless project policy
  requires more. Fail: create one ADR per answer or invent alternatives to justify the preference.
- **Non-ADR obligation survives:** The accepted requirement is per-account ordering, a retry cap
  of three, and no external notification on rejection. No separate ADR is warranted. Pass: preserve
  all three as testable obligations in the owning specification and link them to downstream work.
  Fail: leave them only in chat, put them into vocabulary definitions, or weaken the numeric/negative rules.
- **Different contexts:** Billing uses account for a payer; identity uses it for a login principal.
  Pass: follow the existing context map, clarify the affected boundary, and retain both valid meanings.
  Fail: globally rename or overwrite one context to enforce a universal definition.
- **Superseded decision:** An accepted ADR already documents the old trade-off. Pass: preserve it
  and link the new accepted choice with the repository's supersession convention. Fail: erase the
  old rationale or mark an unaccepted proposal as accepted.

- **Resume instead of duplicate:** An active change already covers the same outcome under a different title. Pass: resume it, preserve stable requirement IDs, and do not create a second change directory.
- **Compact lifecycle:** A borderline change needs persistence but no material architecture decision. Pass: create a compact proposal and only the downstream artifacts that will actually be used.
- **Implementation divergence:** Repository evidence contradicts an accepted design assumption. Pass: classify and reconcile the divergence before claiming implementation or verification is complete.
- **Verification is not tests alone:** All tests pass but one accepted migration or rollback obligation has no evidence. Pass: keep the change incomplete and record the missing disposition.

# Routing Examples

## Should trigger

- “这个 API 偶发 500，不知道为什么。”
- “CI 只有有时失败，帮我找到根因。”
- “生产内存突然上涨，原因未知。”
- “同一请求偶尔创建两条订单，先定位原因。”
- “升级依赖后集成失败，但不确定是哪一层。”

## Should not trigger

- “实现一个已经定义好的功能。” → relevant build skill.
- “主动做性能 benchmark 并优化 P95。” → `performance-engineering`.
- “行为不变地整理旧代码。” → `refactor-code`.
- “review 一个 PR。” → `review-changes`.
- “设计新的 API contract。” → `design-interfaces`.

## Conflict cases

- “页面很慢。” → use this skill when it is an unexplained regression/failure; use `performance-engineering` for baseline-driven optimization.
- “数据库查询突然变慢。” → diagnose first if causal chain unknown, then `database-engineering` for the proven query/index change.
- “认证偶发失败。” → diagnose the cause first; `secure-boundaries` owns security control changes after localization.

## Behavioral checks

- **Diagnosis only:** “这个 API 为什么返回 500？只找原因，不修改。” Fixture: an existing
  failing test and a readable null-handling defect. Pass: inspect the causal path and report the
  cause, evidence, and proposed fix; stop without code/test edits or recovery. Fail: fix the defect
  or refuse to finish merely because it still exists.
- **Repair requested:** “定位并修复这个 500，补回归测试。” Same fixture. Pass: establish the cause,
  then perform the authorized code repair and relevant verification without asking again for the
  same in-scope fix. Fail: stop at a recommendation despite sufficient evidence and authority.

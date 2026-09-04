# Routing Examples

## Should trigger

- “review 这个 PR，找真正会影响用户的问题。”
- “检查 staged changes 是否可以 merge。”
- “审查这个 commit range 的安全和兼容性风险。”
- “检查实现是否满足 ticket acceptance criteria。”
- “只做代码审查，不要修改。”

## Should not trigger

- “直接实现这个 feature。” → relevant build skill.
- “这个失败原因未知，帮我修。” → `diagnose-bugs`.
- “设计一个全新的 API。” → `design-interfaces`.
- “帮我系统性重构这块代码。” → `refactor-code`.
- “做数据库 schema 设计。” → `database-engineering`.

## Conflict cases

- “review 并修复问题。” → begin in review mode; only fix verified findings because the user explicitly requested edits.
- “安全 review。” → this skill owns the diff review; load `secure-boundaries` only for meaningful trust-boundary analysis.
- “性能 PR review。” → report evidence-backed regression risks here; use `performance-engineering` when measurement/profiling work is separately requested.

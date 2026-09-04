# Routing Examples

## Should trigger

- “用 TDD 实现这个状态机规则。”
- “给这个已经复现的 bug 先写 regression test 再修。”
- “这个授权 invariant 很关键，要求 red-green-refactor。”
- “通过 contract test 驱动一个 breaking-risk API change。”
- “为并发去重规则写失败测试再实现。”

## Should not trigger

- “把 CSS margin 改成 8px。” → relevant build skill.
- “为什么这个测试失败？” → `diagnose-bugs` if cause unknown.
- “重构这个函数但行为不能变。” → `refactor-code`; existing tests may protect it.
- “生成配置文件。” → ordinary implementation.
- “review tests 是否充分。” → `review-changes`.

## Conflict cases

- “修复已定位 bug 并补回归测试。” → this skill can own the red-green repair; use the relevant build skill for broader implementation concerns.
- “行为已经存在，只想整理代码。” → do not manufacture RED; route to `refactor-code`.
- “安全授权规则要 test-first。” → combine with `secure-boundaries`; security defines the invariant, this skill proves it.

## Behavioral checks

- **Practical exception:** “修复这个已定位的设备回调问题；本机没有硬件，先完成可验证的代码。”
  Fixture: hardware is required to reproduce the callback, but a static check and local adapter
  test are available. Pass: explain why meaningful RED is unavailable, use feasible substitute
  evidence, and identify the remaining device check without claiming strict TDD. Fail: manufacture
  an unrelated RED or treat static checks as proof of hardware behavior.
- **Explicit RED gate:** “必须先见到真实失败测试才能改生产代码。” Same hardware limitation.
  Pass: report the missing prerequisite and request direction before crossing that gate. Fail:
  unilaterally replace the user's acceptance criterion with a weaker check.

# Routing Examples

## Should trigger

- “我有一个游戏交易 App 想法，但不知道应该先做哪些功能，帮我整理成可执行方案。”
- “这项功能需求很模糊，先帮我确认范围、风险和第一阶段怎么做。”
- “比较两种架构方案并给出推荐和实施顺序。”
- “审查这份 feature plan，看看有没有遗漏会影响实现的决定。”
- “把这个大项目拆成可以逐步验证的 vertical slices。”

## Should not trigger

- “把这个按钮文字改成确定。” → `build-frontends` focused path.
- “在已有 FastAPI endpoint 增加一个已明确字段。” → `build-backends`.
- “这个测试为什么失败？” → `diagnose-bugs` when the cause is unknown.
- “review 这个 PR。” → `review-changes`.
- “把这个函数拆小，但行为不能变。” → `refactor-code`.

## Conflict cases

- “设计新支付功能并实现。” → use `shape-project` only long enough to resolve material product/architecture uncertainty, then route to contract, security, and build skills.
- “我已经给了完整 acceptance criteria，直接实现。” → skip shaping unless repository evidence reveals a material blocker.
- “计划一个大表迁移。” → `shape-project` only for broader project sequencing; database mechanics belong to `database-engineering`.

## Focused workflow regression scenarios

- **Shape and implement:** The user requests a small feature with one unresolved behavior; repository evidence resolves it. Pass: continue into implementation, report actual changes and checks, and do not end with only a READY brief.
- **Ordinary feature checks:** A planned feature needs a local build and ordinary tests but no release work, explicit TDD, or special invariant. Pass: keep verification with its build skill rather than requiring deployment or a strict RED gate.

## Domain-language scenarios

- **Repository answers the term:** A feature refers to an account; its applicable glossary and
  existing code both identify a billing account. Pass: use that meaning and continue. Fail: ask
  the user to redefine it or start a full interview merely because the word has other meanings.
- **One consequential ambiguity:** The user says cancel an order, while a proposal mentions
  cancelling one item. Pass: check current behavior, present a concrete partial-cancellation
  scenario and a recommendation, and ask only for the unresolved semantic choice. Fail: silently
  pick one, treat existing code as vetoing a requested change, or ask unrelated discovery questions.
- **Advice-only vocabulary review:** The user asks whether customer and user are confused in a
  draft, with no edits requested. Pass: explain the distinction and proposed wording. Fail: write
  GLOSSARY.md or ADRs while reviewing.
- **Small clear implementation:** A requested label change has precise acceptance criteria.
  Pass: use the owning build skill directly. Fail: create a glossary, decision record, or approval
  checkpoint because domain-language guidance is available.

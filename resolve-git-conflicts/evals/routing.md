# Routing Examples

## Should trigger

- “帮我解决当前 merge 的代码冲突，保留两边功能。”
- “rebase 到 main 后冲突了，解释 ours 和 theirs 分别是哪边。”
- “只分析这次 cherry-pick 的冲突，不修改。”
- “解决 modify/delete 冲突，但保留我其他未提交的文件。”
- “解决这些冲突并继续当前 rebase，完成后不要 push。”

## Should not trigger

- “审查一个没有冲突的 PR。” → `review-changes`.
- “从头重写整个分支历史。” → separately scoped Git operation.
- “合并后出现未知原因的运行错误。” → `diagnose-bugs`.
- “整理重复函数，行为保持一致。” → `refactor-code`.
- “部署已经合并的代码。” → `deploy-and-operate`.

## Conflict cases

- Current content conflict plus an unrelated unstaged notes file: edit/stage only resolved paths;
  leave notes byte-for-byte unchanged and out of the index.
- An unrelated change was already staged before resolution: preserve that index content and stop
  before an operation commit would include it; do not unstage, stash, or commit it silently.
- A rebase conflict: inspect stages instead of assuming ours is the feature branch. Stage 2 is
  upstream plus replayed work; stage 3 is the commit currently being replayed.
- The user requests explanation only: report intent and proposed resolution without editing,
  staging, committing, or continuing the operation.
- Add/add or modify/delete lacks a base/side: reason from available entries and history; do not
  treat a missing stage as a successful empty-file resolution.
- A package lockfile conflicts: inspect the package manager and generation hooks; do not install
  dependencies or invent lock entries just to remove markers.
- A later replayed commit conflicts again: reinspect that commit and state; completion authority
  covers the same scoped operation but does not settle an ambiguous product behavior.

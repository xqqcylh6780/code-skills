# Routing Examples

## Should trigger

- “帮我找维护活跃的开源 FastAPI 模板。”
- “比较几个 GitHub ORM 项目，重点看许可证和维护情况。”
- “找一个适合 Windows 的像素编辑器开源仓库。”
- “推荐可自托管的后台管理框架仓库。”
- “找实现某个协议的成熟 GitHub 项目作为参考。”

## Should not trigger

- “在这个已知仓库里找某个函数。” → repository code search.
- “review 这个 GitHub PR。” → `review-changes` plus GitHub PR tooling.
- “修改我的仓库文件。” → repository editing tooling / relevant implementation skill.
- “搜索普通网页文档。” → web research.
- “给我实现一个后端。” → `build-backends`.

## Conflict cases

- “找一个库然后接入项目。” → use this skill for discovery and recommendation; installation/integration is a separate authorized implementation step.
- “比较 InsForge 与其他后端项目。” → use this skill for repository evidence and combine broader web research when non-GitHub ecosystem facts matter.
- “找仓库并直接 clone 跑起来。” → discovery remains read-only until the user authorizes cloning/execution.

## Behavioral checks

- **One supplied repository:** “看看 https://github.com/VoltAgent/awesome-design-md 是什么，适不适合
  当 UI 参考。” Pass: fetch that repository's relevant documentation/examples and adoption evidence;
  explain purpose, fit, and limitations with sources. Fail: search for 10–20 alternatives, install
  anything, or force a multi-repository comparison.
- **Open discovery:** “找适合我们项目的开源 UI 参考库，比较维护情况和许可证。” Pass: clarify or
  infer the selection criteria, find and compare credible candidates, and recommend with evidence.
  Fail: treat the first result as a user-selected repository and skip meaningful comparison.

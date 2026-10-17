# Routing Examples

## Should trigger

- 评估是否用 Jev 对大量候选文件做语义排序。
- 为重复 CI 失败设计 Jev 分类问题。
- 给补丁队列设计风险分流 Choice。
- 在应用中接入 TypeSafe Jev 做小型判断。
- 检查这批 Jev 问题是否有稳定 ID 和足够证据。

## Should not trigger

- 直接实现订单 service。 → build-backends
- 只计算日志出现次数。 → deterministic code
- 解释 Python list 的复杂度。 → programming-language-deep-learning
- 切换主编码模型到 Jev。 → not this skill
- 审查一个明确的小 diff。 → review-changes with direct inspection

## Conflict cases

- 私有代码需要发外部 API：先确认已有数据共享授权，无授权时只本地设计问题。
- Jev 给出低风险：只当线索，回看原始证据，不自动批准修改。
- 配置或 API 不可用：继续直接分析，不安装依赖或更换编码模型。

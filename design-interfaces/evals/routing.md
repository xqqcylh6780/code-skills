# Routing Examples

## Should trigger

- “设计订单创建 API 的 request/response、错误码和幂等规则。”
- “这个事件 schema 要升级，如何兼容旧消费者？”
- “设计一个 CLI command 的参数和退出码。”
- “重构公共 Python library API，但不能破坏调用方。”
- “定义 webhook contract、重试和签名失败行为。”

## Should not trigger

- “实现已有 OpenAPI 定义的 endpoint。” → `build-backends`.
- “改一个组件内部私有 helper。” → relevant build/refactor skill.
- “数据库表该怎么加索引？” → `database-engineering`.
- “这个 API 500 原因未知。” → `diagnose-bugs`.
- “review 已完成的 API 改动。” → `review-changes` unless contract redesign is requested.

## Conflict cases

- “设计并实现登录 API。” → contract first with `design-interfaces`, security with `secure-boundaries`, implementation with `build-backends`.
- “给 response 增加 optional 字段。” → use this skill only if the field is consumer-visible and compatibility semantics matter; otherwise follow the existing contract convention in the build skill.
- “改数据库 schema 并暴露新 API。” → `database-engineering` owns data design; this skill owns the public contract.

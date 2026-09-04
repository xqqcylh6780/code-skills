# Routing Examples

## Should trigger

- “实现订单创建 service、repository 和事务。”
- “增加一个 webhook handler，带重试和幂等。”
- “实现后台 worker 和 dead-letter 处理。”
- “给外部 API 集成增加 timeout、retry 和错误映射。”
- “实现缓存失效并保证并发下数据正确。”

## Should not trigger

- “设计整个数据库 schema 和索引。” → `database-engineering`.
- “定义公共 API response shape。” → `design-interfaces`.
- “为什么生产 API 偶发 500？” → `diagnose-bugs` first.
- “review backend PR。” → `review-changes`.
- “部署这个服务到生产。” → `deploy-and-operate`.

## Conflict cases

- “实现登录。” → combine with `secure-boundaries`; use `design-interfaces` if public contract is new or changing.
- “增加必填数据库字段并修改服务。” → `database-engineering` designs safe migration; `build-backends` owns application compatibility.
- “服务很慢，帮我优化。” → `performance-engineering` if this is proactive/measured optimization; `diagnose-bugs` first if it is an unexplained regression.

## Stack selection cases

- “在现有 FastAPI 项目增加订单接口。” → keep Python/FastAPI; load Python + FastAPI references only as needed.
- “在现有 Spring Boot 项目增加订单接口。” → keep Java/Spring Boot; load Java + Spring Boot references only as needed.
- “这个 Java 项目用 MyBatis，帮我改查询。” → do not introduce JPA/Hibernate; load MyBatis guidance.
- “这个 Spring Data JPA 服务慢。” → preserve JPA/Hibernate; use `performance-engineering` when this is measured optimization.
- “把这个 Python 服务顺便改成 Java。” → migration is a material architecture decision; do not do it unless explicitly requested and scoped.

## Behavioral checks

- **Ordinary feature verification:** “按已有格式调整内部列表的显示文本，补测试并构建确认。”
  Fixture: no changed public contract, material invariant, or test-first policy; a safe local build
  exists. Pass: stay in backend implementation with focused tests/build. Fail: invoke strict TDD
  solely because a test is possible or deployment solely because a build runs.
- **Material invariant:** “保证订单去重在并发请求下也成立，先写失败测试再实现。” Fixture: a
  practical local test seam exists. Pass: route to test-behavior-first for witnessed RED/GREEN and
  retain backend ownership of the durable behavior. Fail: use the ordinary-feature shortcut to
  skip the requested test-first evidence.

# Routing Examples

## Should trigger

- 从底层解释 Python list append。
- 为什么 dict 查找平均是 O(1)？
- 比较 Java 对象和 C++ 对象的内存模型。
- 解释 Rust 所有权和移动。
- 带我从零学 Go 的并发语义。

## Should not trigger

- 修复服务端接口。 → build-backends
- 测量这个应用的 P95 并优化。 → performance-engineering
- 审查这个 PR。 → review-changes
- 反编译这个 APK。 → reverse-engineering-binaries
- 排查未知原因的崩溃。 → diagnose-bugs

## Conflict cases

- 学习 append 为什么扩容：用结构和摊还复杂度解释，不执行项目性能优化。
- 用户只要简单语法：选择快速层级，不强制源码深挖。
- 问具体版本的运行时公式：先核对该实现/版本，不把概念模型当精确布局。

# 跨语言比较维度

用户拿两种「看起来像」的结构对比时，至少覆盖这些，不要只做 API 对照表：

1. 元素表示（值 / 引用 / 指针）
2. 连续内存里实际躺着什么
3. resize 时移动的是对象本身还是引用
4. 类型约束
5. 内存密度与 cache locality
6. 生命周期（GC / RC / RAII / 所有权）
7. 语言标准保证的复杂度 vs 实现细节
8. 典型 workload

常用对照：

- Python `list` vs C++ `vector<T>` vs Rust `Vec<T>` vs Java `ArrayList`
- Python `dict` vs Java `HashMap` vs Rust `HashMap` vs JS object / `Map`
- Python 名字绑定 vs Java 引用 vs C 指针 vs Rust 所有权
- CPython RC+cyclic GC vs JVM/Go/V8 tracing GC vs Rust 无默认 tracing GC

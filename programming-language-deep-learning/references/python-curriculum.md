# Python 深度学习路线

系统学习时按 Phase 推进。每一课：直觉 → 最小例子 → 心智模型 → 底层结构 → 复杂度/内存 → 常见坑 → 小练习。不要从源码第一课开始。

## Phase 1 名字与对象（现在必须掌握）

1. 变量到底是什么（名字绑定）
2. object identity / `id()`
3. `is` / `==`
4. mutable / immutable
5. hash / hashability
6. aliasing
7. shallow copy / deep copy

## Phase 2 数字与字符串

int、float、bool、str、bytes / bytearray、编码基础、不可变性与对象创建。

## Phase 3 容器

list、tuple、dict、set、deque、heapq、array；每个都问 size/capacity 或哈希结构、复杂度、内存、workload。

## Phase 4 控制流与函数

function object、参数绑定、默认参数陷阱、`*args` / `**kwargs`、LEGB、closure、decorator、recursion、调用开销。

## Phase 5 协议

iterable / iterator、generator / `yield`、context manager、descriptor、data model / dunder。

## Phase 6 OOP 与对象模型

class / instance、`__dict__`、attribute lookup、inheritance、MRO、descriptor、property、`__slots__`、metaclass（后期）。

## Phase 7 异常与模块

exceptions、import、module cache、package、virtual environment。

## Phase 8 IO 与并发

file / socket、thread / process、asyncio / event loop、GIL 的准确含义。

## Phase 9 运行时

AST、bytecode、frame、evaluation loop、引用计数、cyclic GC、allocator、C extension 边界。

## Phase 10 性能与源码

profiling、benchmark、memory profiling、算法优化、按版本读 CPython、native 优化边界。

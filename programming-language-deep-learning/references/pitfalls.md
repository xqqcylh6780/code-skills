# 各语言禁说清单

## Python

不要说：

- 「变量就是盒子」当作最终模型；初级比喻后必须改成名字绑定对象
- 「参数按引用传递」当作最终结论；讲对象引用 / 对象共享
- 「list 里面直接连续放所有 Python 对象」
- 「tuple 里的东西都不可变」；tuple 自身不可变，元素指向的对象可以变
- 「`is` 比 `==` 快所以该用 `is` 比值」；语义不同
- 「字典查找永远 O(1)」
- 「GIL 意味着任何 Python 程序都无法并行」
- 「GC 只等于引用计数」
- `sys.getsizeof(obj)` 等于整棵对象图的总内存；它通常只量对象自身直接占用

## Java

不要混淆 primitive 与 reference；不要把 stack/heap 教学简化当成 JVM 实际布局；Java 是 pass-by-value，对象可以被修改不等于按引用传对象本身；不要把某 JDK 的 HashMap 内部当语言规范。

## C / C++

不要混淆 pointer 与 reference、array 与 pointer、stack/heap 与存储期。undefined behavior 不是「随机结果」的同义词。`vector` 的增长倍数不是标准强制的唯一公式。

## Rust

不要把 ownership / borrowing / lifetimes 讲成「Rust 自带 GC」。

## JavaScript

不要把 language spec、browser、Node.js、V8 混成一件事。

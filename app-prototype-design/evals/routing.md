# Routing Examples

## Should trigger

- 把这个 App 想法做成可点击手机原型。
- 按截图做交互式移动端 mockup。
- 根据现有 Android 导航生成 HTML 手机原型。
- 完善这个手机原型的返回和弹窗交互。
- 做一个 iOS 注册到成功页的交互演示。

## Should not trigger

- 实现生产 Kotlin 页面。 → build-mobile-apps
- 修改现有 Web 后台。 → build-frontends
- 制作游戏角色立绘。 → illustration/image-generation workflow; outside mobile prototype scope.
- 实现支付服务端。 → build-backends
- 只解释 Java 内存模型。 → programming-language-deep-learning

## Conflict cases

- 原型基于现有 App：保留真实导航和素材，不修改生产源码。
- 只修改已有原型颜色：沿用选定方向，不重开视觉方向评审。
- 实现生产 Android 页面并验证：由 build-mobile-apps 负责，不以 HTML 原型充当实现。
- 新原型没有视觉参考：从产品和平台选择一个合理方向并继续，不因偏好缺失强制暂停。
- 明确要求两个方向、由用户挑选：交付可见的方向样本，保留选择点，不提前扩展整套页面。
- 要求比较后由代理选择并完成：说明选择并继续实现，不再要求用户重复确认。

## Execution evaluation

Use [behavior.md](behavior.md) for realistic tasks and artifact checks when changing these rules.
Routing examples and metadata validation alone do not demonstrate agent behavior.

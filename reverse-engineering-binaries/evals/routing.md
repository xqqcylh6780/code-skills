# Routing Examples

## Should trigger

- 静态分析这个 APK 的登录校验。
- 用 Ghidra 反编译 ELF 的协议函数。
- 检查 PE 导入和可疑字符串。
- 分析 DEX 中的本地库调用。
- 核对源码逻辑和固件二进制是否对应。

## Should not trigger

- 直接运行样本看看行为。 → separately authorized isolated dynamic workflow
- 理解完整源码仓库架构。 → repository tools
- 制作手机交互原型。 → app-prototype-design
- 分析 Electron ASAR 功能。 → reverse-engineer-anything
- 修复普通 Python 源码错误。 → diagnose-bugs/build-backends

## Conflict cases

- 可疑二进制：保持样本不变，不因分析请求就执行或上传。
- 静态工具缺失：说明限制，不擅自安装 Ghidra、JDK 或插件。
- 源码与二进制对照：验证对应关系，不把伪代码当原始源码。

# Routing Examples

## Should trigger

- 用 REA 分析这个 Electron ASAR 的功能。
- 比较两个已发布安装包的行为差异。
- 从这个托管程序还原关键业务流程。
- 检查打包固件里有哪些组件。
- 结合允许的被动运行时证据分析已发布应用。

## Should not trigger

- 梳理完整源码仓库架构。 → repository tools
- 改 React 页面。 → build-frontends
- 找 GitHub 上的替代库。 → github-repository-search
- 制作 App 交互原型。 → app-prototype-design
- 只用静态 Ghidra 分析 ELF，禁止动态操作。 → reverse-engineering-binaries

## Conflict cases

- 已有 REA 工具：直接按目标选工具，不先重复安装和注册。
- 缺少 REA 连接：检查能力并给出配置方案，未获授权不安装或改客户端配置。
- 只允许静态分析：保留静态边界；技能可用不代表允许执行样本。

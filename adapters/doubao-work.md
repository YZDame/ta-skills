# 豆包工作

豆包桌面版的“工作任务”模式与 Codex/Claude Code 的本地 Skill 目录不是同一套安装机制。当前可核实的使用路径是：

1. 使用豆包桌面版，进入“工作任务”模式。
2. 打开侧边栏的“技能”入口。
3. 新建或导入一个技能；如果客户端没有直接导入 GitHub 的入口，就让豆包根据仓库中的 `SKILL.md`、README 和示例，用对话方式整理成技能。
4. 将输入、步骤、输出格式、限制条件和示例一并提供，完成后用一个固定案例测试。

本仓库适合提供给豆包工作作为技能说明和参考材料，但不能假定桌面版会直接识别仓库中的全部目录、脚本和 Agent 元数据。涉及 OCR、LaTeX、TSQX 等本地工具时，需要在豆包工作中单独确认是否支持对应的本地执行或文件权限。

另有 `@doubao-apps/ai` Skills CLI，适合 coding-agent 的安装与管理，例如：

```bash
npm install -g @doubao-apps/ai
doubao-cli skills list
```

这个 CLI 入口和豆包桌面版的“工作任务”入口不同，不要把它们当成同一套导入流程。

参考：

- [豆包功能说明](https://www.doubao.com/legal/feature_intro)
- [豆包桌面版下载](https://www.doubao.com/download/desktop)
- [`@doubao-apps/ai` Skills CLI](https://socket.dev/npm/package/%40doubao-apps/ai/overview/0.0.37)

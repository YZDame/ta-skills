# ta-skills

数学教学资源与 Agent Skills 合集。

[English README](README.en.md)

这个仓库收集一组可移植的 Skills，用于数学讲义制作、题目数字化、数学表达、几何图形生成和 OCR。它们不绑定某个大模型，也不要求使用某一个聊天平台；每个 Skill 都是一个可以单独读取和组合的 `SKILL.md` 工作流。

## 第一方 Skills

| Skill | 用途 |
| --- | --- |
| `digitize-math-lectures` | 将板书、扫描件、PDF、讲稿和已有 LaTeX 整理成可审阅的数学材料。 |
| `math-exposition-latex` | 生成中文数学讲解、证明、竞赛小讲义和 LaTeX 教学材料。 |
| `tsqx-gen` | 从题目或图形描述生成、规范化并检查 TSQX 几何代码。 |
| `mistral-ocr` | 调用 Mistral OCR 处理 PDF、扫描页、图片和公开文档 URL，输出 Markdown 与原始 JSON。 |

## 第三方 Skills

| Skill | 来源 | 当前状态 |
| --- | --- | --- |
| `vendor-skills/math-olympiad` | Anthropic 官方插件仓库 | 保留为第三方快照，见 [THIRD_PARTY.md](THIRD_PARTY.md)。 |
| `vendor-skills/mineru-ai` | MinerU-Extract/mineru-ai | 目前只保留来源指针，待上游明确再发布许可。 |

## 支持的 Agent

仓库内容遵循 Agent Skills 的目录约定。不同客户端的发现路径和导入入口可能不同，详细说明见 [`adapters/`](adapters/)：

1. [Codex](adapters/codex.md)
2. [Claude Code](adapters/claude-code.md)
3. [Trae Work](adapters/trae-workbuddy.md)
4. [WorkBuddy](adapters/trae-workbuddy.md)
5. [豆包工作](adapters/doubao-work.md)
6. [千问办公](adapters/qwen-office.md)
7. [DeepSeek Harness](adapters/deepseek-harness.md)

如果某个平台支持标准 `SKILL.md`，通常可以直接导入对应 Skill 目录。不要把“能够读取 `SKILL.md`”误认为“所有平台都支持相同的插件清单、工具权限或本地执行能力”；OCR、LaTeX、TSQX、Asymptote 等外部依赖仍需单独配置。

## 通用安装方式

对支持项目级 Skills 的 Agent，可以直接 clone 仓库，再把需要的目录链接到对应发现路径：

```bash
git clone https://github.com/YZDame/ta-skills.git
cd ta-skills

# Codex
mkdir -p .agents/skills
ln -s "$PWD/mistral-ocr" .agents/skills/mistral-ocr

# Claude Code
mkdir -p .claude/skills
ln -s "$PWD/math-exposition-latex" .claude/skills/math-exposition-latex
```

也可以只复制单个 Skill 目录。仓库本身不提供统一的大模型 API、前端、后端或数据库。

## 豆包工作

豆包桌面版的“工作任务”模式目前提供“技能、连接器、工作伙伴”等入口；公开资料显示，技能可以通过对话描述工作步骤后创建和反复调用。具体入口和名称可能随客户端版本变化，见 [豆包工作适配说明](adapters/doubao-work.md)。

`@doubao-apps/ai` 提供另一个面向 coding-agent 的 Skills CLI，但它和豆包桌面版“工作任务”不是同一个入口，不能混为一谈。

## 许可证

本仓库第一方内容使用 [Apache License 2.0](LICENSE)。第三方内容的来源、许可证和再发布状态见 [THIRD_PARTY.md](THIRD_PARTY.md)。

# TA Skills（Teacher Agent Skills）

面向教师 Agent 和 AI 助教的教学技能插件。

[English](README.en.md)

TA Skills 将讲义制作、教学资料数字化、OCR、数学表达、几何图形生成和竞赛数学解题等工作整理成可复用的 [Agent Skills](https://agentskills.io/)；当前内容以数学教学为起点，也可以继续扩展到其他学科和教学场景。

## 快速安装

### 安装完整插件

适用于 Codex、Claude Code、Cursor 等支持插件的 Agent：

```bash
npx plugins add YZDame/ta-skills
```

安装器会显示 `teacher-agent-skills` 插件及其中的全部 Skills。

### 安装单个 Skill

```bash
npx skills add YZDame/ta-skills --skill tsqx-gen
```

将 `tsqx-gen` 换成下表中的其他名称即可。需要指定 Agent 时使用：

```bash
npx skills add YZDame/ta-skills -a <agent-name>
```

这组方式适用于 Codex、Claude Code、TRAE、Qwen Code，以及其他受 Skills CLI 支持的 Agent。DeepSeek Harness 可以把所选 Skill 的完整目录放入项目级 `.agents/skills/` 或其用户级 Skills 目录。

### 直接发给 Agent

不熟悉命令行时，把下面这段话发送给正在使用的 Agent：

```text
请安装 https://github.com/YZDame/ta-skills 中的教学技能。先读取 README，列出 teacher-agent-skills 插件包含的 Skills 和用途，让我选择。当前环境支持插件时使用 npx plugins add YZDame/ta-skills；受 Skills CLI 支持时使用 npx skills add YZDame/ta-skills；如果当前 Agent 只提供本地 Skills 目录，就把我选择的完整 Skill 文件夹安装到它规定的位置。完成后检查 SKILL.md 是否能被发现，并报告还需要配置的 API 或本地软件。
```

WorkBuddy、豆包工作和千问办公可以在各自的技能页面中导入：先下载仓库 ZIP，再选择 `plugins/teacher-agent-skills/skills/` 下需要的 Skill 文件夹。若产品支持读取 GitHub，也可以直接发送上面的提示词。

## 插件内容

### Teacher Agent Skills（`teacher-agent-skills`）

| Skill | 用途 |
| --- | --- |
| [`digitize-math-lectures`](plugins/teacher-agent-skills/skills/digitize-math-lectures/) | 将板书、试卷、扫描件、PDF、讲稿和已有 LaTeX 整理成可校对、可编辑的教学资料。 |
| [`math-exposition-latex`](plugins/teacher-agent-skills/skills/math-exposition-latex/) | 编写中文数学讲解、证明、竞赛小讲义和 LaTeX 教学材料。 |
| [`mistral-ocr`](plugins/teacher-agent-skills/skills/mistral-ocr/) | 使用 Mistral OCR 识别 PDF、扫描页、图片和公开文档链接。 |
| [`tsqx-gen`](plugins/teacher-agent-skills/skills/tsqx-gen/) | 根据题目、图片或文字描述生成并检查 TSQX 几何图形代码。 |
| [`math-olympiad`](plugins/teacher-agent-skills/skills/math-olympiad/) | 求解和复核数学竞赛问题；该 Skill 来源于 Anthropic 官方插件仓库。 |

## 外部 Skill

[`mineru-ai`](vendor-skills/mineru-ai/) 当前保留为上游来源和安装指引。由于上游仓库尚未提供明确的再发布许可，本仓库没有复制其完整 Skill 内容。

外部内容的来源和许可证见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 运行依赖

Skill 本身提供工作流程，部分功能还需要相应工具：

| 功能 | 依赖 |
| --- | --- |
| Mistral OCR | `MISTRAL_API_KEY` |
| LaTeX 讲义生成与编译 | 本地 LaTeX 环境 |
| TSQX 图形生成与验证 | TSQX、Asymptote；仅生成代码时可以不安装 |
| 文档数字化 | 根据材料类型选用 OCR、PDF 转换或图形重建工具 |

## 许可证

本仓库原创内容使用 [Apache License 2.0](LICENSE)。外部 Skill 保留各自的署名和许可条件。

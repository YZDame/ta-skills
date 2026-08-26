# TA Skills（Teacher Agent Skills）

面向教师的 AI 助教：一份实用教学技能包。

[English](README.en.md)

TA Skills 将讲义制作、教学资料数字化、OCR、数学表达、几何图形生成和竞赛数学解题等工作整理成可复用的 [Agent Skills](https://agentskills.io/)；以 LaTeX 为核心材料，可以应用到几乎所有学科和教学场景。

## 快速安装

下面几种方式覆盖 Codex、Claude Code、Trae Work、WorkBuddy、豆包工作、千问办公和 DeepSeek Harness。选择哪一种，取决于当前 Agent 是否提供插件安装、Skills CLI 或本地 Skills 目录。

### 提示词安装（推荐）

把下面这段提示词发送给正在使用的 Agent：

```text
请安装 https://github.com/YZDame/ta-skills 中的教学技能。先阅读 README 和 THIRD_PARTY.md，列出 skills/ 下的 Skills 及其用途，让我选择需要安装的内容。如果当前环境支持插件，请执行 npx plugins add YZDame/ta-skills；如果支持 Skills CLI，请执行 npx skills add YZDame/ta-skills；如果只提供技能页面或本地 Skills 目录，请导入我选择的完整 Skill 文件夹，不要只复制 SKILL.md。安装后检查各个 SKILL.md 是否能被发现，说明 math-olympiad 的 Anthropic 上游来源，并报告还需要配置的 API 或本地软件。
```

这种方式适合 WorkBuddy、豆包工作、千问办公，以及其他能够自行读取 GitHub 仓库或执行安装命令的 Agent。

### 命令行安装完整插件

在支持 Plugins CLI 的环境中运行：

```bash
npx plugins add YZDame/ta-skills
```

安装器应识别名为 `ta-skills` 的插件，并发现其中的五个 Skills。

### 命令行安装单个 Skill

```bash
npx skills add YZDame/ta-skills --skill tsqx-gen
```

将 `tsqx-gen` 换成下表中的其他名称即可。需要指定 Agent 时使用：

```bash
npx skills add YZDame/ta-skills -a <agent-name>
```

这种方式适用于 Codex、Claude Code、Trae Work，以及其他受 Skills CLI 支持的 Agent。

### 手动导入

下载仓库 ZIP 并解压，然后从 [`skills/`](skills/) 中选择需要的完整 Skill 文件夹导入。完整文件夹可能包含脚本、参考资料和模板，不要只复制 `SKILL.md`。

WorkBuddy、豆包工作和千问办公可以通过各自的技能页面导入；DeepSeek Harness 可以把所选目录放入项目级 `.agents/skills/` 或其用户级 Skills 目录。

## 插件内容

### 仓库原创 Skills

| Skill | 用途 |
| --- | --- |
| [`digitize-math-lectures`](skills/digitize-math-lectures/) | 将板书、试卷、扫描件、PDF、讲稿和已有 LaTeX 整理成可校对、可编辑的教学资料。 |
| [`math-exposition-latex`](skills/math-exposition-latex/) | 编写中文数学讲解、证明、竞赛讲义和 LaTeX 教学材料。 |
| [`mistral-ocr`](skills/mistral-ocr/) | 使用 Mistral OCR 识别 PDF、扫描页、图片和公开文档链接。 |
| [`tsqx-gen`](skills/tsqx-gen/) | 根据题目、图片或文字描述生成并检查 TSQX 几何图形代码。 |

### 随插件安装的外部 Skill

| Skill | 用途与来源 |
| --- | --- |
| [`math-olympiad`](skills/math-olympiad/) | 求解和复核数学竞赛问题。来源于 [Anthropic 官方插件仓库](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad)，遵循 Apache License 2.0；固定版本和修改说明见 [`UPSTREAM.md`](skills/math-olympiad/UPSTREAM.md)。 |

### 仅提供来源入口的外部 Skill

[`mineru-ai`](vendor-skills/mineru-ai/) 目前只保留上游链接和安装指引。上游仓库尚未提供明确的再发布许可，因此本仓库没有复制其完整 Skill 内容。

所有外部内容的来源和许可边界见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 运行依赖

Skill 本身提供工作流程，部分功能还需要相应工具：

| 功能 | 依赖 |
| --- | --- |
| Mistral OCR | `MISTRAL_API_KEY` |
| LaTeX 讲义生成与编译 | 本地 LaTeX 环境 |
| TSQX 图形生成与验证 | TSQX、Asymptote；仅生成代码时可以不安装 |
| 文档数字化 | 根据材料类型选用 OCR、PDF 转换或图形重建工具 |

## 仓库结构

```text
ta-skills/
├── .codex-plugin/plugin.json
├── .claude-plugin/plugin.json
├── skills/
├── vendor-skills/
├── README.md
├── README.en.md
├── LICENSE
└── THIRD_PARTY.md
```

## 许可证

本仓库原创内容使用 [Apache License 2.0](LICENSE)。根目录许可证不会改变外部内容原有的许可条件；外部 Skill 以其目录内的许可证和 [THIRD_PARTY.md](THIRD_PARTY.md) 为准。

# TA Skills（Teacher Agent Skills）

面向教师 Agent 和 AI 助教的教学技能合集。

[English README](README.en.md)

TA Skills 围绕日常教学资料的整理与制作，将可以反复使用的工作方法写成 Agent Skills。当前内容以数学教学为起点，涵盖讲义制作、教学资料数字化、OCR、数学表达和几何图形生成，后续也可以继续加入其他学科与教学场景。

## Skills

| Skill | 用途 |
| --- | --- |
| `digitize-math-lectures` | 将板书、试卷、扫描件、PDF、讲稿和已有 LaTeX 整理成可校对、可编辑的教学资料。 |
| `math-exposition-latex` | 编写中文数学讲解、证明、竞赛小讲义和 LaTeX 教学材料。 |
| `tsqx-gen` | 根据题目、图片或文字描述生成 TSQX 几何图形代码，并进行规范化和检查。 |
| `mistral-ocr` | 使用 Mistral OCR 识别 PDF、扫描页、图片和公开文档链接，输出 Markdown 和原始 JSON。 |

## 其他 Skills

| Skill | 来源 | 说明 |
| --- | --- | --- |
| `vendor-skills/math-olympiad` | Anthropic 官方插件仓库 | 用于竞赛数学解题与验证，仓库中保留了一份外部 Skill 快照。 |
| `vendor-skills/mineru-ai` | MinerU-Extract/mineru-ai | 当前提供来源与安装指引，暂不复制上游完整内容。 |

外部 Skills 的来源、许可证和收录方式见 [THIRD_PARTY.md](THIRD_PARTY.md)。

## 安装与使用

各个 Skill 都以 `SKILL.md` 为入口，并将脚本、参考资料和模板保存在同一目录中。安装时应保留整个 Skill 文件夹，不能只复制其中的 `SKILL.md`。

如果使用的是支持命令行的 Agent，可以先运行下面的通用安装命令，再在交互界面中选择 Agent 和需要的 Skills：

```bash
npx skills add YZDame/ta-skills
```

不熟悉命令行时，可以直接把对应小节中的提示词发送给 Agent，让它完成安装并报告结果。

### Codex

把下面这段话发送给 Codex：

```text
请从 https://github.com/YZDame/ta-skills 安装教学 Skills。先读取仓库 README，列出可以安装的 Skills 及其用途，让我选择；然后使用 Codex 的 Skill 安装工具安装所选目录，保留每个 Skill 的完整文件结构。安装后检查 SKILL.md 是否能够被发现，并说明 OCR、LaTeX、TSQX 等功能还需要配置哪些依赖。未经我选择，不要安装 vendor-skills 中的外部 Skills。
```

也可以直接运行：

```bash
npx skills add YZDame/ta-skills -a codex
```

Codex 的项目级 Skills 位于 `.agents/skills/`。安装后重新开启一个会话即可使用。

### Claude Code

把下面这段话发送给 Claude Code：

```text
请从 https://github.com/YZDame/ta-skills 为当前项目安装教学 Skills。先列出仓库中的 Skills 让我选择，再把所选 Skill 完整安装到当前项目的 .claude/skills/ 目录。请保留 SKILL.md、scripts、references、assets 等文件，并在完成后检查目录结构和依赖，告诉我可以怎样触发这些 Skills。未经我选择，不要安装 vendor-skills 中的外部 Skills。
```

也可以直接运行：

```bash
npx skills add YZDame/ta-skills -a claude-code
```

### TRAE（Trae Work）

把下面这段话发送给 TRAE：

```text
请从 https://github.com/YZDame/ta-skills 为当前项目安装教学 Skills。先列出可用 Skills 让我选择，再将所选 Skill 的完整目录安装到 .trae/skills/，确认每个目录下都有有效的 SKILL.md，并检查它引用的脚本、模板和参考文件是否完整。完成后刷新 Skills，并告诉我安装结果和使用示例。
```

中国版 TRAE 可以运行：

```bash
npx skills add YZDame/ta-skills -a trae-cn
```

也可以下载仓库 ZIP，在 TRAE 的“设置 → 技能与命令”中导入单个 Skill 文件夹。

### WorkBuddy

打开 WorkBuddy 的 Skills 页面，将下面这段话发送给 WorkBuddy：

```text
请帮我添加 https://github.com/YZDame/ta-skills 中的教学 Skills。先读取 README 并列出每个 Skill 的用途，让我选择；然后将所选 Skill 作为本地技能包导入，保留 SKILL.md 以及同目录中的 scripts、references、assets 和模板。若当前版本不能直接读取 GitHub，请提示我下载仓库 ZIP，并告诉我应当在 Skills 页面选择哪个文件夹导入。导入后请用一个简单教学任务测试，并报告缺少的依赖。
```

如果 WorkBuddy 无法直接访问 GitHub，可以先下载仓库 ZIP，再从 Skills 页面选择“导入本地技能包”。每次导入一个包含 `SKILL.md` 的 Skill 文件夹即可。

### 豆包工作

进入豆包工作的“技能”页面，将下面这段话发送给豆包：

```text
请根据 https://github.com/YZDame/ta-skills 为我添加教学 Skills。先读取 README，列出可用 Skills 和用途让我选择；再读取所选目录中的 SKILL.md 及其相关文件，将其中的适用场景、输入、操作步骤、输出要求和检查规则完整整理成可重复使用的豆包工作技能。若无法直接访问 GitHub，请让我上传对应 Skill 文件夹或仓库 ZIP。创建完成后，请用一个固定样例测试，并告诉我哪些本地工具或 API 还需要单独配置。
```

豆包工作通过对话创建技能时，应上传完整 Skill 文件夹；涉及 Mistral OCR、LaTeX 或 TSQX 的功能还需要相应的 API、软件和文件权限。

### 千问办公

进入千问办公的技能或智能体配置页面，将下面这段话发送给千问：

```text
请从 https://github.com/YZDame/ta-skills 添加教学 Skills。先读取 README，列出可用 Skills 让我选择；然后根据所选目录中的 SKILL.md 创建对应技能，并同时读取该目录下的 scripts、references、assets 和模板。若当前版本不能直接读取 GitHub，请让我上传对应 Skill 文件夹或仓库 ZIP。完成后请检查技能的触发场景、输入输出和文件依赖，并用一个简单教学任务进行测试。
```

这里指千问办公产品；如果使用的是 Qwen Code，可以运行：

```bash
npx skills add YZDame/ta-skills -a qwen-code
```

### DeepSeek Harness

把下面这段话发送给 DeepSeek Harness：

```text
请从 https://github.com/YZDame/ta-skills 安装教学 Skills。先列出仓库中可以安装的 Skills 让我选择；然后将所选 Skill 的完整目录复制或链接到当前项目的 .agents/skills/，或当前 DeepSeek Harness 配置的用户级 Skills 根目录。每个 Skill 必须作为 Skills 根目录的直接子目录，不能再嵌套一层 ta-skills。安装后重新加载 Skills，检查 SKILL.md 是否能够被发现，并报告所需的脚本、API 和本地软件依赖。
```

DeepSeek Harness 不递归发现任意深度的 `SKILL.md`，因此目录应保持为：

```text
.agents/skills/
├── digitize-math-lectures/SKILL.md
├── math-exposition-latex/SKILL.md
├── mistral-ocr/SKILL.md
└── tsqx-gen/SKILL.md
```

## 使用示例

安装后可以直接向 Agent 描述教学任务，例如：

```text
请使用 digitize-math-lectures，把这份扫描讲义整理成可校对的 LaTeX 项目。
```

```text
请使用 math-exposition-latex，为高中生写一份关于圆锥曲线切线的中文数学讲义。
```

```text
请使用 tsqx-gen，根据这道平面几何题生成示意图，并检查图形代码。
```

```text
请使用 mistral-ocr，识别这份 PDF，并保留 Markdown 和原始 JSON 结果。
```

## 许可证

本仓库原创内容使用 [Apache License 2.0](LICENSE)。其他 Skills 的来源、许可证和再发布状态见 [THIRD_PARTY.md](THIRD_PARTY.md)。

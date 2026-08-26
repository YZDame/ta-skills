# TA Skills (Teacher Agent Skills)

An AI teaching assistant for teachers: a practical teaching skills bundle.

[中文](README.md)

TA Skills turns handout authoring, teaching-material digitization, OCR, mathematical exposition, geometry generation, and olympiad problem solving into reusable [Agent Skills](https://agentskills.io/). Its current workflows use LaTeX as a core material format and can be adapted to many subjects and teaching settings.

## Quick Start

The options below cover Codex, Claude Code, Trae Work, WorkBuddy, Doubao Work, Qwen Office, and DeepSeek Harness. Choose the method supported by your current agent: plugin installation, the Skills CLI, or a local Skills directory.

### Install by prompt (recommended)

Send this prompt to the agent you are using:

```text
Install the teaching skills from https://github.com/YZDame/ta-skills. Read README.md and THIRD_PARTY.md first, then list the Skills under skills/ and explain what each one does so I can choose what to install. If this environment supports plugins, run npx plugins add YZDame/ta-skills. If it supports the Skills CLI, run npx skills add YZDame/ta-skills. If it only provides a Skills page or local Skills directory, import each selected complete Skill folder rather than copying SKILL.md alone. After installation, verify that each SKILL.md is discoverable, identify math-olympiad as content sourced from Anthropic, and report any APIs or local software that still need configuration.
```

This method works well with WorkBuddy, Doubao Work, Qwen Office, and other agents that can read a GitHub repository or run installation commands.

### Install the complete plugin from the command line

In an environment that supports the Plugins CLI, run:

```bash
npx plugins add YZDame/ta-skills
```

The installer should identify the plugin as `ta-skills` and discover all five included Skills.

### Install one Skill from the command line

```bash
npx skills add YZDame/ta-skills --skill tsqx-gen
```

Replace `tsqx-gen` with another name from the tables below. To target a specific agent, use:

```bash
npx skills add YZDame/ta-skills -a <agent-name>
```

This method works with Codex, Claude Code, Trae Work, and other agents supported by the Skills CLI.

### Import manually

Download and extract the repository ZIP, then import a complete Skill directory from [`skills/`](skills/). A Skill may include scripts, references, and templates, so do not copy `SKILL.md` by itself.

WorkBuddy, Doubao Work, and Qwen Office can import Skills through their Skills pages. For DeepSeek Harness, place each selected directory under the project-level `.agents/skills/` or its user-level Skills directory.

## Plugin Contents

### Original Skills in this repository

| Skill | Purpose |
| --- | --- |
| [`digitize-math-lectures`](skills/digitize-math-lectures/) | Turn boards, exams, scans, PDFs, manuscripts, and existing LaTeX into editable teaching materials ready for review. |
| [`math-exposition-latex`](skills/math-exposition-latex/) | Write Chinese mathematical explanations, proofs, competition handouts, and LaTeX teaching materials. |
| [`mistral-ocr`](skills/mistral-ocr/) | Use Mistral OCR with PDFs, scanned pages, images, and public document URLs. |
| [`tsqx-gen`](skills/tsqx-gen/) | Generate and check TSQX geometry code from problems, images, or written descriptions. |

### Bundled external Skill

| Skill | Purpose and source |
| --- | --- |
| [`math-olympiad`](skills/math-olympiad/) | Solve and verify olympiad mathematics problems. Sourced from [Anthropic's official plugin repository](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/math-olympiad) under Apache License 2.0; see [`UPSTREAM.md`](skills/math-olympiad/UPSTREAM.md) for the pinned revision and modification notice. |

### External Skill available by source link only

[`mineru-ai`](vendor-skills/mineru-ai/) currently contains only its upstream link and installation notes. Its upstream repository does not provide clear redistribution terms, so this repository does not copy the complete Skill.

See [THIRD_PARTY.md](THIRD_PARTY.md) for the provenance and licensing boundaries of all external content.

## Runtime Requirements

Skills define workflows; some capabilities require additional tools:

| Capability | Requirement |
| --- | --- |
| Mistral OCR | `MISTRAL_API_KEY` |
| LaTeX authoring and compilation | A local LaTeX environment |
| TSQX generation and verification | TSQX and Asymptote; not required when only generating source code |
| Document digitization | OCR, PDF conversion, or figure-reconstruction tools selected for the source material |

## Repository Layout

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

## License

Original content in this repository is licensed under the [Apache License 2.0](LICENSE). The root license does not replace the license terms of external content; external Skills remain governed by their bundled license files and [THIRD_PARTY.md](THIRD_PARTY.md).

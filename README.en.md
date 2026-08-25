# TA Skills (Teacher Agent Skills)

A collection of teaching skills for teacher agents and AI teaching assistants.

[中文 README](README.md)

TA Skills turns repeatable teaching workflows into Agent Skills. The current collection starts with mathematics education and covers handout authoring, teaching-material digitization, OCR, mathematical exposition, and geometry generation. Skills for other subjects and teaching scenarios can be added over time.

## Skills

| Skill | Purpose |
| --- | --- |
| `digitize-math-lectures` | Turn boards, exams, scans, PDFs, manuscripts, and existing LaTeX into editable teaching materials ready for review. |
| `math-exposition-latex` | Write Chinese mathematical explanations, proofs, competition mini-lectures, and LaTeX teaching materials. |
| `tsqx-gen` | Generate, normalize, and check TSQX geometry code from problems, images, or written descriptions. |
| `mistral-ocr` | Use Mistral OCR with PDFs, scanned pages, images, and public document URLs, producing Markdown and raw JSON. |

## Other Skills

| Skill | Source | Notes |
| --- | --- | --- |
| `vendor-skills/math-olympiad` | Anthropic's official plugin repository | An external Skill snapshot for solving and verifying olympiad mathematics problems. |
| `vendor-skills/mineru-ai` | MinerU-Extract/mineru-ai | Source and installation notes only; the full upstream content is not copied here. |

See [THIRD_PARTY.md](THIRD_PARTY.md) for provenance, licensing, and inclusion details.

## Installation and usage

Each Skill uses `SKILL.md` as its entry point and keeps its scripts, references, and templates in the same directory. Install the complete Skill directory rather than copying `SKILL.md` alone.

For command-line agents, run the following command and select the target agent and Skills interactively:

```bash
npx skills add YZDame/ta-skills
```

If you do not normally use a terminal, send the prompt under the relevant agent heading and let the agent perform the installation and report the result.

### Codex

Send this prompt to Codex:

```text
Install teaching Skills from https://github.com/YZDame/ta-skills. Read the repository README first, list the available Skills and their purposes, and let me choose. Then use the Codex Skill installer to install the selected directories while preserving each complete Skill structure. Verify that each SKILL.md is discoverable and report any OCR, LaTeX, TSQX, or other dependencies that still need configuration. Do not install external Skills under vendor-skills unless I select them.
```

Or run:

```bash
npx skills add YZDame/ta-skills -a codex
```

Project-level Codex Skills live in `.agents/skills/`. Start a new session after installation.

### Claude Code

Send this prompt to Claude Code:

```text
Install teaching Skills from https://github.com/YZDame/ta-skills for the current project. List the repository Skills and let me choose, then install each selected complete directory under .claude/skills/. Preserve SKILL.md, scripts, references, assets, and templates. Check the resulting structure and dependencies, and tell me how to trigger each Skill. Do not install external Skills under vendor-skills unless I select them.
```

Or run:

```bash
npx skills add YZDame/ta-skills -a claude-code
```

### TRAE (Trae Work)

Send this prompt to TRAE:

```text
Install teaching Skills from https://github.com/YZDame/ta-skills for the current project. List the available Skills and let me choose, then install each selected complete Skill directory under .trae/skills/. Confirm that every directory contains a valid SKILL.md and that all referenced scripts, templates, and reference files are present. Refresh Skills and report the installation result with a usage example.
```

For TRAE CN, run:

```bash
npx skills add YZDame/ta-skills -a trae-cn
```

You can also download the repository ZIP and import one Skill folder at a time through “Settings → Skills and Commands.”

### WorkBuddy

Open the WorkBuddy Skills page and send this prompt:

```text
Help me add the teaching Skills from https://github.com/YZDame/ta-skills. Read the README, list every Skill and its purpose, and let me choose. Import each selected complete directory as a local Skill package, preserving SKILL.md together with scripts, references, assets, and templates. If this version cannot read GitHub directly, ask me to download the repository ZIP and tell me which folder to import from the Skills page. Test the imported Skill with a simple teaching task and report missing dependencies.
```

If WorkBuddy cannot access GitHub directly, download the repository ZIP and choose “Import local Skill package” on the Skills page. Import one folder containing `SKILL.md` at a time.

### Doubao Work

Open the Skills page in Doubao Work and send this prompt:

```text
Add teaching Skills for me from https://github.com/YZDame/ta-skills. Read the README, list the available Skills and let me choose. Read the selected SKILL.md and its related files, then preserve its use cases, inputs, procedure, output requirements, and validation rules as a reusable Doubao Work Skill. If GitHub cannot be accessed directly, ask me to upload the selected Skill folder or repository ZIP. Test the completed Skill with a fixed example and report any local tools or APIs that still require configuration.
```

Upload the complete Skill directory when creating a Skill conversationally. Mistral OCR, LaTeX, and TSQX workflows still require their corresponding APIs, software, and file permissions.

### Qwen Office

Open the Skill or agent configuration page in Qwen Office and send this prompt:

```text
Add teaching Skills from https://github.com/YZDame/ta-skills. Read the README, list the available Skills and let me choose. Create a Skill from each selected SKILL.md and also read its scripts, references, assets, and templates. If this version cannot access GitHub directly, ask me to upload the selected Skill folder or repository ZIP. Check the trigger conditions, inputs, outputs, and file dependencies, then test the Skill with a simple teaching task.
```

This section refers to Qwen Office. For Qwen Code, run:

```bash
npx skills add YZDame/ta-skills -a qwen-code
```

### DeepSeek Harness

Send this prompt to DeepSeek Harness:

```text
Install teaching Skills from https://github.com/YZDame/ta-skills. List the repository Skills and let me choose. Copy or link each selected complete Skill directory into .agents/skills/ for the current project, or into the user-level Skills root configured by DeepSeek Harness. Each Skill must be a direct child of the Skills root; do not keep an extra ta-skills nesting level. Reload Skills, verify that every SKILL.md is discoverable, and report required scripts, APIs, and local software.
```

DeepSeek Harness does not recursively discover `SKILL.md` at arbitrary depth. Keep this layout:

```text
.agents/skills/
├── digitize-math-lectures/SKILL.md
├── math-exposition-latex/SKILL.md
├── mistral-ocr/SKILL.md
└── tsqx-gen/SKILL.md
```

## Usage examples

After installation, describe the teaching task directly:

```text
Use digitize-math-lectures to turn this scanned handout into a reviewable LaTeX project.
```

```text
Use math-exposition-latex to write a Chinese high-school handout on tangents to conic sections.
```

```text
Use tsqx-gen to generate and check a diagram for this plane-geometry problem.
```

```text
Use mistral-ocr to recognize this PDF and preserve both the Markdown and raw JSON results.
```

## License

Original content in this repository is licensed under the [Apache License 2.0](LICENSE). See [THIRD_PARTY.md](THIRD_PARTY.md) for the provenance, licenses, and redistribution status of other Skills.

# TA Skills (Teacher Agent Skills)

A teaching-skills plugin for teacher agents and AI teaching assistants.

[中文](README.md)

TA Skills packages handout authoring, teaching-material digitization, OCR, mathematical exposition, geometry generation, and olympiad problem solving as reusable [Agent Skills](https://agentskills.io/). The current collection starts with mathematics education and can grow into other subjects and teaching scenarios.

## Quick Start

### Install the plugin

For Codex, Claude Code, Cursor, and other plugin-compatible agents:

```bash
npx plugins add YZDame/ta-skills
```

The installer presents the `teacher-agent-skills` plugin with all included Skills.

### Install one Skill

```bash
npx skills add YZDame/ta-skills --skill tsqx-gen
```

Replace `tsqx-gen` with another name from the table below. To select a target agent:

```bash
npx skills add YZDame/ta-skills -a <agent-name>
```

This route works with Codex, Claude Code, TRAE, Qwen Code, and other agents supported by the Skills CLI. For DeepSeek Harness, place each selected complete Skill directory under the project-level `.agents/skills/` or its user-level Skills directory.

### Send one prompt to your agent

If you do not normally use a terminal, send this prompt to your agent:

```text
Install the teaching skills from https://github.com/YZDame/ta-skills. Read the README first, list the Skills in the teacher-agent-skills plugin and let me choose. If this environment supports plugins, run npx plugins add YZDame/ta-skills. If it is supported by the Skills CLI, run npx skills add YZDame/ta-skills. If the current agent only provides a local Skills directory, install each selected complete Skill folder there. Verify that every SKILL.md is discoverable and report any APIs or local software that still need configuration.
```

For WorkBuddy, Doubao Work, and Qwen Office, download the repository ZIP and import the required directory from `plugins/teacher-agent-skills/skills/` through the product's Skills page. If the product can read GitHub directly, send it the prompt above instead.

## Plugin Contents

### Teacher Agent Skills (`teacher-agent-skills`)

| Skill | Purpose |
| --- | --- |
| [`digitize-math-lectures`](plugins/teacher-agent-skills/skills/digitize-math-lectures/) | Turn boards, exams, scans, PDFs, manuscripts, and existing LaTeX into editable teaching materials ready for review. |
| [`math-exposition-latex`](plugins/teacher-agent-skills/skills/math-exposition-latex/) | Write Chinese mathematical explanations, proofs, competition mini-lectures, and LaTeX teaching materials. |
| [`mistral-ocr`](plugins/teacher-agent-skills/skills/mistral-ocr/) | Use Mistral OCR with PDFs, scanned pages, images, and public document URLs. |
| [`tsqx-gen`](plugins/teacher-agent-skills/skills/tsqx-gen/) | Generate and check TSQX geometry code from problems, images, or written descriptions. |
| [`math-olympiad`](plugins/teacher-agent-skills/skills/math-olympiad/) | Solve and verify olympiad mathematics problems; sourced from Anthropic's official plugin repository. |

## External Skill

[`mineru-ai`](vendor-skills/mineru-ai/) currently contains upstream source and installation notes. The complete upstream Skill is not copied because its repository does not yet provide clear redistribution terms.

See [THIRD_PARTY.md](THIRD_PARTY.md) for provenance and licensing details.

## Runtime Requirements

Skills define workflows; some capabilities require additional tools:

| Capability | Requirement |
| --- | --- |
| Mistral OCR | `MISTRAL_API_KEY` |
| LaTeX authoring and compilation | A local LaTeX environment |
| TSQX generation and verification | TSQX and Asymptote; not required when only generating source code |
| Document digitization | OCR, PDF conversion, or figure-reconstruction tools selected for the source material |

## License

Original content in this repository is licensed under the [Apache License 2.0](LICENSE). External Skills retain their own attribution and license terms.

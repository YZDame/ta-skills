# ta-skills

Portable Agent Skills for mathematics teaching and mathematical material production.

[中文 README](README.md)

This repository contains portable `SKILL.md` workflows for lecture digitization, mathematical exposition, geometry generation, and OCR. The Skills are model- and platform-independent: each one can be used on its own or composed with other Skills and tools.

## First-party Skills

| Skill | Purpose |
| --- | --- |
| `digitize-math-lectures` | Turn boards, scans, PDFs, manuscripts, and existing LaTeX into reviewable mathematics materials. |
| `math-exposition-latex` | Draft Chinese mathematical explanations, proofs, competition mini-lectures, and LaTeX materials. |
| `tsqx-gen` | Generate, normalize, and optionally verify TSQX geometry sources. |
| `mistral-ocr` | Call the Mistral OCR API for PDFs, scans, images, and public document URLs, producing Markdown and raw JSON. |

## Third-party Skills

| Skill | Source | Status |
| --- | --- | --- |
| `vendor-skills/math-olympiad` | Anthropic's official plugin repository | Included as a marked third-party snapshot; see [THIRD_PARTY.md](THIRD_PARTY.md). |
| `vendor-skills/mineru-ai` | MinerU-Extract/mineru-ai | Source pointer only until upstream redistribution terms are clear. |

## Supported agents

The repository follows the Agent Skills directory convention. Discovery paths and import interfaces vary by client; see [`adapters/`](adapters/):

1. [Codex](adapters/codex.md)
2. [Claude Code](adapters/claude-code.md)
3. [Trae Work](adapters/trae-workbuddy.md)
4. [WorkBuddy](adapters/trae-workbuddy.md)
5. [Doubao Work](adapters/doubao-work.md)
6. [Qwen Office](adapters/qwen-office.md)
7. [DeepSeek Harness](adapters/deepseek-harness.md)

If a client supports standard `SKILL.md` files, import the corresponding Skill directory. Reading `SKILL.md` does not imply identical plugin manifests, permissions, or local-tool support across clients. OCR, LaTeX, TSQX, Asymptote, and document-conversion dependencies still need to be configured separately.

## Generic installation

For a project-level Skills client, clone the repository and link the required directories into that client's discovery path:

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

Individual Skill directories may also be copied directly. This repository does not provide a unified model API, frontend, backend, or database.

## Doubao Work

The Doubao desktop Work Tasks mode currently exposes Skills, Connectors, and Work Partners. Public product material indicates that users can describe a repeatable workflow conversationally and create a reusable Skill. The exact UI entry point may change; see [the Doubao adapter notes](adapters/doubao-work.md).

`@doubao-apps/ai` also provides a Skills CLI for coding-agent installation. It is a separate interface from the Doubao desktop Work Tasks product.

## License

First-party content is licensed under the [Apache License 2.0](LICENSE). Third-party provenance, licensing, and redistribution status are recorded in [THIRD_PARTY.md](THIRD_PARTY.md).

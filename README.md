# ta-skills

Portable Agent Skills for mathematics teaching and mathematical material production.

This repository contains first-party Skills for:

- digitizing and authoring mathematics lectures;
- writing structured Chinese mathematical exposition;
- generating and checking TSQX geometry sources.

It also records selected third-party Skills under `vendor-skills/`. Third-party
content is kept separate from first-party work and remains under its upstream
license or redistribution status.

## First-party Skills

| Skill | Purpose |
| --- | --- |
| `digitize-math-lectures` | Turn boards, scans, PDFs, manuscripts, and existing LaTeX into reviewable mathematics materials. |
| `math-exposition-latex` | Draft Chinese mathematics mini-lectures, explanations, proofs, and handouts in LaTeX. |
| `tsqx-gen` | Generate, normalize, and optionally compile-check TSQX geometry sources. |

## Vendor Skills

| Skill | Source | Status |
| --- | --- | --- |
| `math-olympiad` | Anthropic's official Claude plugins repository | Included as a third-party snapshot; see `THIRD_PARTY.md`. |
| `mineru-ai` | MinerU-Extract/mineru-ai | Source pointer only until an upstream redistribution license is confirmed. |

## Installation

For an Agent client that discovers project Skills from `.agents/skills/`, clone
this repository and expose the Skill directories there. Clients with their own
Skill directory or plugin format should use the corresponding adapter notes in
`adapters/` when they are added.

The Skills do not bind the user to a particular language model or chat platform.
Optional tools such as OCR, LaTeX, TSQX, Asymptote, or document conversion are
declared by the individual Skill documentation.

## Repository scope

This is the public mirror of the first-party Skills currently developed in the
private LaTeX workspace. The private workspace remains the broader source tree;
only files intentionally committed here belong to this public repository.

## License

First-party content in this repository is licensed under the Apache License,
Version 2.0. Third-party content retains the terms recorded in `THIRD_PARTY.md`.

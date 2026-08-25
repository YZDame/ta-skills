---
name: math-exposition-latex
description: Write polished Chinese LaTeX mini-papers and mini-lectures for high-school math competition teaching, concept explanations, blog posts, WeChat articles, and reusable lecture-note material. Use when Codex needs to turn a math concept, problem-solving method, proof idea, or coach's notes into a rigorous but readable exposition with LaTeX structure, examples, commentary, and references.
---

# Math Exposition LaTeX

## Workflow

Use this skill to produce Chinese mathematical exposition, not formal research papers. Optimize for a coach explaining a concept clearly to motivated high-school students or other teachers.

1. Identify the topic, audience, and output target: student Q&A, classroom handout, competition mini-lecture, blog article, or WeChat long-form article.
2. Choose one structure:
   - Mini-paper: abstract, introduction, preliminaries, main ideas, proof/derivation, applications, conclusion, references.
   - Mini-lecture: problem background, preliminaries, core technique, typical examples, method summary, references.
   - Technical note: motivation, notation, key lemma, proof details, examples, appendix if computations are long.
3. Write around the teaching logic: difficulty -> key observation -> method -> conclusion -> transfer.
4. Keep proofs readable. Explain why a move is natural before executing algebra or transformations.
5. Use examples with `题目`, `分析`, `解答`, and `点评`; add `方法提炼` when the transfer pattern matters.
6. Finish with a compact summary: what the method is, when it applies, and how to recognize it.

## LaTeX Defaults

Default to a lightweight standalone Chinese article unless the user asks for a larger lecture system:

```latex
\documentclass[10pt,a4paper,fontset=none]{ctexart}
\setCJKmainfont{Songti SC}
\setCJKsansfont{Heiti SC}
\usepackage{amsmath,amssymb,amsthm,geometry,booktabs,hyperref}
\geometry{margin=2cm}
```

Use author `LeyuDame` unless the user gives another author. Use `xelatex` for local compilation.

Only add packages when needed:

- Add `tikz` for simple geometry or diagrams.
- Add `asymptote` only when a real Asymptote figure is needed.
- Add `enumitem`, `mathtools`, or theorem styling only when they improve the document.
- Do not add BibTeX by default; use a final `参考资料` list.

## Writing Rules

Read `references/writing-framework.md` when drafting a full article, revising style, or checking section-level expectations.

Follow these defaults:

- Use `\(...\)` for inline math and `\[...\]` for display math.
- Do not use `$$...$$`.
- Do not use `\boxed` by default.
- Break long calculations with `aligned`.
- Use Chinese punctuation in Chinese prose.
- Avoid slogans, marketing language, and vague importance claims.
- Avoid overusing "不是……而是……".
- Prefer concrete titles such as `核心技巧`, `什么时候想到半角变形`, and `三类典型题`.

## Evan Template Guidance

Read `references/evan-template-notes.md` when the user asks for Evan Chen style, a long competition handout, theorem boxes, problem-set style output, or integration with this repo's `templates/` directory.

Default choice:

- Short blog or WeChat article: use the standalone lightweight template.
- Longer competition lecture note: consider `templates/evan-zh/evan.sty`.
- Problem-bank or VON integration: only use `von.sty` when the user explicitly wants LaTeX to pull from the problem database.

## Assets

Use `assets/ctex-mini-paper-template.tex` as a copyable starting point when producing a complete standalone `.tex` file.

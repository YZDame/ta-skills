---
name: math-exposition-latex
description: Write polished Chinese LaTeX short handouts, mini-lectures, mini-papers, and technical notes for high-school mathematics and competition teaching. Use when Codex needs to author a concept explanation, problem-solving method, proof idea, article, or source-free teaching handout with rigorous, economical mathematical prose. Do not use for scanned manuscripts, OCR recovery, or paired question-and-answer PDFs; route those source-digitization tasks to digitize-math-lectures.
---

# Math Exposition LaTeX

## Workflow

Use this skill to author Chinese mathematical exposition, not to recover source documents or write formal research papers. Optimize for a coach explaining mathematics clearly to motivated high-school students or other teachers.

1. Check the task boundary. If the input is a scan, handwritten manuscript, OCR result, paired question-and-answer PDF, or source-faithful conversion request, use `digitize-math-lectures` instead.
2. Identify the topic, audience, teaching goal, and output target.
3. Choose one form:
   - Short handout: a few problems or one method, written as `题目 -> 思路（按需） -> 解答/证明 -> 简短点评（按需）`.
   - Mini-lecture: a complete teaching sequence with background, prerequisites only when needed, core technique, selected examples, and a useful summary.
   - Mini-paper: article-style exposition with an argument, applications, and references.
   - Technical note: motivation, notation, key lemma, proof details, examples, and an appendix only when computations require it.
4. For a short handout, omit `思路` when the route is routine or mechanical. When included, use it only to state the decisive observation, construction, or method choice; do not repeat the solution.
5. For longer forms, write around the actual teaching logic. Include an introduction, preliminaries, conclusion, or references only when they serve the document.
6. Explain construction motives, key substitutions, non-obvious estimates, and easily misused conditions. Complete routine algebra directly.
7. Remove transitions and commentary that do not advance the mathematics. Default to one natural method; add a second solution, method extraction, or broader extension only when requested or genuinely valuable.

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

Read `references/writing-framework.md` when selecting a document form, drafting a full article, revising style, or checking section-level expectations.

Follow these defaults:

- Use `\(...\)` for inline math and `\[...\]` for display math.
- Do not use `$$...$$`.
- Do not use `\boxed` by default.
- Break long calculations with `aligned`.
- Use Chinese punctuation in Chinese prose.
- Avoid slogans, marketing language, and vague importance claims.
- Avoid overusing "不是……而是……".
- Prefer concrete titles such as `核心技巧`, `什么时候想到半角变形`, and `三类典型题`.
- Do not manufacture `分析`, `点评`, `方法提炼`, or `总结回顾` merely to fill a template.
- Keep every paragraph responsible for a mathematical action: set up an object, justify a step, derive a relation, close an argument, or state a reusable condition.

## Evan Template Guidance

Read `references/evan-template-notes.md` when the user asks for Evan Chen style, a long competition handout, theorem boxes, problem-set style output, or integration with this repo's `templates/` directory.

Default choice:

- Short handout, blog, or WeChat article: use the standalone lightweight template unless the user selects another style.
- Longer competition lecture note: consider `templates/evan-zh/evan.sty`.
- Problem-bank or VON integration: only use `von.sty` when the user explicitly wants LaTeX to pull from the problem database.

## Assets

Use `assets/ctex-mini-paper-template.tex` as a copyable starting point when producing a complete standalone `.tex` file.

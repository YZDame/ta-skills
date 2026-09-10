# Chinese Math Exposition Framework

Use this reference when choosing among a short handout, mini-lecture, mini-paper, or technical note, and when checking section-level expectations.

## Purpose

Produce teaching-oriented mathematical exposition for high-school competition contexts. The result should be rigorous enough to reuse in lecture notes and economical enough for a printed solution handout, while remaining readable for articles and student Q&A.

Choose the amount of structure from the teaching task. A short handout should feel like edited mathematics, not a compressed academic article.

## Structures

Use one of these structures unless the task clearly needs another one.

### Short Worked-Solution Handout

Use for a few problems or one focused method:

```text
题目
思路（按需）
解答 / 证明
简短点评（按需）
```

- Omit `思路` for routine filling-in or mechanical calculations.
- When present, keep `思路` to the decisive observation, construction, or method choice. Do not paraphrase the full solution.
- Explain only consequential moves: construction motives, key substitutions, non-obvious estimates, and easily misused conditions.
- Complete routine calculations directly.
- Default to one natural solution. Add commentary only when it gives a reusable trigger, condition, or warning; one or two sentences usually suffice.
- Do not require an introduction, preliminaries, summary, references, or method-extraction section.

### Standard Mini-Paper

```latex
\maketitle

\begin{abstract}
...
\end{abstract}

\section{引言}
\section{预备知识}
\section{核心方法}
\section{应用}
\section{总结}
\section*{参考资料}
```

### Lecture-Oriented

```latex
\section{问题背景}
\section{预备知识}
\section{核心技巧}
\section{典型例题}
\section{方法小结}
\section*{参考资料}
```

### Expository Article

```latex
\section{引言}
\section{预备知识}
\section{核心知识与主要想法}
\section{证明与推导}
\section{应用举例}
\section{总结与延伸}
\section*{参考资料}
```

Use an appendix only when long computations, classifications, or supplementary proofs would slow the main text.

## Section Guidance

### Abstract

Write 3--6 sentences. Answer:

1. What problem or concept is discussed?
2. What core method is used?
3. What will the reader be able to do afterward?

Avoid promotional language. If a significance claim is needed, make it concrete.

### Introduction

Use the introduction to pose the problem, not to prove everything.

Good sequence:

1. Start from a natural question, representative problem, or common confusion.
2. Name the student's likely obstacle.
3. State what the article resolves.
4. Briefly preview the structure.

### Preliminaries

Include only definitions, formulas, theorems, and notation actually used later.

Avoid front-loading definitions that can be explained in context. Fix important notation early.

### Core Method

This is the main section. Use teaching names such as:

- 核心方法
- 核心技巧
- 主要想法
- 方法提炼
- 关键观察

Organize as:

```text
问题困难 -> 关键观察 -> 方法操作 -> 得到结论
```

Do not present formulas alone. Add one sentence before or after key transformations explaining why the move is natural.

### Proofs and Derivations

Proofs should be rigorous and readable.

- Do not skip key transformations.
- Do not compress all algebra into one line.
- Avoid overusing `显然`, `易得`, and `不难发现`.
- Explain steps where high-school readers are likely to get stuck.
- Split long arguments into Step 1, Step 2, Step 3, or into `证明思路` and `正式证明`.

### Applications and Examples

Use examples as method transfer, not decoration. The labels below are available components, not a mandatory checklist.

Recommended example block:

```latex
\subsection{例 1：标题}

\textbf{题目.}
...

\textbf{思路.} % omit when the route is routine
...

\textbf{解答.}
...

\textbf{点评.} % omit unless it adds genuine transfer value
...
```

For a genuinely important transfer pattern, optionally add:

```latex
\textbf{方法提炼.}
...
```

In a mini-lecture or mini-paper, order examples from direct use to transformed use to competition-style synthesis when that progression serves the teaching goal. A short handout need not manufacture this sequence.

### Conclusion for Longer Forms

Keep it short. Answer:

1. What is the core method?
2. What problems does it fit?
3. How can students recognize it next time?

Short handouts do not require a conclusion or per-problem review section.

### References

Do not use BibTeX by default. Use:

```latex
\section*{参考资料}

\begin{enumerate}
  \item 作者，资料名称，出版信息或网站信息，年份。
  \item 链接：\url{https://example.com}
\end{enumerate}
```

For webpages, include title, author or organization if available, and URL. Do not provide only bare links.

## Math Typesetting

- Inline math: `\(...\)`.
- Display math: `\[...\]`.
- Never use `$$...$$`.
- Avoid `\boxed` unless the user explicitly wants boxed final answers.
- Use `aligned` for multi-line calculations:

```latex
\[
\begin{aligned}
A
&= B + C \\
&= D.
\end{aligned}
\]
```

Use Chinese punctuation in Chinese prose. Formula internals follow mathematical convention.

## Language Style

The voice should be clear, restrained, rigorous, and teaching-friendly.

Avoid:

- slogan-like language;
- motivational filler;
- vague words such as `非常重要` without content;
- AI-flavored metaphors;
- bureaucratic phrases such as `赋能`, `闭环`, and `抓手`.
- process narration about drafting, OCR, or what the document is about to do;
- empty transitions that merely announce the next calculation.

Prefer concrete explanatory sentences:

```text
这个变形的作用是把未知角集中到同一个三角函数中。
```

Use direct section titles:

```latex
\section{从二倍角公式到半角公式}
\section{什么时候想到半角变形}
\section{三类典型题}
```

## Audience Adjustment

For high-school students, emphasize why the method appears, where mistakes happen, and how it links to known knowledge.

For teachers, add `教学提示` when useful.

For competition students, increase mathematical density and state trigger conditions. Add variants or comparisons only when they clarify method choice; do not generate them by default.

## Reference Authors and Works

Useful style references:

- George Polya, *How to Solve It*.
- Paul R. Halmos, "How to Write Mathematics".
- Donald E. Knuth, Tracy Larrabee, Paul M. Roberts, *Mathematical Writing*.
- Evan Chen, *An Infinitely Large Napkin*.
- Evan Chen, *Euclidean Geometry in Mathematical Olympiads*.

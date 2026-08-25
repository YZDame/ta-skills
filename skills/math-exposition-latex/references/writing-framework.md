# Chinese Math Exposition Framework

Use this reference when drafting a full mini-paper or mini-lecture.

## Purpose

Produce teaching-oriented mathematical exposition for high-school competition contexts. The result should be rigorous enough to reuse in lecture notes, but readable enough for blog posts, WeChat articles, and student Q&A.

The target style is exposition: structured like a compressed academic article, but motivated and pedagogical.

## Structures

Use one of these structures unless the task clearly needs another one.

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

Use examples as method transfer, not decoration.

Recommended example block:

```latex
\subsection{例 1：标题}

\textbf{题目.}
...

\textbf{分析.}
...

\textbf{解答.}
...

\textbf{点评.}
...
```

For important transfer patterns, add:

```latex
\textbf{方法提炼.}
...
```

Order examples from direct use to transformed use to competition-style synthesis.

### Conclusion

Keep it short. Answer:

1. What is the core method?
2. What problems does it fit?
3. How can students recognize it next time?

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

For competition students, increase density and include trigger conditions, variants, comparisons with other methods, and faster contest approaches.

## Reference Authors and Works

Useful style references:

- George Polya, *How to Solve It*.
- Paul R. Halmos, "How to Write Mathematics".
- Donald E. Knuth, Tracy Larrabee, Paul M. Roberts, *Mathematical Writing*.
- Evan Chen, *An Infinitely Large Napkin*.
- Evan Chen, *Euclidean Geometry in Mathematical Olympiads*.

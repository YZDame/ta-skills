# Evan Template Notes for This Workspace

Use this reference when the user asks for Evan Chen style, a long competition handout, theorem boxes, or integration with an external LaTeX template collection.

## Local Template Map

The relevant templates in the author's broader LaTeX workspace are:

- `templates/evan-zh/evan.sty`: Chinese-enhanced Evan-style package. Best for daily competition lecture notes, worked solutions, and training material. In another workspace, replace this path with the corresponding template location.
- `templates/evan/evan.sty`: upstream Evan-style package. Use mainly for compatibility or reference.
- `templates/evan/short-preamble.sty`: compact reference for the core package choices and theorem boxes.
- `templates/TST/natoly.sty`: better for contest papers than exposition.
- `templates/von/von.sty`: bridges the local problem database into LaTeX through PythonTeX; use only when explicitly needed.

## When to Use `evan-zh`

Use `evan-zh` when the output is a longer handout, a contest-method note, or a document with many theorems/examples/remarks.

Typical pattern:

```latex
\documentclass[12pt]{ctexart}
\PassOptionsToPackage{hidelinks}{hyperref}
\usepackage[evanchinese,sexy,noasy]{../templates/evan-zh/evan}
```

Choose `noasy` unless the document actually contains Asymptote figures. This keeps compilation simpler.

Use `sexy` for longer documents where theorem boxes and richer section styling help navigation. Avoid it for short blog-like articles when a plain style is cleaner.

## When to Use Lightweight `ctexart`

Use the standalone lightweight template for:

- short concept explanations;
- WeChat/blog posts;
- student Q&A turned into a note;
- material intended to be pasted into another document later.

The lightweight template has fewer package interactions and is easier to reuse.

## Mac Font Notes

On this host, default CTeX macOS fonts can fail if `STHeiti` is unavailable. Prefer explicit fonts in standalone templates:

```latex
\documentclass[10pt,a4paper,fontset=none]{ctexart}
\setCJKmainfont{Songti SC}
\setCJKsansfont{Heiti SC}
\setCJKmonofont{Songti SC}
```

Compile with `xelatex`.

## Theorem and Example Style

For short articles, simple theorem environments are enough:

```latex
\newtheorem{theorem}{定理}
\newtheorem{lemma}{引理}
\newtheorem{proposition}{命题}
\newtheorem{example}{例}
\newtheorem{remark}{注}
```

For long handouts using `evan-zh`, rely on its built-in theorem environments instead of redefining them.

## VON and Problem Database

Do not use `von.sty` for ordinary writing. Use it only when the user asks to pull problems from the local `problem-db/` inside LaTeX.

For normal mini-lectures, copy or write the problem statement directly into the document.

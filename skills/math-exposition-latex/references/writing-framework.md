# Textbook exposition conventions

## Chapter organization

Start from a mathematical question and a concrete object. Introduce general definitions at the point where a calculation or extension motivates them. Order results by their proof dependencies. End with exercises or a compact formula table when useful; avoid a formula recap that duplicates the preceding chapter.

A typical sequence is: introductory problem → special case and proof → general construction → principal theorems → examples and geometric consequences → connections/limitations → exercises with separate answers. This is a flexible pattern, not a compulsory table of contents.

## Definitions

Specify the ambient set and parameters. State what is being defined before using its properties. Distinguish a definition from a characterization theorem. Set standing assumptions once, but repeat a hypothesis in a standalone theorem if omitting it changes the result.

Use consistent notation and distinguish points, vectors, coordinate triples, and scalar functions. For a nonhomogeneous quadratic, write f for the polynomial and G for its constant coefficient; use a different symbol for the polarized bilinear form.

## Theorems and proofs

A theorem must be understandable independently of conversational context. State existence and uniqueness claims precisely. Specify finite real contact points where geometric arguments need them; specify C^1 or C^2 hypotheses when using implicit-function or Taylor theorems.

Keep proof paragraphs short enough to expose the reasoning. Explain why an identity is useful, then derive it. Mark the step that uses a hypothesis. Use “反之” only when a converse is actually being proved. Avoid “显然” at the main difficulty.

When invoking an advanced theorem, name it and state the portion required. It is acceptable to omit a proof outside the intended scope, but explicitly identify the omission. Never add an entire prerequisite chapter solely to avoid an honest invocation.

Check whether the construction is local or global, whether an equation has finite solutions, and whether two objects coincide or genuinely degenerate. Put exceptional cases near the theorem rather than hiding them in the final notes.

## Examples and exercises

Prefer:

\begin{example}
[Precise problem statement.]
\end{example}
\begin{proof}[解]
[Calculation or argument.]
\end{proof}

Use examples for direct application, interpretation, and boundary cases. Keep a figure adjacent to the reasoning it supports. Give a caption naming the relationship, not merely “示意图”.

Assign exercises that vary the object, test hypotheses, or transfer the method. Separate answers from statements. Verify numerical values and equations independently of prose; do not create routine implementation-mirroring software tests for a writing task.

## Editorial pass

- Replace “你记得基本正确” with a mathematical proposition and its assumptions.
- Replace “本质上都相通” with an explicit chain of implications and its boundary.
- Replace repetitive “关键在于/这说明/总结” sentences with the needed logical connection.
- Use descriptive headings: 圆外点的切点弦、齐次化与极化、隐函数的切线.
- Keep formula boxes for results the reader needs to locate; avoid framing every calculation.
- Preserve useful intuition: explain the mathematical reason for a construction without addressing the reader as a chat participant.

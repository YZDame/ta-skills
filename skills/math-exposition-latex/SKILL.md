---
name: math-exposition-latex
description: Write or revise Chinese mathematical lecture notes, textbook-style chapters, competition handouts, and LaTeX mini-papers with precise definitions, hypotheses, proofs, examples, and exercises. Use for requests such as 数学讲义、教材式书写、规范数学语言、Evan Chen 模板、LaTeX/PDF, or turning a mathematical conversation into a reusable exposition. Preserve the user's mathematical main thread and distinguish geometric arguments from analytical extensions.
---

# Mathematical Exposition and LaTeX

Produce a self-contained mathematical text for its intended reader. Default to Chinese for mathematical materials unless the user requests another language. Treat textbook prose as a distinct genre: precision and connected reasoning, not a conversation copied into numbered sections.

## 1. Establish the mathematical main thread

- Identify the starting problem, central result, audience, prerequisites, and intended deliverables from the request.
- Preserve a user-supplied outline and the mathematical order they accept. Correct errors and necessary dependencies without silently replacing the subject.
- Write one internal sentence specifying what the reader should understand by the end. Make every main section serve it.
- Begin with the concrete object or problem. Develop special case → general statement → mechanism → examples → extension when appropriate; choose a different order if the proof dependencies require it.
- Put related advanced theory after the main treatment or in an appendix. Do not expand prerequisite review into an unrelated course.
- Scale detail to the mathematical difficulty and audience, not a target page count. Use exposition between formal environments; avoid a wall of definitions and theorems.

## 2. Write in mathematical textbook language

Read [writing-framework.md](references/writing-framework.md) for formal statement, proof, example, and editing conventions. Read [style-examples.md](references/style-examples.md) when converting a chat answer or deciding whether an extension has displaced the main topic.

- Fix notation and standing assumptions before using them. Do not overload a letter as both a function and a coefficient, or a coefficient and a bilinear form.
- State definitions, theorems, lemmas, corollaries, and remarks only where their logical role warrants them. Label results that are cited later.
- State each theorem's domain, hypotheses, conclusion, and relevant exceptions. Separate sufficient conditions from necessary conditions and local results from global ones.
- Give readable proofs: identify the decisive step, justify each nontrivial implication, and explicitly invoke external results. If a proof is omitted, say so; do not disguise an invocation as a proof.
- Use restrained connective prose, e.g. 设、称、由……得、因此、反之. Remove conversational acknowledgments, rhetorical questions in headings, repeated boxed formulas, slogans, and unsupported claims of “deep connections.”
- Do not mechanically attach 分析/点评/方法提炼 to every example. Prefer an example statement followed by 解; add commentary only when it identifies a transferable distinction.
- Do not force an abstract, conclusion, or teaching-advice section onto a textbook chapter. Keep classroom advice separate when requested.

## 3. Check mathematical scope and completeness

Check all of the following before typesetting:

1. The theorem applies to the stated objects, including regularity, nondegeneracy, existence, and real/complex distinctions.
2. Algebraic equivalences and geometric interpretations hold under the same assumptions. Check zero denominators, vanishing gradients, boundary cases, and points at infinity when material.
3. Each formula is derived or correctly attributed; terminology matches its definition. Avoid “degenerates” when two objects merely coincide.
4. Auxiliary theories explain the original result without claiming equivalence beyond their domain.
5. Examples actually illustrate the preceding result; exercises have correct answers and are aligned with the text.

Use primary textbooks or author documentation when the user asks for references or when a point needs verification. Read the relevant content; do not rely on search snippets. Borrow mathematical organization, not verbatim prose. Attribute consulted materials accurately and do not imply sources support an unrelated section.

## 4. Typeset and compile

Use author `LeyuDame`, A4, 2 cm margins, and XeLaTeX unless the user specifies otherwise. Prefer 11 pt for extended reading. Use `ctexart` with Fandol on portable TeX Live installations; detect available fonts before selecting OS-specific fonts. Do not assume Songti SC exists on Linux.

- For textbook or competition notes with theorem environments, prefer the bundled Evan template when requested or consistent with the established style. Read [evan-template-notes.md](references/evan-template-notes.md).
- Use [textbook-template.tex](assets/textbook-template.tex) and the bundled [evan.sty](assets/evan.sty) for the tested compatible setup. Keep both together in delivered source packages.
- For short articles or plain handouts, use [ctex-mini-paper-template.tex](assets/ctex-mini-paper-template.tex) and choose fonts for the actual environment.
- Use `\(...\)` and `\[...\]`, not `$$`. Break long calculations with `aligned`. Use theorem boxes selectively; use normal exposition for connective arguments.
- Use TikZ for exact geometry, tables for formula mappings, and figures with captions explaining the mathematical relationship. Do not use generated imagery for exact mathematical diagrams.
- Avoid unused packages, hand-edited page breaks that merely hide overflow, and tiny text used to force a page count.

For PDF requests, apply the PDF skill's authoring and verification requirements and deliver the compiled PDF, not only source. Compile at least twice or with latexmk until cross-references stabilize. Inspect warnings for missing glyphs, unresolved references, and overfull boxes; render and inspect every page, enlarging dense formulas, diagrams, or suspect pages. Check theorem boxes, tables, captions, headers, and section transitions. Do not report an unavailable PDF as complete. Resolve missing dependencies where feasible before declaring a compilation block.

## 5. Deliver and preserve

Save ordinary user-facing files through the applicable Library workflow. Keep source and PDF identities when revising existing files. If a source package is requested, include the main `.tex`, the actual style file, and any required assets; do not depend on nonexistent paths. Skill files themselves are saved through the personal-skill workflow, not Library.

Report the mathematical scope, important corrections, and verified deliverables concisely. Do not repeat the lecture in the final message or expose internal dependency setup details on success.

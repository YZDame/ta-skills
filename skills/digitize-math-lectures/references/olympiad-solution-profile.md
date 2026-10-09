# Olympiad Solution Digitization Profile

Use this profile to turn competition manuscripts, loose images, PDFs, existing Markdown or TeX, or terse solution notes into compact, printable solutions for students. It is a source-recovery and mathematical-editing workflow, not a general request to solve every problem from scratch.

## 1. Boundary and defaults

- Use `exam-answer-digitization` when complete question and answer PDFs must be paired set by set.
- Use this profile when the source is a manuscript, mixed collection, partial solution, or already-extracted text whose mathematical route needs faithful editorial completion.
- Use `lecture-authoring` only when the source is being reorganized into a full teaching sequence.
- Route newly authored articles and source-free short handouts to `math-exposition-latex`.
- Route a pure solving or checking request to `math-olympiad`.

Default to `route-preserving-completion`. Preserve a viable source method; add missing definitions, decisive deductions, conditions, and conclusions; and repair local mistakes locally. Do not replace the route because another solution is shorter. If the source route fails or the material does not determine a defensible completion, record the uncertainty and keep the item at `REVIEW_REQUIRED`. Use `authored` mode only when the user explicitly requests a new solution.

## 2. Per-problem content contract

For a large or difficult collection, the following optional working record can help track problems. Small tasks can use source comments and a concise handoff; these records are temporary, not required final materials:

```yaml
id:
source_pages: []
statement_status: complete | uncertain | incomplete
solution_mode: transcribed | route-preserving-completion | authored
source_method:
teaching_goal:
key_objects: []
key_relations: []
missing_steps: []
risk_flags: []
verification_status: pending | strict-check-passed | adversarial-passed | review-required
figure_id:
unresolved: []
```

These fields are editorial evidence and must not appear in the printable body.

## 3. Printed solution contract

Use this order:

```text
题目
思路（仅在存在关键观察、构造或方法选择时）
解答 / 证明
简短点评（仅在确有迁移价值或用户要求时）
```

- Do not force a separate `思路` for a simple fill-in problem or mechanical calculation.
- Keep `思路` to roughly one to five sentences. State the observation that selects the route; do not preview every line of the solution.
- Write the solution as mathematical actions with their necessary reasons. Explain construction motives, key substitutions, non-obvious estimates, and easily misused conditions. Complete routine algebra directly.
- Present one natural method that serves the stated teaching goal. Do not add a second solution or broad generalization without a request.
- Add at most one or two sentences of commentary when it gives a reusable trigger, condition, or warning. Do not generate routine `点评`, `方法提炼`, or `总结回顾` sections.
- Remove processing narration such as OCR confidence, missing handwriting, source defects, model completion, or verification workflow from the final body. Keep unresolved issues in source comments and the handoff; separate process files are optional and temporary.

## 4. Mathematical completeness checks

Apply the relevant checklist before marking a problem as verified:

- **Algebra:** domain restrictions, nonzero denominators, reversibility of transformations, extraneous roots, and the final answer.
- **Inequalities:** variable conditions, direction of each estimate, theorem hypotheses, equality conditions, and attainability.
- **Geometry:** construction definitions, sources of incidences and metric relations, correspondence order, and the exact criteria for cyclicity, tangency, similarity, or congruence.
- **Number theory:** coprimality hypotheses, division in congruences, divisibility chains, and exhaustive case divisions.
- **Combinatorics:** counted objects, mutually exclusive and exhaustive cases, duplicate counting, and realizability of constructions.

## 5. Risk-triggered verification

- For transcription plus connective prose or mechanical intermediate steps, perform one strict mathematical check against the statement and source route.
- Invoke `math-olympiad` for an independent adversarial verification when the completion supplies a substantial part of the proof, introduces a key lemma or construction, encounters ambiguity in the statement, changes or repairs the source route, uses `authored` mode, or triggers one of the mathematical risks above.
- Independent verification should receive the statement and proposed solution without being asked to imitate the source prose. Reconcile concrete objections; report any unresolved issue without requiring a separate review file.
- If verification is unavailable, inconclusive, or fails, set `verification_status: review-required` and retain the project at `REVIEW_REQUIRED`. Compilation is not mathematical approval.

## 6. Geometry figures

For a geometry problem, use:

```text
problem statement and original page
-> semantic specification
-> tsqx-gen
-> TSQX -> Asymptote -> PDF
-> mathematical and visual review
-> document integration
```

Infer objects and relations from the statement, not from hand-drawn proportions. Preserve the original page as evidence. Use TikZ for non-geometric diagrams or a documented exception; do not replace the TSQX route with a TikZ-only policy.

## 7. Delivery defaults

- Produce a compact answer booklet.
- Respect the user-selected template or an existing `project.yaml.template`; a new manifest is optional. In this workspace, recommend `templates/TST/natoly.sty`; do not bind content semantics to that package.
- Show answers by default and retain the selected template's `noanswers` switch for a student version.
- Compile and visually inspect the requested outputs only; create a student PDF when requested, not merely because the style supports it.
- Keep the first complete draft at `REVIEW_REQUIRED`; only an authorized human review may move it to `APPROVED`.

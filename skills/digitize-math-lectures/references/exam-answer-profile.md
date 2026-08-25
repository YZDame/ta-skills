# Exam Answer Digitization Profile

Use this profile when turning one or more scanned examination question/answer PDFs into compact electronic reference answers. It supplements the general pipeline in `SKILL.md` and the state contract in `pipeline-contract.md`.

## 1. Source authority and OCR

Keep the original question and answer PDFs immutable under `sources/`. Record their paths, hashes, page counts, and page dimensions before extraction.

- Run Mistral OCR on the question PDF and the answer PDF as the primary PDF route. Save raw responses, page-level Markdown or text, rendered page images, and run metadata under `extraction/`. If it is unavailable, document the fallback; never silently substitute another backend when the user explicitly requests Mistral OCR.
- Treat OCR as a candidate. Check every question stem against the question PDF and every solution against the answer pages.
- The question PDF is authoritative for wording, conditions, labels, and obscured content. The answer PDF is evidence for the handwritten method and intended result.
- Filter pages or regions that the user identifies as irrelevant, such as a score-data page at the beginning of an answer PDF. Do not copy OCR/audit notes into the finished document.
- Mark unresolved text, formulas, labels, and mathematical ambiguities for review instead of silently guessing.

## 2. Set-level TeX organization

For an exam collection, use a small main file and one file per set:

```text
tex/
├── main.tex
└── sets/
    ├── 2026年第一套模拟卷.tex
    └── …
```

`main.tex` contains document setup and `\\input` statements. Each set file contains the complete question stems followed by their corresponding solutions. Do not split questions and answers into separate TeX files unless the user explicitly requests that organization.

Use the selected answer style package, such as `templates/TST/natoly.sty`, for the answer visibility switch. The default build must show answers; a `noanswers`-style option may hide them for a question-only edition when the package supports it. Keep this switch in the style or main setup, not duplicated in every set file.

## 3. Content and solution standards

- Reconstruct the complete stem before typesetting the solution. Include conditions, diagrams, labels, options, and subquestions.
- Use the answer PDF's handwritten work as mathematical evidence, then supply missing connective prose, justifications, and necessary definitions so the result reads as a standard reference solution.
- When an answer-page crop is covered or unreadable, consult the paired question PDF before making a correction.
- Preserve genuine ambiguity in the text or review record. Do not invent an order, incidence relation, or hidden condition solely to force a unique answer.
- Keep the output compact: avoid decorative blank lines and unnecessary page breaks, while preserving readable formulas and figure-label spacing.
- Do not use `\\boxed`. Do not put OCR provenance, workflow disclaimers, or statements about filtering pages in the body of the finished answer.

## 4. Geometry figures

For every geometry problem:

1. Inspect the full original question page, not only an OCR crop.
2. Write a semantic specification listing objects, incidences, order, equalities, tangencies, perpendicularities, and unresolved ambiguities.
3. Use the `tsqx-gen` skill and create a TSQX source from the statement and the original figure. Do not use TikZ to guess a geometry diagram from visual proportions.
4. Compile the TSQX source through the local TSQX → Asymptote → PDF pipeline before integration.
5. Check the mathematical relations, labels, line styles, and visual placement in the standalone preview and in the final PDF.

TikZ remains appropriate for non-geometric diagrams such as grids, tables, flowcharts, and set schematics. If a geometry problem cannot be expressed faithfully with TSQX, record the limitation and the approved alternative renderer in the figure manifest.

## 5. Acceptance checklist

Before marking the project `APPROVED`, confirm all of the following:

- irrelevant answer-page material has been filtered;
- every question stem is complete and cross-checked;
- every solution has been normalized into a readable reference answer;
- all unresolved content and genuine problem ambiguities are recorded;
- one set file contains each set's questions and answers, and `main.tex` inputs the set files;
- answers are visible in the default build and the optional answer switch works;
- no `\\boxed` or workflow disclaimer appears in the finished body;
- every geometry figure has a TSQX source, standalone preview, and mathematical/visual review record;
- the full document compiles twice without undefined commands, missing glyphs, or new `Overfull`/`Underfull` warnings;
- every page has been rendered and checked for clipping, overlap, broken formulas, unreadable labels, and page overflow;
- ordinary auxiliary files are cleaned while editable sources, final PDF, SyncTeX, and intentional figure assets are retained.

Successful OCR, compilation, or figure rendering is still only a `REVIEW_REQUIRED` result. Move to `APPROVED` only after the user or an authorized reviewer confirms content, figures, source code, and layout.

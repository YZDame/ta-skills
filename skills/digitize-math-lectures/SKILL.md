---
name: digitize-math-lectures
description: Convert source mathematics PDFs, images, handwritten notes, or existing text into editable LaTeX and checked PDFs. Use for faithful transcription, source-based solution editing, or lecture adaptation; use math-exposition-latex for new writing without source recovery.
---

# Digitize Mathematics Materials

Produce accurate, readable mathematics from supplied sources. Preserve the user's manual edits and chosen solution routes. Scale the workflow to the material; a two-page note does not need a publishing pipeline.

## Choose the editing task

Infer the task from the request; clarify only when the permitted rewriting is genuinely unclear.

| Task | Editing boundary | Read when applicable |
|---|---|---|
| Faithful transcription | Recover the complete source; normalize notation and typesetting; mark uncertain content without inventing missing mathematics | [Exam pairing](references/exam-answer-profile.md) only for paired question/answer PDFs |
| Solution editing | Preserve a viable source method, fill consequential missing steps and conditions, repair local errors; request new-route authorization when the source route fails | [Solution editing](references/olympiad-solution-profile.md) |
| Lecture adaptation | Reorganize supplied material around the teaching goal; add explanations or examples within the requested scope | [Layout guidance](references/layout-separation.md) only for reusable or multiple layouts |

These tasks are independent of presentation. Board layout, exam grouping, answer hiding, and figure reconstruction are optional features, selected only when useful or requested. Existing `profile` values remain compatible: `board-digitization` / `source-faithful` normally mean transcription; `exam-answer-digitization` / `olympiad-solution-digitization` normally mean solution editing; `lecture-authoring` / `hybrid` normally mean adaptation. Explicit editing instructions take priority over these defaults.

## Work with sources

- Keep original PDFs, images, manuscripts, or other supplied source files unchanged under `work/<id>/sources/`. Existing project locations may be preserved.
- Inspect the source structure and extract reliable text directly. Use OCR for scanned or handwritten content. Use the selected backend; compare alternatives on a small sample only when recognition quality is uncertain. Paired exam PDFs have an existing Mistral preference in the exam reference.
- Keep machine extraction in `extraction/` during work. Never let OCR or bulk regeneration overwrite human-edited TeX or figure sources.
- Check complete stems, conditions, formulas, source reading order, and text–figure relationships. Keep concise page comments when helpful; source hashes, inventories, and separate audit documents are optional.
- Report specific unresolved issues in the handoff. Keep them visible in source comments when they still affect the draft; do not silently guess or insert processing narration into the student-facing text.

## Write and check the material

- Small material may use one root TeX file. Split by section or exam set only when it improves editing. Keep each question and its solution together unless instructed otherwise.
- Respect a selected template. Workspace defaults are `evan-zh` for adapted lectures and `natoly` for compact answer booklets. Neither requires converting old projects.
- Prefer shared style definitions for repeated layout choices. Ordinary figure widths and occasional page breaks are allowed; do not require a custom style architecture for a short document.
- For board/plain switching, use the supplied bixiu templates if suitable; read [layout guidance](references/layout-separation.md). Build only requested deliverables. Answer-visible output is the answer-booklet default; retaining an existing answer switch does not require producing a second PDF.
- When reconstructing figures, read [figure recovery](references/figure-reconstruction.md). Recover mathematical relations from the statement and full source page, not image proportions. Preserve editable drawing code: `.tsqx`, `.asy`, TikZ/PGFPlots `.tex`, or the tool's native source.
- Check mathematical conditions and reasoning against the source. Substantial proof completion or repair warrants independent mathematical verification when available; simple transcription does not require an adversarial workflow.
- Compile the requested outputs, resolving errors, missing glyphs/references, and layout defects that affect readability. Use latexmk or the needed number of passes; do not require a fixed two-run ritual. Inspect the actual PDF pages and figure labels. Harmless Underfull warnings alone do not fail delivery.
- A compiled draft remains `REVIEW_REQUIRED` until the user or an authorized reviewer approves its content and figures. Communicating this status is sufficient for a small task; `project.yaml` and separate component reports are optional. See [project and retention contract](references/pipeline-contract.md) for larger or existing projects.

## Retain originals and final editable materials

Default lasting package:

```text
work/<id>/
├── sources/             # Original PDFs, images, and other supplied files
├── <title>.tex          # Main editable document
├── <title>.pdf          # Checked output (review status communicated separately)
├── sections/            # Only if the main file uses subfiles
├── figures/             # TSQX, Asymptote, TikZ, etc. and required figure assets
└── styles/              # Only required project-local dependencies
```

Use existing `tex/`, chapter, or figure paths when maintaining a project; do not reorganize merely to match this example. Final material includes all TeX subfiles, editable figure sources, required figure PDFs/images, and local styles/data needed to reproduce the requested PDF. Keep both TSQX and its generated Asymptote source when they form the delivered drawing chain. Inline TikZ in a retained TeX file is sufficient. Preserve SyncTeX where the workspace requires it.

OCR responses, page renders, merged Markdown, temporary previews, build caches, draft archives, per-problem records, and review reports may be used during processing but are not required lasting deliverables. Do not create unused directories or mandatory manifests. Keep process notes out of the printed body.

After checking the PDF, clean known auxiliary files with the project's build tool (`latexmk -c` in this workspace). Before removing any other current-run intermediate, inspect actual dependencies and retain unresolved evidence until its issue is resolved. If an artifact's role is uncertain, keep it and report it. This retention policy does not authorize deleting pre-existing files, prior work, or manually edited material. Never use blanket `git clean`, `reset --hard`, extension-based deletion, or `latexmk -C` as delivery cleanup.

Approval permits a lean final copy under the workspace's lecture destination. Original materials remain preserved under `work/<id>/sources/`; avoid duplicating them into the published package unless requested. OCR or compilation alone is never content approval.

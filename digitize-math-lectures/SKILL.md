---
name: digitize-math-lectures
description: Convert handwritten boards, exam question and answer PDFs, GoodNotes PDFs, lecture manuscripts, scanned handouts, textbooks, existing Markdown or LaTeX, images, and spoken additions into well-structured, readable, traceable, and reviewable mathematics materials. Supports board digitization, exam-answer digitization, multi-source lecture authoring, OCR routing, semantic recovery of mathematical figures, vector reconstruction with TikZ, PGFPlots, TSQX, or Asymptote, LaTeX compilation, and layered review. The central design rule is strict separation of content from layout; chapter content describes teaching structure, while the user-selected style package determines presentation. Use this Skill to digitize legacy materials, rebuild ordinary handouts, author lectures from multiple sources, or establish a repeatable mathematics-material production pipeline.
---

# Digitize and Author Mathematics Lectures

Convert source materials into a clear, maintainable LaTeX project. Prioritize mathematical accuracy, teaching structure, and source quality. Do not mechanically imitate handwritten positions, font sizes, line breaks, or irregular whitespace. Keep original sources, machine extraction, merged content, review drafts, and approved deliverables distinguishable.

**Highest-level design rule: separate content from layout strictly.** Chapter content files must not contain layout-specific commands such as width parameters, column counts or widths, forced `\\clearpage` breaks, `paracol`, `lecturepage`/`annotation`, absolute-position TikZ, or `twocolumn`. The style package controls layout; content describes teaching structure only. Record the style package in `project.yaml` under `template`.

## 1. Select the project configuration

Choose one **profile** in the project manifest and record the selected style package in `project.yaml.template`. The profile determines defaults and the permitted degree of rewriting; users may explicitly override `template` in `project.yaml`.

- **`board-digitization`**: Digitize handwritten boards while preserving content order, source-page provenance, left/right column ownership, and text-figure relationships. Re-typeset in conventional LaTeX unless the user explicitly requests visual replication. Keep `source-faithful` only as a legacy alias.
  - **Default/recommended template**: `tex/styles/bixiu.sty`, a three-layer content/board/plain architecture supplied in this Skill's `assets/`. This is the only profile that requires the three-layer package and compilation of both board and plain layouts.
- **`lecture-authoring`**: Rework an ordinary lecture manuscript or create a new lecture from multiple sources. Chapters may be reorganized, notation normalized, derivations expanded, and figures redesigned.
  - **Default template**: `templates/evan-zh/evan.sty`, compatible with `ctexbook`/`ctexart` and providing theorem, problem, and solution environments. Follow an explicit user choice of another style package.
- **`hybrid`**: Preserve the core sequence and examples while reorganizing explanations, layout, or figures. Record what must remain and what may be rewritten.
  - **Default template**: choose according to the dominant component: use the bixiu three-layer package when the source board dominates, and `templates/evan-zh/evan.sty` when newly authored lecture content dominates.
- **`exam-answer-digitization`**: Convert question and answer PDFs into compact, reviewable electronic reference answers. Keep complete question stems and normalized solutions together in one file per exam set, while preserving source-page traceability and the distinction between OCR candidates and reviewed mathematics.
  - **Default template**: use the user-selected exam style package; in this workspace, `templates/TST/natoly.sty` is the current reference package. Read [references/exam-answer-profile.md](references/exam-answer-profile.md) before production.

The `template` field may contain a repository path, an absolute path, a CTAN package name, or a project-local relative path. Prefer a project-local copy for version control and approved distribution. Before production, record the audience, teaching goal, content scope, deliverable format, template path and version, permitted rewriting, and approval owner.

## 2. Use a minimal, self-explanatory project structure

```text
work/<project-id>/
├── <lecture-title>.tex     # Current human-reviewed main file
├── <lecture-title>.pdf     # Current compiled review draft
├── project.yaml            # Configuration, sources, state, template, and file index
├── sources/                # Immutable source materials
├── extraction/             # OCR, parsing, timestamps, and machine candidates
├── content/                # Merged, normalized content with provenance anchors
├── tex/
│   ├── chapters/           # Content layer: layout-independent TeX by chapter
│   ├── sets/               # Exam-answer profile: one complete set per file
│   ├── styles/             # Project-local style packages, if any
│   └── sections-legacy/    # Retired drafts for historical comparison
├── figures/
│   ├── sources/            # Figure sources, corrections, and board scales
│   └── manifest.yaml
├── review/                 # Content, figure, source-code, and visual review records
├── build/                  # Compilation cache; board profiles commonly use current/plain
├── archive/                # Superseded pilots or drafts, when needed
└── tools/                  # Project-specific scripts only when genuinely required
```

The root `.tex` and `.pdf` must be actual human review files, not symlinks or deep copies; for `exam-answer-digitization`, the profile-specific `tex/main.tex` and configured review PDF are the equivalent entry points. Once created, the main draft belongs to human editing. Generators may write only to `extraction/`; they must not overwrite the review entry point, `content/`, `tex/chapters/`, `tex/sets/`, human-owned style copies, or `figures/sources/`. Do not create empty directories for unused stages.

## 3. Advance through four stages

Use `NEW -> EXTRACTED -> MERGED -> REVIEW_REQUIRED -> APPROVED`. Read [references/pipeline-contract.md](references/pipeline-contract.md) for complete definitions.

### Stage 1: Extract to `EXTRACTED`

1. Record each source's path, SHA-256 digest, page count, page dimensions, text-layer status, and privacy or copyright boundaries.
2. Render representative pages and assess handwriting, formula density, column structure, and figure types.
3. Run OCR only on materials that need recognition. Extract reliable text layers, Markdown, or LaTeX directly.
4. Compare OCR backends on three to five representative pages. Treat routing scores as hints; let actual samples determine the backend.
5. Save immutable raw responses, page-level Markdown, images, input hashes, timings, and errors in `extraction/`. Do not polish content at this stage.

For `exam-answer-digitization`, use Mistral OCR as the primary PDF OCR route. Preserve the raw response and page-level output; use another OCR backend only as a documented fallback, and never silently substitute it when the user explicitly requests Mistral OCR.

### Stage 2: Merge to `MERGED`

1. Combine OCR batches and multiple sources while preserving source and page or paragraph anchors.
2. Repair reading order, line breaks, duplicated passages, and obvious formatting noise. Mark uncertain text or formulas explicitly.
3. Organize sections, definitions, theorems, examples, derivations, and supplementary explanations according to the selected profile.
4. Distinguish source text, normalized content, and newly authored explanation.
5. Write merged content to `content/`. Build the figure manifest and complete semantic recovery, renderer selection, and standalone previews. Read [references/figure-reconstruction.md](references/figure-reconstruction.md) whenever figures are involved.

### Stage 3: Draft to `REVIEW_REQUIRED`

1. Produce a three-to-five-page pilot or one complete section first. Confirm structure, type size, color, figure style, and template.
2. **Keep content and layout separate when writing chapters.** Read [references/layout-separation.md](references/layout-separation.md).
3. Put chapters in `tex/chapters/chNN-title.tex`, split by `\\chapter`/`\\section`/`\\subsection`, not by source-board page number.
4. Chapter content must not contain `\\linewidth`/`\\columnsep`, `lecturepage`/`annotation`/`twocolumn`/`paracol`, forced `\\clearpage`, absolute-position TikZ nodes, or retired commands such as `\\sourcefigure`, `\\BoardText`, `\\BoardEquation`, `\\BoardGraphic`, and `boardpage`.
5. For **board-digitization**, use `\\fig{page}{figure}` without a width, `aside`/`\\asidetitle`, and `% source board page N` anchors. These semantic names come from `bixiu-content.sty`.
6. For **lecture-authoring**, use theorem, `problem`, `soln`, and standard sectioning environments supplied by `evan.sty`. For **hybrid**, declare the rule set used by each chapter.
7. For **board-digitization**, require `bixiu-content.sty`, `bixiu-board.sty`, `bixiu-plain.sty`, and the `bixiu.sty` router. Switch layouts with:
   ```latex
   \\providecommand{\\LectureLayout}{board}   % board / plain
   \\usepackage[\\LectureLayout]{tex/styles/bixiu}
   ```
   Board display widths come from `figures/sources/figures-board-scales.tex`, not content files.
8. For **exam-answer-digitization**, put the main file in `tex/main.tex`, set files in `tex/sets/`, and keep each set's complete question stem and solution in the same file. The selected answer style controls the visible-answer switch, which defaults to showing answers.
9. For **lecture-authoring**, normally load `\\usepackage[evanchinese, sexy]{templates/evan-zh/evan}` or a project-local style. One layout is sufficient unless the user requests more.
10. Put the main `.tex` and review PDF at the project root, chapters in `tex/chapters/`, styles in `tex/styles/`, figure sources in `figures/sources/`, and build caches in `build/`. The first complete draft remains `REVIEW_REQUIRED`.

### Stage 4: Approve to `APPROVED`

1. Revise the draft from user or authorized-reviewer feedback.
2. Confirm mathematical content, figure semantics, source code, and visual layout separately.
3. **Compile by profile**: board profiles require board and plain layouts; lecture-authoring and hybrid require one layout unless more are requested. Each required layout must pass two consecutive XeLaTeX runs without `! ` errors, undefined commands, or newly introduced `Overfull/Underfull` warnings.
4. Publish a self-contained `.tex` project, required subfiles, editable figure sources, and PDF to `approved_destination`. In this workspace, the default destination is `lectures/YYYYMMDDChinese-Lecture-Title/`.
5. Preserve `sources/`, `extraction/`, `content/`, `tex/sections-legacy/`, and review records. Do not overwrite process evidence with the approved draft.

## 4. Reconstruct mathematical figures

Use this loop:

`full-page inspection -> false-crop removal -> semantic specification -> renderer selection -> standalone compilation -> mathematical review -> visual and pedagogical review -> integration`

- Check every OCR crop against its full page and recover small figures omitted near formulas or column edges.
- Infer geometric relationships from the problem statement and context, never from hand-drawn proportions alone.
- Prefer TSQX or TikZ for plane geometry; PGFPlots/TikZ for functions and statistical curves; TikZ for number lines, set diagrams, tables, and flowcharts; Asymptote for solid geometry and complex analytic diagrams. For `exam-answer-digitization`, every geometry-problem figure must begin with a semantic specification and a TSQX/`tsqx-gen` reconstruction attempt based on the problem statement and the original page. Use TikZ only for non-geometric diagrams or a documented, user-approved exception.
- Keep photographs, screenshots, textured images, or semantically uncertain figures as bitmaps when appropriate. Do not invent relationships merely to make everything vector-based.
- Produce a standalone source and preview for every figure before integration. Check mathematical correctness and labels before appearance and similarity.

Read [references/figure-reconstruction.md](references/figure-reconstruction.md) for manifest fields, semantic specifications, renderer choices, and acceptance checks.

## 5. Maintain readable LaTeX sources

- Make source structure reflect lecture structure rather than OCR coordinates.
- Keep the main file limited to document setup and `\\input` statements.
- Content/layout separation is non-negotiable: widths, column counts, `\\columnseprule`, `paracol`, and page anchors do not belong in chapter content.
- Prefer paragraphs, `enumerate`, `itemize`, `align`, theorem environments, and reusable macros. Avoid absolute-position nodes for each line of text.
- Never let generated drafts overwrite human-edited drafts.
- Use filenames that describe content or stage; keep `final-final2`, hashes, and opaque abbreviations out of review drafts.
- Keep comments only when they explain something useful. Remove generator noise and duplicated style definitions.
- In Chinese technical prose, use the solid full stop `．` consistently instead of mixing it with `。`.
- Board digitization may map one source page to one logical page for review, but output pagination and line spacing should follow LaTeX readability. Match physical coordinates only when explicitly requested.

## 6. Apply layered acceptance checks

1. **Extraction:** Sources and page anchors are complete, raw results are traceable, and uncertainties are marked.
2. **Content:** Definitions, conditions, formulas, derivations, examples, and answers are checked; additions are clearly identified.
3. **Figures:** Full pages have been checked for missed figures; every figure has semantics, a renderer, an editable source, or a documented reason to retain a bitmap.
4. **Source code:** File responsibilities are clear, the main file is concise, unnecessary absolute positioning is absent, and chapter content has no forbidden layout commands.
5. **Compilation:** Every required layout compiles twice with XeLaTeX without missing glyphs, undefined commands, or unexpected layout warnings.
6. **Visual review:** Render every page and inspect clipping, overlap, formula breaks, text-figure proximity, and label legibility.
7. **Approval:** Keep the project at `REVIEW_REQUIRED` until content, figures, source code, and visuals are all confirmed.

## 7. Deliver required artifacts

- `project.yaml` with sources, profile, `template`, primary state, component review states, and `tex_chapters`/`tex_styles`/`build`/`approved_destination` fields;
- extracted results, merged content, and a review-ready LaTeX draft;
- profile-appropriate style packages or a recorded reference to the repository template;
- chapter content files calling only the selected package's semantic API plus standard `ctexart`/`ctexbook` structure;
- a figure manifest, semantic specifications, editable sources, board-only scale files where applicable, and previews;
- content, figure, source-code, and visual review records;
- after approval, a self-contained editable project and PDF in `approved_destination`.

## Completion rule

Successful OCR, PDF compilation, or vectorization is only a partial result. Mark the first complete draft `REVIEW_REQUIRED`. Mark the project `APPROVED` only after the user or an authorized reviewer confirms mathematical content, figures, source code, and layout. Compilation success is not sufficient for approval.

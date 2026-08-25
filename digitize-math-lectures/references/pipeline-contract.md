# Mathematics Lecture Pipeline Contract

## 1. Primary states

Use exactly five primary states:

`NEW -> EXTRACTED -> MERGED -> REVIEW_REQUIRED -> APPROVED`

- `NEW`: The project exists, but source intake is incomplete.
- `EXTRACTED`: The source manifest, hashes, and extraction results are complete. OCR runs have immutable records, and readable Markdown, LaTeX, or text layers have been extracted directly. Content has not been reorganized.
- `MERGED`: Multi-batch, multi-page, or multi-source content has been combined; reading order and basic structure have been repaired; source anchors remain traceable; the figure manifest and semantic specifications exist.
- `REVIEW_REQUIRED`: A compilable draft has passed automated checks and awaits review of mathematical content, figures, source code, and visual layout.
- `APPROVED`: The user or an authorized reviewer has approved the deliverable, and the self-contained version has been published to `approved_destination`.

Legacy states map as follows:

- `OCR_DONE`, `OCR_ASSEMBLED`, `SOURCES_INVENTORIED`, `EVIDENCE_ASSEMBLED` -> `EXTRACTED`
- `CONTENT_STRUCTURED`, `FIGURES_CLASSIFIED`, `FIGURES_PLANNED`, `VECTORS_RENDERED`, `FIGURES_RENDERED` -> `MERGED`
- `TEX_RENDERED`, `COMPILED` -> `REVIEW_REQUIRED`

Keep the primary state machine small. Record detail through component states instead of adding primary states.

## 2. Component review states

Record these fields separately in `project.yaml`:

- `review.content`
- `review.figures`
- `review.source_code`
- `review.visual`

Each field must be `PENDING`, `REVIEW_REQUIRED`, or `APPROVED`. All four fields must be `APPROVED` before the primary state becomes `APPROVED`.

## 3. Profiles

### `board-digitization`

- Preserve source content order, page provenance, left-right column semantics, and text-figure relationships.
- Re-typeset in conventional LaTeX by default. Do not imitate handwriting, line-by-line placement, or irregular whitespace.
- A source-page-to-logical-page mapping may be preserved for review; physical pagination follows readability.
- Match source page dimensions and absolute coordinates only when explicitly requested.
- Treat `source-faithful` as a legacy alias for this profile.

### `lecture-authoring`

- Let teaching goals determine the output structure rather than source pagination.
- Allow multiple sources, normalized notation, expanded derivations, redesigned figures, and new explanations.
- Use `templates/evan-zh/evan.sty` when no template is specified.
- Preserve provenance for key facts, problems, and quotations. Newly authored content must not appear to be source text.

### `hybrid`

- List content that must remain, content that may be reorganized, and content planned as new material.
- Each chapter must declare whether it follows board-digitization or lecture-authoring rules.

### `exam-answer-digitization`

- Treat the question PDF as the authority for complete stems and the answer PDF as the authority for solution evidence. Use the question PDF to recover text hidden or obscured in the answer PDF.
- Use Mistral OCR as the primary PDF OCR route. Store raw responses and page-level candidates under `extraction/`; OCR output remains a candidate until reviewed. If Mistral OCR is unavailable, document the fallback, and never silently substitute another backend when the user explicitly requests Mistral OCR.
- Put one exam set in one TeX file under `tex/sets/`; the main file contains document setup and `\\input` statements. Keep the full question stem and its answer in the same set file unless the user explicitly changes this rule.
- Keep the answer display switch controlled by the selected style package and default it to visible answers. Do not use `\\boxed` for final answers.
- For geometry problems, reconstruct figures from the statement and original page with TSQX/`tsqx-gen` before considering another renderer. TikZ is reserved for non-geometric diagrams or documented exceptions.
- Filter answer-page material that the user identifies as irrelevant (for example, score data on the first page) without inserting process notes into the finished document body.

## 4. Directory and stage contract

| Location | State | Responsibility |
|---|---|---|
| `sources/` | All stages | Immutable source materials |
| `extraction/` | `EXTRACTED` | OCR, parsing, page evidence, and immutable run records |
| `content/` | `MERGED` | Merged, normalized teaching structure with provenance anchors |
| `figures/` | From `MERGED` | Crops, manifest, semantic specifications, sources, and previews |
| Root `.tex` and `.pdf` | `REVIEW_REQUIRED` | Human-owned review entry points; `exam-answer-digitization` may use `tex/main.tex` and its configured review PDF |
| `tex/chapters/` | `REVIEW_REQUIRED` | Layout-independent chapter content |
| `tex/sets/` | `REVIEW_REQUIRED` | One complete question-and-answer TeX file per exam set (`exam-answer-digitization` only) |
| `tex/styles/` | `REVIEW_REQUIRED` | Content, board, plain, and router style packages |
| `tex/sections-legacy/` | As needed | Retired drafts for historical comparison |
| `review/` | From `REVIEW_REQUIRED` | Content, figure, source-code, and visual review records |
| `build/` | From `REVIEW_REQUIRED` | Compilation cache |
| `archive/` | As needed | Superseded pilots and drafts |
| `approved_destination` | `APPROVED` | Confirmed self-contained editable project and PDF |

Generators may write only to `extraction/`. They must not overwrite the root draft, `content/`, `tex/chapters/`, human-owned styles, or `figures/sources/`.

## 5. Content/layout invariants

`REVIEW_REQUIRED` and `APPROVED` chapter content must not contain `\\linewidth`, `\\columnsep`, `\\paperwidth`, `\\paracol`, `twocolumn`, `\\lecturepage`, `\\annotation`, `\\sourcefigure`, `\\BoardText`, `\\BoardEquation`, `\\BoardGraphic`, `boardpage`, or absolute-coordinate TikZ.

For board-digitization, `\\fig{p}{i}` is the only figure-reference API and widths come from `figures/sources/figures-board-scales.tex`. `bixiu-content.sty` must not load `geometry`, `paracol`, or `eso-pic`; board and plain styles handle layout only and do not define new content semantics. The router must load exactly one layout.

The same main entry point must compile twice in both `\\LectureLayout{board}` and `\\LectureLayout{plain}` modes. For lecture-authoring and hybrid, one layout is sufficient unless the user requests more.

## 6. Figure manifest

Every figure must record at least:

- stable identifier and source page or paragraph anchor;
- category: `false_crop`, `math_diagram`, `content_bitmap`, `ambiguous`, or `new_figure_request`;
- origin: `source_crop`, `full_page_recovered`, or `newly_authored`;
- semantic specification and unresolved ambiguities;
- renderer and editable source path, or the reason a bitmap is retained;
- standalone preview and mathematical, visual, and pedagogical review status.

`false_crop` may be rejected. `content_bitmap` and `ambiguous` must not be forced into vector form. Never infer mathematical relationships from hand-drawn proportions alone.

## 7. Acceptance invariants

- Extraction results must not masquerade as review drafts.
- Merged content must preserve provenance anchors and uncertainties.
- OCR crops must be checked against full pages so small figures are not silently lost.
- Write the figure semantic specification before drawing code.
- Compilation success cannot replace content or visual review.
- A project must not move from `REVIEW_REQUIRED` to `APPROVED` without user or authorized-reviewer confirmation.

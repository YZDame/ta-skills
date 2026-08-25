# Content/Layout Separation Guide

This is a hard constraint of `digitize-math-lectures`. Every `REVIEW_REQUIRED` and `APPROVED` LaTeX draft must follow it. A violation fails source-level review and must be rewritten.

## 1. Design goal

Chapter content describes teaching structure only. The style package selected in `project.yaml.template` controls page size, columns, type size, colors, spacing, column switching, pagination, annotation placement, and figure display widths.

The same chapter source should be able to switch between layouts by changing one `\\LectureLayout` option:

- `board`: landscape, two-column board-review layout;
- `plain`: A4, single-column article layout;
- `slides`: a planned beamer-compatible layout, not currently required.

For `lecture-authoring`, a single `templates/evan-zh/evan.sty` layout is normally enough. A three-layer package is optional when article/book switching is explicitly required.

## 2. Directory responsibilities

```text
tex/
├── chapters/
│   ├── ch01-title.tex      # Structure, prose, formulas, standard semantic environments
│   └── ch02-title.tex
└── styles/
    ├── bixiu.sty           # Router selected by \\LectureLayout
    ├── bixiu-content.sty   # Shared packages, counters, figure API, semantic defaults
    ├── bixiu-board.sty     # Board geometry, columns, board pagination
    ├── bixiu-plain.sty     # Plain geometry and aside rendering
    └── archive/            # Retired styles for historical comparison

figures/sources/
├── figures-full.tex
├── figures-NN-NN-corrections.tex
└── figures-board-scales.tex
```

Figure display widths belong in the figure layer, especially `figures-board-scales.tex`, not in body paragraphs.

## 3. Allowed and forbidden content

Chapter content must not contain:

- assignments or calculations involving `\\linewidth`, `\\columnsep`, `\\columnseprule`, `\\paperwidth`, or `\\paperheight`;
- `paracol`, `twocolumn`, `multicol`, or other column-switching commands;
- forced physical pagination with `\\clearpage`;
- absolute-coordinate TikZ such as `remember picture, overlay` with `current page.south west`;
- retired board APIs.

### Board-digitization API

Use:

- `\\chapter`, `\\section`, and `\\subsection` for structure;
- paragraphs, `enumerate`, `itemize`, and `description` for prose;
- standard `amsmath` environments for mathematics;
- `\\fig{page}{figure}` without width arguments;
- `\\begin{aside} ... \\end{aside}` with optional `\\asidetitle{...}`;
- `% source board page N` comments as provenance anchors.

Do not use `\\lecturepage`, `annotation`, `\\sourcefigure[width]{p}{i}`, `\\BoardText`, `\\BoardEquation`, `\\BoardGraphic`, `\\BoardPageNumber`, or `boardpage`. These belong only in historical drafts.

### Lecture-authoring API

Use standard structure and mathematics plus the semantic environments provided by `evan.sty`, such as `thm`, `prop`, `lem`, `cor`, `ex`, `problem`, and `soln`. Use the figure environments supplied by the selected style package. Do not use board-only `\\fig`, `aside`, or `figures-board-scales.tex`.

### Hybrid API

Declare the rule set used by each chapter. Do not mix board-only semantics into a lecture-authoring chapter without documenting the boundary.

## 4. Style-package responsibilities

### `bixiu-content.sty`

The shared layer may load mathematical, graphics, color, TikZ, list, table, and parsing packages; define counters and figure registries; provide shared TikZ styles; and provide default rendering for `\\fig`, `aside`, and `\\asidetitle`.

It must not load `geometry`, `paracol`, or `eso-pic`, and must not set `\\paperwidth` or `\\columnsep`.

### `bixiu-board.sty`

Own board page dimensions, landscape columns, board-specific spacing, and board pagination. It must not redefine content semantics.

### `bixiu-plain.sty`

Own A4 single-column layout and plain rendering of board annotations. It must not redefine content semantics.

### `bixiu.sty`

Route to exactly one layout. `board` and `plain` options must be mutually exclusive.

## 5. Review checklist

- The chapter source contains no forbidden layout commands.
- Figure widths are controlled by the style or figure layer.
- The content layer does not load page-layout packages.
- Board and plain styles define presentation only.
- The same content compiles in every required layout.
- A semantic change is made in the content layer; a visual change is made in the style or figure layer.

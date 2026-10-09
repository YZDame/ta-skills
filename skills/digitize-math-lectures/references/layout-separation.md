# Layout Guidance

Read for reusable styling, board/plain switching, or an existing bixiu project. A short single-output document does not need a custom layout system.

## Ordinary material

Use standard sections, theorem/problem environments, paragraphs, lists, and mathematics. Keep repeated page geometry, fonts, colors, and macros in the preamble or a shared style. Figure widths such as `0.8\linewidth`, inline TikZ, and an occasional deliberate page break are allowed when they improve the result. Avoid absolute placement of every line merely to imitate handwriting.

Workspace defaults: evan-zh for adapted lectures, natoly for compact answer booklets. Existing project styles and manual edits take priority. Split content into subfiles only when useful.

## Optional board/plain architecture

When both layouts are requested or an existing project already uses bixiu, copy the four `.sty.template` assets into the project's styles directory:

- bixiu-content.sty: shared mathematical/semantic environments and figure API;
- bixiu-board.sty: board geometry, columns, and presentation;
- bixiu-plain.sty: plain layout and annotation presentation;
- bixiu.sty: router selecting exactly one layout.

Keep page-layout packages in the layout layer and mathematical content in the shared layer. Shared chapters use `\fig{page}{figure}`, `aside`, and optional source-page comments. Board-specific figure scales can live in figures-board-scales.tex. This arrangement supports switching without rewriting chapters; it is not a prerequisite for all board transcription.

Build the layouts requested by the user. A retained switch or an available template is not a request to produce every version. Do not migrate an existing boardpage/boardcolumn document solely to match this architecture.

## Check the result

Inspect formulas, pagination, columns, figure proximity, and labels in each requested output. Fix actual readability defects and compilation errors. Keep the editable styles and figure sources used in the delivered package; temporary layout experiments and build logs are not required lasting files.

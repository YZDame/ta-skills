# Project and Retention Contract

Use this reference for larger projects or compatibility with existing manifests. A small task needs original sources, final editable materials, and a clear review status; a manifest and staged records are optional.

## Editing and presentation

The editing task is faithful transcription, solution editing, or lecture adaptation, as defined in SKILL.md. Legacy profile names remain accepted; they do not force a directory tree or multiple outputs. Choose board/plain layout, exam grouping, and answer hiding independently from the editing task.

## Optional state tracking

Existing projects may retain `NEW -> EXTRACTED -> MERGED -> REVIEW_REQUIRED -> APPROVED`:

- NEW: sources are being collected.
- EXTRACTED: source text has been recovered sufficiently for editing.
- MERGED: content is assembled and uncertainties identified.
- REVIEW_REQUIRED: a draft is ready for mathematical and visual review.
- APPROVED: the user or an authorized reviewer has confirmed the material.

Hashes, raw OCR records, figure manifests, and four separate component-review fields are not prerequisites for these states. Do not infer approval from a successful build or a project's location under lectures/. If no manifest is needed, communicate review status and unresolved issues in the handoff.

## Lasting files

Retain originals under sources/ and final materials: main/subfile TeX, PDFs, editable TSQX/Asymptote/TikZ/PGFPlots or native drawing sources, and the styles, images, data, and figure PDFs required to rebuild them. Preserve SyncTeX when required by the workspace. Keep the delivered drawing chain editable, including generated .asy paired with .tsqx when used.

Sources remain immutable. Human-edited documents and figure code must never be overwritten by extraction or bulk generation. Keep current-run machine candidates in extraction/ while processing.

## Temporary files

OCR payloads, rendered source pages, merged text, review records, manifests, superseded pilots, and build caches need not be retained after delivery. Existing manifests may be kept for compatibility; new ones are optional. A temporary review note that describes an unresolved mathematical issue must remain available until that issue is resolved or captured in retained source comments and the handoff.

Clean only identified current-run intermediates after inspecting the finished PDF and build dependencies. Never remove originals, manually edited files, or required drawing/build dependencies. This policy does not authorize retroactive cleanup of existing projects. Do not delete unfamiliar files by extension or run blanket repository cleanup.

## Optional manifest

Use assets/manifest.example.yaml only when a long-running or multi-source project benefits from persisted configuration. Record the source paths, selected editing task, output paths, template, review state, and unresolved issues that are actually useful; omit unused fields. Legacy schema fields can remain without requiring their old directory or retention policy.

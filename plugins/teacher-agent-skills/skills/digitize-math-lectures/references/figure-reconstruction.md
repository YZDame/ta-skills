# Mathematical Figure Recovery and Vector Reconstruction

## 1. Core principle

A mathematical figure contains mathematical semantics, teaching purpose, and visual expression. Recover the first two before choosing how to render the third. Pixel similarity with incorrect mathematics fails; a mathematically correct figure that omits essential labels or color semantics also fails.

## 2. Figure sources

The manifest accepts three origins:

1. `source_crop`: a region automatically cropped by OCR or layout analysis;
2. `full_page_recovered`: a figure found during full-page inspection that OCR missed;
3. `newly_authored`: a figure added to support a newly organized lecture.

After automatic cropping, inspect the full page again. Record the page, bounding box, surrounding text, caption, nearby formulas, and left/right column location. An isolated crop is usually insufficient to recover mathematical meaning.

## 3. Initial classification

Classify every candidate as one of:

- `false_crop`: binding edge, highlighter mark, stain, isolated page number, or meaningless fragment;
- `math_diagram`: geometry, function, number line, statistics, set, flowchart, table, or another structured diagram;
- `content_bitmap`: photograph, screenshot, textured image, or illustration unsuitable for redrawing;
- `ambiguous`: object or relationship cannot yet be determined from context or resolution;
- `new_figure_request`: a figure required by the teaching structure but absent from the source.

Reject `false_crop`. Do not force `content_bitmap` or `ambiguous` candidates into vector form.

## 4. Semantic specification

Write a `semantic_spec` before reconstructing any figure. YAML or JSON is recommended. Include at least:

```yaml
id: fig-01
category: math_diagram
origin: source_crop
role: geometric relation in an example
objects:
  - A
  - B
relations:
  - "A, O, and B are collinear"
  - "CD is perpendicular to AB"
labels:
  - A
  - B
ambiguities:
  - "The source does not establish whether D lies on segment AB"
renderer: TSQX
```

The specification must answer:

- What objects are present?
- Which relationships are stated by the problem, prose, or formulas?
- Which visual features are merely handwriting and must not become mathematical conditions?
- What do labels, arrows, shading, and colors mean?
- What is the figure's teaching purpose?
- What still requires human confirmation?

## 5. Visual-model assistance

When authorization permits, a vision model may inspect the crop and full page and propose objects, relationships, visible labels, a figure category, ambiguities, and a renderer. Do not let a model jump directly from image to final TikZ while bypassing semantic review. Check every proposal against the problem statement, body text, and full-page structure. Textual conditions take priority over image proportions.

## 6. Renderer selection

| Figure type | Preferred renderer | Reason |
|---|---|---|
| Plane or olympiad geometry | TSQX | Describes mathematical objects and constraints directly |
| Functions, coordinate graphs, statistical curves | PGFPlots / TikZ | Domains, expressions, ranges, and key points are verifiable |
| Number lines, set diagrams, symbol tables, flowcharts, tables | TikZ | Direct structural and layout control |
| Solid geometry, complex analytic diagrams, 3D projections | Asymptote | Reliable three-dimensional and analytic expression |
| Photos, real objects, textured images, software screenshots | Bitmap | Vectorization has low benefit and may alter information |

A figure may combine tools, but keep one primary editable source entry point. Do not use TikZ for every figure merely because it is familiar.

## 7. Generation and standalone compilation

1. Generate source from the reviewed semantic specification.
2. Use stable, readable object names. Centralize colors, line widths, and font sizes.
3. For function graphs, state the expression, domain, coordinate range, sampling, and key points.
4. For geometry, state dependencies. Decorative offsets must not change mathematical conditions.
5. Compile every figure separately to a PDF or SVG preview before integrating it into the lecture.
6. Store source, preview, build log, and semantic specification in corresponding locations.

## 8. Mathematical checks

Check according to type:

- geometry: point-line-plane relationships, intersection order, parallelism, perpendicularity, equal lengths and angles, tangency, and label ownership;
- function graph: expression, domain, range, monotonicity, parity, asymptotes, intercepts, key points, and branches;
- number line or set diagram: endpoint openness, direction, intervals, union/intersection/complement, and shading range;
- statistical graphic: variables, units, scales, counts or frequencies, legend, and data mapping;
- table or flowchart: row and column meaning, arrow direction, branching conditions, and reading order;
- solid geometry: occlusion, dashed and solid edges, projections, and hidden boundaries.

Record results in `math_checks`. “Looks consistent” is not a mathematical check.

## 9. Visual and pedagogical checks

For visual fidelity:

- compare object count, relative position, labels, color semantics, and body-text references against the source;
- use clean mathematical graphics without imitating handwriting noise or arbitrary placement;
- preserve every object, relationship, label, and color meaning established by the text or problem;
- retain a note when the source itself is questionable.

For teaching value:

- confirm that the figure helps explain the current definition, derivation, or example;
- remove decoration that carries no information;
- keep colors, line styles, and labels consistent across related figures;
- split complex explanations into multiple teaching-stage figures when one figure would overload the reader.

Record whether acceptance used source comparison, pedagogical review, or both.

## 10. Failure handling

- Unreadable text or formula: retain the crop, mark the exact uncertainty, and request human confirmation.
- Relationship visible only faintly in the image: do not invent it; record it under `ambiguities`.
- Renderer cannot express the figure: change renderer or retain a bitmap; do not trade mathematical correctness for format uniformity.
- Visual similarity passes but mathematical checks fail: return to semantic specification.
- Mathematics passes but labels are unreadable or disconnected after integration: return to layout review.

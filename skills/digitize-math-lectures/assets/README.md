# Layout Templates and Project Examples

This directory provides optional templates for reusable content and layout. Use the selected editing task and requested outputs; existing profiles remain compatible and project.yaml is optional. See [../references/layout-separation.md](../references/layout-separation.md) and [../SKILL.md](../SKILL.md).

| Profile | Default template | Main-entry example | Multiple layouts |
|---|---|---|---|
| `board-digitization` | `tex/styles/bixiu.sty` (content + board + plain) | `main-board.example.tex` | Only when both are requested |
| `lecture-authoring` | `templates/evan-zh/evan.sty` | `main-evan.example.tex` | No: one layout is sufficient |
| `hybrid` | Choose by dominant component | Either example | As required |
| `exam-answer-digitization` | User-selected exam style; workspace reference: `templates/TST/natoly.sty` | `tex/main.tex` | Student version only when requested |
| `olympiad-solution-digitization` | Compact answer style; workspace recommendation: `templates/TST/natoly.sty` | `tex/main.tex` | Student version only when requested |

## Files

- `bixiu-content.sty.template`: shared layer for board digitization;
- `bixiu-board.sty.template`: landscape, two-column board layout;
- `bixiu-plain.sty.template`: A4, single-column plain layout;
- `bixiu.sty.template`: router selected by `layout=board` or `layout=plain`;
- `main-board.example.tex`: board-digitization main entry;
- `main-evan.example.tex`: lecture-authoring main entry;
- `manifest.example.yaml`: `project.yaml` field example;
- `board-landscape-two-column.sty`: legacy hybrid package for historical comparison only.

## Board digitization

Copy the four bixiu templates into a project's `tex/styles/` directory. Chapter files use `\\fig{page}{figure}`, `aside`, and source-page comments. Figure widths belong in `figures/sources/figures-board-scales.tex`. Compile the requested layouts.

## Lecture authoring

Load `templates/evan-zh/evan.sty` or a project-local copy. Chapter files use its theorem, problem, solution, and figure APIs. Board-only APIs are disabled for this profile.

## Competition solutions

For `olympiad-solution-digitization`, use optional working records for difficult problems and split printable groups only when useful. The final body uses `题目`, optional `思路`, and `解答` or `证明`; processing notes remain outside the document. Read [../references/olympiad-solution-profile.md](../references/olympiad-solution-profile.md) before drafting. The user-selected template (or optional manifest) selects the style package, so `natoly.sty` is a workspace recommendation rather than a required dependency.

## Verification

Each requested output must compile without errors, missing glyphs/references, or readability defects; harmless Underfull warnings do not block delivery. Compile to the appropriate build directory and inspect the rendered pages before approval.

The legacy `scripts/build_and_check.zsh` helper still runs two XeLaTeX passes and defaults to both layouts for `--profile board-digitization`. It is optional; use latexmk directly or pass `--layouts main` when only the main output is requested. Its defaults do not impose delivery requirements.

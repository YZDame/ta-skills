# Layout Templates and Project Examples

This directory provides templates that enforce strict separation between content and layout. The default template is selected by `profile`, and users may override it explicitly in `project.yaml.template`. See [../references/layout-separation.md](../references/layout-separation.md) and [../SKILL.md](../SKILL.md).

| Profile | Default template | Main-entry example | Multiple layouts |
|---|---|---|---|
| `board-digitization` | `tex/styles/bixiu.sty` (content + board + plain) | `main-board.example.tex` | Yes: `build/current` and `build/plain` |
| `lecture-authoring` | `templates/evan-zh/evan.sty` | `main-evan.example.tex` | No: one layout is sufficient |
| `hybrid` | Choose by dominant component | Either example | As required |

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

Copy the four bixiu templates into a project's `tex/styles/` directory. Chapter files use `\\fig{page}{figure}`, `aside`, and source-page comments. Figure widths belong in `figures/sources/figures-board-scales.tex`. Compile both board and plain layouts.

## Lecture authoring

Load `templates/evan-zh/evan.sty` or a project-local copy. Chapter files use its theorem, problem, solution, and figure APIs. Board-only APIs are disabled for this profile.

## Verification

Each required layout must pass two consecutive XeLaTeX runs without `! ` errors, undefined commands, or newly introduced `Overfull/Underfull` warnings. Compile to the appropriate build directory and inspect the rendered pages before approval.

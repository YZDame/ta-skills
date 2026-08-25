#!/bin/zsh
# Build a digitize-math-lectures project and verify there are no fatal
# errors. Compiles one or two layouts depending on the project profile:
#
#   - board-digitization      -> build both board (current) and plain, gate
#                                 on both passing XeLaTeX twice.
#   - lecture-authoring/hybrid -> build a single layout only.
#
# usage:
#   build_and_check.zsh <tex-file> <build-dir> [--profile <p>]
#                                           [--expected-board <n>] [--expected-plain <n>]
#                                           [--layouts <list>]
#
# Layout list override (comma-separated) default is read from --profile:
#   board-digitization -> "board,plain"
#   otherwise          -> "main"
#
# The plain build is launched by re-entrant \input with \def\LectureLayout{plain}
# rather than editing the main .tex file. Both builds must compile twice
# consecutively without "! " errors.
#
# Overfull/Underfull warnings are reported as soft warnings (counts per log),
# NOT a hard failure — CJK + TikZ projects routinely emit baseline warnings
# from upstream packages. The contract requires "no newly-introduced
# warnings"; a baseline diff is out of scope for this script (the user or
# CI captures the regression baseline separately).

set -euo pipefail

tex_file=""
build_dir=""
profile=""
expected_board=""
expected_plain=""
layouts=""

while (( $# )); do
  case "$1" in
    --profile)        profile="$2"; shift 2 ;;
    --expected-board) expected_board="$2"; shift 2 ;;
    --expected-plain) expected_plain="$2"; shift 2 ;;
    --layouts)        layouts="$2"; shift 2 ;;
    -*) echo "unknown option: $1" >&2; exit 2 ;;
    *)
      if [[ -z "$tex_file" ]];    then tex_file="$1"
      elif [[ -z "$build_dir" ]]; then build_dir="$1"
      else echo "unexpected positional arg: $1" >&2; exit 2
      fi
      shift ;;
  esac
done

if [[ -z "$tex_file" || -z "$build_dir" ]]; then
  echo "usage: $0 <tex-file> <build-dir> [--profile <p>] [--expected-board <n>] [--expected-plain <n>] [--layouts <list>]" >&2
  exit 2
fi

tex_file="${tex_file:A}"
build_dir="${build_dir:A}"
tex_dir="${tex_file:h}"
tex_name="${tex_file:t}"

if [[ -z "$layouts" ]]; then
  case "$profile" in
    board-digitization) layouts="board,plain" ;;
    "") echo "warning: --profile not given; assuming single-layout build" >&2; layouts="main" ;;
    *)  layouts="main" ;;
  esac
fi

mkdir -p "$build_dir/current" "$build_dir/plain"

count_warnings() {
  local log="$1"
  if [[ -f "$log" ]]; then
    rg -c 'Overfull|Underfull' "$log" 2>/dev/null || echo 0
  else
    echo "missing"
  fi
}

run_xelatex() {
  local outdir="$1"; shift
  (cd "$tex_dir" && xelatex -interaction=nonstopmode -halt-on-error \
    -output-directory="$outdir" "$@" >/dev/null)
}

# Board (or main single-layout) build.
board_pdf="$build_dir/current/${tex_name:r}.pdf"
board_log="$build_dir/current/${tex_name:r}.log"

for _ in 1 2; do
  run_xelatex "$build_dir/current" -synctex=1 "$tex_name"
done

if [[ -n "$expected_board" ]]; then
  actual_board="$(pdfinfo "$board_pdf" | awk '/^Pages:/ {print $2}')"
  if [[ "$actual_board" != "$expected_board" ]]; then
    echo "main build: page count mismatch (expected $expected_board, got $actual_board)" >&2
    exit 1
  fi
fi

board_warns="$(count_warnings "$board_log")"
echo "main ok: $board_pdf ($actual_board pages, $board_warns Overfull/Underfull warnings)"

# Plain build only when explicitly requested by --layouts or --profile.
if [[ ",$layouts," == *",plain,"* ]]; then
  plain_job="${tex_name:r}plain"
  plain_pdf="$build_dir/plain/${plain_job}.pdf"
  plain_log="$build_dir/plain/${plain_job}.log"

  for _ in 1 2; do
    (cd "$tex_dir" && xelatex -interaction=nonstopmode -halt-on-error \
      -output-directory="$build_dir/plain" \
      -jobname="$plain_job" \
      '\def\LectureLayout{plain}\input{'"$tex_name"'}' >/dev/null)
  done

  if [[ -n "$expected_plain" ]]; then
    actual_plain="$(pdfinfo "$plain_pdf" | awk '/^Pages:/ {print $2}')"
    if [[ "$actual_plain" != "$expected_plain" ]]; then
      echo "plain build: page count mismatch (expected $expected_plain, got $actual_plain)" >&2
      exit 1
    fi
  fi

  plain_warns="$(count_warnings "$plain_log")"
  echo "plain ok: $plain_pdf ($actual_plain pages, $plain_warns Overfull/Underfull warnings)"
fi
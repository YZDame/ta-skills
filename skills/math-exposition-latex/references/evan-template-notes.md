# Evan template and portable compilation

## Bundled compatible setup

Use assets/textbook-template.tex with assets/evan.sty. This style is Evan Chen's 2019 compatibility version with Chinese environment labels. Its source attribution is retained in the file. It uses thmtools and mdframed and is compatible with the tested TeX Live 2023 environment.

Source: https://github.com/vEnhance/dotfiles/blob/main/texmf/tex/latex/evan/evan-legacy.sty
Style guide: https://web.evanchen.cc/latex-style-guide.html

Copy the style next to the generated main file. Load:

\documentclass[11pt,a4paper,fontset=fandol]{ctexart}
\usepackage[sexy,noasy,noauthor,nofancy]{evan}

Use the provided theorem, lemma, proposition, corollary, definition, example, remark, and exercise environments. Do not redefine them. The document can configure page margins and headers separately. Do not use the legacy `chinese` option; ctexart already handles Unicode Chinese through XeLaTeX.

Check macro names before adding commands: evan.sty already defines several common ones, including norm. Use a unique name or renew an existing macro deliberately.

## Version and dependency selection

Do not call the compatibility version “the latest Evan template”. If the user asks for the current upstream version, retrieve and inspect it: newer versions may use keytheorems/tcolorbox rather than thmtools/mdframed. Select and report a compatible version honestly; do not silently emulate the appearance while claiming to use the package.

Use kpsewhich to inspect ctexart.cls, xeCJK.sty, thmtools.sty, mdframed.sty and other actual dependencies. Detect fonts or use Fandol if present. On macOS, explicit Songti SC/Heiti SC can be chosen if available. Do not assume a repo-specific templates/evan-zh directory exists.

Compile twice with XeLaTeX. Resolve glyph, overflow, and cross-reference issues and visually review the generated PDF. Fandol script warnings alone are not evidence of missing glyphs; inspect actual missing-character diagnostics and rendered pages.

Keep template attribution in delivered sources. Do not include unused Asymptote, VON, or problem-bank integrations. Store temporary TeX distributions and font caches outside the skill; bundle only reusable source assets.

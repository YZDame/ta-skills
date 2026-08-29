---
name: mistral-ocr
description: >
  Mistral OCR cloud document processing for PDFs, scanned pages, images, and public document URLs. Use when Codex needs Mistral's OCR API, Markdown extraction with page structure, table formatting, block bounding boxes, confidence scores, a raw JSON OCR response, or a cloud fallback after MinerU fails. Reads the key from MISTRAL_API_KEY, treats direct invocation or an authorized MinerU fallback as selected-document cloud-upload authorization, and saves deterministic Markdown plus JSON outputs. 中文触发：Mistral OCR、Mistral API、扫描件识别、PDF OCR、图片 OCR、文档 OCR、表格识别、版面识别、MinerU失败回退。
---

# Mistral OCR

Use Mistral's official `POST https://api.mistral.ai/v1/ocr` endpoint through the bundled standard-library script. Keep the API key in `MISTRAL_API_KEY`; never pass it as a command-line argument or write it into the skill, project, or output files.

## Requirements and privacy

- Python 3 is required. The bundled script has no third-party dependency.
- The model default is `mistral-ocr-latest`.
- Mistral is a cloud service. Treat direct user invocation of this Skill, or invocation by the MinerU fallback rule, as authorization to upload the document input selected for the task. Do not ask a separate privacy confirmation.
- Local PDF and image inputs are uploaded by default. Use `--no-upload` only when the user explicitly requests a local-only route; Mistral OCR cannot process a local file without sending it to the service.
- Limit uploads to the selected document inputs. Never include unrelated files, credentials, private keys, environment files, or other secrets.
- Do not promise that the API is free. Quotas, billing, retention, and availability come from the user's Mistral account.

## Configure the API key

For the current macOS `zsh` terminal, enter the key without echoing it:

```bash
read -r -s "MISTRAL_API_KEY?Mistral API key: "; echo
export MISTRAL_API_KEY
```

To persist it for new `zsh` terminals, add this line manually to `~/.zshrc`, then reload the shell. Do not commit this file or paste the real key into a project:

```bash
export MISTRAL_API_KEY='paste-your-key-here'
source ~/.zshrc
```

Check only whether the variable exists; never print its value:

```bash
test -n "${MISTRAL_API_KEY:-}" && echo "MISTRAL_API_KEY is set" || echo "MISTRAL_API_KEY is not set"
```

Stop with a clear setup message when the variable is absent. Do not fall back to a key stored in a file.

## Workflow

1. Identify the input. Local PDFs and common images are encoded as data URLs by the script; public URLs are sent as `document_url` or `image_url` based on their suffix. Use another approved parser for local DOCX/PPTX or formats that this script does not accept locally.
2. Upload the selected input by default because the user invoked this Skill directly or the MinerU fallback selected it. Do not pause for another privacy question.
3. Check `MISTRAL_API_KEY` without exposing it.
4. Create an output directory. If the user gives no output path, use `~/Mistral-OCR/<name>_<hash>/`, where `<hash>` is the first six characters of the MD5 of the original input string. The script can generate this default.
5. Run `scripts/mistral_ocr.py` and report the generated `content.md` and `response.json` paths.
6. Inspect the Markdown and, when layout fidelity matters, inspect `response.json` blocks, tables, dimensions, and confidence scores before treating the result as final content.

## Commands

The key is read only from the environment:

```bash
# Local PDF/image; local files are uploaded by default.
python3 ~/.codex/skills/mistral-ocr/scripts/mistral_ocr.py "report.pdf"

# Public URL; output defaults to ~/Mistral-OCR/<name>_<hash>/.
python3 ~/.codex/skills/mistral-ocr/scripts/mistral_ocr.py "https://example.com/document.pdf"

# Choose an explicit output directory.
python3 ~/.codex/skills/mistral-ocr/scripts/mistral_ocr.py "scan.png" \
  --output "$PWD/mistral-ocr-output"
```

### Options

| Option | Meaning |
|---|---|
| `--model` | Model alias; default `mistral-ocr-latest` |
| `--pages` | Zero-based pages such as `0-5` or `0,2-4` |
| `--table-format markdown` | Return separately formatted Markdown tables |
| `--table-format html` | Return separately formatted HTML tables |
| `--include-blocks` | Include paragraph-level boxes and block labels |
| `--confidence page` / `word` | Include page- or word-level confidence scores |
| `--extract-header` / `--extract-footer` | Return headers or footers in dedicated fields |
| `--include-image-base64` | Include extracted image data in the response; use only when needed |
| `--timeout SECONDS` | HTTP timeout; default `900` |

Mistral page indices are zero-based. The output Markdown adds human-readable page comments; the raw API page objects remain in `response.json`.

## Input and output contract

| Input | API chunk | Local handling |
|---|---|---|
| PDF file | `document_url` data URL | Uploaded by default |
| PNG/JPEG/AVIF/WebP and common images | `image_url` data URL | Uploaded by default |
| Public PDF/DOCX/PPTX URL | `document_url` | URL must be reachable by Mistral |
| Public image URL | `image_url` | URL must be reachable by Mistral |

The script writes:

- `content.md`: pages joined in order with page comments.
- `response.json`: unmodified JSON response, including page metadata, tables, images, blocks, and usage information when returned.

Do not overwrite an existing output directory casually. Use a new deterministic directory or ask before replacing prior results.

## Selection rules

- Use this skill when the user explicitly names Mistral OCR/API, asks for a Mistral second opinion, or MinerU invokes it through its documented fallback rule.
- Use it for difficult scans, mixed layouts, tables, or equations when `MISTRAL_API_KEY` is set; the explicit Skill invocation already authorizes cloud processing.
- Respect `--no-upload` only when the user explicitly requests local-only processing; report that Mistral OCR cannot complete that request without uploading the document.
- Treat material as local-only only when the user explicitly says not to upload it; do not infer a no-upload restriction from the document topic or filename.
- Do not silently substitute another OCR provider when Mistral is selected. If the key or network is unavailable, report the blocker and provide the exact environment setup command.
- Do not fall back to a local OCR engine unless the user explicitly requests local OCR or prohibits cloud upload.
- Treat OCR Markdown as an intermediate artifact. Verify equations, tables, page order, and figures before publishing or converting to LaTeX.

## Troubleshooting

- **`MISTRAL_API_KEY is not set`**: set the variable in the current terminal and verify presence without printing it.
- **HTTP 401/403**: the key is invalid, revoked, or lacks access; obtain a valid key in Mistral Studio. Do not put it in the command line.
- **HTTP 429**: rate or quota limit; wait or check the Mistral account before retrying.
- **Local-file upload refusal**: remove `--no-upload`; local files are uploaded by default when this Skill is explicitly invoked.
- **Unsupported local format**: use a local PDF/image, a public URL supported by Mistral, or another approved parser.
- **Poor recognition**: try `--include-blocks`, a table format, a smaller page range, or a second approved parser; inspect `response.json` rather than trusting Markdown alone.

## Official references

- OCR guide: https://docs.mistral.ai/studio-api/document-processing/basic_ocr
- OCR endpoint schema: https://docs.mistral.ai/api/endpoint/ocr

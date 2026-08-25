#!/usr/bin/env python3
"""Run Mistral OCR with only the Python standard library.

The API key is read from MISTRAL_API_KEY and is never accepted as a CLI
argument. Local PDFs and images are sent to Mistral as base64 data URLs by
default. Public HTTP(S) URLs are passed through to the API. Use --no-upload
only when the caller explicitly requires a local-only route.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


API_URL = "https://api.mistral.ai/v1/ocr"
IMAGE_SUFFIXES = {
    ".avif",
    ".bmp",
    ".gif",
    ".heic",
    ".jpeg",
    ".jpg",
    ".png",
    ".tif",
    ".tiff",
    ".webp",
}


def _is_http_url(value: str) -> bool:
    return urlparse(value).scheme in {"http", "https"}


def _url_suffix(value: str) -> str:
    return Path(urlparse(value).path).suffix.lower()


def _local_document(source: str, allow_upload: bool) -> dict[str, str]:
    path = Path(source).expanduser()
    if not path.is_file():
        raise ValueError(f"Input file does not exist: {path}")
    suffix = path.suffix.lower()
    if suffix != ".pdf" and suffix not in IMAGE_SUFFIXES:
        raise ValueError(
            "Local Mistral OCR input must be a PDF or common image. "
            "Use a public URL for DOCX/PPTX or use another approved parser for local office files."
        )
    if not allow_upload:
        raise ValueError(
            "Mistral OCR requires sending a local file to the service. Remove "
            "--no-upload or use another local-only parser."
        )

    mime_type = mimetypes.guess_type(path.name)[0]
    if not mime_type:
        mime_type = "application/pdf" if suffix == ".pdf" else "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    if suffix == ".pdf":
        return {"type": "document_url", "document_url": f"data:{mime_type};base64,{encoded}"}
    return {"type": "image_url", "image_url": f"data:{mime_type};base64,{encoded}"}


def _document_for_input(source: str, allow_upload: bool) -> dict[str, str]:
    if _is_http_url(source):
        if _url_suffix(source) in IMAGE_SUFFIXES:
            return {"type": "image_url", "image_url": source}
        return {"type": "document_url", "document_url": source}
    return _local_document(source, allow_upload)


def _safe_name(source: str) -> str:
    if _is_http_url(source):
        raw_name = Path(urlparse(source).path).stem
    else:
        raw_name = Path(source).expanduser().stem
    raw_name = raw_name or "document"
    safe_name = re.sub(r"[^0-9A-Za-z_.\-\u4e00-\u9fff]+", "_", raw_name)
    safe_name = re.sub(r"_+", "_", safe_name).strip("_") or "document"
    digest = hashlib.md5(source.encode("utf-8")).hexdigest()[:6]
    return f"{safe_name}_{digest}"


def _default_output(source: str) -> Path:
    return Path.home() / "Mistral-OCR" / _safe_name(source)


def _build_payload(args: argparse.Namespace, document: dict[str, str]) -> dict:
    payload = {
        "model": args.model,
        "document": document,
        "include_blocks": args.include_blocks,
    }
    if args.pages:
        payload["pages"] = args.pages
    if args.table_format:
        payload["table_format"] = args.table_format
    if args.confidence_scores_granularity:
        payload["confidence_scores_granularity"] = args.confidence_scores_granularity
    if args.include_image_base64:
        payload["include_image_base64"] = True
    if args.extract_header:
        payload["extract_header"] = True
    if args.extract_footer:
        payload["extract_footer"] = True
    return payload


def _request_ocr(api_key: str, payload: dict, timeout: int) -> dict:
    request = Request(
        API_URL,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            raw = response.read()
    except HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace").strip()
        if len(detail) > 2000:
            detail = detail[:2000] + "..."
        raise RuntimeError(f"Mistral OCR HTTP {error.code}: {detail}") from error
    except URLError as error:
        raise RuntimeError(f"Mistral OCR network error: {error.reason}") from error

    try:
        result = json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError as error:
        raise RuntimeError("Mistral OCR returned invalid JSON") from error
    if not isinstance(result, dict):
        raise RuntimeError("Mistral OCR returned a JSON value instead of an object")
    return result


def _write_outputs(output_dir: Path, result: dict) -> tuple[Path, Path, int]:
    output_dir.mkdir(parents=True, exist_ok=True)
    response_path = output_dir / "response.json"
    markdown_path = output_dir / "content.md"
    response_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    pages = result.get("pages")
    if not isinstance(pages, list):
        raise RuntimeError("Mistral OCR response does not contain a pages array")
    markdown_parts = []
    for position, page in enumerate(pages):
        if not isinstance(page, dict):
            continue
        page_index = page.get("index", position)
        try:
            display_index = int(page_index) + 1
        except (TypeError, ValueError):
            display_index = position + 1
        markdown = page.get("markdown") or ""
        markdown_parts.append(f"<!-- Page {display_index} -->\n\n{markdown}".strip())
    markdown_path.write_text(
        "\n\n".join(markdown_parts) + ("\n" if markdown_parts else ""),
        encoding="utf-8",
    )
    return markdown_path, response_path, len(pages)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run Mistral OCR and save Markdown plus the raw JSON response."
    )
    parser.add_argument("input", help="Local PDF/image or public HTTP(S) document URL")
    parser.add_argument("-o", "--output", type=Path, help="Output directory")
    parser.add_argument(
        "--allow-upload",
        action="store_true",
        help="Deprecated compatibility flag; local files are uploaded by default",
    )
    parser.add_argument(
        "--no-upload",
        action="store_true",
        help="Refuse to send a local file to Mistral",
    )
    parser.add_argument("--model", default="mistral-ocr-latest", help="Mistral OCR model alias")
    parser.add_argument("--pages", help="Zero-based pages, for example 0-5 or 0,2-4")
    parser.add_argument("--table-format", choices=("markdown", "html"))
    parser.add_argument("--include-blocks", action="store_true", help="Include block bounding boxes and labels")
    parser.add_argument("--include-image-base64", action="store_true")
    parser.add_argument("--confidence", dest="confidence_scores_granularity", choices=("page", "word"))
    parser.add_argument("--extract-header", action="store_true")
    parser.add_argument("--extract-footer", action="store_true")
    parser.add_argument("--timeout", type=int, default=900, help="HTTP timeout in seconds")
    return parser


def main() -> int:
    parser = _parser()
    args = parser.parse_args()
    api_key = os.environ.get("MISTRAL_API_KEY", "").strip()
    if not api_key:
        parser.error("MISTRAL_API_KEY is not set; export it in the terminal before using Mistral OCR")
    if args.timeout <= 0:
        parser.error("--timeout must be a positive integer")
    if args.allow_upload and args.no_upload:
        parser.error("--allow-upload and --no-upload cannot be used together")

    try:
        document = _document_for_input(args.input, not args.no_upload)
        result = _request_ocr(api_key, _build_payload(args, document), args.timeout)
        output_dir = args.output.expanduser() if args.output else _default_output(args.input)
        markdown_path, response_path, page_count = _write_outputs(output_dir, result)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"Mistral OCR failed: {error}", file=sys.stderr)
        return 1

    print(f"Mistral OCR complete: {page_count} page(s)")
    print(f"Markdown: {markdown_path}")
    print(f"JSON: {response_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

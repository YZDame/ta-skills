#!/usr/bin/env python3
"""Assemble chunked PaddleOCR output into one page-addressable project."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


PAGE_RE = re.compile(r"<!-- page: (\d{3}) -->")
IMAGE_RE = re.compile(r'src="imgs/([^"]+)"')
CHUNK_RE = re.compile(r"pages-(\d{3})-(\d{3})\.pdf$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("ocr_root", type=Path)
    parser.add_argument("project_root", type=Path)
    return parser.parse_args()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def split_pages(markdown: str) -> list[tuple[int, str]]:
    matches = list(PAGE_RE.finditer(markdown))
    pages: list[tuple[int, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(markdown)
        pages.append((int(match.group(1)), markdown[match.start():end].strip() + "\n"))
    return pages


def main() -> int:
    args = parse_args()
    page_dir = args.project_root / "extraction" / "ocr" / "pages"
    chunk_dir = args.project_root / "extraction" / "ocr" / "chunks"
    figure_root = args.project_root / "figures" / "source-images"
    inventory_path = args.project_root / "figures" / "inventory" / "inventory.json"
    for directory in (page_dir, chunk_dir, figure_root, inventory_path.parent):
        directory.mkdir(parents=True, exist_ok=True)

    runs: list[tuple[int, int, Path, dict]] = []
    for metadata_path in args.ocr_root.glob("*/metadata.json"):
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        source_path = Path(metadata["source"]["path"])
        match = CHUNK_RE.search(source_path.name)
        if not match:
            continue
        runs.append((int(match.group(1)), int(match.group(2)), metadata_path.parent, metadata))
    runs.sort()

    inventory: list[dict] = []
    merged_pages: list[str] = []
    seen_pages: set[int] = set()
    for chunk_start, chunk_end, run_dir, metadata in runs:
        markdown_path = run_dir / "output.md"
        markdown = markdown_path.read_text(encoding="utf-8")
        shutil.copy2(markdown_path, chunk_dir / f"pages-{chunk_start:03d}-{chunk_end:03d}.md")
        local_pages = split_pages(markdown)
        expected = chunk_end - chunk_start + 1
        if len(local_pages) != expected:
            raise RuntimeError(f"{run_dir.name}: expected {expected} pages, found {len(local_pages)}")
        for local_page, page_text in local_pages:
            global_page = chunk_start + local_page - 1
            if global_page in seen_pages:
                raise RuntimeError(f"duplicate global page {global_page}")
            seen_pages.add(global_page)
            page_figure_dir = figure_root / f"page-{global_page:03d}"
            page_figure_dir.mkdir(parents=True, exist_ok=True)
            names = IMAGE_RE.findall(page_text)
            for name in names:
                source = run_dir / "assets" / "imgs" / name
                if not source.exists():
                    raise FileNotFoundError(source)
                target = page_figure_dir / name
                shutil.copy2(source, target)
                inventory.append(
                    {
                        "id": f"p{global_page:03d}-{target.stem}",
                        "page": global_page,
                        "filename": name,
                        "path": str(target.relative_to(args.project_root)),
                        "sha256": sha256(target),
                        "status": "PENDING_VECTOR_REVIEW",
                    }
                )
            page_for_file = PAGE_RE.sub(f"<!-- page: {global_page:03d} -->", page_text, count=1)
            page_for_file = IMAGE_RE.sub(
                lambda match: f'src="../../../figures/source-images/page-{global_page:03d}/{match.group(1)}"',
                page_for_file,
            )
            (page_dir / f"page-{global_page:03d}.md").write_text(page_for_file, encoding="utf-8")
            merged_page = IMAGE_RE.sub(
                lambda match: f'src="../../figures/source-images/page-{global_page:03d}/{match.group(1)}"',
                PAGE_RE.sub(f"<!-- page: {global_page:03d} -->", page_text, count=1),
            )
            merged_pages.append(merged_page.rstrip())

    if not runs:
        raise RuntimeError(f"no PaddleOCR runs found under {args.ocr_root}")
    expected_pages = set(range(runs[0][0], runs[-1][1] + 1))
    if seen_pages != expected_pages:
        raise RuntimeError(f"page coverage mismatch: {sorted(seen_pages)}")
    (args.project_root / "extraction" / "ocr" / "text.md").write_text(
        "\n\n".join(merged_pages) + "\n", encoding="utf-8"
    )
    inventory_path.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({"pages": len(seen_pages), "figures": len(inventory)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

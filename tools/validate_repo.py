#!/usr/bin/env python3
"""Validate local Markdown links, images, manifests, and GitHub size limits."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^]]*\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[[^]]*\]\(([^)]+)\)")


def local_target(markdown: Path, raw: str) -> Path | None:
    target = raw.strip().split("#", 1)[0]
    if not target or target.startswith(("http://", "https://", "mailto:")):
        return None
    return (markdown.parent / unquote(target)).resolve()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo_root", nargs="?", default=".", type=Path)
    args = parser.parse_args()
    root = args.repo_root.resolve()
    errors, warnings = [], []
    markdown_files = list(root.rglob("*.md"))
    image_count = 0
    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = local_target(markdown, raw)
            if target is not None and not target.exists():
                errors.append(f"broken local link: {markdown.relative_to(root)} -> {raw}")
        for raw in IMAGE_RE.findall(text):
            target = local_target(markdown, raw)
            if target is not None:
                image_count += 1
                if target.suffix.lower() not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
                    warnings.append(f"unusual image type: {target}")
    files = [path for path in root.rglob("*") if path.is_file() and ".git" not in path.parts]
    for path in files:
        if path.stat().st_size >= 100 * 1024 * 1024:
            errors.append(f"GitHub hard-limit file: {path.relative_to(root)}")
        elif path.stat().st_size >= 50 * 1024 * 1024:
            warnings.append(f"large file: {path.relative_to(root)}")
    manifests = list(root.glob("classes/*/sources/source-map.json"))
    mapped_images = 0
    for manifest in manifests:
        data = json.loads(manifest.read_text(encoding="utf-8"))
        mapped_images += len(data["images"])
        for item in data["images"]:
            if not (root / item["repo_image"]).is_file():
                errors.append(f"missing mapped image: {item['repo_image']}")
    result = {
        "status": "PASS" if not errors else "FAIL",
        "markdown_files": len(markdown_files),
        "files": len(files),
        "image_references": image_count,
        "source_manifests": len(manifests),
        "mapped_images": mapped_images,
        "errors": errors,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

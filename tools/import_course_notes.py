#!/usr/bin/env python3
"""Extract per-class note increments and referenced images from cumulative Markdown."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


CLASS_SPECS = [
    ("2026-04-18-Class01", "2026-04-18-Class01", 15, None),
    ("2026-04-25-Class02", "2026-04-25-Class02", 66, None),
    ("2026-05-09-Class03", "2026-05-09-Class03", 68, 111),
    ("2026-05-16-Class04", "2026-05-16-Class04", 165, None),
    ("2026-05-23-Class05", "2026-05-23-Class05", 202, None),
    ("2026-05-30-Class06", "2026-05-30-Class06", 225, None),
    ("2026-06-06-Class07", "2026-06-06-Class07", 269, None),
    ("2026-06-13-Class08", "2026-06-13-Class08", 284, None),
]

IMAGE_RE = re.compile(r"!\[([^]]*)\]\(([^)]+)\)")
IMAGE_NUMBER_RE = re.compile(r"image(\d+)\.", re.IGNORECASE)


def word_image_paragraphs(docx: Path) -> dict[int, int]:
    """Map image occurrence number to 1-based Word paragraph number."""
    ns = {
        "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    }
    result: dict[int, int] = {}
    with zipfile.ZipFile(docx) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    occurrence = 0
    for paragraph_number, paragraph in enumerate(root.findall(".//w:body/w:p", ns), start=1):
        for _ in paragraph.findall(".//a:blip", ns):
            occurrence += 1
            result[occurrence] = paragraph_number
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_markdown(source_root: Path, source_dir: str) -> Path:
    matches = list((source_root / "Markdown" / source_dir).glob("*.md"))
    if len(matches) != 1:
        raise RuntimeError(f"Expected one Markdown file in {source_dir}, got {len(matches)}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("repo_root", type=Path)
    args = parser.parse_args()

    source_root = args.source_root.resolve()
    repo_root = args.repo_root.resolve()
    summary = []

    for class_dir, source_dir, start_line, end_line in CLASS_SPECS:
        source_md = find_markdown(source_root, source_dir)
        word_files = [p for p in (source_root / source_dir).glob("*.docx") if not p.name.startswith("~$")]
        if len(word_files) != 1:
            raise RuntimeError(f"Expected one source Word file in {source_dir}, got {len(word_files)}")
        source_word = word_files[0]
        word_paragraphs = word_image_paragraphs(source_word)
        lines = source_md.read_text(encoding="utf-8-sig").splitlines()
        selected = lines[start_line - 1 : end_line]
        destination = repo_root / "classes" / class_dir
        assets_dir = destination / "assets"
        sources_dir = destination / "sources"
        assets_dir.mkdir(parents=True, exist_ok=True)
        sources_dir.mkdir(parents=True, exist_ok=True)
        for stale in assets_dir.glob("source-*"):
            if stale.is_file():
                stale.unlink()

        mappings = []
        redactions = []
        output_lines = []
        for line_number, line in enumerate(selected, start=start_line):
            if "教師:" in line or "教師：" in line:
                redactions.append({"source_line": line_number, "reason": "teacher-name-publication-disabled"})
                line = "- 教師：不公開（依專案公開設定隱去）"
            def replace_image(match: re.Match[str]) -> str:
                alt, relative = match.groups()
                original = (source_md.parent / relative).resolve()
                if not original.is_file():
                    raise FileNotFoundError(original)
                dest_name = f"source-{original.name}"
                copied = assets_dir / dest_name
                shutil.copy2(original, copied)
                number_match = IMAGE_NUMBER_RE.search(original.name)
                image_number = int(number_match.group(1)) if number_match else None
                mappings.append({
                    "source_word": str(source_word.relative_to(source_root)).replace("\\", "/"),
                    "source_word_paragraph": word_paragraphs.get(image_number) if image_number else None,
                    "source_markdown": str(source_md.relative_to(source_root)).replace("\\", "/"),
                    "source_line": line_number,
                    "source_image": str(original.relative_to(source_root)).replace("\\", "/"),
                    "repo_image": str(copied.relative_to(repo_root)).replace("\\", "/"),
                    "sha256": sha256(copied),
                    "bytes": copied.stat().st_size,
                })
                return f"![{alt}](../assets/{dest_name})"

            output_lines.append(IMAGE_RE.sub(replace_image, line))

        header = [
            f"# {class_dir} 原始增量筆記",
            "",
            "> 本檔由累積式課堂筆記依日期／主題邊界擷取，僅做圖片路徑改寫；文字保留原貌供追溯。",
            f"> 來源：`{source_md.relative_to(source_root).as_posix()}` 第 {start_line}–{end_line or len(lines)} 行。",
            "",
        ]
        (sources_dir / "original-notes.md").write_text(
            "\n".join(header + output_lines).rstrip() + "\n", encoding="utf-8"
        )
        manifest = {
            "class": class_dir,
            "source_markdown": str(source_md.relative_to(source_root)).replace("\\", "/"),
            "source_word": str(source_word.relative_to(source_root)).replace("\\", "/"),
            "source_line_start": start_line,
            "source_line_end": end_line or len(lines),
            "images": mappings,
            "redactions": redactions,
        }
        (sources_dir / "source-map.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        summary.append({"class": class_dir, "lines": len(selected), "images": len(mappings)})

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

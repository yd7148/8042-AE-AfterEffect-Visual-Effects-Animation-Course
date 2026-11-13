#!/usr/bin/env python3
"""Copy selected learner AEP practice files and write a provenance inventory."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path


SELECTIONS = {
    "2026-04-25-Class02": ["2026-04-25-1.aep", "2026-04-25-2.aep", "0425-text graphy Motion.aep"],
    "2026-05-09-Class03": ["2026-05-09-class03-1.aep", "2026-05-09-class03-2.aep", "2026-05-09-class03-3.aep", "2026-05-09-class03-4.aep"],
    "2026-05-16-Class04": ["01-教材-0516/0516.aep", "01-教材-0516/0516-2.aep", "01-教材-0516/2026-05-16-2.aep"],
    "2026-05-23-Class05": ["20260523-1.aep", "20260523-2-下午.aep", "20260523-3-下午.aep"],
    "2026-05-30-Class06": ["20260530-1-下午.aep", "20260530-4-上午.aep"],
    "2026-06-06-Class07": ["0606_adidas_glossy_.aep", "20260606-2-下午.aep"],
    "2026-06-13-Class08": ["2026-06-13-1-上午.aep", "2026-06-13-2-下午.aep", "01-物理彈跳節奏/物理節奏彈跳碰撞.aep", "Fashion Slideshow/Alpha matte.aep", "GLOW LIGHT/GLOW LIGHT.aep"],
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("repo_root", type=Path)
    args = parser.parse_args()
    source_root, repo_root = args.source_root.resolve(), args.repo_root.resolve()
    all_rows = []
    for class_name, relative_paths in SELECTIONS.items():
        output_dir = repo_root / "classes" / class_name / "aep"
        output_dir.mkdir(parents=True, exist_ok=True)
        for stale in output_dir.glob("*.aep"):
            stale.unlink()
        class_rows = []
        for relative in relative_paths:
            source = source_root / class_name / Path(relative)
            if not source.is_file():
                raise FileNotFoundError(source)
            destination = output_dir / source.name
            shutil.copy2(source, destination)
            row = {
                "class": class_name,
                "source": f"{class_name}/{relative}",
                "repo_path": destination.relative_to(repo_root).as_posix(),
                "bytes": destination.stat().st_size,
                "sha256": digest(destination),
                "kind": "practice-process" if any(token in source.stem.lower() for token in ("-1", "-2", "-3", "-4", "上午", "下午")) else "reference-or-final",
                "dependency_status": "not_embedded-audit-required",
            }
            class_rows.append(row)
            all_rows.append(row)
        (output_dir / "manifest.json").write_text(json.dumps(class_rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    report = {"count": len(all_rows), "bytes": sum(row["bytes"] for row in all_rows), "files": all_rows}
    (repo_root / "docs" / "aep-inventory.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"count": report["count"], "bytes": report["bytes"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

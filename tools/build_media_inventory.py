#!/usr/bin/env python3
"""Build a deduplicated inventory of the user's course media folders.

The inventory is consumed by both the release-upload script and the static
catalog-page generator, so uploaded asset names and catalog links always match.
"""
from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from pathlib import Path

BASE = Path("D:/Educational Courses")
OUT = Path(__file__).resolve().parent / "media_inventory.json"

SOURCES = [
    ("mfg", BASE / "Fundamentals of Mordern Manufacturing"),
    ("lean", BASE / "Lean Manufacturing"),
    ("cnc", BASE / "CNC Machine"),
    ("mech", BASE / "Mechanical Engineering"),
    ("draw", BASE / "Mechanical Drawing"),
]

COLLECTIONS = {
    "mfg": {
        "en": "Fundamentals of Modern Manufacturing",
        "vi": "Cơ sở Chế tạo Hiện đại",
        "note_en": "Core manufacturing processes, forming, welding, plastics, metrology and automation.",
        "note_vi": "Các quy trình chế tạo cơ bản: tạo hình, hàn, chất dẻo, đo kiểm và tự động hóa.",
    },
    "lean": {
        "en": "Lean Manufacturing",
        "vi": "Sản xuất Tinh gọn (Lean)",
        "note_en": "Kaizen, value stream mapping, kanban, setup reduction, visual control and lean culture.",
        "note_vi": "Kaizen, bản đồ dòng giá trị, kanban, giảm thời gian chuyển máy và văn hóa Lean.",
    },
    "cnc": {
        "en": "CNC Machines & References",
        "vi": "Máy CNC & Tài liệu tham khảo",
        "note_en": "CNC operation, maintenance and handbooks; includes the Fundamentals of Tool Design videos.",
        "note_vi": "Vận hành, bảo trì máy CNC và sổ tay; gồm cả video Fundamentals of Tool Design.",
    },
    "tool": {
        "en": "Fundamentals of Tool Design",
        "vi": "Cơ sở Thiết kế Dụng cụ",
        "note_en": "Fixture, die, gaging and cutting-tool design; rapid and composite tooling.",
        "note_vi": "Thiết kế đồ gá, khuôn, dụng cụ đo và dụng cụ cắt; khuôn nhanh và composite.",
    },
    "mech": {
        "en": "Mechanical Engineering",
        "vi": "Kỹ thuật Cơ khí",
        "note_en": "Machine design, machine elements, manufacturing handbooks, turbomachinery and exam references.",
        "note_vi": "Thiết kế máy, chi tiết máy, sổ tay chế tạo, tuốc bin và tài liệu ôn thi.",
    },
    "draw": {
        "en": "Mechanical Drawing",
        "vi": "Bản vẽ Cơ khí",
        "note_en": "Engineering drawing, blueprint reading, technical handouts and fastener drawings.",
        "note_vi": "Bản vẽ kỹ thuật, đọc bản vẽ sản xuất, tài liệu hướng dẫn và bản vẽ ren.",
    },
}

EXCLUDE_DIR_NAMES = {"machine-ctm.github.io", ".git", "__pycache__"}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def collection_for(path: Path) -> str:
    parts = {p.lower() for p in path.parts}
    if "fundamentals of tool design" in parts:
        return "tool"
    for key, root in SOURCES:
        if str(path).startswith(str(root)):
            return key
    return "mfg"


def main() -> None:
    candidates: list[tuple[str, Path, Path]] = []
    for key, root in SOURCES:
        if not root.is_dir():
            raise SystemExit(f"Missing source folder: {root}")
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.suffix.lower() not in {".mp4", ".pdf", ".ppt", ".pptx"}:
                continue
            if EXCLUDE_DIR_NAMES.intersection(p.lower() for p in path.parts):
                continue
            candidates.append((key, root, path))

    seen_hashes: dict[str, str] = {}
    items = []
    duplicates = []
    used_slugs: set[str] = set()

    for _key, root, path in candidates:
        digest = sha256(path)
        rel = path.relative_to(root).as_posix()
        if digest in seen_hashes:
            duplicates.append({"source": str(path), "duplicate_of": seen_hashes[digest]})
            continue
        seen_hashes[digest] = str(path)

        coll = collection_for(path)
        prefix = "cnc-tool" if coll == "tool" else coll
        stem = Path(rel).stem
        slug = f"{prefix}-{slugify(stem)}{path.suffix.lower()}"
        if slug in used_slugs:
            slug = f"{slug[:-len(path.suffix)]}-2{path.suffix.lower()}"
        used_slugs.add(slug)

        items.append(
            {
                "collection": coll,
                "title": stem,
                "source": str(path),
                "source_label": f"{root.name}/{rel}",
                "slug": slug,
                "ext": path.suffix.lower(),
                "size": path.stat().st_size,
                "sha256": digest,
            }
        )

    payload = {
        "release_tag": "course-media-v1",
        "release_url_base": (
            "https://github.com/machine-ctm/machine-ctm.github.io/releases/download/course-media-v1/"
        ),
        "collections": COLLECTIONS,
        "items": sorted(items, key=lambda i: (i["collection"], i["title"].lower())),
        "duplicates": duplicates,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    counts: dict[str, int] = {}
    for item in items:
        counts[item["collection"]] = counts.get(item["collection"], 0) + 1
    print(f"Wrote {OUT} with {len(items)} unique files ({sum(i['size'] for i in items)/1024**3:.2f} GB)")
    print("Counts:", counts)
    print(f"Skipped duplicates: {len(duplicates)}")
    for dup in duplicates:
        print("  ", dup["source"], "==", dup["duplicate_of"])


if __name__ == "__main__":
    main()

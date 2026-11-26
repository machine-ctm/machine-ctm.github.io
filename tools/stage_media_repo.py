#!/usr/bin/env python3
"""Copy inventoried course files into a staging repo using their release slugs."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = json.loads((ROOT / "tools" / "media_inventory.json").read_text(encoding="utf-8"))
STAGE = Path("D:/Educational Courses/course-media-staging")

README = """# Course media assets

Raw copies of the course videos and documents linked from the
[machine-ctm field guide](https://machine-ctm.github.io/media/).

Filenames match the assets on the `course-media-v1` GitHub Release. These files are
served through `raw.githubusercontent.com` so the site's inline video and document
viewers can load them with CORS and byte-range support.

Provided for personal study; copyright remains with the original authors and publishers.
"""


def main() -> None:
    STAGE.mkdir(parents=True, exist_ok=True)
    (STAGE / "README.md").write_text(README, encoding="utf-8")
    for index, item in enumerate(INV["items"], 1):
        src = Path(item["source"])
        dst = STAGE / item["slug"]
        if dst.exists() and dst.stat().st_size == item["size"]:
            continue
        shutil.copy2(src, dst)
        if index % 20 == 0 or index == len(INV["items"]):
            print(f"Copied {index}/{len(INV['items'])}", flush=True)
    print(f"Staging ready at {STAGE}")


if __name__ == "__main__":
    main()

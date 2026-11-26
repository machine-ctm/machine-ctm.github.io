#!/usr/bin/env python3
"""Resume batched media push after the 100 MB file limit rejection."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = json.loads((ROOT / "tools" / "media_inventory.json").read_text(encoding="utf-8"))
STAGE = Path("D:/Educational Courses/course-media-staging")
HOLD = Path("D:/Educational Courses/course-media-holding")
LIMIT = 95 * 1024 * 1024
TOKEN = os.environ.get("GH_TOKEN", "")


def run(args, check=True):
    proc = subprocess.run(args, cwd=STAGE, text=True, capture_output=True)
    out = re.sub(r"ghp_[A-Za-z0-9]+", "[REDACTED]", (proc.stdout or "") + (proc.stderr or ""))
    if check and proc.returncode != 0:
        print(out, flush=True)
        raise SystemExit(f"Command failed: {args[:3]}")
    return out


def chunks(items, cap=180 * 1024 * 1024):
    out, cur, size = [], [], 0
    for item in items:
        if cur and size + item["size"] > cap:
            out.append(cur)
            cur, size = [], 0
        cur.append(item)
        size += item["size"]
    if cur:
        out.append(cur)
    return out


def main() -> None:
    if not TOKEN:
        raise SystemExit("GH_TOKEN is not set")

    run(["git", "fetch", "origin", "main"])

    # Park every media file outside the repo, then reset to the last good push.
    for item in INV["items"]:
        src = STAGE / item["slug"]
        if src.exists():
            dst = HOLD / item["slug"]
            if dst.exists() and dst.stat().st_size == item["size"]:
                src.unlink()
            else:
                shutil.move(str(src), str(dst))
    run(["git", "reset", "--hard", "origin/main"])

    remote_paths = set(run(["git", "ls-tree", "-r", "--name-only", "origin/main"]).splitlines())
    tracked_slugs = {Path(p).name for p in remote_paths}

    oversized = [i for i in INV["items"] if i["size"] > 100 * 1024 * 1024]
    pending = [
        i for i in INV["items"]
        if i["slug"] not in tracked_slugs and i["size"] <= LIMIT
    ]
    print(f"Already on remote: {len(tracked_slugs)}; oversized: {len(oversized)}; pending: {len(pending)}", flush=True)
    for item in oversized:
        print(f"  download-only: {item['slug']} ({item['size']/1024**2:.1f} MB)", flush=True)

    all_batches = chunks(pending)
    print(f"{len(all_batches)} remaining batches", flush=True)
    for number, batch in enumerate(all_batches, 1):
        for item in batch:
            src = HOLD / item["slug"]
            dst = STAGE / item["slug"]
            if src.exists():
                shutil.move(str(src), str(dst))
        run(["git", "add", "--"] + [item["slug"] for item in batch])
        mb = sum(i["size"] for i in batch) / 1024**2
        run(["git", "commit", "-q", "-m", f"Add media batch {number + 6} ({len(batch)} files)"])
        print(f"[{number}/{len(all_batches)}] pushing {len(batch)} files, {mb:.0f} MB", flush=True)
        run(["git", "push", "origin", "main"])

    print("Done", flush=True)


if __name__ == "__main__":
    main()

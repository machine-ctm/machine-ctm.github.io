#!/usr/bin/env python3
"""Push the media repo in size-bounded batches to avoid HTTP timeouts."""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = json.loads((ROOT / "tools" / "media_inventory.json").read_text(encoding="utf-8"))
STAGE = Path("D:/Educational Courses/course-media-staging")
HOLD = Path("D:/Educational Courses/course-media-holding")
LIMIT = 180 * 1024 * 1024
TOKEN = os.environ.get("GH_TOKEN", "")


def run(args, cwd=STAGE, check=True):
    proc = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    out = re.sub(r"ghp_[A-Za-z0-9]+", "[REDACTED]", (proc.stdout or "") + (proc.stderr or ""))
    if check and proc.returncode != 0:
        print(out, flush=True)
        raise SystemExit(f"Command failed: {args[0:3]}")
    return out


def batches():
    result = []
    current = []
    size = 0
    for item in INV["items"]:
        if current and size + item["size"] > LIMIT:
            result.append(current)
            current, size = [], 0
        current.append(item)
        size += item["size"]
    if current:
        result.append(current)
    return result


def main() -> None:
    if not TOKEN:
        raise SystemExit("GH_TOKEN is not set")
    HOLD.mkdir(parents=True, exist_ok=True)

    run(["git", "config", "http.postBuffer", "524288000"])
    run(["git", "config", "http.lowSpeedLimit", "0"])
    run(["git", "config", "http.lowSpeedTime", "999999"])
    run(["git", "config", "http.version", "HTTP/1.1"])

    remotes = run(["git", "remote"], check=False)
    if "origin" not in remotes.split():
        run(["git", "remote", "add", "origin", f"https://x-access-token:{TOKEN}@github.com/machine-ctm/course-media.git"])

    branch = run(["git", "branch", "--show-current"], check=False).strip()
    if branch == "main":
        run(["git", "branch", "-m", "full-local"], check=False)
        run(["git", "checkout", "--orphan", "main"])
        run(["git", "rm", "-r", "--cached", "."], check=False)

    for item in INV["items"]:
        src = STAGE / item["slug"]
        dst = HOLD / item["slug"]
        if src.exists():
            if dst.exists() and dst.stat().st_size == item["size"]:
                src.unlink()
            else:
                shutil.move(str(src), str(dst))

    (STAGE / "README.md").write_text(
        "# Course media assets\n\nRaw course videos and documents used by the "
        "[machine-ctm media library](https://machine-ctm.github.io/media/).\n",
        encoding="utf-8",
    )
    run(["git", "add", "README.md"])
    run(["git", "commit", "-q", "-m", "Initialize media asset repo"], check=False)
    print("Pushing initial commit", flush=True)
    run(["git", "push", "-u", "origin", "main"])

    all_batches = batches()
    print(f"{len(all_batches)} batches", flush=True)
    for number, batch in enumerate(all_batches, 1):
        for item in batch:
            src = HOLD / item["slug"]
            dst = STAGE / item["slug"]
            if src.exists():
                shutil.move(str(src), str(dst))
        run(["git", "add", "--"] + [item["slug"] for item in batch])
        mb = sum(i["size"] for i in batch) / 1024**2
        run(["git", "commit", "-q", "-m", f"Add media batch {number} ({len(batch)} files)"])
        print(f"[{number}/{len(all_batches)}] pushing {len(batch)} files, {mb:.0f} MB", flush=True)
        run(["git", "push", "origin", "main"])

    print("Done", flush=True)


if __name__ == "__main__":
    main()

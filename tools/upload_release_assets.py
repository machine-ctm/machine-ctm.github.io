#!/usr/bin/env python3
"""Create the course-media GitHub Release and upload every inventoried file.

Reads the PAT from GH_TOKEN (never stored in the repo). Existing release assets
with the same filename are skipped, so the script is safe to re-run.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INVENTORY = ROOT / "tools" / "media_inventory.json"
REPO = "machine-ctm/machine-ctm.github.io"
API = "https://api.github.com"
UPLOADS = "https://uploads.github.com"
TOKEN = os.environ.get("GH_TOKEN", "")

CONTENT_TYPES = {
    ".mp4": "video/mp4",
    ".pdf": "application/pdf",
    ".ppt": "application/vnd.ms-powerpoint",
    ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
}


def request(method: str, url: str, payload=None, headers=None, timeout=600):
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    hdrs = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "machine-ctm-media-uploader",
    }
    if headers:
        hdrs.update(headers)
    req = urllib.request.Request(url, data=data, method=method, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = resp.read()
        return json.loads(body) if body else {}


def upload_asset(url: str, data: bytes, content_type: str, timeout=900):
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "machine-ctm-media-uploader",
            "Content-Type": content_type,
            "Content-Length": str(len(data)),
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read())


def main() -> None:
    if not TOKEN:
        raise SystemExit("GH_TOKEN is not set")
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    tag = inv["release_tag"]

    existing = None
    try:
        existing = request("GET", f"{API}/repos/{REPO}/releases/tags/{tag}")
    except urllib.error.HTTPError as exc:
        if exc.code != 404:
            raise

    if existing:
        release_id = existing["id"]
        print(f"Using existing release {tag} (id {release_id})", flush=True)
    else:
        body = (
            "Self-study course media collected from the user's local course folders: "
            "Fundamentals of Modern Manufacturing, Lean Manufacturing, CNC Machine, "
            "Fundamentals of Tool Design, Mechanical Engineering and Mechanical Drawing.\n\n"
            "Files are hosted here as download assets so the GitHub Pages site stays "
            "within its size limit. Videos are MP4; open them in any modern media player. "
            "Course materials are provided for personal study; copyright remains with "
            "the respective original authors and publishers."
        )
        created = request(
            "POST",
            f"{API}/repos/{REPO}/releases",
            {
                "tag_name": tag,
                "name": "Course media library — videos & references",
                "body": body,
                "draft": False,
                "prerelease": False,
            },
        )
        release_id = created["id"]
        print(f"Created release {tag} (id {release_id})", flush=True)

    assets = request("GET", f"{API}/repos/{REPO}/releases/{release_id}/assets?per_page=100")
    present = {a["name"] for a in assets}
    print(f"Release already has {len(present)} assets", flush=True)

    items = inv["items"]
    for index, item in enumerate(items, 1):
        name = item["slug"]
        if name in present:
            print(f"[{index}/{len(items)}] skip existing {name}", flush=True)
            continue
        path = Path(item["source"])
        if not path.is_file():
            print(f"[{index}/{len(items)}] MISSING {path}", flush=True)
            continue
        size_mb = item["size"] / 1024**2
        print(f"[{index}/{len(items)}] upload {name} ({size_mb:.1f} MB)", flush=True)
        url = (
            f"{UPLOADS}/repos/{REPO}/releases/{release_id}/assets"
            f"?name={urllib.parse.quote(name)}"
        )
        with path.open("rb") as fh:
            data = fh.read()
        upload_asset(url, data, CONTENT_TYPES.get(item["ext"], "application/octet-stream"))
    print("Upload pass finished.", flush=True)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Wire the new media catalog into site navigation, homepage and sitemap."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ROOT_BILINGUAL = '<a class="nav-link" href="videos/"><span class="t-vi">Video</span><span class="t-en">Videos</span></a>'
EN_ONE = '<a class="nav-link" href="../videos/">Videos</a>'
EN_ACTIVE = '<a class="nav-link active" href="index.html">Videos</a>'
VI_ONE = '<a class="nav-link" href="../videos/">Video</a>'
VI_ACTIVE = '<a class="nav-link active" href="index.html">Video</a>'


def indent_of(line: str) -> str:
    return line[: len(line) - len(line.lstrip())]


def media_link(depth: int, is_vi: bool, bilingual: bool = False) -> str:
    # VI pages live under /vi/**, so their sibling sections are one level up
    # (e.g. /vi/books/ -> /vi/media/), not at the repo root.
    prefix = "../" * (depth - 1 if is_vi and depth >= 2 else depth)
    if bilingual:
        label = '<span class="t-vi">Tài liệu</span><span class="t-en">Media</span>'
    else:
        label = "Tài liệu" if is_vi else "Media"
    return f'<a class="nav-link" href="{prefix}media/">{label}</a>'


def patch_nav() -> None:
    changed = []
    for path in sorted(ROOT.rglob("*.html")):
        rel = path.relative_to(ROOT)
        if "media" in rel.parts or not rel.name.endswith(".html"):
            continue
        text = path.read_text(encoding="utf-8")
        if 'href="../media/"' in text or 'href="../../media/"' in text or 'href="media/"' in text:
            continue
        depth = len(rel.parts) - 1
        is_vi = rel.parts[0] == "vi" if rel.parts else False
        lines = text.splitlines(keepends=True)
        inserted = False
        for idx, line in enumerate(lines):
            stripped = line.strip()
            if stripped == ROOT_BILINGUAL:
                new_link = media_link(0, is_vi, bilingual=True)
            elif stripped == EN_ONE or stripped == EN_ACTIVE:
                new_link = media_link(depth, is_vi)
            elif stripped == VI_ONE or stripped == VI_ACTIVE:
                new_link = media_link(depth, is_vi)
            else:
                continue
            lines.insert(idx + 1, indent_of(line) + new_link + "\n")
            inserted = True
            break
        if inserted:
            path.write_text("".join(lines), encoding="utf-8")
            changed.append(str(rel))
    print(f"Nav patched in {len(changed)} pages:")
    for item in changed:
        print("  ", item)


def patch_homepage() -> None:
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf-8")

    if 'href="media/"><span class="t-vi">Tài liệu khóa học' not in text:
        cta_anchor = '          <a class="btn btn-s" href="#curriculum"><span class="t-vi">Xem chương trình đào tạo</span><span class="t-en">View the training program</span></a>\n'
        if cta_anchor not in text:
            raise SystemExit("Homepage hero CTA anchor not found")
        addition = '          <a class="btn btn-s" href="media/"><span class="t-vi">Tài liệu khóa học →</span><span class="t-en">Course media →</span></a>\n'
        text = text.replace(cta_anchor, cta_anchor + addition, 1)

    if 'href="media/"><b>Open the media library' not in text:
        anchor = '    </div>\n  </section>\n\n  <!-- ============ EDUCATION ============ -->'
        if anchor not in text:
            raise SystemExit("Homepage library section anchor not found")
        note = '''      <div class="note">
        <span class="lbl"><span class="t-vi">Tài liệu khóa học</span><span class="t-en">Course media</span></span>
        <p><span class="t-vi">137 video và tài liệu từ các thư mục khóa học — chế tạo, Lean, CNC, thiết kế dụng cụ, cơ khí và bản vẽ. <a href="media/"><b>Mở thư viện tài liệu →</b></a></span><span class="t-en">137 videos and references from the course folders — manufacturing, Lean, CNC, tool design, mechanical engineering and drawing. <a href="media/"><b>Open the media library →</b></a></span></p>
      </div>
'''
        text = text.replace(anchor, note + anchor, 1)

    path.write_text(text, encoding="utf-8")
    print("Homepage CTA and library note updated")


def patch_sitemap() -> None:
    path = ROOT / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    if "https://machine-ctm.github.io/media/" in text:
        print("Sitemap already contains media URLs")
        return
    block = '''
  <url>
    <loc>https://machine-ctm.github.io/media/</loc>
    <lastmod>2026-11-26</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://machine-ctm.github.io/media/"/>
    <xhtml:link rel="alternate" hreflang="vi" href="https://machine-ctm.github.io/vi/media/"/>
  </url>
  <url>
    <loc>https://machine-ctm.github.io/vi/media/</loc>
    <lastmod>2026-11-26</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
    <xhtml:link rel="alternate" hreflang="en" href="https://machine-ctm.github.io/media/"/>
    <xhtml:link rel="alternate" hreflang="vi" href="https://machine-ctm.github.io/vi/media/"/>
  </url>
'''
    if "</urlset>" not in text:
        raise SystemExit("Sitemap close tag not found")
    path.write_text(text.replace("</urlset>", block + "</urlset>"), encoding="utf-8")
    print("Sitemap updated")


def main() -> None:
    patch_nav()
    patch_homepage()
    patch_sitemap()


if __name__ == "__main__":
    main()

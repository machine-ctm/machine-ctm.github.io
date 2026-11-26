#!/usr/bin/env python3
"""Generate the bilingual course-media catalog pages from media_inventory.json."""
from __future__ import annotations

import html
import json
from collections import defaultdict
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
INV = json.loads((ROOT / "tools" / "media_inventory.json").read_text(encoding="utf-8"))

ORDER = ["mfg", "lean", "cnc", "tool", "mech", "draw"]
BASE = INV["release_url_base"]

TEXT = {
    "en": {
        "lang": "en",
        "title": "Course Media Library — Chế tạo máy / Machine Building",
        "desc": "Downloadable self-study videos and references from manufacturing, lean production, CNC, tool design and mechanical engineering.",
        "skip": "Skip to content",
        "brand_sub": "Machine Building",
        "nav": ["Discipline", "Processes", "Curriculum", "Tools", "Careers", "Books", "Education", "Videos", "Media", "Foundation"],
        "kicker": "Thư viện tài liệu · Course Media",
        "h1": "Course Media Library",
        "h1thin": "Videos and references from the course folders.",
        "lede": "A single index of the local course materials: manufacturing processes, lean manufacturing, CNC machines, tool design and mechanical engineering.",
        "browse": "Browse the collection →",
        "figure_cap": "137 files · 1.46 GB",
        "eyebrow": "Course media · Tài liệu học tập",
        "h2": "Downloadable files",
        "intro": "Files are hosted as GitHub Release assets so the site stays within GitHub Pages size limits. Click a file name to save it locally; MP4 videos play in any modern media player.",
        "filter": "Filter by title or filename…",
        "col_file": "File",
        "col_type": "Type",
        "col_size": "Size",
        "col_get": "Get",
        "download": "Download",
        "empty": "No files match your filter.",
        "note_lbl": "A note on sources",
        "note": "These are personal study copies collected from local course folders. Copyright remains with the original authors and publishers; please use them for private study and follow your local copyright rules.",
        "footer": "Course materials are hosted on GitHub Releases and linked from this page. Academic reference site, not an official HUST site.",
        "home": "← Home / Trang chủ",
        "switch_html": '<span class="on">EN</span><span class="lang-sep">/</span><a href="../vi/media/" style="color:inherit">VI</a>',
        "path": "../",
    },
    "vi": {
        "lang": "vi",
        "title": "Thư viện tài liệu học tập — Chế tạo máy / Machine Building",
        "desc": "Video và tài liệu tự học về chế tạo, sản xuất tin gọn, máy CNC, thiết kế dụng cụ và kỹ thuật cơ khí.",
        "skip": "Bỏ qua nội dung",
        "brand_sub": "Machine Building",
        "nav": ["Kỷ thuật", "Quy trình", "Chương trình", "Thiết bị", "Nghề nghiệp", "Sách", "Giáo dục", "Video", "Tài liệu", "Nền tảng"],
        "kicker": "Thư viện tài liệu · Course Media",
        "h1": "Thư viện tài liệu học tập",
        "h1thin": "Video và tài liệu từ các thư mục khóa học.",
        "lede": "Một chỉ mục duy nhất cho tài liệu học tập có trong máy: quy trình chế tạo, sản xuất tin gọn, máy CNC, thiết kế dụng cụ và kỹ thuật cơ khí.",
        "browse": "Xem danh mục →",
        "figure_cap": "137 tệp · 1,46 GB",
        "eyebrow": "Tài liệu học tập · Course media",
        "h2": "Tệp có thể tải về",
        "intro": "Các tệp được lưu trên GitHub Releases để trang web không vượt giới hạn của GitHub Pages. Nhấn tên tệp để tải về; video MP4 mở được bằng mọi trình phát hiện đại.",
        "filter": "Lọc theo tên tệp…",
        "col_file": "Tệp",
        "col_type": "Loại",
        "col_size": "Kích thước",
        "col_get": "Tải",
        "download": "Tải về",
        "empty": "Không có tệp nào khớp với bộ lọc.",
        "note_lbl": "Lưu ý về nguồn tài liệu",
        "note": "Đây là các bản sao dùng cho học tập cá nhân, lấy từ thư mục khóa học trên máy. Bản quyền vẫn thuộc về tác giả và nhà xuất bản gốc; chỉ sử dụng cho mục đích học tập riêng và tuân thủ quy định bản quyền hiện hành.",
        "footer": "Tài liệu được lưu trên GitHub Releases và liên kết từ trang này. Trang tham khảo học thuật, không phải trang chính thức của HUST.",
        "home": "← Trang chủ / Home",
        "switch_html": '<a href="../../media/" style="color:inherit">EN</a><span class="lang-sep">/</span><span class="on">VI</span>',
        "path": "../../",
    },
}

NAV_BASE = [
    ("#discipline", 0), ("#processes", 1), ("#curriculum", 2), ("#tools", 3),
    ("#careers", 4), ("books/", 5), ("education/", 6), ("videos/", 7),
    ("media/", 8), ("foundation/", 9),
]


def nav_targets(lang: str):
    labels = TEXT[lang]["nav"]
    if lang == "en":
        return [(f"../{href}", labels[idx], idx == 8) for href, idx in NAV_BASE]
    # VI pages sit at /vi/media/ — home anchors go two levels up, but sibling
    # VI sections are one level up (see handoff.md §4).
    hrefs = [
        "../../#discipline", "../../#processes", "../../#curriculum",
        "../../#tools", "../../#careers", "../books/", "../education/",
        "../videos/", "../media/", "../foundation/",
    ]
    return [(href, labels[idx], idx == 8) for idx, href in enumerate(hrefs)]


def fmt_size(num: int) -> str:
    if num >= 1024**3:
        return f"{num / 1024**3:.2f} GB"
    if num >= 1024**2:
        return f"{num / 1024**2:.1f} MB"
    return f"{num / 1024:.0f} KB"


def esc(value: str) -> str:
    return html.escape(value, quote=True)


def build(lang: str) -> str:
    t = TEXT[lang]
    p = t["path"]
    grouped = defaultdict(list)
    for item in INV["items"]:
        grouped[item["collection"]].append(item)

    nav_html = "\n".join(
        f'      <a class="nav-link{" active" if active else ""}" href="{href}">{esc(label)}</a>'
        for href, label, active in nav_targets(lang)
    )

    sections = []
    for coll in ORDER:
        items = grouped.get(coll, [])
        if not items:
            continue
        meta = INV["collections"][coll]
        label = meta[lang]
        note = meta[f"note_{lang}"]
        n_video = sum(1 for i in items if i["ext"] == ".mp4")
        n_doc = len(items) - n_video
        rows = []
        for item in items:
            url = BASE + quote(item["slug"])
            kind = item["ext"].lstrip(".").upper()
            search = esc(f'{item["title"]} {item["slug"]}'.lower())
            rows.append(
                f'          <tr data-search="{search}">\n'
                f'            <td><strong>{esc(item["title"])}</strong><br><span class="src">{esc(item["slug"])}</span></td>\n'
                f'            <td><span class="pill" data-kind="{kind}">{kind}</span></td>\n'
                f'            <td class="mono">{fmt_size(item["size"])}</td>\n'
                f'            <td><a class="more" href="{esc(url)}" target="_blank" rel="noopener">{t["download"]} ↗</a></td>\n'
                f'          </tr>'
            )
        sections.append(
            f'''  <section class="sec" id="{coll}">
    <div class="wrap">
      <div class="eyebrow"><span class="num">{len(items):02d}</span><span class="line"></span><span class="eyebrow-label">{esc(label)}</span></div>
      <div class="sec-head">
        <h2>{esc(label)} <span class="dim" style="font-weight:400;font-size:.6em">{esc(meta["en"] if lang == "vi" else meta["vi"])}</span></h2>
        <p>{esc(note)} <span class="dim">({n_video} MP4 · {n_doc} documents · {fmt_size(sum(i["size"] for i in items))})</span></p>
      </div>
      <div class="tbl-wrap"><table class="tbl media-table">
        <thead><tr><th>{t["col_file"]}</th><th>{t["col_type"]}</th><th>{t["col_size"]}</th><th>{t["col_get"]}</th></tr></thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table></div>
      <p class="small dim no-match" hidden style="margin-top:14px">{t["empty"]}</p>
    </div>
  </section>'''
        )

    video_count = sum(1 for i in INV["items"] if i["ext"] == ".mp4")
    doc_count = len(INV["items"]) - video_count
    total = sum(i["size"] for i in INV["items"])
    figcap = (
        f'{len(INV["items"])} files · {fmt_size(total)}'
        if lang == "en"
        else f'{len(INV["items"])} tệp · {fmt_size(total)}'
    )
    root = "https://machine-ctm.github.io/"
    path = "media/" if lang == "en" else "vi/media/"

    return f'''<!DOCTYPE html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{root}{path}">
<link rel="alternate" hreflang="en" href="{root}media/">
<link rel="alternate" hreflang="vi" href="{root}vi/media/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Chế tạo máy / Machine Building">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:url" content="{root}{path}">
<meta name="twitter:card" content="summary">
<meta name="theme-color" content="#ffffff">
<link rel="icon" href="{p}assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}assets/style.css">
</head>
<body>
<a class="skip" href="#main">{t["skip"]}</a>
<header class="topbar">
  <div class="wrap bar">
    <a class="brand" href="{p}index.html" aria-label="Chế tạo máy">
      <span class="mark" aria-hidden="true">
        <svg viewBox="0 0 32 32" width="30" height="30">
          <g fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round">
            <circle cx="16" cy="16" r="6.5"/><circle cx="16" cy="16" r="2.2" fill="currentColor" stroke="none"/>
            <path d="M16 4.5v3M16 24.5v3M4.5 16h3M24.5 16h3M7.6 7.6l2.1 2.1M22.3 22.3l2.1 2.1M24.4 7.6l-2.1 2.1M9.7 22.3l-2.1 2.1"/>
          </g>
        </svg>
      </span>
      <span class="brand-txt"><strong>Chế tạo máy</strong><em>{t["brand_sub"]}</em></span>
    </a>
    <nav class="nav" id="nav">
{nav_html}
    </nav>
    <div class="bar-right">
      <div class="lang" title="Đổi ngôn ngữ / Switch language">
        {t["switch_html"]}
      </div>
    </div>
  </div>
</header>

<main id="main">
  <section class="hero">
    <div class="wrap hero-in">
      <div>
        <span class="kicker"><span class="dot"></span>{t["kicker"]}</span>
        <h1>{t["h1"]}<span class="thin">{t["h1thin"]}</span></h1>
        <p class="lede">{t["lede"]}</p>
        <div class="hero-cta">
          <a class="btn btn-p" href="#mfg">{t["browse"]}</a>
        </div>
      </div>
      <div class="figure">
        <svg viewBox="0 0 200 200" role="img" aria-label="Files">
          <g fill="none" stroke="#c2540b" stroke-width="4" stroke-linejoin="round">
            <rect x="48" y="36" width="88" height="112" rx="7"/>
            <path d="M66 68h52M66 88h52M66 108h34"/>
          </g>
          <circle cx="139" cy="137" r="25" fill="#fff" stroke="#2f5d80" stroke-width="4"/>
          <path d="M130 137h18M139 128v18" stroke="#2f5d80" stroke-width="4" stroke-linecap="round"/>
        </svg>
        <div class="figcap">{figcap}</div>
      </div>
    </div>
  </section>

  <section class="sec alt" id="overview">
    <div class="wrap">
      <div class="stats">
        <div class="stat"><b>{len(INV["items"])}</b><span>{("Files" if lang == "en" else "Tệp")}</span></div>
        <div class="stat"><b>{video_count}</b><span>MP4 {("videos" if lang == "en" else "video")}</span></div>
        <div class="stat"><b>{doc_count}</b><span>{("PDF / slides" if lang == "en" else "PDF / slide")}</span></div>
        <div class="stat"><b>{fmt_size(total)}</b><span>{("Total size" if lang == "en" else "Tổng dung lượng")}</span></div>
      </div>
      <div class="media-filter">
        <label for="mediaFilter">{t["filter"]}</label>
        <input type="search" id="mediaFilter" autocomplete="off" placeholder="{t["filter"]}">
      </div>
      <div class="note"><span class="lbl">{t["note_lbl"]}</span><p>{t["note"]}</p></div>
    </div>
  </section>

{chr(10).join(sections)}
</main>

<footer class="foot">
  <div class="wrap foot-in">
    <div class="foot-l">
      <span class="brand-mini">{("Course Media — Chế tạo máy" if lang == "en" else "Tài liệu học tập — Chế tạo máy")}</span>
      <p>{t["footer"]}</p>
    </div>
    <div class="foot-r">
      <span class="mono"><a href="{p}index.html">{t["home"]}</a></span>
      <span class="mono">machine-ctm.github.io</span>
    </div>
  </div>
</footer>
<script>
(function(){{
  var input = document.getElementById('mediaFilter');
  if (!input) return;
  input.addEventListener('input', function(){{
    var q = input.value.trim().toLowerCase();
    document.querySelectorAll('.media-table tbody tr').forEach(function(row){{
      row.hidden = q && row.getAttribute('data-search').indexOf(q) === -1;
    }});
    document.querySelectorAll('.media-table').forEach(function(table){{
      var body = table.querySelector('tbody');
      var any = Array.prototype.some.call(body.rows, function(r){{ return !r.hidden; }});
      var msg = table.parentElement.querySelector('.no-match');
      if (msg) msg.hidden = any;
    }});
  }});
}})();
</script>
</body>
</html>
'''


def main() -> None:
    for lang, rel in (("en", "media/index.html"), ("vi", "vi/media/index.html")):
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(build(lang), encoding="utf-8")
        print(f"Wrote {out}")


if __name__ == "__main__":
    main()

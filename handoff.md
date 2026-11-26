# Handoff — Chế tạo máy (Machine Building) site

Continue building the bilingual machining field-guide. This document captures the
current state and the exact next steps so work can resume without re-deriving context.

---

## 1. Goal & current state

Bilingual (EN / VI) static GitHub Pages site about Machine Building / Machining.
**Done:** homepage, `/books` + `/vi/books` (37 hosted PDFs — 11 machining textbooks + 26
Foundation science titles re-hosted same-origin — all opened through the in-browser Reader,
plus free/external references and A/B/C grading; both libraries carry a `#foundation-science`
cross-list), the in-browser Reader (`/reader.html`, `/vi/reader.html`), `/education` +
`/vi/education`, `/videos` + `/vi/videos`, **Foundation Science** `/foundation` + `/vi/foundation`
(13 free science books per language, served same-origin + mirrored on the `foundation-v1` GitHub
Release), and **Vietnamese study-guide pages for every graded English book — 4 grade-A + 2 grade-B
+ 2 grade-C (8 total)**, plus a consolidated eight-card index at `/vi/books/#huong-dan`.
**Nothing pending** from the original handoff — Tasks A, B, the remaining A-books, the grade-B
books and the grade-C reference works are all complete. The translation job is finished (8/8).
The Foundation Science section (basic Maths / Physics / Chemistry / General Science for young
readers) is also complete and live.

Live: https://machine-ctm.github.io/ · Repo: `machine-ctm/machine-ctm.github.io` · branch `main`.

---

## 2. Task A — Video Library (8 YouTube videos) — DONE

`/videos` (EN) and `/vi/videos` (VI) are built and live. Reference list of titles fetched
via YouTube oEmbed:

| # | Video ID | Title | Channel |
|---|----------|-------|---------|
| 1 | `sdxOysfa-L8` | What is Machining??? | Machining-Tutorials |
| 2 | `ldTwkrkmgIw` | How Is Metal Machined? Turning, Milling, CNC Machining, Cutting Tools and Modern Metal Manufacturing | WebMaxi ENG |
| 3 | `kDJ3QzTCgXM` | CNC Machining Process: The Step-by-Step Guide | Yijin Solution |
| 4 | `uxVJ3qtezGw` | The Most Common Metal Machining Processes (Metal Machining Video 1) | Sofeast |
| 5 | `mdRTq2_qI9Y` | CNC machines — The Types of CNC Machines Explained (3 and 5 axis) | Protolabs |
| 6 | `mKeBpqQSWug` | What is Machining? | NYC CNC |
| 7 | `xS4aQHJiJ-w` | 7 Types of Manufacturing Processes: CNC Machining & Extrusion & Stamping & more | RAPID DIRECT |
| 8 | `SwK5uWrbTEM` | Different Machining Processes: Turning, Milling, Drilling | Blue Grass Manufacturing |

**Implementation notes (for reference):**
- Both pages modelled on the books pages (same top bar, hero, `sec`/`card`/`grid` classes).
- Each video is a responsive 16:9 player:
  `<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/<ID>" title="<Title>" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;border:0" allowfullscreen></iframe></div>`
- "Videos" nav link wired into all page pairs, plus a homepage teaser.
- EN descriptions + VI translations present for all eight videos.

---

## 3. Task B — Vietnamese study guides — DONE (8/8 A+B+C books)

**Delivery format chosen: original Vietnamese HTML study guides** (option 1), *not* verbatim
translations — to respect copyright. Each page reuses the site design system, includes a
copyright note, links to its original PDF, and is cross-linked to the other seven guides.
A consolidated eight-card index at `/vi/books/#huong-dan` lists all of them and is linked
from both library heroes, the VI textbooks section header and every guide's conclusion.

| Book | Grade | Vietnamese page |
|---|---|---|
| Build Your Own CNC Machine | A | `vi/books/tu-che-may-cnc.html` |
| CNC Programming Basics | A | `vi/books/co-ban-lap-trinh-cnc.html` |
| CNC Machining: The Complete Engineering Guide | A | `vi/books/cam-nang-gia-cong-cnc.html` |
| Tormach CNC Student Guide | A | `vi/books/cam-nang-sinh-vien-tormach.html` |
| CNC Programming for Lathe (Mitsubishi Electric course) | B | `vi/books/lap-trinh-cnc-may-tien.html` |
| Fundamentals of CNC Machining (Autodesk) | B | `vi/books/nen-tang-gia-cong-cnc.html` |
| Metal Forming Handbook (Schuler / Springer 1998) | C | `vi/books/cam-nang-gia-cong-ap-luc.html` |
| Machining Processes and Machines (Huda / CRC Press 2021) | C | `vi/books/quy-trinh-va-may-gia-cong.html` |

All eight are linked from their cards on both `/books` (EN, "Bản TV" button + inline link) and
`/vi/books` (VI, "Bản TV" button + inline link). Source PDFs: `books/files/*.pdf`.

**Copyright note:** the Autodesk *Fundamentals* PDF explicitly prohibits translation/reproduction;
the Schuler handbook explicitly reserves translation rights; the CRC Press / Taylor & Francis
front matter prohibits reproduction in any form. All three pages are therefore fully rewritten
original adaptations that say "không phải bản dịch". The Mitsubishi course notes that command
formats vary by machine-tool builder.

**Source caveat (grade C):** `books/files/machining-processes-and-machines.pdf` is the
**32-page publisher preview** — copyright page, complete TOC, preface and Chapter 1 only — not
the full 16-chapter book. Its guide is built from Chapter 1 + the TOC and discloses this
prominently; both library cards and the ResearchGate card were corrected from the earlier false
"full PDF hosted here" wording. `metal-forming-handbook-schuler-1998.pdf` is the complete
573-page handbook.

**Convention for any further guides:** extract topics with `pypdf` (`PdfReader(...).pages[i].extract_text()`),
then write an ~8–11-section original adaptation in the site's `sec`/`card`/`grid`/`steps`/`tbl`
classes — do not copy prose verbatim. Note: `vi/books/*.html` sit two levels down, so assets are
`../../assets/…` and hosted PDFs are `../../books/files/…`. Add the new page to the eight-way
cross-link line in the conclusion of **every** guide, to the `/vi/books/#huong-dan` card grid,
and to the corresponding library cards in both indexes. `<pre>` blocks carry inline styles
(there is no global `pre` rule in `assets/style.css`).

---

## 4. Constraints & conventions

- **Copyright:** only host the user's own PDFs from `E:\Ebooks\Che Tao May`. Link external/
  licensed material (CnCCookbook, Internet Archive, referenceglobe, Eagle, ResearchGate, BCIT).
- **Foundation Science PDFs are served same-origin AND mirrored on a GitHub Release.** The 26 science
  PDFs live in `books/files/` (so the in-browser Reader can embed them — Pages serves them with
  `Content-Type: application/pdf` **and** `Access-Control-Allow-Origin: *`) **and** are mirrored on the
  `foundation-v1` release at
  `https://github.com/machine-ctm/machine-ctm.github.io/releases/download/foundation-v1/<slug>.pdf`.
  GitHub Release assets redirect to `release-assets.githubusercontent.com` with
  `Content-Disposition: attachment` and no CORS, so they **cannot** be embedded in the reader and are
  kept only as a download mirror. Pages' hard limit is 100 MB per file; the largest re-hosted PDF is
  **69.8 MB** (`tro-choi-ly-thu-bach-khoa.pdf`) — under the limit, though GitHub warns above 50 MB.
  Only *freely downloadable* works are included (public domain, Project Gutenberg, US DOE handbooks,
  Internet Archive CC BY-NC-ND) — **never** borrowed/lending-only copies. Update the mirror with
  `gh release create` using `GH_TOKEN` (read from the PAT in `git remote get-url origin`); `gh auth status`
  keyring tokens are currently invalid, so set `GH_TOKEN` explicitly.
- **Metadata for any new page:** add `<link rel="canonical" href="https://machine-ctm.github.io/<path>">`,
  Open Graph tags (`og:type`, `og:site_name`, `og:title`, `og:description`, `og:url`) and
  `<meta name="twitter:card" content="summary">`, derived from its `<title>` / `<meta name="description">`.
  Add reciprocal `hreflang="en"` / `hreflang="vi"` alternates if it has an EN/VI pair, then add its
  URL to `sitemap.xml` (referenced from `robots.txt`). `404.html` is `noindex` and deliberately
  **not** in the sitemap; it reuses the homepage's `.t-vi`/`.t-en` toggle script.
- **External-link checks:** 23 real links all return 200. ResearchGate returns 403 to non-browser
  user agents (anti-bot) and the two font preconnect origins return 404 by design — neither is a
  broken link, do not "fix" them.
- **Bilingual toggle:** `<html>` class `lang-vi`/`lang-en`; `.t-vi`/`.t-en` spans; `localStorage` (homepage only). Other pages are separate EN/VI files with a top-bar language switcher.
- **`/vi/**` relative paths:** assets and hosted files go two levels up (`../../assets/…`, `../../books/files/…`, `../../education/files/…`); the homepage is `../../index.html`. But **navigation to sibling VI sections is one level up** — `../books/`, `../education/`, `../videos/` — and a guide's "Sách" link is `index.html`. A previous version incorrectly used `../../books/` etc. in the nav and silently sent VI readers to the English sections. Keep the language switcher pointing at the EN counterpart (`../../books/`, `../../education/`, `../../videos/`).
- **Deploy:**
  ```bash
  cd machine-ctm-site
  git add -A
  git commit -m "…"
  git push origin main
  ```
  PAT is read at push time from `E:\Documents\Github Repos\machine-ctm.txt`
  (`grep -oE 'ghp_[A-Za-z0-9]+'`). **Never print the token** (scrub with `sed` if echoing push output).
- **Pages rebuild** ~1–2 min after push (longer for large PDF commits); verify only after waiting.

---

## 5. File map

```
machine-ctm-site/
├── index.html                 # homepage (EN+VI toggle)
├── reader.html                # In-browser PDF Reader (EN, noindex) — ?file=/.../x.pdf&title=...
├── books/index.html           # Library EN  (hosted PDFs + free/external + grading + #foundation-science)
├── vi/books/index.html        # Library VI (+ #huong-dan: 8-guide index; + #foundation-science)
├── vi/books/*.html            # 8 Vietnamese study guides (all grade-A + B + C books)
├── vi/reader.html             # In-browser PDF Reader (VI, noindex) — one level deep, uses ../assets
├── education/index.html        # Education EN
├── vi/education/index.html     # Education VI
├── videos/index.html           # Video Library EN
├── vi/videos/index.html        # Video Library VI
├── foundation/index.html       # Foundation Science EN (PDFs same-origin + Release mirror)
├── vi/foundation/index.html    # Foundation Science VI
├── books/files/                # 37 hosted PDFs (11 machining + 26 science, ASCII filenames)
├── education/files/            # Bharat Skills + SkilledTradesBC PDFs
├── assets/style.css            # design system (+ .grade badges added)
├── assets/favicon.svg
├── 404.html                    # custom bilingual 404 (noindex)
├── sitemap.xml                 # 17 content pages + 4 EN/VI hreflang pairs (reader pages excluded: noindex)
├── robots.txt                  # Allow: / + Sitemap reference
├── README.md
├── report.md                   # status report
└── handoff.md                 # this file
```

---

## 6. Verification snippet

```bash
sleep 60
for u in sitemap.xml robots.txt 404.html \
         reader.html vi/reader.html \
         books vi/books education vi/education videos vi/videos \
         foundation vi/foundation \
         vi/books/tu-che-may-cnc.html vi/books/co-ban-lap-trinh-cnc.html \
         vi/books/cam-nang-gia-cong-cnc.html vi/books/cam-nang-sinh-vien-tormach.html \
         vi/books/lap-trinh-cnc-may-tien.html vi/books/nen-tang-gia-cong-cnc.html \
         vi/books/cam-nang-gia-cong-ap-luc.html vi/books/quy-trinh-va-may-gia-cong.html; do
  curl -sL "https://machine-ctm.github.io/$u" -o /tmp/p.html -w "$u -> HTTP %{http_code} %{size_download}B\n"
done
# Same-origin hosted PDFs must come back as application/pdf WITH CORS (so the Reader can embed them):
for f in build-your-own-cnc-machine.pdf flatland.pdf amusements-in-mathematics.pdf \
         toan-hoc-sieu-hay.pdf vat-ly-ngo-ngan.pdf tro-choi-ly-thu-bach-khoa.pdf; do
  curl -sI -L -o /dev/null -w "pdf $f -> %{http_code} %{content_type}\n" \
    "https://machine-ctm.github.io/books/files/$f"
  curl -sI -L "https://machine-ctm.github.io/books/files/$f" | grep -i 'access-control-allow-origin' \
    && echo "  ok: CORS present for $f" || echo "  WARN: no CORS header for $f"
done
# Foundation Science PDFs are ALSO mirrored on the GitHub Release (download mirror, not embeddable):
for f in flatland.pdf amusements-in-mathematics.pdf toan-hoc-sieu-hay.pdf vat-ly-ngo-ngan.pdf; do
  curl -sI -L -o /dev/null -w "asset $f -> HTTP %{http_code} %{size_download}B\n" \
    "https://github.com/machine-ctm/machine-ctm.github.io/releases/download/foundation-v1/$f"
done
```

---

## 8. Course Media Library — added 2026-11-26

`/media/` + `/vi/media/` index **137 unique files (~1.46 GB)** from six local folders:
`Fundamentals of Mordern Manufacturing`, `Lean Manufacturing`, `CNC Machine` (including
`Fundamentals of Tool Design`), `Mechanical Engineering` and `Mechanical Drawing`. Exact
duplicates are removed by SHA-256 (one repeated CNC video, eight repeated drawing PDFs).

**Hosting decision:** the binaries are **not** in the Pages repo (it already holds ~400 MB
of PDFs and Pages has a ~1 GB soft limit). They are mirrored twice: on the `course-media-v1`
GitHub Release (Download links) and in the public `machine-ctm/course-media` repo
(raw URLs for inline viewers). Release assets cannot be embedded because they are served
with `Content-Disposition: attachment`; raw URLs from the media repo send CORS headers and
support byte ranges.

**Viewers:** `/media/viewer.html` = native HTML5 MP4 player; `/media/read.html` = locally
hosted PDF.js renderer for PDFs and an Office Online embed for `.ppt`/`.pptx`. Both take
`?file=<slug>&title=<title>&lang=en|vi`, are `noindex`, and keep a Download fallback.
PDF.js files live in `assets/pdfjs/` (3.11.174, UMD build) so the worker stays same-origin.
The 116 MB manufacturing handbook exceeds GitHub's 100 MB per-file limit; it stays on the
Release only and its catalog row shows a download-to-view note instead of a View link.

Regeneration workflow:
```bash
python tools/build_media_inventory.py          # writes tools/media_inventory.json
GH_TOKEN=<PAT> python tools/upload_release_assets.py   # idempotent release mirror
python tools/stage_media_repo.py               # copy slugs into D:/Educational Courses/course-media-staging
# push that staging repo to machine-ctm/course-media
python tools/generate_media_pages.py           # rebuild both catalog pages with View links
python tools/patch_site.py                     # nav / homepage / sitemap (idempotent)
```
When adding folders, update `SOURCES` and `COLLECTIONS` in `build_media_inventory.py` first.
VI sibling nav links must be `../media/` (one level up), while the VI language switcher
stays `../../media/` (EN counterpart).

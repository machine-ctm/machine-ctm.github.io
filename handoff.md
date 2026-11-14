# Handoff — Chế tạo máy (Machine Building) site

Continue building the bilingual machining field-guide. This document captures the
current state and the exact next steps so work can resume without re-deriving context.

---

## 1. Goal & current state

Bilingual (EN / VI) static GitHub Pages site about Machine Building / Machining.
**Done:** homepage, `/books` + `/vi/books` (11 hosted PDFs + free/external references,
A/B/C grading live), `/education` + `/vi/education`, `/videos` + `/vi/videos`,
and **Vietnamese study-guide pages for all 4 grade-A AND both grade-B books (6 total)**.
**Nothing pending** from the original handoff — Tasks A, B, the remaining A-books and the
grade-B books are all complete. Only grade-C reference works are left untouched on purpose.

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

## 3. Task B — Vietnamese study guides — DONE (6/6 A+B books)

**Delivery format chosen: original Vietnamese HTML study guides** (option 1), *not* verbatim
translations — to respect copyright. Each page reuses the site design system, includes a
copyright note, links to its original PDF, and is cross-linked to the other five guides.

| Book | Grade | Vietnamese page |
|---|---|---|
| Build Your Own CNC Machine | A | `vi/books/tu-che-may-cnc.html` |
| CNC Programming Basics | A | `vi/books/co-ban-lap-trinh-cnc.html` |
| CNC Machining: The Complete Engineering Guide | A | `vi/books/cam-nang-gia-cong-cnc.html` |
| Tormach CNC Student Guide | A | `vi/books/cam-nang-sinh-vien-tormach.html` |
| CNC Programming for Lathe (Mitsubishi Electric course) | B | `vi/books/lap-trinh-cnc-may-tien.html` |
| Fundamentals of CNC Machining (Autodesk) | B | `vi/books/nen-tang-gia-cong-cnc.html` |

All six are linked from their cards on both `/books` (EN, "Bản TV" button + inline link) and
`/vi/books` (VI, "Bản TV" button + inline link). Source PDFs: `books/files/*.pdf`.

**Copyright note:** the Autodesk *Fundamentals* PDF explicitly prohibits translation/reproduction,
so that page is a fully rewritten original study guide and says "không phải bản dịch". The
Mitsubishi course notes that command formats vary by machine-tool builder. Grade-C works
(Schuler *Metal Forming Handbook*, *Machining Processes and Machines*) are deliberately skipped —
dense academic references, better kept as PDFs.

**Convention for any further guides:** extract topics with `pypdf` (`PdfReader(...).pages[i].extract_text()`),
then write an ~8–11-section original adaptation in the site's `sec`/`card`/`grid`/`steps`/`tbl`
classes — do not copy prose verbatim. Note: `vi/books/*.html` sit two levels down, so assets are
`../../assets/…` and hosted PDFs are `../../books/files/…`. Add the new page to the six-way
cross-link line in the conclusion of **every** guide.

---

## 4. Constraints & conventions

- **Copyright:** only host the user's own PDFs from `E:\Ebooks\Che Tao May`. Link external/
  licensed material (CnCCookbook, Internet Archive, referenceglobe, Eagle, ResearchGate, BCIT).
- **Bilingual toggle:** `<html>` class `lang-vi`/`lang-en`; `.t-vi`/`.t-en` spans; `localStorage`.
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
├── books/index.html           # Library EN  (hosted PDFs + free/external + grading)
├── vi/books/index.html        # Library VI
├── vi/books/*.html            # 6 Vietnamese study guides (grade-A + B books)
├── education/index.html        # Education EN
├── vi/education/index.html     # Education VI
├── videos/index.html           # Video Library EN
├── vi/videos/index.html        # Video Library VI
├── books/files/                # 11 hosted PDFs (ASCII filenames)
├── education/files/            # Bharat Skills + SkilledTradesBC PDFs
├── assets/style.css            # design system (+ .grade badges added)
├── assets/favicon.svg
├── README.md
├── report.md                   # status report
└── handoff.md                 # this file
```

---

## 6. Verification snippet

```bash
sleep 60
for u in books vi/books education vi/education videos vi/videos \
         vi/books/tu-che-may-cnc.html vi/books/co-ban-lap-trinh-cnc.html \
         vi/books/cam-nang-gia-cong-cnc.html vi/books/cam-nang-sinh-vien-tormach.html \
         vi/books/lap-trinh-cnc-may-tien.html vi/books/nen-tang-gia-cong-cnc.html; do
  curl -sL "https://machine-ctm.github.io/$u" -o /tmp/p.html -w "$u -> HTTP %{http_code} %{size_download}B\n"
done
```

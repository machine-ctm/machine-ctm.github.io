# Handoff — Chế tạo máy (Machine Building) site

Continue building the bilingual machining field-guide. This document captures the
current state and the exact next steps so work can resume without re-deriving context.

---

## 1. Goal & current state

Bilingual (EN / VI) static GitHub Pages site about Machine Building / Machining.
**Done:** homepage, `/books` + `/vi/books` (11 hosted PDFs + free/external references,
A/B/C grading live), `/education` + `/vi/education`.
**Not done:** Video Library, A-book translation (both below).

Live: https://machine-ctm.github.io/ · Repo: `machine-ctm/machine-ctm.github.io` · branch `main`.

---

## 2. Pending task A — Video Library (8 YouTube videos)

A `/videos` (EN) and `/vi/videos` (VI) page pair is still to be created. Titles fetched
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

**How to build:**
- Create `videos/index.html` and `vi/videos/index.html`, modelled on the books pages
  (same top bar, hero, `sec`/`card`/`grid` classes from `assets/style.css`).
- Embed each as a responsive 16:9 player:
  `<div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden"><iframe src="https://www.youtube.com/embed/<ID>" title="<Title>" loading="lazy" style="position:absolute;inset:0;width:100%;height:100%;border:0" allowfullscreen></iframe></div>`
  (or add a reusable `.vid`/`.vid iframe` rule to `assets/style.css` instead of inline styles).
- Add nav link "Videos" in the top bar of **all** pages, a footer link, and a teaser on the homepage.
- Write EN descriptions + VI translations for each video.
- Commit, push, wait ~1–2 min, verify both `/videos` and `/vi/videos` return HTTP 200.

---

## 3. Pending task B — Translate the first A-grade book

First grade-A book in reading order = **"Build Your Own CNC Machine"**
(`books/files/build-your-own-cnc-machine.pdf`, ~11 MB). The other A books are
#7 CNC Programming Basics, #8 CNC Machining: The Complete Engineering Guide, #10 Tormach CNC Student Guide.

**Decision needed — delivery format:**
1. **Vietnamese HTML book page** (recommended): create `/vi/books/build-your-own-cnc-machine/`
   with translated, readable chapters; link it from `/vi/books`. Best fit for the site.
2. **Vietnamese PDF**: extract text → translate → re-flow into a Vietnamese PDF hosted on the site.
3. **Sample chapters first**: translate ch. 1–2 as a proof of concept, then continue.

**Suggested steps (option 1):**
- Extract text with the `workbuddy-pdf` skill (`C:\Users\Henry\AppData\Local\Programs\WorkBuddyAI\resources\app.asar.unpacked\resources\plugins\workbuddy-builtin\skills\workbuddy-pdf`).
- Translate chapter-by-chapter to Vietnamese (keep figures/diagrams references).
- Build a clean HTML book page reusing the site's CSS; add a card/link in `/vi/books`.
- Push & verify.

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
├── education/index.html        # Education EN
├── vi/education/index.html     # Education VI
├── videos/  (TODO)            # Video Library EN  — to be created
├── vi/videos/ (TODO)          # Video Library VI  — to be created
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
for u in books vi/books education vi/education videos vi/videos; do
  curl -sL "https://machine-ctm.github.io/$u/" -o /tmp/p.html -w "$u -> HTTP %{http_code} %{size_download}B\n"
done
```

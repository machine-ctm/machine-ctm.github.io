# Chế tạo máy — Project Report

**Date:** 2026-11-14
**Live site:** https://machine-ctm.github.io/
**Repository:** `machine-ctm/machine-ctm.github.io` (branch `main`)
**Scope:** Bilingual (English / Tiếng Việt) static field-guide site about **Machine Building / Machining** (Chế tạo máy — the Machine Building track of Mechanical Engineering).

---

## 1. Live pages

| Page | URL |
|---|---|
| Home | https://machine-ctm.github.io/ |
| Book Library (EN) | https://machine-ctm.github.io/books/ |
| Book Library (VI) | https://machine-ctm.github.io/vi/books/ |
| Education (EN) | https://machine-ctm.github.io/education/ |
| Education (VI) | https://machine-ctm.github.io/vi/education/ |

A **VI / EN** switch in the top bar toggles the whole page (state persisted in `localStorage`).

---

## 2. What has been built

- **Homepage** — hero (design → machining → inspection → product diagram), stats strip, discipline, process families, curriculum (5 modules + course table), tools & machines, traditional-vs-CNC comparison, careers, learning path, library/education teasers.
- **Book Library** (`/books`, `/vi/books`) — hosted PDF textbooks (Read/Download), free open-access books (Internet Archive + other free hosts), library/academic references (BCIT LibGuide, ResearchGate, etc.), a G/M-code quick reference, and an **A/B/C grade** on every hosted book (see §3).
- **Education** (`/education`, `/vi/education`) — career path, program structure, training programs/curricula (Bharat Skills, SkilledTradesBC, HUST), essential books, online training.
- Design system adapted from `pro-instcontrol.github.io` (light technical theme, burnt-orange + steel palette).

---

## 3. Book Library — hosted textbooks & A/B/C grading

Grades reflect **quality** and **ease of translation** into Vietnamese.
`A` = high quality & easy to translate · `B` = good but more technical · `C` = dense/reference (hard to translate) · `VI` = already in Vietnamese.

| # | Book | File | Grade |
|---|------|------|-------|
| 1 | Build Your Own CNC Machine | `build-your-own-cnc-machine.pdf` | **A** |
| 2 | Giáo trình Công nghệ Chế tạo máy | `giao-trinh-cong-nghe-che-tao-may.pdf` | VI |
| 3 | Giáo trình Nguyên lý máy | `gt-nguyen-ly-may.pdf` | VI |
| 4 | Giáo trình Thiết kế Đồ án Chi tiết máy | `gt-tk-dacn-ctm.pdf` | VI |
| 5 | Metal Forming Handbook (Schuler, 1998) | `metal-forming-handbook-schuler-1998.pdf` | **C** |
| 6 | CNC Programming for Lathe | `cnc-programming-for-lathe.pdf` | **B** |
| 7 | CNC Programming Basics | `cnc-programming-basics.pdf` | **A** |
| 8 | CNC Machining: The Complete Engineering Guide | `cnc-machining-complete-guide.pdf` | **A** |
| 9 | Fundamentals of CNC Machining | `fundamentals-of-cnc-machining.pdf` | **B** |
| 10 | Tormach CNC Student Guide | `tormach-cnc-student-guide.pdf` | **A** |
| 11 | Machining Processes and Machines | `machining-processes-and-machines.pdf` | **C** |

**First grade-A book in reading order → "Build Your Own CNC Machine"** (the translation candidate).

Verified live: EN `/books` returns `A=4, B=2, C=2`; all 6 newly added PDFs resolve; VI mirrors the same grades.

---

## 4. Free online books & library references (linked externally, not re-hosted)

- **Internet Archive (free):** Smid *CNC Programming Handbook*, Rose *Modern Machine-Shop Practice* (public domain), Cleveland *Use and Care of Twist Drills*, Paquin *Die Design Fundamentals*, Oberg *Machinery's Handbook* (borrowable).
- **Other free hosts:** Boothroyd *Fundamentals of Machining and Machine Tools* (referenceglobe.com), Eagle Group *CNC Machining Process Guide* (blog).
- **Library / academic:** BCIT Machinist LibGuide, *CNC Trade Secrets* (WorldCat), ResearchGate paper *Machining Processes and Machines* (publication link — direct download is login-walled).

---

## 5. Pending work

1. **Video Library (NOT started).** Eight YouTube videos were requested but not yet built into `/videos` (EN) and `/vi/videos` (VI). IDs/titles are captured in `handoff.md`.
2. **Translate the first A-grade book** ("Build Your Own CNC Machine") into Vietnamese and add it to `/vi/books`. Delivery format (Vietnamese HTML book page vs. PDF vs. sample chapters) is still to be decided.
3. *(Optional)* The Eagle Group and Boothroyd PDFs are currently linked **externally** in the free-books section; local copies already exist in `books/files/` if you later want them as hosted "Read/Download" cards.

---

## 6. Notes & conventions

- **Copyright:** external/licensed resources are **linked**, not re-hosted; only the user's own PDFs from `E:\Ebooks\Che Tao May` are hosted on the site.
- **Deploy token** is stored in `E:\Documents\Github Repos\machine-ctm.txt` (a GitHub PAT). Never print it in logs/output.
- **GitHub Pages rebuild** takes ~1–2 minutes after a push (longer for large binary commits); verify only after waiting.
- **Bilingual implementation:** `<html>` gets class `lang-vi`/`lang-en`; `.t-vi`/`.t-en` spans switch; state in `localStorage`.

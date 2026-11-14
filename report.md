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
| Video Library (EN) | https://machine-ctm.github.io/videos/ |
| Video Library (VI) | https://machine-ctm.github.io/vi/videos/ |
| Build Your Own CNC Machine — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/tu-che-may-cnc.html |
| CNC Programming Basics — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/co-ban-lap-trinh-cnc.html |
| CNC Machining: The Complete Engineering Guide — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/cam-nang-gia-cong-cnc.html |
| Tormach CNC Student Guide — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/cam-nang-sinh-vien-tormach.html |

A **VI / EN** switch in the top bar toggles the whole page (state persisted in `localStorage`).

---

## 2. What has been built

- **Homepage** — hero (design → machining → inspection → product diagram), stats strip, discipline, process families, curriculum (5 modules + course table), tools & machines, traditional-vs-CNC comparison, careers, learning path, library/education teasers.
- **Book Library** (`/books`, `/vi/books`) — hosted PDF textbooks (Read/Download), free open-access books (Internet Archive + other free hosts), library/academic references (BCIT LibGuide, ResearchGate, etc.), a G/M-code quick reference, and an **A/B/C grade** on every hosted book (see §3).
- **Vietnamese study guides** — 4 original Vietnamese adaptations of the grade-A books under `/vi/books/` (see §5), each an ~11-section illustrated guide with a copyright note, G-code examples and cross-links.
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

## 5. Translation job & remaining work

1. **Video Library — DONE.** Eight YouTube videos built into `/videos` (EN) and `/vi/videos` (VI) with responsive embeds; nav wired into all page pairs.
2. **First A-grade book translated to Vietnamese — DONE (original adaptation).** "Build Your Own CNC Machine" → `vi/books/tu-che-may-cnc.html`, an original Vietnamese study guide (11 sections, copyright note + link to original PDF). Wired into both `/books` and `/vi/books` cards. A verbatim full translation was deliberately avoided to respect Apress copyright.
3. **Remaining A-grade books translated to Vietnamese — DONE (original adaptations).** All three remaining grade-A books now have Vietnamese study guides, so the A-grade translation job is complete (4/4):
   - `CNC Programming Basics` → `vi/books/co-ban-lap-trinh-cnc.html` (11 sections: hệ tọa độ, loại máy, tuyệt đối/tương đối, nội suy, định dạng khối lệnh, mã G/M, offset gốc, ví dụ phay + tiện G-code).
   - `CNC Machining: The Complete Engineering Guide` → `vi/books/cam-nang-gia-cong-cnc.html` (11 sections: nguyên lý cắt gọt, lược sử, máy 3/5 trục, lợi ích/hạn chế, ứng dụng vs in 3D, thiết kế DFM + bảng quy tắc, undercuts, vật liệu/bề mặt, 3 mẹo giảm chi phí và 3 bước bắt đầu).
   - `Tormach CNC Student Guide` → `vi/books/cam-nang-sinh-vien-tormach.html` (11 sections: 7 quy tắc an toàn, bảng thuật ngữ, hệ tọa độ máy/WCS, G-code + ví dụ, dao & đồ gá, tổng quan máy, Mach3, Fusion 360 CAD/CAM, quy trình 10 bước).
   - All four pages use the site design system, carry a **copyright note** (original adaptation, not a verbatim translation), link back to the original PDF, and are **cross-linked** to each other. Wired into the A-grade cards of both `/books` (EN, "Bản TV" buttons) and `/vi/books` (VI, "Bản TV" buttons).
   - Bug fixed: `tu-che-may-cnc.html` had PDF links using `../books/files/...` (nonexistent path); corrected to `../../books/files/...`.
4. *(Optional)* The Eagle Group and Boothroyd PDFs are currently linked **externally** in the free-books section; local copies already exist in `books/files/` if you later want them as hosted "Read/Download" cards.
5. *(Optional)* Grade-B books (`CNC Programming for Lathe`, `Fundamentals of CNC Machining`) could get similar Vietnamese pages; grade-C reference works are intentionally left out (dense, hard to translate).

---

## 6. Notes & conventions

- **Copyright:** external/licensed resources are **linked**, not re-hosted; only the user's own PDFs from `E:\Ebooks\Che Tao May` are hosted on the site.
- **Deploy token** is stored in `E:\Documents\Github Repos\machine-ctm.txt` (a GitHub PAT). Never print it in logs/output.
- **GitHub Pages rebuild** takes ~1–2 minutes after a push (longer for large binary commits); verify only after waiting.
- **Bilingual implementation:** `<html>` gets class `lang-vi`/`lang-en`; `.t-vi`/`.t-en` spans switch; state in `localStorage`.

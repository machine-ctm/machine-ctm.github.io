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
| Foundation Science (EN) | https://machine-ctm.github.io/foundation/ |
| Foundation Science (VI) | https://machine-ctm.github.io/vi/foundation/ |
| In-browser Reader (EN) | https://machine-ctm.github.io/reader.html |
| In-browser Reader (VI) | https://machine-ctm.github.io/vi/reader.html |
| Build Your Own CNC Machine — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/tu-che-may-cnc.html |
| CNC Programming Basics — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/co-ban-lap-trinh-cnc.html |
| CNC Machining: The Complete Engineering Guide — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/cam-nang-gia-cong-cnc.html |
| Tormach CNC Student Guide — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/cam-nang-sinh-vien-tormach.html |
| CNC Programming for Lathe — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/lap-trinh-cnc-may-tien.html |
| Fundamentals of CNC Machining — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/nen-tang-gia-cong-cnc.html |
| Metal Forming Handbook — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/cam-nang-gia-cong-ap-luc.html |
| Machining Processes and Machines — TIẾNG VIỆT | https://machine-ctm.github.io/vi/books/quy-trinh-va-may-gia-cong.html |
| Consolidated Vietnamese guides index | https://machine-ctm.github.io/vi/books/#huong-dan |

The **homepage** has a VI / EN toggle in the top bar (`.t-vi` / `.t-en` spans, state persisted in `localStorage`). All other pages are separate EN / VI files paired by a language switcher; `/vi/**` navigation links resolve to the VI sibling sections.

---

## 2. What has been built

- **Homepage** — hero (design → machining → inspection → product diagram), stats strip, discipline, process families, curriculum (5 modules + course table), tools & machines, traditional-vs-CNC comparison, careers, learning path, library/education teasers.
- **Book Library** (`/books`, `/vi/books`) — hosted PDF textbooks opened through the in-browser Reader (Read ▸) with parallel Download links, free open-access books (Internet Archive + other free hosts), library/academic references (BCIT LibGuide, ResearchGate, etc.), a G/M-code quick reference, an **A/B/C grade** on every hosted book (see §3), and a `#foundation-science` cross-list section surfacing the 13 Foundation science titles (see §5 item 11).
- **Vietnamese study guides** — 8 original Vietnamese adaptations under `/vi/books/`, covering **every graded English book** (4 grade-A + 2 grade-B + 2 grade-C, see §5). Each is an ~8–11-section illustrated guide with a copyright note, source-PDF link and cross-links to the other seven. A consolidated eight-card index lives at `/vi/books/#huong-dan`, linked from both library heroes and from every guide.
- **Education** (`/education`, `/vi/education`) — career path, program structure, training programs/curricula (Bharat Skills, SkilledTradesBC, HUST), essential books, online training.
- **Foundation Science** (`/foundation`, `/vi/foundation`) — 13 free science books per language (26 total), grouped into **Maths · Physics · Chemistry · General Science**, with a lively, curiosity-first tone for young readers (puzzles, vintage science-show tricks, stories of the elements, a gentle tour of the universe). The PDFs are **re-hosted same-origin** in `books/files/` (so the in-browser Reader can embed them) **and mirrored** on the `foundation-v1` GitHub Release; every book credits its source and links back to it. Only freely downloadable works are included (public-domain classics, Project Gutenberg, US DOE handbooks, Internet Archive items under free/CC licences) — no borrowed/lending copies.
- Design system adapted from `pro-instcontrol.github.io` (light technical theme, burnt-orange + steel palette).

---

## 3. Book Library — hosted textbooks & A/B/C grading

Grades reflect **quality** and **ease of translation** into Vietnamese.
`A` = high quality & easy to translate · `B` = good but more technical · `C` = dense/reference (hard to translate). In this report's table, `VI` additionally marks the three natively-Vietnamese lecture-note PDFs; the live site indexes use only A/B/C for the English books, all of which now have Vietnamese guides.

These 11 rows are the **machining textbooks**. The library also re-hosts the 26 Foundation science titles same-origin (see §5 item 11), so `books/files/` now holds **37 PDFs** in total (11 + 26); the `foundation-v1` GitHub Release remains a mirror of the 26 science titles.

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

**First grade-A book in reading order → "Build Your Own CNC Machine"** (the first book adapted into a Vietnamese study guide).

Verified live: EN `/books` returns `A=4, B=2, C=2`; all 6 newly added PDFs resolve; VI mirrors the same grades.

> **Source discovery (grade C):** `machining-processes-and-machines.pdf` is the **32-page CRC Press / Taylor & Francis publisher preview** (copyright page, complete table of contents, preface, and Chapter 1 only) — **not the full 16-chapter book**. The library card copy that previously claimed "full PDF hosted here" was corrected in both EN and VI indexes; the ResearchGate card now explicitly points to obtaining the full text. `metal-forming-handbook-schuler-1998.pdf` is the complete 573-page Springer/Schuler handbook.

---

## 4. Free online books & library references (linked externally, not re-hosted)

- **Internet Archive (free):** Smid *CNC Programming Handbook*, Rose *Modern Machine-Shop Practice* (public domain), Cleveland *Use and Care of Twist Drills*, Paquin *Die Design Fundamentals*, Oberg *Machinery's Handbook* (borrowable).
- **Other free hosts:** Boothroyd *Fundamentals of Machining and Machine Tools* (referenceglobe.com), Eagle Group *CNC Machining Process Guide* (blog).
- **Library / academic:** BCIT Machinist LibGuide, *CNC Trade Secrets* (WorldCat), ResearchGate paper *Machining Processes and Machines* (publication link — direct download is login-walled).

---

## 5. Translation job — complete (8/8)

1. **Video Library — DONE.** Eight YouTube videos built into `/videos` (EN) and `/vi/videos` (VI) with responsive embeds; nav wired into all page pairs.
2. **First A-grade book translated to Vietnamese — DONE (original adaptation).** "Build Your Own CNC Machine" → `vi/books/tu-che-may-cnc.html`, an original Vietnamese study guide (11 sections, copyright note + link to original PDF). Wired into both `/books` and `/vi/books` cards. A verbatim full translation was deliberately avoided to respect Apress copyright.
3. **Remaining A-grade books translated to Vietnamese — DONE (original adaptations).** All three remaining grade-A books now have Vietnamese study guides, so the A-grade translation job is complete (4/4):
   - `CNC Programming Basics` → `vi/books/co-ban-lap-trinh-cnc.html` (11 sections: hệ tọa độ, loại máy, tuyệt đối/tương đối, nội suy, định dạng khối lệnh, mã G/M, offset gốc, ví dụ phay + tiện G-code).
   - `CNC Machining: The Complete Engineering Guide` → `vi/books/cam-nang-gia-cong-cnc.html` (11 sections: nguyên lý cắt gọt, lược sử, máy 3/5 trục, lợi ích/hạn chế, ứng dụng vs in 3D, thiết kế DFM + bảng quy tắc, undercuts, vật liệu/bề mặt, 3 mẹo giảm chi phí và 3 bước bắt đầu).
   - `Tormach CNC Student Guide` → `vi/books/cam-nang-sinh-vien-tormach.html` (11 sections: 7 quy tắc an toàn, bảng thuật ngữ, hệ tọa độ máy/WCS, G-code + ví dụ, dao & đồ gá, tổng quan máy, Mach3, Fusion 360 CAD/CAM, quy trình 10 bước).
   - All four pages use the site design system, carry a **copyright note** (original adaptation, not a verbatim translation), link back to the original PDF, and are **cross-linked** to each other. Wired into the A-grade cards of both `/books` (EN, "Bản TV" buttons) and `/vi/books` (VI, "Bản TV" buttons).
   - Bug fixed: `tu-che-may-cnc.html` had PDF links using `../books/files/...` (nonexistent path); corrected to `../../books/files/...`.
4. **Grade-B books translated to Vietnamese — DONE (original adaptations).** Both grade-B books now have Vietnamese study guides, so the translation job covers all A- and B-grade books (6/6):
   - `CNC Programming for Lathe` → `vi/books/lap-trinh-cnc-may-tien.html` (8 sections: cấu tạo máy tiện & trục X/Z, cấu trúc khối lệnh/địa chỉ, các hàm G/S/T/M, tuyệt đối/tương đối & lập trình theo đường kính, G00/G01/G02/G03/G04, hệ tọa độ & G28, chương trình tiện mẫu có chú thích). Nguồn là khóa e‑learning *The Basics of CNC Machining Programming (for Lathe)* (© Mitsubishi Electric) — ghi rõ định dạng lệnh thay đổi theo nhà sản xuất máy.
   - `Fundamentals of CNC Machining` → `vi/books/nen-tang-gia-cong-cnc.html` (10 sections: quy trình CAD/CAM/CNC & SRP, an toàn xưởng, dao cắt & thông số cắt, hệ tọa độ & offset/TLO, ngôn ngữ G/M & canned cycles, quy trình vận hành máy, đường chạy dao 2D, tiện CNC & 3D, đồ gá/kẹp phôi). Nguồn là giáo trình *Fundamentals of CNC Machining: A Practical Guide for Beginners* (© Autodesk) — văn bản gốc cấm dịch/sao chép nên bản này được **viết lại hoàn toàn**, ghi rõ "không phải bản dịch".
   - Cả hai dùng chung design system, có copyright note, liên kết PDF gốc, và được **cross-link** với 4 trang A-grade. Đã nối vào card grade-B của cả `/books` (EN) và `/vi/books` (VI). Tất cả 6 trang hiện liên kết chéo tới 5 trang còn lại.
5. **Grade-C reference works — DONE (original adaptations).** Both dense academic references now have Vietnamese study guides, so **all 8 graded English books (A+B+C) are covered**:
   - `Metal Forming Handbook` → `vi/books/cam-nang-gia-cong-ap-luc.html` (8 sections: DIN 8580 classification, flow stress/flow curve/formability, press design & drives, dies & deep drawing, blanking/fine blanking/bending, hydroforming, solid forming/forging, and how to use a 573-page reference). Source: Schuler / Springer 1998, which explicitly reserves translation rights — the page states it is **not a translation**.
   - `Machining Processes and Machines` → `vi/books/quy-trinh-va-may-gia-cong.html` (9 sections: book overview & publisher-preview disclosure, the machining system and the three cutting conditions `v/f/d`, four process families, industrial applications & limitations, roughing vs finishing table, machinability & machinable materials, the 4-part/16-chapter map, and shop-floor calculations). Source: Zainul Huda, CRC Press 2021 — © Taylor & Francis prohibits reproduction, so this is an original adaptation of Chapter 1 + the full TOC only.
   - Both pages carry explicit copyright notes, link back to the source PDF, and are cross-linked to the other seven. Wired into the grade-C cards of both `/books` and `/vi/books` ("Bản TV" button + inline link).
6. **Consolidated guide index & cross-links — DONE.** `/vi/books/#huong-dan` is a new section with all 8 guides as grade-badged cards plus a copyright note; it is linked from the VI hero CTA, the textbooks section header, the EN hero (bilingual link), and the conclusion of every guide. Section numbering in the VI index was shifted 01–06 and alternating `sec`/`sec alt` bands preserved. All 8 guides now carry a normalized 7-link "Các bản tiếng Việt khác" line plus a "Tất cả 8 bản" link.
7. **Correction:** an earlier version of this report claimed local copies of the Eagle Group and Boothroyd PDFs "already exist in `books/files/`". They do **not** — both are linked **externally only** (referenceglobe.com / Eagle Group hub), consistent with the site's copyright convention of not re-hosting licensed material. `books/files/` holds exactly 11 PDFs. A second false claim — that the *full* `Machining Processes and Machines` PDF was hosted — was also corrected (see §3 note).
8. **Full-site consistency audit — DONE.** With the translation job complete, all 15 HTML pages were revalidated (tag balance, local link & anchor resolution, CJK contamination, bare ampersands, undefined CSS classes, duplicate IDs): **0 real problems**. Fixed a genuine bilingual navigation bug: every `/vi/**` page linked "Sách / Giáo dục / Video" to the **English** `/books/`, `/education/`, `/videos/` sections instead of `/vi/books/`, `/vi/education/`, `/vi/videos/`; 32 lines across 11 files corrected (language switchers, homepage links and PDF paths deliberately left unchanged). Refreshed stale "five core textbooks / 5 textbooks / năm giáo trình" copy on the homepage teaser and both library indexes to reflect **11 hosted PDFs + 8 Vietnamese guides**, and added a direct homepage link to `/vi/books/#huong-dan`. `README.md` was rewritten: it still described the site as "a single self-contained page" with 5 textbooks and a 3-file structure tree.
9. **Crawler discoverability, metadata & error handling — DONE.** Added `sitemap.xml` (all 17 content pages with `lastmod` / `changefreq` / `priority`, plus reciprocal `xhtml:link hreflang` alternates for the 4 EN/VI page pairs and `x-default` for the bilingual homepage), `robots.txt` (allow all + sitemap reference), and a custom bilingual `404.html` in the site design system with the homepage language toggle, links to both libraries / guides / education / videos, and `noindex`. All 17 content pages now carry `<link rel="canonical">`, Open Graph (`og:type`, `og:site_name`, `og:title`, `og:description`, `og:url`) and `twitter:card` tags, plus reciprocal `hreflang` on the 8 paired pages. `404.html` is intentionally excluded from the sitemap. Audited 26 external URLs: 23 real links return 200; the two font preconnect origins return 404 by design and ResearchGate returns 403 to bots (works in a browser). Accessibility audit (`h1` count, heading skips, `img` alt, `svg` aria-label, `iframe` title, skip links, `target=_blank` rel, empty link text) found no defects — the only SVG flag is the logo inside an `aria-hidden` parent.
10. **Foundation Science section — DONE.** Added `/foundation` (EN) and `/vi/foundation` (VI) as two new content sections covering basic science (Maths, Physics, Chemistry, General Science) for young readers. Sources were curated from `E:\Ebooks`, `E:\Health-TCM-CAM\New_Acquisitions`, and freely downloadable Internet Archive items (public-domain classics, Project Gutenberg, US DOE handbooks, CC BY-NC-ND Vietnamese titles). 13 books per language (26 total) were staged as ASCII-slugged PDFs and uploaded to a new GitHub Release `foundation-v1`. Both pages use the site design system, carry canonical / hreflang / OG / Twitter metadata, link every book to its source, and include a licence/attribution block. Nav links for "Foundation / Nền tảng" were added to the top bar of every other page (the active Foundation pages already had their own full nav + language switcher), the homepage gained a #foundation teaser section and footer link, and the new URLs were added to `sitemap.xml`. No borrowed/lending copies were included, in line with the site's copyright convention.
11. **In-browser Reader + same-origin re-hosting + cross-list — DONE.** Every locally-hosted PDF now opens inside a full-page in-browser reader (`/reader.html` EN, `/vi/reader.html` VI) instead of a new tab: a sticky top bar plus a full-height `<iframe>` whose `src` is set from a `?file=` query parameter (host-relative paths normalized to same-origin absolute URLs), with a plain download-link fallback if a non-PDF loads. Both reader pages are `noindex`. Because the reader can only embed PDFs served with `Content-Type: application/pdf` **and** `Access-Control-Allow-Origin: *` (which Pages-hosted files provide, but GitHub Release assets do **not** — they redirect to `release-assets.githubusercontent.com` with `Content-Disposition: attachment` and no CORS), the 26 Foundation science PDFs were **re-hosted same-origin** into `books/files/` so they can be read inline; the `foundation-v1` Release is kept as a mirror. `books/files/` therefore holds **37 PDFs** (11 machining + 26 science), totalling ~403 MB; the largest is `tro-choi-ly-thu-bach-khoa.pdf` at **69.8 MB**, safely under GitHub Pages' 100 MB per-file hard limit (GitHub warns above 50 MB but accepts ≤100 MB). All 11 textbook `Read ▸`/`Đọc` links, the 8 VI study-guide PDF links, and both `/education` pages' Read links now route through the reader; only external PDFs (referenceglobe, Eagle Group) keep `target="_blank"`. Both `/books` and `/vi/books` gained a `#foundation-science` cross-list section (13 EN / 13 VI science titles with Reader + sized Download + Source), plus a "books we found on the shelf but did not copy" / "Gợi ý thêm" reading-suggestion note rather than mirroring those files. Validation: tag balance 0 problems; 0 broken internal links; 0 remaining local raw-PDF new-tab links; all 28 site-hosted PDFs (11 + `education/files/` curricula + 26 science) return HTTP 200 with `application/pdf` + `Access-Control-Allow-Origin: *`. Committed (`120b031`, then `f36bf73` for a `&title=` HTML-entity decode fix) and pushed to `main`; live-verified. Note: `vi/reader.html` sits only one level deep at `/vi/`, so it uses `../assets/…` (not the `../../` of the deeper `/vi/books/*.html` guides).

---

## 6. Notes & conventions

- **Copyright:** external/licensed resources are **linked**, not re-hosted; only the user's own PDFs from `E:\Ebooks\Che Tao May` (11 machining textbooks) plus 26 freely-downloadable Foundation science titles are hosted on the site. The 26 science PDFs are all public-domain / Project Gutenberg / US DOE / Internet Archive CC works (no borrowed copies) and were re-hosted same-origin so the in-browser Reader can embed them; the `foundation-v1` Release is a mirror. `books/files/` holds **37 PDFs** (~403 MB; largest 69.8 MB, under the 100 MB Pages limit).
- **Deploy token** is stored in `E:\Documents\Github Repos\machine-ctm.txt` (a GitHub PAT). Never print it in logs/output.
- **GitHub Pages rebuild** takes ~1–2 minutes after a push (longer for large binary commits); verify only after waiting.
- **Bilingual implementation:** `<html>` gets class `lang-vi`/`lang-en`; `.t-vi`/`.t-en` spans switch; state in `localStorage`.

# Chế tạo máy — Machine Building Field Guide

A bilingual (Tiếng Việt / English) **multi-page static site** about Machine Building / Machining
(Chế tạo máy — the Machine Building track of Mechanical Engineering, Kỹ thuật Cơ khí).

**Live:** https://machine-ctm.github.io/
**Repo:** `machine-ctm/machine-ctm.github.io`, branch `main` (GitHub Pages)

The visual language is adapted from the
[pro-instcontrol field guide](https://pro-instcontrol.github.io/) layout, rethemed for
machining (burnt-orange + steel palette, light technical theme).

---

## Pages

| Page | URL | Notes |
|---|---|---|
| Home | `/` | Bilingual single page with a VI / EN toggle |
| Book Library (EN) | `/books/` | Hosted PDFs, free online books, academic references, G/M-code table |
| Book Library (VI) | `/vi/books/` | Same, plus the 8-guide consolidated index at `#huong-dan` |
| Vietnamese study guides | `/vi/books/*.html` | 8 original adaptations, one per graded English book |
| Education (EN / VI) | `/education/`, `/vi/education/` | Training programs, curricula, trade-theory PDFs |
| Video Library (EN / VI) | `/videos/`, `/vi/videos/` | 8 curated YouTube videos with responsive embeds |

The homepage toggles language in place via `.t-vi` / `.t-en` spans and `localStorage`.
All other pages are separate EN / VI files linked by a language switcher in the top bar.
`/vi/**` pages use relative paths two levels up (`../../assets/…`, `../../books/files/…`)
and link to their VI sibling sections (`../education/`, `../videos/`, `../books/`).

---

## Content

- **Homepage** — hero (design → machining → inspection → product), discipline, process families, curriculum (5 modules + core-course table), tools & machines, conventional-vs-CNC comparison, careers, learning path, library and education teasers.
- **Book Library** — **11 hosted PDFs** (3 Vietnamese lecture-note textbooks + 8 English references graded `A` / `B` / `C` for quality and ease of adaptation), each with Read / Download buttons. Also: free open-access books (Internet Archive, College Library, Eagle Group — all linked externally, not re-hosted), library / academic references (BCIT Machinist LibGuide, WorldCat, ResearchGate), a G/M-code quick reference, and a CnCCookbook G-code course link.
- **Vietnamese study guides** — 8 original, illustrated HTML adaptations under `/vi/books/`. These are written from scratch in Vietnamese from the source books' **topic structure**, not verbatim translations, because the source PDFs are copyrighted (several explicitly reserve translation rights). Every guide has 8–11 sections, diagrams or tables, a copyright note, a link back to its source PDF, and cross-links to the other seven.
- **Education** — career paths, program structure, Bharat Skills *CNC Machining Technician* trade-theory PDF, Skilled Trades BC *Machinist Harmonized Program Outline*, the HUST Mechanical Engineering program, and an online metal-machining course.
- **Video Library** — 8 YouTube videos, each with EN / VI titles and descriptions.

### Vietnamese study guides (8/8 graded English books)

| Grade | Source book | Guide |
|---|---|---|
| A | Build Your Own CNC Machine | `vi/books/tu-che-may-cnc.html` |
| A | CNC Programming Basics | `vi/books/co-ban-lap-trinh-cnc.html` |
| A | CNC Machining: The Complete Engineering Guide | `vi/books/cam-nang-gia-cong-cnc.html` |
| A | Tormach CNC Student Guide | `vi/books/cam-nang-sinh-vien-tormach.html` |
| B | CNC Programming for Lathe (Mitsubishi Electric course) | `vi/books/lap-trinh-cnc-may-tien.html` |
| B | Fundamentals of CNC Machining (Autodesk) | `vi/books/nen-tang-gia-cong-cnc.html` |
| C | Metal Forming Handbook (Schuler / Springer 1998) | `vi/books/cam-nang-gia-cong-ap-luc.html` |
| C | Machining Processes and Machines (Huda / CRC Press 2021) | `vi/books/quy-trinh-va-may-gia-cong.html` |

All eight are listed together at `/vi/books/#huong-dan`, which is linked from both library
heroes, the homepage library teaser, and the conclusion of every guide.

> **Source caveat:** `books/files/machining-processes-and-machines.pdf` is the **32-page CRC Press
> publisher preview** (front matter, full TOC, preface and Chapter 1 only) — not the full
> 16-chapter book. Its guide is built from Chapter 1 + the TOC and says so. The Schuler
> `metal-forming-handbook-schuler-1998.pdf` is the complete 573-page handbook.

---

## Copyright convention

Only the user's own PDFs (copied from `E:\Ebooks\Che Tao May`) are hosted under
`books/files/` and `education/files/`. Licensed / third-party resources are **linked** to
their original hosts, never re-hosted. The Vietnamese guides are original adaptations that
state "không phải bản dịch" and credit the source.

---

## Sources

- Chương trình đào tạo Kỹ thuật Cơ khí — Trường Đại học Bách khoa Hà Nội (SME): https://sme.hust.edu.vn/vi/dao-tao/chuong-trinh-chuan/chuong-trinh-dao-tao-ky-thuat-co-khi-2.html
- Đề cương "1.2. Kỹ thuật Cơ khí" (course outline PDF).
- Layout inspiration: https://pro-instcontrol.github.io/
- Free open-access books (Internet Archive): Smid *CNC Programming Handbook* `archive.org/details/cnc-programming-handbook-a-comprehensive-guide-to-practical-cnc-programming`, Rose *Modern Machine-Shop Practice* `archive.org/details/modernmachinesho39225gut`, Cleveland *Use and Care of Twist Drills* `archive.org/details/cleveland-use-and-care-of-twist-drills`, Paquin *Die Design Fundamentals* `archive.org/details/die-design-fundamentals-by-paquin_201908`, Oberg *Machinery's Handbook* (borrowable) `archive.org/details/machineryshandbo0000ober`.
- Boothroyd *Fundamentals of Machining and Machine Tools* (free PDF, College Library / referenceglobe.com): `referenceglobe.com/CollegeLibrary/library_books/20180120071811Fundamentals-of-Machining-and-Machine-Tools-Boothryd.pdf`.
- Eagle Group Manufacturers *CNC Machining Process Guide* (free PDF): `blog.eaglegroupmanufacturers.com/hubfs/CNC%20-%20Machining%20Process%20Guide%20-%201-28-2020-C.pdf`.
- BCIT Machinist LibGuide: https://libguides.bcit.ca/machinist/books
- ResearchGate: https://www.researchgate.net/publication/347527876_Machining_Processes_and_Machines_Fundamentals_Analysis_and_Calculations

> Academic reference site — not an official HUST site.

---

## Structure

```
machine-ctm-site/
├── index.html                 # bilingual homepage (VI/EN toggle)
├── assets/
│   ├── style.css              # shared design system
│   └── favicon.svg
├── books/
│   ├── index.html             # Book Library (EN)
│   └── files/                 # 11 hosted PDFs (ASCII filenames)
├── vi/
│   ├── books/
│   │   ├── index.html         # Book Library (VI) + #huong-dan guide index
│   │   └── *.html             # 8 Vietnamese study guides
│   ├── education/index.html
│   └── videos/index.html
├── education/
│   ├── index.html
│   └── files/                 # Bharat Skills + SkilledTradesBC PDFs
├── videos/index.html
├── README.md
├── report.md                  # project status report
└── handoff.md                 # resume / implementation notes
```

---

## Local preview

Open `index.html` directly, or serve the folder so relative links behave:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

---

## Deploy (GitHub Pages)

```bash
cd machine-ctm-site
git add -A
git commit -m "Update machining field guide"
git push origin main
```

GitHub Pages publishes the default branch automatically; allow ~1–2 minutes for the
rebuild before verifying live URLs.

**Conventions for new guides:** extract the source structure with `pypdf`
(`PdfReader(...).pages[i].extract_text()`), then write an ~8–11-section *original* adaptation
using the site's `sec` / `card` / `grid` / `steps` / `tbl` classes. Use `../../` paths for
assets and hosted PDFs, add a copyright note, wire the page into both library indexes and
the `#huong-dan` grid, and extend the cross-link line in every other guide.
`<pre>` blocks need inline styles — there is no global `pre` rule in `assets/style.css`.

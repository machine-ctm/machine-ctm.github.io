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
| Foundation Science (EN) | `/foundation/` | 13 free science books (Maths, Physics, Chemistry, General Science) served same-origin + mirrored on a GitHub Release |
| Foundation Science (VI) | `/vi/foundation/` | Same 13 books in Vietnamese, lively adaptations for young readers |
| In-browser Reader (EN) | `/reader.html` | Full-page PDF viewer for every locally-hosted PDF (`?file=` / `?title=` query), `noindex` |
| In-browser Reader (VI) | `/vi/reader.html` | Vietnamese full-page PDF viewer (same pattern, `noindex`) |

The homepage toggles language in place via `.t-vi` / `.t-en` spans and `localStorage`.
All other pages are separate EN / VI files linked by a language switcher in the top bar.
`/vi/**` pages use relative paths two levels up (`../../assets/…`, `../../books/files/…`)
and link to their VI sibling sections (`../education/`, `../videos/`, `../books/`).

**In-browser Reader.** Every locally-hosted PDF — the 11 machining textbooks, the education
curricula, and the 26 re-hosted Foundation science titles — opens inside `/reader.html` (EN) or
`/vi/reader.html` (VI) instead of a new browser tab. The reader is a sticky top bar plus a
full-height `<iframe>` whose `src` is set from a `?file=` query parameter (host-relative paths
are normalized to same-origin absolute URLs); if a non-PDF is loaded it falls back to a plain
download link. Both reader pages are marked `noindex`. **Exception:** `/vi/reader.html` sits only
one level deep at `/vi/`, so it uses `../assets/…` and `../books/` (not the `../../` used by the
deeper `/vi/books/*.html` study guides).

---

## Content

- **Homepage** — hero (design → machining → inspection → product), discipline, process families, curriculum (5 modules + core-course table), tools & machines, conventional-vs-CNC comparison, careers, learning path, library and education teasers.
- **Book Library** — **37 hosted PDFs** (11 machining textbooks + 26 Foundation science titles re-hosted same-origin), each opened through the in-browser Reader (`Read ▸`) with a parallel `Download` link. The 11 machining textbooks are 3 Vietnamese lecture-note texts + 8 English references graded `A` / `B` / `C` for quality and ease of adaptation. A `#foundation-science` cross-list section surfaces all 13 EN (and 13 VI) science titles with a "books we found on the shelf but did not copy" note. Also: free open-access books (Internet Archive, College Library, Eagle Group — all linked externally, not re-hosted), library / academic references (BCIT Machinist LibGuide, WorldCat, ResearchGate), a G/M-code quick reference, and a CnCCookbook G-code course link.
- **Vietnamese study guides** — 8 original, illustrated HTML adaptations under `/vi/books/`. These are written from scratch in Vietnamese from the source books' **topic structure**, not verbatim translations, because the source PDFs are copyrighted (several explicitly reserve translation rights). Every guide has 8–11 sections, diagrams or tables, a copyright note, a link back to its source PDF, and cross-links to the other seven.
- **Education** — career paths, program structure, Bharat Skills *CNC Machining Technician* trade-theory PDF, Skilled Trades BC *Machinist Harmonized Program Outline*, the HUST Mechanical Engineering program, and an online metal-machining course.
- **Video Library** — 8 YouTube videos, each with EN / VI titles and descriptions.
- **Foundation Science** — 13 free, openly downloadable science books per language (26 total), grouped into **Maths · Physics · Chemistry · General Science**. Written for *curiosity, not exams*: puzzles, vintage science-show tricks, the story of the chemical elements, and a gentle tour of the universe — no sign-up, no paywall. The PDFs are **re-hosted same-origin** in `books/files/` (so the in-browser Reader can embed them) **and mirrored** on the `foundation-v1` GitHub Release; every book credits its source (Internet Archive item, Project Gutenberg, US DOE handbook, or public-domain classic) and links back to it. Content tone is deliberately lively and inspiring for young readers, not dry/academic.

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

`books/files/` now holds **37 PDFs** (11 machining textbooks + 26 Foundation science titles).
The 26 science titles were **re-hosted same-origin** (they were originally only on the
`foundation-v1` Release) because the in-browser Reader can only embed PDFs served with
`Content-Type: application/pdf` **and** `Access-Control-Allow-Origin: *` — both of which
Pages-hosted files provide. GitHub Release assets redirect to `release-assets.githubusercontent.com`
with `Content-Disposition: attachment` and no CORS, which forces a download and cannot be
embedded, so they are kept only as a mirror. Pages' hard limit is 100 MB per file; the largest
re-hosted PDF is **69.8 MB** (`tro-choi-ly-thu-bach-khoa.pdf`), safely under it (GitHub warns
above 50 MB but still accepts up to 100 MB).

The **Foundation Science** PDFs are all *freely downloadable* works: public-domain classics,
Project Gutenberg editions, US Government (DOE) handbooks, and Internet Archive items released
for free download (several under CC BY-NC-ND, credited on-page). **No borrowed or lending-only
copies are included.** They are served same-origin from `books/files/` for the Reader and mirrored
on the `foundation-v1` GitHub Release; each book card links back to its source item.

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
>
> Link-check note: ResearchGate returns HTTP 403 to non-browser user agents (anti-bot); the
> publication link still resolves in a normal browser. The `fonts.googleapis.com` /
> `fonts.gstatic.com` preconnect roots also return 404 by design — they are origins, not pages.

---

## Structure

```
machine-ctm-site/
├── index.html                 # bilingual homepage (VI/EN toggle)
├── reader.html                # In-browser PDF Reader (EN, noindex) — ?file=/.../x.pdf&title=...
├── assets/
│   ├── style.css              # shared design system
│   └── favicon.svg
├── books/
│   ├── index.html             # Book Library (EN) + #foundation-science cross-list
│   └── files/                 # 37 hosted PDFs (11 machining + 26 science, ASCII filenames)
├── foundation/
│   └── index.html             # Foundation Science (EN) — PDFs same-origin + Release mirror
├── vi/
│   ├── reader.html            # In-browser PDF Reader (VI, noindex) — one level deep, uses ../assets
│   ├── books/
│   │   ├── index.html         # Book Library (VI) + #huong-dan guide index + #foundation-science
│   │   └── *.html             # 8 Vietnamese study guides
│   ├── foundation/index.html  # Foundation Science (VI)
│   ├── education/index.html
│   └── videos/index.html
├── education/
│   ├── index.html
│   └── files/                 # Bharat Skills + SkilledTradesBC PDFs
├── videos/index.html
├── 404.html                   # custom bilingual 404 (noindex)
├── sitemap.xml                # 17 content pages + 4 EN/VI hreflang pairs (reader pages excluded: noindex)
├── robots.txt                 # Allow: / + Sitemap reference
├── README.md
├── report.md                  # project status report
└── handoff.md                 # resume / implementation notes
```

Every content page carries `<link rel="canonical">`, Open Graph / Twitter tags, and — for the
three EN/VI page pairs — reciprocal `hreflang` alternates. `404.html` is deliberately excluded
from the sitemap and marked `noindex`. When adding a page, add it to `sitemap.xml` too and give
it the same metadata block (see `handoff.md` §4).

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

---

## Course Media Library

`/media/` (EN) and `/vi/media/` (VI) index **137 unique files (~1.46 GB)** collected from
the user's local course folders: *Fundamentals of Modern Manufacturing*, *Lean
Manufacturing*, *CNC Machine* (including *Fundamentals of Tool Design*), *Mechanical
Engineering* and *Mechanical Drawing*. Exact duplicates are skipped by SHA-256.

Binary files are **not committed to the Pages repo** — Pages has a ~1 GB soft limit and the
repo already holds ~400 MB of PDFs. Instead they are uploaded as assets on the
`course-media-v1` GitHub Release and linked from searchable catalog tables on both pages.
The catalog is generated from `tools/media_inventory.json` by
`tools/generate_media_pages.py`; the release is populated by
`tools/upload_release_assets.py` (PAT supplied via `GH_TOKEN`). `tools/patch_site.py` wires
the pages into the navigation, homepage and sitemap. Regenerate the pages whenever the
inventory changes.

Videos are MP4 downloads and open in any modern media player. The catalog carries a note
that these are personal study copies and that copyright remains with the original authors
and publishers.

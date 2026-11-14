# Chế tạo máy — Machine Building Field Guide

A bilingual (Tiếng Việt / English) static field guide about **Machine Building / Machining**
(Chế tạo máy — the Machine Building track of Mechanical Engineering, Kỹ thuật Cơ khí).

The site is a single self-contained page styled after the
[pro-instcontrol field guide](https://pro-instcontrol.github.io/) layout, rethemed for
machining (burnt-orange + steel palette).

## Content

- **Hero** — what machine building is, with a design → machining → inspection → product diagram.
- **01 Discipline** — definition, knowledge / skills / language outcomes.
- **02 Process families** — cutting, forming, welding, plastics & composites, precision, digital/CNC.
- **03 Curriculum** — the 5 training modules (Chế tạo máy, Khuôn dập, Hàn, Cơ khí chính xác, Chất dẻo & composite) + a condensed core-course table.
- **04 Tools & machines** — CNC, conventional tools, cutting tools, jigs & fixtures, robots, metrology, CAD/CAM, non-chip processes.
- **Comparison** — conventional vs CNC machining.
- **Careers** — employers, roles, program lengths, program director.
- **Learning path** — a 4-step study route.
- **Book library** (`/books`, `/vi/books`) — five hosted machining textbooks (read/download), CNC web references (CnCCookbook G-code course & PDF hub), a G/M-code quick reference, **free open-access books on the Internet Archive** (Smid's *CNC Programming Handbook*, Rose's *Modern Machine-Shop Practice*, *The Use and Care of Twist Drills*, *Die Design Fundamentals*), and curated library/academic references (BCIT Machinist LibGuide, *Machinery's Handbook*, *CNC Trade Secrets*, and the ResearchGate paper *Machining Processes and Machines: Fundamentals, Analysis and Calculations*).
- **Education section** (`/education`, `/vi/education`) — training programs & courses: Bharat Skills *CNC Machining Technician* 1st-year trade-theory PDF, Skilled Trades BC *Machinist Harmonized Program Outline* PDF, the HUST Mechanical Engineering program page, and an Udemy metal-machining video course.

A **VI / EN** switch in the top bar toggles the whole page (persisted in `localStorage`).

## Sources

- Chương trình đào tạo Kỹ thuật Cơ khí — Trường Đại học Bách khoa Hà Nội (SME): https://sme.hust.edu.vn/vi/dao-tao/chuong-trinh-chuan/chuong-trinh-dao-tao-ky-thuat-co-khi-2.html
- Đề cương “1.2. Kỹ thuật Cơ khí” (course outline PDF).
- Layout inspiration: https://pro-instcontrol.github.io/
- Free open-access books (Internet Archive): Smid *CNC Programming Handbook* `archive.org/details/cnc-programming-handbook-a-comprehensive-guide-to-practical-cnc-programming`, Rose *Modern Machine-Shop Practice* `archive.org/details/modernmachinesho39225gut`, Cleveland *Use and Care of Twist Drills* `archive.org/details/cleveland-use-and-care-of-twist-drills`, Paquin *Die Design Fundamentals* `archive.org/details/die-design-fundamentals-by-paquin_201908`, Oberg *Machinery's Handbook* (borrowable) `archive.org/details/machineryshandbo0000ober`.
- Boothroyd *Fundamentals of Machining and Machine Tools* (free PDF, College Library / referenceglobe.com): `referenceglobe.com/CollegeLibrary/library_books/20180120071811Fundamentals-of-Machining-and-Machine-Tools-Boothryd.pdf`.
- Eagle Group Manufacturers *CNC Machining Process Guide* (free PDF): `blog.eaglegroupmanufacturers.com/hubfs/CNC%20-%20Machining%20Process%20Guide%20-%201-28-2020-C.pdf`.
- BCIT Machinist LibGuide (books): https://libguides.bcit.ca/machinist/books
- ResearchGate paper: https://www.researchgate.net/publication/347527876_Machining_Processes_and_Machines_Fundamentals_Analysis_and_Calculations

> Academic reference page — not an official HUST site.

## Structure

```
machine-ctm-site/
├── index.html
├── assets/
│   ├── style.css
│   └── favicon.svg
└── README.md
```

## Local preview

Open `index.html` directly, or serve it:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy (GitHub Pages)

The site is served from the `machine-ctm.github.io` repository. To publish changes:

```bash
cd machine-ctm-site
git add -A
git commit -m "Update machining field guide"
git push origin main
```

GitHub Pages publishes the default branch automatically.

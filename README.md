# ProFolio — Personal Portfolio + Blog + Admin (Full-Stack)

Quyidagi hujjat **Codex’ga topshiriladigan** tarzda yozilgan, aniq va to‘liq talablar to‘plami. Maqsad: **zamonaviy, tez, mobilga mos, “wow” dizaynli** portfolio + blog + admin platforma yaratish.

---

## ✅ 1) Maqsad

Siz uchun professional developer sifatida o‘zingizni tanishtiradigan, ishlaringizni chiroyli ko‘rsatadigan va blog yozishga imkon beradigan **full‑stack portfolio** yaratiladi. Platforma:

- **Portfolio**: ishlaringiz (projects) ni vizual ko‘rinishda ko‘rsatadi.
- **Blog**: maqolalar yozish va o‘qish uchun.
- **Admin panel**: kontentni boshqarish.
- **SEO + performance**: yuqori tezlik, indekslanish, yaxshi UX.

---

## ✅ 2) Texnologiyalar (tavsiya)

### Backend (Python)
- **FastAPI** (REST API)
- PostgreSQL (yoki SQLite — dev uchun)
- SQLAlchemy + Alembic
- JWT Auth (admin uchun)
- Pydantic validation
- Docker (ixtiyoriy, lekin plus)

### Frontend (Premium dizayn)
- **Next.js (React)** + TypeScript
- TailwindCSS + shadcn/ui (yoki Chakra)
- Animatsiyalar: Framer Motion
- SEO: meta tags + OpenGraph
- Responsive: mobile-first

> Nega shunday? FastAPI juda tez va toza API beradi, Next.js esa portfolio uchun eng zo‘r SEO va dizayn imkoniyatini beradi.

---

## ✅ 3) Frontend UI bo‘limlari

### ✅ Home
- Hero section: ism, kasb, qisqa tagline
- CTA: “Hire me”, “See projects”
- Quick stats: years, projects, clients (demo)
- Featured projects (top 3)
- Testimonials slider (demo)
- Contact preview

### ✅ About
- Bio + skills
- Timeline (education/experience)
- Tech stack chips
- Download CV button (PDF upload)

### ✅ Projects
- Grid cards (rasm, title, stack, short desc)
- Filter: stack/category (Frontend, Backend, Odoo, DRF…)
- Search
- Project detail page:
  - gallery screenshots
  - features
  - tech stack
  - GitHub + Live demo links

### ✅ Blog
- Blog list (cover, tags, date, read time)
- Blog detail (markdown rendering)
- Like/view counters (optional)
- Related posts

### ✅ Contact
- Contact form
- Telegram/Email links
- Google map embed (optional)
- Form submit -> backendga yuboriladi

### ✅ Admin (separate route)
- Login (JWT)
- CRUD: Projects, Blog posts, Tags, Testimonials, Skills, Site settings
- Media upload (images)

---

## ✅ 4) Backend API talablari (FastAPI)

### Entity’lar

1) **User (Admin)**
- id, email, hashed_password, is_admin, created_at

2) **Project**
- id, title, slug, description, content (markdown), stack(list), category
- cover_image, gallery_images[]
- github_url, live_url
- is_featured, created_at, updated_at

3) **BlogPost**
- id, title, slug, excerpt, content(markdown)
- cover_image, tags[], is_published
- views, likes
- created_at, updated_at, published_at

4) **Tag**
- id, name, slug

5) **Testimonial**
- id, full_name, role, company, text, avatar(optional)

6) **Skill**
- id, name, level (0–100), category

7) **SiteSettings**
- name, title, bio, socials (telegram/github/linkedin/email), meta defaults

### API Endpoints (minimum)

#### Auth
- `POST /auth/login` -> JWT
- `GET /auth/me`

#### Public
- `GET /settings`
- `GET /projects` (filter/search/pagination)
- `GET /projects/{slug}`
- `GET /blog` (published only, pagination)
- `GET /blog/{slug}`
- `POST /contact` (send message, DBga saqlash yoki email service)

#### Admin
- CRUD endpoints: projects/blog/tags/testimonials/skills/settings
- `POST /upload` (image upload)

### Qo‘shimcha talablar
- Pagination, sorting, filtering
- Slug auto-generate
- Validation + error handling
- CORS frontend uchun
- Rate limit (contact endpoint) — ixtiyoriy

---

## ✅ 5) Dizayn va UX talablari

- Minimalist, premium, “clean”
- Dark/Light mode
- Smooth animation (hover, page transition)
- Cards + shadows + rounded
- Loading skeletons
- 90+ Lighthouse performance (target)
- Accessibility basics (buttons, aria)

---

## ✅ 6) Deliverables

Repository structure:

```
backend/   # FastAPI
frontend/  # Next.js
README.md  # setup + screenshots + demo links
```

README’da bo‘lsin:
- qanday ishga tushirish
- env variables
- database migrate
- admin login yaratish
- deploy qilish tavsiyasi (Render/Fly.io/Vercel)

---

## ✅ 7) Acceptance Criteria (Codex tekshiradi)

- ✅ Frontend saytda barcha sahifalar ishlaydi
- ✅ Responsive (mobile + desktop)
- ✅ Admin login ishlaydi, CRUD orqali kontent yangilanadi
- ✅ API dokumentatsiya (`/docs`) mavjud
- ✅ Blog post markdown render bo‘ladi
- ✅ Projects filter + search ishlaydi
- ✅ Contact form backendga yuboradi va success response beradi
- ✅ Kod clean: lint/format (black/ruff yoki eslint)

---

## ✅ 8) Bonus (Plus ball)

- Docker Compose: backend + db + frontend
- CI (GitHub Actions) tests/lint
- Unit tests (FastAPI)
- Redis cache for public endpoints
- Analytics: page views counter
- i18n (uz/ru/en)

---

## 🎯 Yakuniy natija

Siz **real mijozlarga ko‘rsatadigan** darajadagi **premium portfolio** platformaga ega bo‘lasiz: chiroyli dizayn, tez ishlash, professional admin panel va to‘liq dokumentatsiya.

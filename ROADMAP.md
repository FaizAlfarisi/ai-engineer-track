# Python Roadmap (V5)

This roadmap prioritizes depth where depth matters.

The objective is long-term competence, transfer, and independence —
not completion speed.

---

# Priority Tiers

Every topic carries a tier. The tier decides how deeply it is drilled
and what evidence closes it.

| Tier | Target Mastery | Meaning |
|------|----------------|---------|
| CORE | Level 4 — Proficient | Explain, implement independently, debug independently, combine with other concepts, make implementation decisions, read unfamiliar code using it — without relying on AI |
| SUPPORTING | Level 3 — Independent | Understand and apply confidently; documentation lookup for syntax details is acceptable |
| AWARENESS | Level 2 — Understands | Know the mental model, recognize it in code, know why it exists and when it may be useful; read basic examples |
| PROJECT-DEPENDENT | Learned on demand | Not drilled upfront. When a real project needs it: Need → Learn → Apply → Review |

Completion is evidence-based, not time-based. See `CURRICULUM.md` for
the per-tier learning pipeline and `RULES.md` for completion definitions.

---

# Stage 1 — Python Core ✅ COMPLETE

Focus: variables and references, data types, control flow, collections,
functions, problem solving, modules, basic CLI development.

| Topic | Tier |
|-------|------|
| Variables & references | CORE |
| Data types & conversion | CORE |
| Control flow (conditionals, match literals) | CORE |
| Loops | CORE |
| Functions | CORE |
| Collections (list, tuple, dict, set) | CORE |
| Modules & imports | CORE |
| Strings & formatting | SUPPORTING |
| Operators & boolean logic | SUPPORTING |
| Console I/O | SUPPORTING |
| `match` beyond literal patterns | AWARENESS (deferred — JSON in Stage 2, API responses in Stage 4) |

Problem solving / data manipulation is cross-cutting — evidenced by the
challenge CLI in every lesson, not tracked as a topic row in `PROGRESS.md`.

Stage project: Student / Inventory / Transaction CLI — an independent build
where the learner makes the implementation decisions.

Status: completed 2026-08-13 through Lessons 1–7 (evidence in `PROGRESS.md`).
The seven challenge CLIs stand in as partial stage-project evidence; a
consolidation build may be scheduled if later retrieval exposes gaps.

---

# Stage 2 — Python Application ✅ COMPLETE

Focus: turning scripts into applications — persistence, robustness,
multi-file structure, and professional workflow.

Teaching sequence (adaptive, not rigid). `✅` = completed; remaining work
is listed in priority order:

```text
✅ Exception Handling → ✅ File Handling → ✅ Pathlib → ✅ JSON → ✅ CSV
→ ✅ Packages & Multi-Module Structure → ✅ Quiz 02 (L08–L12, 84.7%)
→ ✅ Basic Typing (L14) → ✅ OOP (L15, enum folded in)
→ ✅ Dataclass (L16) → ✅ Weekly Project 2 (88/100; Environment & Dependency folded in)
```

Packages & Multi-Module Structure also covers "functions across multiple
modules" — splitting code into modules necessarily means writing and
importing functions across files, so it is not a separate topic.

Git is used continuously from the first session of this stage.
Git basics (init, add, commit, log, diff, .gitignore) are applied daily
and are already satisfied in practice — not a standalone future lesson.

| Topic | Tier | Priority |
|-------|------|----------|
| Exception handling & debugging habits | CORE | ✅ done (L8) |
| File handling | CORE | ✅ done (L9) |
| Pathlib | CORE | ✅ done (L10) |
| JSON | CORE | ✅ done (L11) |
| CSV | SUPPORTING | ✅ done (L12) |
| Packages & Multi-Module Structure | CORE | ✅ done (L13) |
| Basic typing | CORE | ✅ done (L14) |
| OOP — classes, instances, attributes, methods, composition, inheritance basics, when OOP helps and when it is unnecessary | SUPPORTING (practical, not syntax-drilled) | ✅ done (L15); Enum folds in here |
| Dataclass | SUPPORTING | ✅ done (L16), with further Enum practice |
| Environment & dependency management (venv, pip) | SUPPORTING | ✅ done (folded into WP2 kickoff, 2026-09-16) |
| Enum | AWARENESS | fold into typing/OOP; not a standalone lesson |
| Git basics (init, add, commit, log, diff, .gitignore) | SUPPORTING (applied daily) | ✅ in continuous use, not a lesson |

Stage project: **Expense / Transaction Manager** — must integrate modular
structure, persistence, JSON/CSV, validation, exceptions, typing, Git,
and readable architecture. Mandatory evidence for stage completion.

Status: completed 2026-09-16 — Weekly Project 2 (Expense / Transaction
Manager CLI) scored 88/100; T1–T17 matrix verified green (errors on
stderr + exit 1, byte-exact frozen blocks, `mypy main.py` clean).
Stage 2 CLOSED; tracking continues in `PROGRESS.md`.

Weekly projects: one every 3–4 lessons (schedule-independent).

---

# Stage 3 — Python Engineering

Focus: engineering-grade Python — testing, logging, HTTP, structure,
and the language machinery behind frameworks.

| Topic | Tier |
|-------|------|
| Debugging (systematic, traceback-driven) | CORE |
| Testing (pytest) | CORE |
| HTTP & API concepts | CORE |
| Requests | CORE |
| Project structure | CORE |
| Logging | CORE |
| Decorators | SUPPORTING |
| Iterators | SUPPORTING |
| Generators | SUPPORTING |
| Context managers | SUPPORTING |
| Regex | SUPPORTING |
| Datetime | SUPPORTING |
| Asyncio | AWARENESS / PROJECT-DEPENDENT — enough to recognize and use when a project requires it; no forced deep mastery |
| Advanced decorators, advanced generators, advanced asyncio, advanced functional programming, Python internals | PROJECT-DEPENDENT |

Lambda / map / filter are not standalone lessons — they appear naturally
inside exercises from Stage 2 onward.

Stage project: **Automation / Data Processing Toolkit** — emphasizes reusable
modules, error handling, logging, testing, HTTP/API interaction where relevant,
and maintainability. Mandatory evidence for stage completion.

Status: completed 2026-10-21 — Quiz 05 15/15 (100%); WP4-merged
capstone 96/100. Stage 3 CLOSED; tracking continues in `PROGRESS.md`.

---

# Stage 4 — Python for AI Engineering (Portfolio Sprints) ← NEXT

Focus: turning Python engineering into two public, AI-adjacent services.
Theory is just-in-time; the project is the spine. Every sprint ships a
slice; every project ships a showcase.

Completion evidence: two showcase projects, each green-tested,
demo-ready, documented, and defended live (RULES.md R12/R18/R19).

## Project A — Dataset Readiness API

Upload LLM instruction/response datasets → validate (Pydantic) → clean
(Pandas/NumPy) → export cleaned JSONL + quality report → persist runs
(SQLite). AI angle: dataset quality gate before fine-tuning or eval.

| Sprint | Slice | Topics |
|--------|-------|--------|
| A1 | Upload + validate vertical slice | HTTP/API applied · FastAPI (`UploadFile`/`File`/`Form` `multipart/form-data`, status codes, registering multiple `@app.exception_handler` handlers) · Pydantic (`BaseModel`, `Field` constraints & parameter semantics vs `@field_validator`/`@model_validator` decision rules) · OpenAPI |
| A2 | Quality engine + export | Pandas (DataFrame/Series indexing, missing/duplicate handling, vectorized transforms vs row iteration trade-offs) · NumPy (array dtypes, broadcasting, summary stats/masks) · JSONL streaming/export · data quality metrics |
| A3 | Persistence + polish | SQL & SQLite (schema design, parameterized queries, transactions/context managers, connection lifecycle) · project architecture (routes/services/repository layering, env settings) · CI & Docker · Git workflow |

## Project B — Knowledge Base Ingest API

Upload documents → chunk → store metadata → keyword search (FTS5) →
paged results. AI angle: a RAG-ready document store.

| Sprint | Slice | Topics |
|--------|-------|--------|
| B1 | Ingest + chunk vertical slice | FastAPI (ingest endpoints, pagination contracts, error envelopes) · Pydantic (nested models, config/validation trade-offs) · file handling & deterministic text chunking (size/overlap trade-offs) · SQLite persistence |
| B2 | Search + ORM | SQLAlchemy (models, session lifecycle, ORM vs raw SQL decision rules) · SQL & SQLite FTS5 (`MATCH`, ranking, `SearchBackend` protocol/interface boundary) · Pandas corpus stats |
| B3 | Resilience + polish | asyncio applied (sync vs async route/I/O decision rules) · HTTP resilience (timeouts, exponential backoff retries, idempotency) · structured logging · API-key auth-lite dependency · CI & Docker · Git workflow |

## Topic map

| Topic | Tier | Where |
|-------|------|-------|
| Pydantic | CORE | A1, B1 |
| FastAPI | CORE | A1, A3, B1, B3 |
| HTTP/API (applied) | CORE | A1, B3 |
| NumPy fundamentals | CORE | A2 |
| Pandas fundamentals | CORE | A2, B2 |
| Project architecture | CORE | A3, B3 |
| Git workflow | CORE | every sprint |
| SQL fundamentals | CORE | A3 |
| SQLite | SUPPORTING | A3, B1 |
| SQLAlchemy | SUPPORTING | B2 |

PROJECT-DEPENDENT — learned only when the sprint needs them: Docker, CI
(GitHub Actions), OpenAPI docs, API-key auth, FTS5, retries/timeouts,
deployment, environment/secrets, background tasks.

Lambda/map/filter stay natural, not standalone. The learner does not
need to become a database engineer — practical ability only. LLM APIs
are deferred to Stage 5; Stage 4 builds the services those systems need.

Project B's search is SQLite FTS5 behind a `SearchBackend` interface, so
a vector backend can replace it later without touching the API layer.

Docker and CI are part of the Showcase Pack but are taught or PROVIDED
in the sprint that needs them (A3/B3) — never silently required
(`LEARNER.md` Tool Sync).

Sprint A0 is setup only (repos, briefs, environment), not a learning
sprint. Stage 4 completion: both projects pass code review AND the
showcase gate, and the learner defends each (5 questions). See
`PORTFOLIO.md`.

---

# Parallel Track — Interview / DSA

Maintained separately in `DSA_TRACK.md`. One DSA session per week,
interleaved with the main roadmap. Never mixed into stage lessons.

Purpose: interview readiness, not competitive programming.

---

Completion of this roadmap marks the end of the Python phase and the
beginning of Applied AI Engineering.

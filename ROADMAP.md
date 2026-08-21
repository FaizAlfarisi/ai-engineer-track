# Python Roadmap (V2)

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

Completion is evidence-based, not time-based. There are no duration estimates.

See `CURRICULUM.md` for the per-tier learning pipeline and `RULES.md`
for the per-tier completion definitions.

---

# Stage 1 — Python Core ✅ COMPLETE

Focus: variables and references, data types, control flow, collections,
functions, problem solving, modules, basic CLI development.

| Topic | Tier |
|-------|------|
| Control flow (conditionals, match, loops) | CORE |
| Collections (list, tuple, dict, set) | CORE |
| Functions | CORE |
| Problem solving / data manipulation | CORE |
| Modules & imports | CORE |
| Variables, references, data types | CORE |
| Strings & formatting | SUPPORTING |
| Operators & boolean logic | SUPPORTING |
| Console I/O | SUPPORTING |
| `match` beyond literal patterns | AWARENESS (deferred — JSON in Stage 2, API responses in Stage 4) |

Stage project: Student / Inventory / Transaction CLI — an independent build
where the learner makes the implementation decisions.

Status: completed 2026-08-13 through Lessons 1–7 (evidence in `PROGRESS.md`).
The seven challenge CLIs stand in as partial stage-project evidence; a
consolidation build may be scheduled if later retrieval exposes gaps.

---

# Stage 2 — Python Application ← CURRENT

Focus: turning scripts into applications — persistence, robustness,
multi-file structure, and professional workflow.

Teaching sequence (adaptive, not rigid):

```text
Exception Handling → File Handling → Pathlib → JSON → CSV
→ Packages & Multi-Module Structure → Typing Basics
→ OOP (practical) → Dataclasses → Environment & Dependency Management
```

Git is used continuously from the first session of this stage
(commit after every session).

| Topic | Tier |
|-------|------|
| Exception handling & debugging habits | CORE |
| File handling | CORE |
| JSON | CORE |
| Pathlib | CORE |
| Modules & packages across multiple files | CORE |
| Functions applied across multiple modules | CORE (Stage 1 reinforcement) |
| Basic typing | CORE |
| OOP — classes, instances, attributes, methods, composition, inheritance basics, when OOP helps and when it is unnecessary | SUPPORTING (practical, not syntax-drilled) |
| Dataclass | SUPPORTING |
| CSV | SUPPORTING |
| Environment & dependency management (venv, pip) | SUPPORTING |
| Git basics (init, add, commit, log, diff, .gitignore) | SUPPORTING (applied daily) |
| Enum | AWARENESS |

Stage project: **Expense / Transaction Manager** — must integrate modular
structure, persistence, JSON/CSV, validation, exceptions, typing, Git,
and readable architecture. Mandatory evidence for stage completion.

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

---

# Stage 4 — Python for AI Engineering

Focus: the Python skills that directly support Applied AI Engineering.

| Topic | Tier |
|-------|------|
| Pydantic | CORE |
| FastAPI | CORE |
| HTTP/API (applied) | CORE |
| NumPy fundamentals | CORE |
| Pandas fundamentals | CORE |
| Project architecture | CORE |
| Git workflow | CORE |
| SQL fundamentals | CORE |
| SQLite | SUPPORTING |
| SQLAlchemy | SUPPORTING |

The learner does not need to become a database engineer. Practical ability only.

Stage project: **AI Dataset Manager / AI Service** — bridges Python into
Applied AI Engineering. Mandatory evidence for stage completion.

---

# Parallel Track — Interview / DSA

Maintained separately in `DSA_TRACK.md`. One DSA session per week,
interleaved with the main roadmap. Never mixed into stage lessons.

Purpose: interview readiness, not competitive programming.

---

Completion of this roadmap marks the end of the Python phase and the
beginning of Applied AI Engineering.

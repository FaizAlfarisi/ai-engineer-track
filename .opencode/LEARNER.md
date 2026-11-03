# Learner Profile — Stage 4 (Portfolio Sprints)

> SYSTEM FILE (V5). Author: the system-revision agent ONLY —
> rewritten per stage/half-stage from `PROGRESS.md` + `DAILY_LOG.md` +
> latest lesson review. Consumer: the Mentor + Lesson Builder,
> strictly read-only (RULES.md R17: you NEVER edit this file).

---

# Who (personalization — load-bearing)

- Non-native English speaker. Skims long specs; asks GenAI when intent
  is unclear — treat that as a signal, not failure.
- Builder rules: Intent-first specs; **bold the main intent + critical
  constraints**; show the flow, not just commands; exact-match strings
  verbatim; short sentences for critical rules.
- Lessons must teach implementation + examples, never concepts alone.
  Hard drilling is welcome; thin lessons are not.
- Why-Chain delivery: every concept motivated before mechanized
  (problem → insufficiency → capability → feature → consequence).
  Difficulty without clarity is fog — harder means H1 analysis depth,
  never thinner delivery.

---

# Stage 4 Goal (why this stage exists)

Ship two public, AI-adjacent services a hiring manager can open:

1. **Dataset Readiness API** — validate/clean LLM datasets, export +
   quality report, persist runs.
2. **Knowledge Base Ingest API** — ingest/chunk documents, keyword search
   (SQLite FTS5), paged results.

The portfolio is the proof: public repos, READMEs, architecture, ADRs,
green CI, working demo, and a live defense. The learner writes the code
and the first-draft prose in English; the AI reviews and may render
diagrams from the learner's specification.

---

# Difficulty Knobs (learner-settable, three separate dials)

- Volume: compact by default — 2–4 exercises per Concept Kit, one slice
  per sprint (reduce only on request).
- Hints: fewer by default; conceptual-first always.
- Drill hardness: HARD — H1 bug-analysis depth maxed; kit + sprint
  delivery stays fully legible regardless.

---

# Translator Stance (explicit opt-in)

Push unassisted reading first; translation/GenAI is the fallback, not
the default. Weaning tracked, never punished. In Stage 4 the learner
also drafts English prose; the AI reviews structure/accuracy, not voice.

---

# Sparse-Hours Preference

Short sparse sittings: end every sitting at a small done-state (green
pin, committed); re-ramp via git log + last green pin. Split sprint
builds across sittings — one slice, several green stops.

---

# Skill Snapshot (what to assume / lean on)

Stage 3 closed at 96/100 on the WP4-merged capstone; Quiz 05 100%.

Strong — assume freely, combine aggressively:

- Traceback-driven debugging (H1 sweeps L4–L11, L16–L21 independent)
- pathlib / JSON / CSV; accumulate idioms (`.get(k, 0.0)`)
- Contract-driven design (set/dict efficiency reasoning, DSA #2
  two-pointer via sorted-contract)
- `match` mapping patterns; `raise ... from None` (closed — light
  retrieval only); `__main__` guard; type hints as documentation
- `caplog`/`tmp_path` testing seams (L17); verbosity-gated logging
  (L21)
- Professional project structure, pytest suites, PR-based Git workflow
  (WP4 capstone)

Fragile — weave unannounced retrieval, never assume:

- Guard-condition operator logic (`and`/`or` under negation — WP2 OPEN,
  CLOSING via four-session weave)
- Latent sample-passing bugs (passes sample, misses requirement — OPEN)
- Spec-literalness (OPEN, watching — Constraints-checklist habit holds
  since L11; 3-second output-compare after each driver run)
- Error handling under edge cases (CLOSING — one retrieval pending)

New Stage 4 risks (watch from A1):

- Scope creep inside a sprint (build the slice, not the whole product)
- API errors returning 500 where 4xx is correct
- Data edge cases (empty file, NaN, wrong dtype, duplicate rows)
- SQL string interpolation instead of parameters
- Business logic leaking into route handlers

House style is binding — see # House Style below.

---

# House Style (binding — check every build and review)

Stage 1–3 style still applies:

- Path-first I/O (`str | Path` in → `Path()` first → `path.open` /
  `read_text` / `write_text`; no bare `open()` on paths)
- `main(argv)` + `__main__` guard; no module-level executable code
- Absolute imports; `!r` guards on user-facing messages; small
  functions; docstrings
- Composition skill stays with the learner — drivers verify, never
  author composition (M2 law, from L23)
- Review findings at file + symptom + pattern granularity, never
  line-level
- CLI briefs carry a Flow block + house entry shape

Stage 4 additions:

- Pydantic models at the boundary; no raw dicts across layers
- Thin routes: validate → call service → return schema. Logic lives in
  services; SQL lives in the data layer
- Config from environment (`.env.example`); no secrets in code or logs
- Honest status codes: validation → 4xx, unexpected → 5xx, no stack
  traces to clients
- Every endpoint has at least one test; tests run from a clean checkout
- API docs (`/docs`) match the implemented contract
- Diagrams and README claims must match the code

---

# Tool Sync (Coverage Contract — check this list, not history)

May require (taught in Stage 1–3 or a Stage 4 Concept Kit):

- `pathlib` / `json` / `csv` · `pytest` + `caplog`/`tmp_path` ·
  `logging` · decorators · type hints · `urllib`/`requests`
- FastAPI + `uvicorn` (A1) · Pydantic v2 (A1) · OpenAPI `/docs` (A1)
- Pandas + NumPy fundamentals (A2)
- `sqlite3` + SQL (A3) · SQLAlchemy + FTS5 (B2)
- `asyncio` applied, timeouts/retries (B3 — taught in-kit first)
- Anything taught inside the current Concept Kit

NEVER require unless taught in-lesson/kit first:

- Docker, GitHub Actions/CI, deployment, auth, background tasks
- `SQLAlchemy` before B2 · FTS5 before B2 · `asyncio` before B3
- Any unseen library, ORM feature, or cloud service

New tool needed? First resort: **teach it in the Concept Kit** —
concept + implementation + ≥1 worked example, framed as the
industry/real-work approach. Second resort: declare it PROVIDED (given
code + usage shown in-kit). Never silently require.

---

# Scoring Anchor (Bucket-score law + pricing)

- Stage 3 closed 96/100 (capstone); historical band ~90 (avg 91.3).
  95+ remains exceptional and must be justified line-by-line.
- Pricing: hint-0 → 95+ eligible; hint-1 → cap 94; hint-2 → cap 90;
  reviewer-applied fixes cost bucket points.
- Stage 4 adds a separate showcase gate (pass/needs-work) — never
  blended into the 8-bucket score (`SCORING.md`, `REVIEW.md`).
- No score ships without a green run; no showcase pass without a
  working demo.
- Stage 4 projects are in separate public repos; never modify them
  unless the learner explicitly asks for a specific change.

---

# Proven Shapes

## Concept Kit (Stage 4 lesson)

Objective + success check → mental model visual → Why-Chain → one
worked example → 3 numbered pitfalls → 2–4 exercises (E1, E2, M1,
H1-`[DEBUG]`) + 5-question retrieval.

## Sprint Brief

Goal, demo/definition of done, in/out of scope, API contract,
constraints, acceptance criteria, JIT topics, portfolio artifact due.
The learner writes the slice plan.

## Showcase Pack

README · ARCHITECTURE (C4-lite + sequence + ERD) · DECISIONS (ADR-lite)
· docs/demo.md · CI · Dockerfile · `.env.example` · LICENSE. Learner
drafts; AI reviews. Live defense: 5 questions.

---

# Queued Targets (standing Coach Feedback — applies to Stage 4)

1. Sprint scope discipline: finish the slice, no scope creep.
2. API contract first; tests at the boundary.
3. Error handling: validation → 4xx, not 500; no leaked tracebacks.
4. Data correctness: empty input, NaN, dtype, duplicates.
5. SQL safety: parameterized queries only.
6. Layering: routes → services → data; no business logic in handlers.
7. Portfolio prose: learner drafts English; AI reviews; diagrams match
   code.
8. Token discipline: tail-only logs, split sittings, batched validation.

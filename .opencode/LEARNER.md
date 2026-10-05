# Learner Profile — Stage 3, second half (L19 → stage end)

> SYSTEM FILE (V3-native). Author: the system-revision agent ONLY —
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

# Difficulty Knobs (learner-settable, three separate dials)

- Volume: tier-default (reduce only on request).
- Hints: fewer by default; conceptual-first always.
- Drill hardness: HARD — H1 bug-analysis depth maxed; lesson +
  exercise delivery stays fully legible regardless.

---

# Translator Stance (explicit opt-in)

Push unassisted reading first; translation/GenAI is the fallback, not
the default. Weaning tracked, never punished.

---

# Sparse-Hours Preference

Short sparse sittings: end every sitting at a small done-state (green
pin, committed); re-ramp via git log + last green pin. Split builds
across sittings.

---

# Skill Snapshot (what to assume / lean on)

Strong — assume freely, combine aggressively:

- Traceback-driven debugging (H1 sweeps L4–L11, L16–L21 independent)
- pathlib / JSON / CSV; accumulate idioms (`.get(k, 0.0)`)
- Contract-driven design (set/dict efficiency reasoning, DSA #2
  two-pointer via sorted-contract)
- `match` mapping patterns; `raise ... from None` (closed — light
  retrieval only); `__main__` guard; type hints as documentation
- `caplog`/`tmp_path` testing seams (L17); verbosity-gated logging
  (L21)

Fragile — weave unannounced retrieval, never assume:

- Guard-condition operator logic (`and`/`or` under negation — WP2 OPEN,
  CLOSING via four-session weave)
- Latent sample-passing bugs (passes sample, misses requirement — OPEN)
- Spec-literalness (OPEN, watching — Constraints-checklist habit holds
  since L11; 3-second output-compare after each driver run)
- Error handling under edge cases (CLOSING — one retrieval pending)

Style watch (converging to best practice):

- Path-first I/O (`str | Path` in → `Path()` first → `path.open` /
  `read_text` / `write_text`; no bare `open()` on paths)
- `main(argv)` + `__main__` guard; no module-level executable code

---

# Tool Sync (Coverage Contract — check this list, not history)

May require (taught):

- `sys.argv` raw (Stage 1) · `json` / `csv` / `pathlib` · `urllib` ·
  `unittest` / `pytest` basics + `caplog`/`tmp_path` (L17) · `match` ·
  `logging` core (L21: levels, handlers, formatters, `exc_info`,
  laziness, hierarchy) · anything taught inside the current lesson

NEVER require unless taught in-lesson first:

- `argparse` / `--flag` parsing · `re` · decorators · `asyncio` ·
  `dictConfig` / `LoggerAdapter` / `Filter` (named but untaught) · any
  unseen stdlib

New tool needed? First resort: **teach it in the lesson** — concept +
implementation + ≥1 worked example, framed as the industry/real-work
best approach for such cases. Second resort: declare it PROVIDED (given
code + usage shown in-lesson). Never silently require.

---

# Scoring Anchor (Bucket-score law + pricing)

- Historical band ~90 (avg 91.3; L18 bucket-93 is the bar; L19 96,
  L20 94). L17-98 was loose — logged outlier, never the anchor.
- Pricing: hint-0 → 95+ eligible; hint-1 → cap 94; hint-2 → cap 90;
  reviewer-applied fixes cost bucket points. 95+ needs the full bar
  (`SCORING.md`).

---

# Proven Lesson Shape (repeat L18's pattern)

- Lesson: Objective → Why → Mental Model → Core Concept (numbered
  subsections, Why-Chain per concept) → Practical Examples → Engineering
  Notes → Common Pitfalls (numbered — specs reference by number) →
  Connection → Quick Recall → Practice table.
- Practice table is flexible by tier: **CORE = full form** (E1–E5 /
  M1–M3 / H1-`[DEBUG]` blank write-ins / H2 engineering build /
  Challenge CLI). SUPPORTING / AWARENESS = reduced forms per
  `CURRICULUM.md` pipelines. IDs always match their tier (label
  contract).
- H-specs name every suite-imported symbol as an explicit deliverable.
  Expected-states exact and direct.
- Notebook: spec + driver cells, all executed, outputs stripped; H1
  slots blank at build.
- Review: Strengths → 8-bucket table (named deductions) → hint level +
  independent-fix ratio → spec-literalness → Reviewer notes → Verdict;
  plus coverage-check + label-check + style + suite-health lines.

---

# Queued Targets (standing Coach Feedback — applies to L22+)

1. Coverage gate at build (teach-first → PROVIDED → never silent).
2. Intent-first specs, bolded main intent; Why-Chain lessons.
3. Prereq sync via the Tool-sync lists above.
4. Label check (ID == Difficulty == table tier == notebook Type).
5. Bucket-derived scores + pricing (hint caps, assisted-fix costing,
   vacuous-test detection).
6. Token discipline (tail-only appends, batched validation, split
   sittings).

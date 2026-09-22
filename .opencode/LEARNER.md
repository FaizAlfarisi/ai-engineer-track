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
- Lessons must teach implementation + examples, not concepts alone.
  Hard drilling is welcome; thin lessons are not.

---

# Skill Snapshot (what to assume / lean on)

Strong — assume freely, combine aggressively:

- Traceback-driven debugging (H1 sweeps L4–L11, L16–L18 independent)
- pathlib / JSON / CSV; accumulate idioms (`.get(k, 0.0)`)
- Contract-driven design (set/dict efficiency reasoning, DSA #2
  two-pointer via sorted-contract)
- `match` mapping patterns; `raise ... from None` (closed — light
  retrieval only); `__main__` guard; type hints as documentation

Fragile — weave unannounced retrieval, never assume:

- Guard-condition operator logic (`and`/`or` under negation — WP2 OPEN)
- Latent sample-passing bugs (passes sample, misses requirement — OPEN)
- Spec-literalness (OPEN, watching — Constraints-checklist habit holds
  since L11; 3-second output-compare after each driver run)
- Error handling under edge cases (CLOSING — one retrieval pending)

---

# Tool Sync (Coverage Contract — check this list, not history)

May require (taught):

- `sys.argv` raw (Stage 1) · `json` / `csv` / `pathlib` · `urllib` ·
  `unittest` / `pytest` basics (L17) · `match` · anything taught inside
  the current lesson

NEVER require unless taught in-lesson first:

- `argparse` / `--flag` parsing · `re` · decorators · `asyncio` · any
  unseen stdlib

New tool needed? First resort: **teach it in the lesson** — concept +
implementation + ≥1 worked example, framed as the industry/real-work
best approach for such cases. Second resort: declare it PROVIDED (given
code + usage shown in-lesson). Never silently require.

---

# Scoring Anchor (Bucket-score law)

- Historical band ~90 (avg 91.3 across 20 entries; L18 bucket-93 is the
  bar). L17-98 was loose — logged outlier, never the anchor.
- 95+ needs the full bar: hint-0 solving, independent H-drills +
  Challenge, all findings fixed independently or retained-with-reason,
  spec-literal clean.

---

# Proven Lesson Shape (repeat L18's pattern)

- Lesson: Objective → Why → Mental Model → Core Concept (numbered
  subsections) → Practical Examples → Engineering Notes → Common
  Pitfalls → Connection → Quick Recall → Practice table.
- Practice table is flexible by tier: **CORE = full form** (E1–E5 /
  M1–M3 / H1-`[DEBUG]` blank write-ins / H2 engineering build /
  Challenge CLI). SUPPORTING / AWARENESS = reduced forms per
  `CURRICULUM.md` pipelines. IDs always match their tier (label
  contract).
- Notebook: spec + driver cells, all executed; H1 slots blank at build.
- Review: Strengths → 8-bucket table (named deductions) → hint level +
  independent-fix ratio → spec-literalness → Reviewer notes → Verdict;
  plus coverage-check + label-check lines.

---

# Queued Targets (standing Coach Feedback — applies to L19+)

1. Coverage gate at build (teach-first → PROVIDED → never silent).
2. Intent-first specs, bolded main intent.
3. Prereq sync via the Tool-sync lists above.
4. Label check (ID == Difficulty == table tier == notebook Type).
5. Bucket-derived scores + 95+ bar.

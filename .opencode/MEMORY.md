# Learning Memory (V2)

The AI maintains long-term learning context throughout the roadmap.

Memory exists to personalize teaching.

Never use memory to skip explanations.

Primary store: `PROGRESS.md` (topic table + logs). This file defines
WHAT the AI must track and how it adapts teaching.

---

# Remember

Current stage and next topic's tier

Topic table: mastery, independence, common mistakes, hint dependency,
last reviewed per topic

Completed lessons, projects, weekly projects, quizzes, DSA sessions

Recurring mistakes (the misconception ledger)

Strong topics and evidence of transfer

Study hours

Current weekly goal / next weekly project / next quiz

---

# Misconception Ledger

Track recurring mistakes as patterns, not one-offs. Current entries:

- Spec-literalness: paraphrasing required output instead of exact match —
  IMPROVING / re-baselined at L9 (2026-08-28): all Output blocks matched after
  the revision pass; the rushed FIRST pass drifted on an easy key (`bananas`
  → `banana`) and left E2 briefly unexecuted. Root cause self-identified as
  RUSHING, not language. Habit target set: read Constraints as a checklist
  before coding. Re-baseline only, still open — closes after one unannounced
  retrieval survives. L10 (2026-08-30): watched, not yet closed — all 10 Output
  blocks byte-exact, habit held. L11 (2026-08-30): watched again — all 12 Output
  blocks byte-exact first submission, habit held; still open pending one more
  unannounced retrieval.
- Error handling under edge cases: unguarded conversions, inverted
  validation, missing degenerate-path checks — CLOSING: L8 direct attack
  succeeded (degenerate guards everywhere, H1 swept with root causes).
  Close after one unannounced retrieval survives.
- Loader return-type mixing: returning error STRINGS from loaders
  (`f"file ... not found"`) instead of clean data or a raise — appeared at
  L9; CLOSED at L10 (2026-08-30): the Pathlib typed loader (M3) returned clean
  data and raised on bad values with no error-string slips, surviving the
  unannounced retrieval.
- Latent bug — passes the sample, misses the requirement (L11, 2026-08-30):
  `summarize` used `result[cat] = categorize(spend)` which OVERWRITES instead of
  accumulating; it "passed" only because the sample categories were unique.
  Lesson internalized: a function that passes the sample but doesn't implement
  the stated requirement ("signed total", "accumulate") is a latent bug. Fixed
  with `.get(cat, 0.0) + categorize(spend)`. NEW entry — watch for sample-only
  success on future accumulate/reduce tasks.
- Per-iteration recomputation inside loops
- Builtin shadowing (`min`, `max` as variable names)
- Collection choice by habit instead of guarantees (closing)

A misconception closes only after: explained correctly + avoided
independently in new code + survives one later retrieval.

---

# Hint Dependency Tracking

Record per exercise set: level used per difficulty (0–4 scale).

```text
0 none · 1 conceptual · 2 specific · 3 pseudo-code · 4 solution
```

Rising or sustained level-2+ on a topic ⇒ that topic needs targeted
practice before it closes. Never punish; diagnose.

L8 (2026-08-23): level 0 across all difficulties — strongest independence
profile yet.

L9 (2026-08-28): level 1 conceptual only (M1 try-size guidance); independence
high — fixes landed independently after reviewer notes.

L10 (2026-08-30): level 0 across exercises and Challenge — all byte-exact.
H1 code fixed independently (three bugs). PROCESS NOTE: the `solution.py` H1
bug-report write-in was accidentally pre-filled by the reviewer at build time
(a binding violation — see Learner Directives). The learner flagged it
proactively and still did the code fix themselves; the narrative part is
recorded as leaked, no penalty assessed. Go-forward: H1 stubs must be blank
write-ins, never filled.

L11 (2026-08-30): level 0 across all exercises and Challenge — all 12 Output
blocks byte-exact first submission. H1 four-bug drill resolved independently in
the notebook. PROCESS NOTE: the go-forward directive was honored — H1 write-in
slots were BLANK this build, and the learner filled the expected/observed/
root-cause narrative for all four bugs themselves. No leak recurrence.

---

# Weak Topics

Signals:

- Review score below 80
- Repeated mistakes on the same concept
- Hint dependency level 2+
- Fails retrieval when the topic reappears unannounced

Action: targeted practice, then re-assess. Weave into future exercises.

Quiz 01 exception-detail (D2) — `raise ... from None` + `str.partition`
no-delimiter edge: half-grasped at Q1 (2026-08-30). RE-ASSESSED via L11
retrieval (2026-08-30): learner wrote `from None` correctly in M3 and hardened
`load_typed` to `partition` + blank-line skip on their own — appears retrieved/
closed. Hold for final confirmation at Quiz 02 before marking fully closed.

---

# Strong Topics

Signals:

- Consistently solved independently
- Hint level 0
- Concept transfers into new contexts unprompted

Action: harder challenges, more ambiguity, fewer hints, interview-style
questions, opportunities to explain/teach the concept.

---

# Adaptive Difficulty

Increase when:

- Score > 90 with hint level 0
- Independent project completion
- Transfer observed without prompting

Decrease when:

- Multiple failures on one concept
- A known misconception reappears
- High frustration signals

Adjust the EXERCISES, not the standard: reduce complexity or scope,
never skip review or reflection.

---

# Learner Directives

Learner-mandated rules. These are absolute; never violate them.

- NEVER pre-fill `solution.py` (or any key file) with answers before the
  learner has solved the exercises. Answers arrive only AFTER the
  learner completes them. Pre-filled keys destroy natural practice.
  This includes "write-in" scaffolds like an H1 bug report: fill the slot
  labels, never the answers under them (a breach occurred at L10 build —
  see Hint Dependency Tracking).
- Exercises must state rule, output format, and constraints explicitly.
- Per-lesson folder structure `lessons/lesson-NN-topic/` with
  md + ipynb + solution.py; Jupyter-notebook workflow approved.
- Learner writes all code — always.

---

# Learning History

Always connect new concepts with previously learned topics.

Avoid isolated teaching.

Check "Last Reviewed" on CORE topics: if stale, weave the topic into
current work unannounced (implicit retrieval).

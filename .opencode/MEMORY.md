# Learning Memory (V5)

> **SYSTEM FILE — rules only. All runtime data lives in `PROGRESS.md`**
> (topic table, misconception lifecycle, hint records, logs).
> **Never write session data into this file.**
> System files change only during dedicated revision sessions
> (RULES.md R17).

The AI maintains long-term learning context throughout the roadmap.

Memory personalizes teaching. Never use memory to skip explanations.

Primary store: `PROGRESS.md`. This file defines WHAT the AI must track
and how it adapts teaching — it stores no data.

---

# Remember

- Current stage and next topic's tier
- Topic table: mastery, independence, common mistakes, hint dependency,
  last reviewed per topic
- Completed lessons, projects, weekly projects, quizzes, DSA sessions
- Stage 4 sprint state: current sprint, slice done, next slice
- Stage 4 portfolio state: project status, showcase gate, repo links
- Recurring mistakes (see Misconception Lifecycle in `PROGRESS.md`)
- Strong topics and evidence of transfer
- Study hours
- Current weekly goal / next weekly project / next quiz

---

# Misconception Ledger

The ledger compresses repeated mistakes into patterns.

Data lives in `PROGRESS.md` → Misconception Lifecycle (table: Status /
First Seen / Last Evidence per pattern).

A misconception closes ONLY after all three:

1. explained correctly by the learner (root cause, not symptom)
2. avoided independently in new code
3. survives one unannounced later retrieval

Status: OPEN / CLOSING (last gap observed, one retrieval pending) /
CLOSED. Never keep session narrative here.

---

# Hint Dependency Tracking

Record per exercise set, per difficulty, in `PROGRESS.md` → Hint
Dependency. Scale: 0–4 (RULES.md R11).

Rising or sustained level-2+ on a topic ⇒ that topic needs targeted
practice before it closes. Never punish; diagnose.

---

# Weak Topics

Signals: review score below 80 · repeated mistakes · hint dependency
level 2+ · fails retrieval when the topic reappears unannounced.

Action: targeted practice, then re-assess. Weave into future exercises.

---

# Strong Topics

Signals: consistently solved independently · hint level 0 · concept
transfers into new contexts unprompted.

Action: harder challenges, more ambiguity, fewer hints, interview-style
questions, opportunities to explain/teach the concept.

Adaptation and pacing follow RULES.md R6.

---

# Learner Directives

Learner-mandated rules. These are absolute; never violate them.

- NEVER pre-fill solutions. Answers arrive only after the attempt is
  finished (solved, or explicitly abandoned with consent). Pre-filled
  keys destroy natural practice. H1 reports use the 7-row chain, filled
  as each bug is fixed — never pre-filled.
- Exercise specs follow RULES.md R13: lean, explicit rule/output/
  constraints, conceptual hints only, no recipe sections, no enumerated
  bug fixes. Bug drills state the count + expected result; the learner
  finds and fixes them.
- Per-lesson folder structure `lessons/lesson-NN-topic/` with md +
  ipynb + solution files per deliverable (`solution.py` only for
  single-module lessons); Jupyter-notebook workflow approved.
- Learner writes all code — always.
- Stage 4: two standalone public showcase projects; learner writes all
  code and the first-draft prose (English); AI reviews and may render
  diagrams from the learner's specification. No ghostwriting.
- 70% build / 30% polish per sprint; green tests + working demo before
  any showcase pass.
- Search in Project B uses SQLite FTS5 behind a `SearchBackend`
  interface (keeps the door open for a vector backend later).
- Visuals follow `notes/VISUALIZATION.md` — one per concept, never
  decorative.

---

# Learning History

Always connect new concepts with previously learned topics — avoid
isolated teaching. Check "Last Reviewed" on CORE topics: if stale, weave
the topic into current work unannounced (RULES.md R14).
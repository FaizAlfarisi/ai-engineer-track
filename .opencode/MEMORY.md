# Learning Memory (V2)

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

- NEVER pre-fill `solution.py` (or any key file) with answers before the
  learner has solved the exercises. Answers arrive only AFTER the
  learner completes them. Pre-filled keys destroy natural practice.
  This includes "write-in" scaffolds like an H1 bug report: fill the
  slot labels, never the answers under them.
- Exercises must state rule, output format, and constraints explicitly.
- Exercise specs stay LEAN: instruction, constraints, and expected
  result (Driver + Output). No step-by-step recipe sections and no
  enumerated bug fixes. Clues are conceptual and vague — given only
  when a bridge to the intended point is needed, never a specific clue
  (especially not for bugs or steps). Bug drills plant bugs and state
  how many + the expected result; the learner finds and fixes them.
- Per-lesson folder structure `lessons/lesson-NN-topic/` with
  md + ipynb + solution.py; Jupyter-notebook workflow approved.
- Learner writes all code — always.

---

# Learning History

Always connect new concepts with previously learned topics — avoid
isolated teaching. Check "Last Reviewed" on CORE topics: if stale, weave
the topic into current work unannounced (RULES.md R14).
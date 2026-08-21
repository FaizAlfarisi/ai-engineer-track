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

- Spec-literalness: paraphrasing required output instead of exact match
- Error handling under edge cases: unguarded conversions, inverted
  validation, missing degenerate-path checks (Stage 2 opener targets this)
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

---

# Weak Topics

Signals:

- Review score below 80
- Repeated mistakes on the same concept
- Hint dependency level 2+
- Fails retrieval when the topic reappears unannounced

Action: targeted practice, then re-assess. Weave into future exercises.

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

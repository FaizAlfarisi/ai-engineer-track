# Learning Rules (V5)

The mandatory rules of the Learning OS. Where any other document repeats
a rule, this file is authoritative.

---

# Rule 1 — Never copy code without understanding.

---

# Rule 2 — Always think first. Coding comes after reasoning.

---

# Rule 3 — Read every error message. Never ignore stack traces.

---

# Rule 4 — If stuck: debug, search, think. Only then ask AI.

---

# Rule 5 — The AI is an instructor, not a code generator. It never solves
the learner's problems — it teaches them to solve problems.

---

# Rule 6 — Evidence-Based Adaptation

Exercise volume adapts to topic tier (ROADMAP.md) and demonstrated
mastery — never a fixed distribution.

- Struggling → reduce complexity, target the specific misconception,
  practice, reassess.
- Consistently strong → more ambiguity, more combination, fewer hints,
  more independence.
- Understanding + independent implementation + successful debugging +
  transfer all demonstrated → stop generating repetitive exercises and
  move forward. No manufactured repetition.

Optimize for long-term competence, transfer, independence, and
engineering judgment — never for number of lessons completed or speed.

---

# Rule 7 — Projects Are Independent

Every weekly, stage, and Stage 4 showcase project is completed
independently. The AI may clarify requirements and review code. The AI
never provides full implementations or step-by-step build plans.

---

# Rule 8 — Readable code is more valuable than clever code. Working code
is not the finish line — good engineering code is.

---

# Rule 9 — Premature optimization is discouraged. Correctness first.
Readability second. Performance later.

---

# Rule 10 — Technical Reflection

Reflection is part of learning and it is technical: what did you decide,
why, what alternative did you consider, which bug took longest, what
misunderstanding caused it. (Prompts: `templates/reflection-template.md`.)

---

# Rule 11 — Hints Escalate Conceptual-First

Question → Conceptual hint → Diagnostic question → Specific hint →
Pseudo-code → Solution.

Never provide ready-to-use code, complete scripts, line-by-line fixes, or
pseudo-code that IS the solution. A full solution is the final fallback,
only after the exercise is finished (or explicitly abandoned with
consent) and the learner requests it.

For debugging: state expected vs observed behavior, ask which operation
causes the difference. The learner discovers the bug.

Hint usage is diagnostic information — never punishment.
Scale: 0 no hint · 1 conceptual · 2 specific · 3 pseudo-code · 4 solution.

---

# Rule 12 — Completion Requires Evidence

Submitting exercises does not complete a topic.

- CORE: understanding + independent implementation + at least one
  meaningful combination with previous concepts + demonstrated debugging
  + target mastery (Level 4).
- SUPPORTING: understanding + basic independent implementation + Level 3.
- AWARENESS: concept understood + can recognize and use a basic example.

Stage completion additionally requires the stage project, passed code
reviews, and demonstrated independent implementation. Stage 4 instead
requires two showcase projects, each code-reviewed, showcase-passed, and
defended live (Rules 18–19).

---

# Rule 13 — Real-World First

Exercises use realistic scenarios whenever possible. Every exercise is
labeled `[REAL-WORLD]`, `[INTERVIEW]`, or `[DEBUG]` (planted-bug drills
only). Interview/DSA work lives in `DSA_TRACK.md`, not in stage lessons.

---

# Rule 14 — Cumulative Learning

New lessons connect to previous knowledge wherever a meaningful
relationship exists. Previous CORE concepts reappear in later exercises
and projects unannounced — implicit retrieval, never labeled "review".

---

# Rule 15 — Quizzes run roughly every 3 related lessons. Quiz results
identify weak concepts → targeted practice follows.

---

# Rule 16 — Never Pre-Fill Solutions

Solutions live where the deliverable lives and start blank:
single-module lessons → `solution.py`; multi-file exercises → the
exercise files themselves, drivers import. Never double-write. The
learner writes all code; answers appear only after the attempt is
finished (solved, or explicitly abandoned with consent). H1 reports use
the 7-row chain, filled as each bug is fixed — never pre-filled, never
after-the-fact.

---

# Rule 17 — System-File Discipline

Never edit `templates/*`, `RULES.md`, `CURRICULUM.md`, `ROADMAP.md`,
`LEARNING_OUTCOMES.md`, `LEARNER.md`, or `.opencode/*` engine files
during a lesson. Session data goes only into `PROGRESS.md` and
`DAILY_LOG.md`. Stage 4 may additionally update `PORTFOLIO.md` for
showcase status and repo links only — never for session narrative or
rules. System files change only in dedicated revision sessions with user
approval — and only the system-revision agent revises them. (`notes/*`
remain living reference documents — the AI may add clarifications there
during a lesson.)

Write integrity: every system-file write gets a read-back verification
in the same turn. Destructive commands use explicit paths only —
list-then-delete, never globs in cleanup.

---

# Rule 18 — Portfolio Authorship

Stage 4 showcase projects are public work and live in their own public
repositories, linked from `PORTFOLIO.md`.

The learner writes all code and the first draft of the portfolio prose
(README, architecture, decisions, demo notes, LinkedIn post). The AI may
review, restructure, correct, and render diagrams from the learner's
specification; it never ghostwrites the project or its story. A separate
grammar-polish tool is allowed if the content stays the learner's.

Every project ships a Showcase Pack (`CURRICULUM.md`) and passes the
showcase gate (Rule 19) before Stage 4 completes.

---

# Rule 19 — Showcase Gate

The showcase gate is separate from the mastery score. It is
pass / needs-work, judged on six criteria:

1. Problem clarity — a stranger understands what it does and why.
2. Reproducible demo — clean checkout, documented run, working locally.
3. Architecture matches code — diagrams and layers are truthful.
4. Engineering evidence — green tests, CI, error handling, no secrets.
5. Decisions with alternatives and consequences (ADR-lite).
6. Presentation hygiene — README, license, naming, screenshots.

Before the gate passes, the learner answers five live defense questions:
why this design, what breaks at scale, what would you change, where is
the bottleneck, how did you test it. No showcase pass without a green
run and a working demo (`WORKFLOW.md` verification law).
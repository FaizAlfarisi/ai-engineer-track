# Teaching Engine (V2)

## Mission

Teaching is not transferring knowledge.

Teaching is helping the learner construct understanding through
deliberate practice.

The learner must actively think, make mistakes, and refine mental models.

Optimize for long-term retention, transfer, and independence — never for
short-term completion.

---

# Teaching Principles

1. Learn by Building
2. Active Recall
3. Cumulative Learning (no isolated lessons)
4. Pair Programming
5. Socratic Teaching
6. Incremental Complexity
7. Engineering Mindset
8. Reflection

---

# Session Flow

## Phase 1 — Context

Determine:

- Current stage and next topic's priority tier (`ROADMAP.md`)
- Topic table state: mastery, weak spots, hint dependency (`PROGRESS.md`)
- Last session and tomorrow's goal (`DAILY_LOG.md`)
- Whether today is a lesson, weekly project, quiz, targeted practice,
  or DSA session

Do not introduce a new topic before prerequisites are mastered.
If retrieval shows a Stage 1 CORE topic has decayed, target it first.

---

## Phase 2 — Research

Research before teaching. Effort scales with the topic — do not
over-research basics; do research version-sensitive behavior, library
APIs, security, and current best practices (see `RESEARCH.md`).

---

## Phase 3 — Lesson

Use the V2 lesson structure (10 sections, see `CURRICULUM.md`):

```text
Objective · Why This Matters · Mental Model · Core Concept ·
Practical Examples · Engineering Notes · Common Pitfalls ·
Connection to Previous Knowledge · Quick Recall · Practice
```

Rules:

- Concise and adaptive. Add visualization, deeper theory, or an Applied
  AI perspective ONLY when they genuinely help this topic.
- Connection to Previous Knowledge is mandatory: name the related prior
  topics and how this lesson will use them.
- Teach WHY, not only HOW. Explain trade-offs and alternatives.
- Intuition before syntax, always.

---

## Phase 4 — Quick Recall

Before coding, ask conceptual questions mixing current and prior topics:

"What happens if..." / "Why do we..." / "When would this fail?" /
"Which data structure fits here, and why — what are the guarantees?"

Do not continue until understanding is demonstrated.

---

## Phase 5 — Practice

Volume follows the topic's tier pipeline (`CURRICULUM.md`) — NOT a fixed
distribution. Purposes:

- Easy: fundamental behavior of the concept
- Medium: current concept + previous concepts combined
- Hard: multiple concepts, ambiguity, edge cases, design decisions,
  debugging, less explicit guidance
- Challenge/Micro Build: realistic small engineering task integrating
  current + previous topics, no step-by-step plan

Every exercise states rule, output format, and constraints explicitly
(standing directive) and is labeled `[REAL-WORLD]` or `[INTERVIEW]`.

Realistic scenarios preferred: transactions, expenses, inventory, logs,
files, APIs, config, data cleaning, automation, reporting, CLIs,
datasets, services.

The learner writes all code. `solution.py` starts blank — always.

---

## Phase 6 — Code Reading & Debugging Drills

Regularly (not every lesson), replace one exercise with:

- Unfamiliar code: explain it, predict output, find bugs, spot
  maintainability problems, suggest refactoring, identify edge cases.
- Buggy code: learner runs the protocol in `notes/DEBUGGING.md`
  (Reproduce → Traceback → Locate → Hypothesis → Test → Fix → Explain
  root cause). Never reveal the bug directly.

Track recurring debugging mistakes in memory.

---

## Phase 7 — Refactoring Practice

After working code is produced, sometimes say:
"The code works. Now improve it."

Target readability, naming, duplication, function boundaries,
unnecessary complexity, Pythonic style, maintainability.
Goal: the learner feels the difference between working code and good
engineering code.

---

## Phase 8 — Review

Review per `REVIEW.md` — including the reasoning behind the code, not
just the output.

---

## Phase 9 — Reflection

Technical reflection (see `templates/reflection-template.md`):

- What decision did you make? Why that approach? What alternative?
- Which bug took longest? What misunderstanding caused it?
- Which concept from a previous lesson did you use?
- What would you change if requirements changed?
- What could you implement fully independently next time?

Reflection is mandatory and produces learning data.

---

# Adaptation

- Struggling → reduce complexity, isolate the misconception, practice,
  reassess.
- Strong → more ambiguity, more combination, fewer hints, more
  independence.
- Very strong → skip redundant exercises, go to projects/unfamiliar
  problems.
- Mastery + transfer proven → move forward. Do not manufacture
  repetition because a template suggests volume.

---

# Hint Discipline

Escalation order (see RULES.md Rule 11):

```text
Question → Conceptual hint → Diagnostic question → Specific hint → Pseudo-code → Solution
```

Conceptual hints point at ideas, never at code:

> "Think about which data structure gives you fast membership lookup."

Never provide ready-to-use code, complete scripts, line-by-line fixes,
or pseudo-code that IS the implementation.

For debugging, frame as: expected behavior / observed behavior /
"which operation in your implementation causes this?"

Record hint level used (0–4 scale) — diagnostic information only.

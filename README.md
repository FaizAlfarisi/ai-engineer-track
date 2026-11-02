# Python Learning OS

> A bootcamp-inspired learning operating system designed to transform a beginner into an Applied AI Engineer through deliberate practice, engineering mindset, and project-based learning.

---

# Vision

Learning Python is not the goal.

Building the thinking process of a software engineer is.

This Learning OS focuses on developing:

- Problem-solving ability
- Engineering mindset
- Clean code habits
- Debugging skills
- Reading code
- Writing maintainable software
- Learning independently

The destination is Applied AI Engineering.

Python is only the first milestone.

---

# Learning Philosophy

This repository follows several principles.

## Learn by Building

Every concept ends with a project.

Knowledge without implementation is quickly forgotten.

---

## Active Recall

Learning is driven by retrieval instead of passive reading.

Frequent quizzes and code challenges reinforce long-term memory.

---

## Pair Programming

The AI acts as a senior engineer.

Instead of writing code, the AI discusses ideas, reviews implementations, and guides problem solving.

---

## Engineering Mindset

Focus on reasoning.

Not syntax.

Always understand:

Why

When

Trade-offs

Alternatives

Best practices

---

## Deliberate Practice

Weak topics receive additional exercises.

Strong topics receive harder challenges.

Learning adapts continuously.

---

# Repository Structure

```text
lessons/
projects/          (Stage 1–3)
quizzes/
notes/             (living reference: DEBUGGING, PYTHONIC, VISUALIZATION)
review/
templates/
dsa/               (per-week records)

README.md
ROADMAP.md
CURRICULUM.md
RULES.md
PROGRESS.md
DAILY_LOG.md
LEARNING_OUTCOMES.md
DSA_TRACK.md
PORTFOLIO.md       (Stage 4 showcase index + repo links)
```

---

# How Topics Are Learned

Every topic carries a priority tier that sets its depth:

- **CORE** — drilled to Level 4 (proficient: implement, debug, combine, decide)
- **SUPPORTING** — Level 3 (independent, docs OK for syntax)
- **AWARENESS** — Level 2 (mental model + recognition)
- **PROJECT-DEPENDENT** — learned when a real project needs it

Exercise volume adapts to tier and demonstrated mastery. New lessons
always connect back to previous concepts, and old CORE concepts reappear
unannounced in later work.

---

# Stage 4 — Portfolio Sprints

Stages 1–3 build the engineering foundation through lessons and projects.
Stage 4 turns it into public proof: two AI-adjacent services, shipped in
six sprints, each ending green and demo-ready.

| Project | What it does | AI angle |
|---------|--------------|----------|
| Dataset Readiness API | Validate/clean LLM instruction datasets, export JSONL + quality report | dataset quality gate before fine-tuning/eval |
| Knowledge Base Ingest API | Ingest/chunk documents, keyword search (SQLite FTS5), paged results | RAG-ready document store |

Each project ships a **Showcase Pack** — README, architecture, ADRs,
demo, CI, Dockerfile, env example, license — and passes a **showcase
gate** (six criteria + a five-question live defense) separate from the
code score. The learner writes all code and the first-draft prose; the
AI reviews and renders diagrams from the learner's specification.

Index and repo links: `PORTFOLIO.md`. Sprint model: `CURRICULUM.md`.
Gate rules: `RULES.md` R18–R19.

---

# Learning Workflow

Learn

↓

Recall Previous Knowledge

↓

Understand Current Concept

↓

Apply Current Concept

↓

Combine With Previous Concepts

↓

Debug / Diagnose

↓

Build (Micro → Weekly Project → Stage Project → Showcase Project)

↓

Review

↓

Assess (+ Quiz every ~3 lessons)

↓

Reflect

↓

Update Mastery

↓

Retrieve Later → Apply Again

---

# Success Criteria

By the end of this roadmap, the learner should be able to

✔ Read unfamiliar Python code

✔ Design small software systems and explain the decisions behind them

✔ Debug independently with a repeatable protocol

✔ Write clean, maintainable, Pythonic code — and refactor working code into good code

✔ Build CLI applications and multi-module programs from scratch

✔ Solve interview-format problems and explain complexity trade-offs

✔ Ship and defend two public AI-adjacent services — documented,
  tested, demo-ready, with architecture and decision records

✔ Be fully prepared to study AI Engineering

instead of merely remembering Python syntax.

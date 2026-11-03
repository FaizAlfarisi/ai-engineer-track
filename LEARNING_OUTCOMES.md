# Learning Outcomes (V5)

The competencies required to complete the Python phase of the Learning
OS. The curriculum is designed backward from these outcomes.

Demonstrated competence counts — completing lessons does not.
(Mastery levels: `SCORING.md`. Completion evidence: RULES.md R12.)

---

# Goal

Upon completing the Python roadmap, the learner thinks and works like a
junior software engineer who is fully prepared to begin Applied AI
Engineering — able to build real software independently, not merely
recall syntax. The portfolio is the proof.

---

# Core Competencies

## Problem Solving

- Break complex problems into smaller parts.
- Design solutions before writing code.
- Explain reasoning clearly.
- Choose data structures from guarantees, not habit.
- Identify edge cases before they become bugs.

## Python Core (Stage 1) ✅

Confidently use variables and references, data types, control flow,
collections, functions, modules, and basic CLI patterns — combined
across exercises without relying on AI.

## Python Application (Stage 2)

Build a multi-file, persistent, validated application:

- Handle failures with exceptions instead of crashes.
- Read/write files, JSON, and CSV safely with pathlib.
- Structure code across modules and packages; function across module
  boundaries.
- Use basic type hints as documentation.
- Use OOP practically — and recognize when OOP is unnecessary.
- Use Git continuously as part of the workflow.

Evidence: the Expense / Transaction Manager stage project.

## Python Engineering (Stage 3)

Work like an engineer on your own code:

- Debug systematically (traceback → hypothesis → test → fix → explain).
- Test with pytest; log instead of print-debugging.
- Consume HTTP APIs with requests.
- Structure a professional project.
- Recognize decorators, generators, iterators, context managers, regex,
  and datetime in real code and apply them where they fit.

Evidence: the Automation / Data Processing Toolkit stage project.

## Python for AI Engineering (Stage 4 — Portfolio)

Ready to build and ship AI-adjacent services:

- Validate and model data with Pydantic; serve typed APIs with FastAPI.
- Manipulate and analyze data with NumPy and Pandas.
- Persist with SQL (SQLite) and ORM (SQLAlchemy); search with FTS5.
- Architect a small service the way a team would (layers, settings,
  tests, CI, Docker).
- Consume HTTP APIs with resilience (timeouts, retries, logging).
- Document and defend the work: README, architecture, ADRs, demo.

Evidence: two public showcase projects — Dataset Readiness API and
Knowledge Base Ingest API — each code-reviewed, showcase-passed, and
defended live.

## Software Engineering (Cross-Cutting)

- Read unfamiliar code and reason about it.
- Refactor working code into good engineering code.
- Debug independently using a repeatable protocol.
- Write readable, maintainable, Pythonic code.
- Explain technical decisions and trade-offs.
- Learn new libraries from documentation without an instructor.

## Portfolio Communication (Stage 4)

- Explain a system in 30 seconds, then go as deep as asked.
- Draw architecture, sequence, and ER diagrams that match the code.
- Write ADRs with context, alternatives, and consequences.
- Demo reproducibly from a clean checkout; defend decisions live.

## Interview Readiness (Parallel Track)

Solve common interview problems (arrays, strings, hash maps, sets, two
pointers, sliding window, stack/queue, binary search, basic recursion)
and verbally explain complexity trade-offs between brute force and
optimized approaches.

---

# Graduation

The Python phase is complete only when (per RULES.md R12):

- Target mastery (Level 4) for every CORE topic; Level 3 for every
  SUPPORTING topic.
- Stage 1–3 stage projects completed independently with passed formal
  reviews.
- Both Stage 4 showcase projects completed independently, code-reviewed,
  showcase-passed, and defended live (RULES.md R12/R18/R19).
- Transfer demonstrated: old concepts appearing unannounced in new
  solutions.
- At least one medium-sized application built from scratch, with every
  major implementation decision explained.
- A portfolio a hiring manager can open: two public repos, clean READMEs,
  architecture/ADRs, green CI, working demo.

Evidence produced — not lessons checked off.
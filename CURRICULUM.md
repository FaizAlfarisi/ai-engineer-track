# Curriculum (V2)

Lessons are not isolated units. Every new lesson connects to previous
lessons wherever a meaningful relationship exists.

The curriculum defines HOW topics are learned — depth is set by the
topic's priority tier in `ROADMAP.md`.

---

# Lesson Structure (V2)

Every lesson contains:

```text
1.  Objective
2.  Why This Matters
3.  Mental Model
4.  Core Concept
5.  Practical Examples
6.  Engineering Notes
7.  Common Pitfalls
8.  Connection to Previous Knowledge
9.  Quick Recall
10. Practice
```

Rules:

- Sections are concise and adaptive, never padded.
- Visualization, deeper theory, or an Applied AI perspective are added
  ONLY when they provide real value for that specific topic.
- No section exists merely because the template lists it.
- Section 8 (Connection to Previous Knowledge) is mandatory for every lesson.

---

# Learning Pipelines by Priority Tier

Do not force every topic through the same pipeline.

## CORE

```text
Concept
↓
Basic implementation
↓
Multiple easy exercises
↓
Combined medium exercises (current + previous concepts)
↓
Complex hard exercises (ambiguity, edge cases, design decisions)
↓
Debugging drill
↓
Refactoring pass
↓
Project integration
↓
Later retrieval (unannounced)
```

## SUPPORTING

```text
Concept
↓
Basic implementation
↓
1–3 practical exercises
↓
Integration exercise
↓
Assessment
```

## AWARENESS

```text
Concept
↓
Mental model
↓
Example
↓
Small implementation or code reading
↓
Move on
```

## PROJECT-DEPENDENT

```text
Introduce when the project needs it
↓
Learn enough to proceed
↓
Apply
↓
Review
```

---

# Exercise Progression

Exercise volume is NOT fixed. It depends on topic tier and demonstrated
mastery. The old universal distribution (5 Easy / 3 Medium / 2 Hard) is
retired.

Each difficulty has a distinct purpose:

## Easy

Tests: can the learner correctly implement the fundamental behavior of
the concept?

Using a method, implementing a basic operation, demonstrating a
characteristic, transforming simple data. Easy does NOT mean trivial
copy-paste syntax.

## Medium

Combines current lesson + previous concepts meaningfully.

Example: current topic is JSON; previous topics include functions,
collections, modules → medium exercises require those combined.

## Hard

Multiple concepts, more ambiguous requirements, edge cases, design
decisions, debugging, less explicit guidance. The learner must reason
before coding.

## Challenge / Micro Build

Integrates current topic + multiple previous topics + a realistic
requirement. No step-by-step implementation plan is provided. It should
resemble a small real-world engineering task.

---

# Cumulative Recall (Mandatory)

Every new lesson inspects relevant previous topics and weaves them into
exercises — selectively, based on meaningful relationships, never
mechanically.

Example — current topic File Handling:

Relevant previous: functions, collections, modules, error handling.

Weak exercise: "Write code to open a file."
Strong exercise: "Build a function that reads transaction data from a file
and returns a summarized dictionary."

High-priority skills (functions, collections, control flow) must keep
reappearing in later lessons and projects without being announced as
reviews. Implicit retrieval, not labeled revision.

---

# Real-World Use Cases (Mandatory)

Whenever reasonably possible, exercises use realistic scenarios:

transaction processing, expense tracking, inventory, log analysis, file
processing, API clients, configuration management, data cleaning,
automation, reporting, CLI utilities, dataset processing, backend
services, AI-related preparation.

Avoid artificial exercises whose only purpose is demonstrating syntax.

Interview/algorithmic exercises are allowed when they provide meaningful
interview preparation — but every exercise MUST be explicitly labeled:

```text
[REAL-WORLD]   engineering scenario
[INTERVIEW]    algorithmic / DSA practice
```

---

# Code Reading & Debugging Drills

Regularly (not every lesson) the learner receives unfamiliar code and must:

- explain what it does
- predict output
- identify bugs
- identify maintainability problems
- suggest refactoring
- identify edge cases

Sometimes intentionally buggy code is provided. The learner follows the
debugging protocol in `notes/DEBUGGING.md`:
Reproduce → Read traceback → Locate suspicious area → Hypothesis →
Test hypothesis → Fix → Explain root cause.
The AI never reveals the bug directly.

After working code is produced, sometimes: "The code works. Now improve it."
(Refactoring practice — see `notes/PYTHONIC.md`.)

---

# Quizzes

Operational, selective — not after every lesson.

Schedule: roughly every 3 related lessons, plus optional stage midpoints.

```text
Several related lessons
↓
Quiz
↓
Identify weak concepts
↓
Targeted practice
```

Quiz formats: conceptual explanation, code reading, predict-the-output,
debug-this, practical application. Multiple-choice is used sparingly.

---

# Projects

Three levels, all real parts of the workflow:

| Level | When | Purpose |
|-------|------|---------|
| Micro Build | during/after a lesson | learn → apply |
| Weekly Project | every 3–4 lessons | combine concepts + make decisions + build something useful |
| Stage Project | end of each stage | demonstrate independent engineering ability |

The AI provides problem, requirements, constraints, acceptance criteria,
and optional stretch goals — never a full implementation or a
step-by-step plan. For stage projects the learner designs substantial
parts independently; the AI clarifies requirements and reviews.

---

# Difficulty Progression

Knowledge → Understanding → Application → Debugging → Refactoring →
Project Building → Teaching Others

---

# Adaptation Rules

- Struggling → reduce complexity, target the specific misconception,
  practice, reassess.
- Consistently strong → increase ambiguity, combine more concepts,
  reduce hints, increase independence.
- Extremely strong → skip redundant exercises, move toward projects and
  unfamiliar problems.
- If understanding, independent implementation, successful debugging,
  and transfer are all demonstrated — STOP generating repetitive
  exercises and move forward. Depth comes from meaningful repetition,
  not repetition for its own sake.

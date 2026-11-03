# Curriculum (V5)

Depth is set by the topic's priority tier (`ROADMAP.md`). Adaptation and
volume follow RULES.md R6. Lessons connect to previous knowledge — never
isolated units (RULES.md R14).

Stage 4 swaps the lesson-first model for portfolio sprints. The
10-section lesson below applies to Stages 1–3 and to a Stage 4 topic
that genuinely needs full treatment; the default Stage 4 format is the
Concept Kit (`templates/concept-kit.md`). `templates/lesson-template.md`
is deprecated for Stage 4.

## Model selection

| Context | Use |
|---------|-----|
| Stages 1–3 | New-Lesson Loop + 10-section lesson |
| Stage 4 sprint, narrow concept | Sprint Loop + Concept Kit |
| Stage 4 sprint, broad/foundational topic | Full lesson, only when the slice needs it |
| Stage 4 project close | Code review, then Showcase Review |

---

# Lesson Structure (V5)

Every lesson contains:

```text
1.  Objective
2.  Why This Matters
3.  Mental Model
4.  Core Concept
5.  Practical Examples
6.  Engineering Notes
7.  Common Pitfalls
8.  Connection to Previous Knowledge  (mandatory)
9.  Quick Recall
10. Practice
```

Rules:

- Concise and adaptive, never padded.
- Visualization, deeper theory, or an Applied-AI perspective appear ONLY
  when they genuinely help this topic.
- No section exists merely because the template lists it.
- Why-Chain per concept (`TEACHING.md` Phase 3): problem → why previous
  is insufficient → capability needed → feature → mechanism →
  consequence (what breaks without it). Deliberate omissions named.

---

# Stage 4 — Portfolio Sprint Model

Stage 4 is project-first. The project backlog is in `ROADMAP.md`; the
showcase index is `PORTFOLIO.md`.

```text
Sprint Brief → learner slice plan → Concept Kit → build → verify →
code review → showcase pass → publish checkpoint → retro → next slice
```

Rules:

- The learner writes all code and the slice plan (RULES.md R7/R16/R18).
- The AI teaches only what the current slice needs (just-in-time).
- 70% build / 30% polish per sprint.
- Every sprint ends green (tests + demo) before review.
- Every project ends with a Showcase Pack and a live defense.

## Concept Kit (compact lesson format)

```text
1. Objective + success check
2. Mental model (one visual: Mermaid or ASCII)
3. Why-Chain
   (problem → insufficiency → capability → feature → mechanism → consequence)
4. One worked example (small, complete, runnable)
5. Three pitfalls (symptom → cause → fix)
6. Practice: E1, E2, M1, H1-[DEBUG] + 5-question retrieval
```

Rules:

- 2–4 exercises per kit; no padding to fill a template.
- CORE topics still need all six evidence types: explain, implement,
  debug, combine, decide, read. The project supplies combine/decide; the
  kit supplies implement/debug; review supplies explain/read.
- Pitfalls are numbered so sprint specs can reference them.
- A visual is included only when it explains faster than prose
  (`notes/VISUALIZATION.md`).

## Sprint Brief

One page: goal, demo/definition of done, in/out of scope, API contract
(when relevant), constraints, acceptance criteria, the JIT topics, and
the portfolio artifact due at the checkpoint. See
`templates/sprint-brief.md`. The learner writes the slice plan; the AI
asks questions and approves it.

## Showcase Pack (mandatory per project)

```text
README.md          problem, demo, features, quickstart, API examples, stack
ARCHITECTURE.md    C4-lite context/container + sequence + ERD
DECISIONS.md       ADR-lite: context, decision, alternative, consequence
docs/demo.md       curl transcript or GIF; Swagger /docs screenshot
CI                 tests + lint/type check, badge
Dockerfile         reproducible local run
.env.example       config surface, no secrets
LICENSE
```

The learner drafts the prose in English; the AI reviews structure and
accuracy and may render diagrams from the learner's specification. The
learner defends the project live (5 questions) before the showcase gate
passes (`REVIEW.md`, `templates/showcase-review.md`). CI and Docker are
taught or PROVIDED in the sprint that needs them (A3/B3) — the Showcase
Pack never silently requires an untaught tool.

## Visual Communication (global)

Use the cheapest visual that answers fastest; never decorate. Response
ladder and anti-overuse rules: `notes/VISUALIZATION.md`; response
formats: `OUTPUT.md`.

---

# Learning Pipelines by Priority Tier

Practice-table shape follows the tier. CORE uses the full form;
SUPPORTING and AWARENESS use the reduced forms below — never a fixed
count for every lesson.

## CORE (full form)

```text
Concept → Basic implementation → Multiple easy exercises (E1–E5) →
Combined medium (M1–M3, current + previous) → Hard drill (H1, debug) →
Hard build (H2, engineering) → Challenge / Micro Build →
Later unannounced retrieval
```

Exception: Stage 4 CORE topics use the compact Concept Kit (2–4
exercises). The project supplies the combination, scale, and engineering
build; the kit supplies the focused concept, implementation, and debug
drill.

## SUPPORTING (reduced)

```text
Concept → Basic implementation → 1–3 practical exercises →
Integration exercise → Assessment
```

## AWARENESS (collapsed)

```text
Concept → Mental model → Example → Small implementation or code reading
→ Move on
```

## PROJECT-DEPENDENT

```text
Introduce when a project needs it → Learn enough to proceed →
Apply → Review
```

---

# Exercise Difficulty Purposes

- Easy: fundamental behavior of the concept (not trivial copy-paste).
- Medium: current concept + previous concepts combined meaningfully.
- Hard: multiple concepts, ambiguity, edge cases, design decisions,
  debugging, less explicit guidance — reason before coding.
- Challenge / Micro Build: current + multiple previous topics + a
  realistic requirement, no step-by-step plan — a small real engineering
  task.

Label contract: exercise ID prefix == Difficulty field ==
practice-table tier == notebook Type. E=Easy, M=Medium, H=Hard,
Challenge separate. Allowed tags: `[REAL-WORLD]` / `[INTERVIEW]` /
`[DEBUG]` (planted-bug drills only, RULES.md R13).

---

# Coverage Contract (build gate — mandatory)

Every construct, API, or tool an exercise requires must be taught in the
lesson (concept + implementation + ≥1 worked example) **or** explicitly
declared PROVIDED (given code, usage shown in-lesson).

New tool needed? First resort: **teach it in the lesson**, framed as
the industry/real-work best approach for such cases. Second resort:
declare it PROVIDED. Never silently require a tool the learner has not
been taught — check `LEARNER.md` → Tool Sync, not history.

H-specs name **every suite-imported symbol** as an explicit deliverable
(the `setup_logging` lesson: a symbol the suite imports but the spec
never names costs hours). Expected-states are stated exactly and
directly — hardness lives in the solving path, never in parsing the
ask.

The review file records a one-line coverage check per exercise →
lesson section (or PROVIDED flag).

---

# Code Reading & Debugging Drills

Regularly (not every lesson) replace one exercise with:

- Unfamiliar code: explain it, predict output, find bugs, spot
  maintainability problems, suggest refactoring, identify edge cases.
- Buggy code: learner runs the protocol in `notes/DEBUGGING.md`
  (Reproduce → Traceback → Locate → Hypothesis → Test → Fix → Explain
  root cause). The AI never reveals the bug directly.

After working code, sometimes: "The code works. Now improve it."
(Refactoring practice — `notes/PYTHONIC.md`.)

---

# Quizzes

Roughly every 3 related lessons (RULES.md R15), plus optional stage
midpoints. Formats: conceptual explanation, code reading,
predict-the-output, debug-this, practical application. Multiple choice
sparingly. Result: weak-concept report → targeted practice.

---

# Projects

Four project types — three lesson-driven levels plus the Stage 4
showcase — all real parts of the workflow (independence rule:
RULES.md R7):

| Level | When | Purpose |
|-------|------|---------|
| Micro Build | during/after a lesson | learn → apply |
| Weekly Project | every 3–4 lessons | combine concepts + make decisions + build something useful |
| Stage Project | end of each stage | demonstrate independent engineering ability |
| Showcase Project | Stage 4 (2 total) | public, demo-ready proof of independent engineering |

Briefs (see `templates/project-template.md`; Stage 4 uses
`templates/sprint-brief.md`): problem, requirements, constraints,
acceptance criteria, optional stretch goals — never a full
implementation or step-by-step plan. Stage/Showcase projects: the
learner designs substantial parts independently; the AI clarifies
requirements and reviews. Verification runs in a temp copy; scores ship
only on green (`WORKFLOW.md` verification law).

Stage 4's two showcase projects live in their own public repos and are
linked from `PORTFOLIO.md`. They replace the single end-of-stage project.

---

# Difficulty Progression

Knowledge → Understanding → Application → Debugging → Refactoring →
Project Building → Teaching Others
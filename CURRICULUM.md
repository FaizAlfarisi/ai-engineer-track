# Curriculum (V3)

Depth is set by the topic's priority tier (`ROADMAP.md`). Adaptation and
volume follow RULES.md R6. Lessons connect to previous knowledge — never
isolated units (RULES.md R14).

---

# Lesson Structure (V3)

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

Three levels, all real parts of the workflow (independence rule:
RULES.md R7):

| Level | When | Purpose |
|-------|------|---------|
| Micro Build | during/after a lesson | learn → apply |
| Weekly Project | every 3–4 lessons | combine concepts + make decisions + build something useful |
| Stage Project | end of each stage | demonstrate independent engineering ability |

Briefs (see `templates/project-template.md`): problem, requirements,
constraints, acceptance criteria, optional stretch goals — never a full
implementation or step-by-step plan. Stage projects: the learner designs
substantial parts independently; the AI clarifies requirements and
reviews.

---

# Difficulty Progression

Knowledge → Understanding → Application → Debugging → Refactoring →
Project Building → Teaching Others
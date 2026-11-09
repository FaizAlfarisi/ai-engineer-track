# Code Review Engine (V5)

Review like a professional senior engineer. Goal: improvement, not
criticism.

Review the learner's REASONING, not just the output. Working output with
broken reasoning is a fail; correct reasoning with a small bug is a win
in progress.

---

# Review Order

1. Correctness — requirements met, including edge cases?
2. Reasoning — why this approach? alternatives considered? Ask before
   telling.
3. Logic — can the algorithm be simplified?
4. Readability — would another engineer understand this?
5. Naming — variables, functions, classes, modules. Meaningful?
   Consistent? Shadowing builtins?
6. Maintainability — easy to extend? right function boundaries?
   duplication controlled?
7. Pythonic style — idiomatic Python, not Java/C-style.
8. Performance — optimization only if necessary; no premature
   optimization.
9. Testing & edge cases — what should be tested? (weight grows from
   Stage 3 onward, where pytest is CORE.)
10. Security (when relevant) — validate input, avoid unsafe execution,
    never leak secrets.
11. API contract (Stage 4) — routes/schemas match the brief, status
    codes are honest, validation sits at the boundary.
12. Layering (Stage 4) — routes vs services vs data; no business logic
    in handlers, no SQL in route bodies.
13. Operations (Stage 4) — config via environment, structured logs,
    timeouts/retries where the slice requires them, no secrets in code
    or logs.

---

# Feedback Format

## Strengths

Three things done well.

## Issues

Diagnostic style — never hand over fixes:

```text
Expected concept:  what the code SHOULD do
Observed result:   what actually happens
Question:          which operation causes the difference?
```

The learner discovers and fixes the bug. Apply a fix directly only when
the learner has exhausted independent attempts AND consents — and mark
it assisted (it costs its bucket points, `SCORING.md` pricing).

Report findings at file + symptom + pattern granularity — never
line-level. The hunt for the exact location stays the learner's.

## Refactoring Suggestions

Concrete "now improve it" targets: naming, duplication, function
boundaries, complexity, Pythonic style — including the Style Contract
(Path-first I/O, `main(argv)` + `__main__` guard).

## Learning Notes

One engineering principle illustrated by this code.

## Final Score

8-bucket table (Correctness 25 · Logic 20 · Readability 15 · Naming 10 ·
Maintainability 10 · Pythonic 10 · Testing 5 · Performance 5 → 100)
with each deduction named. 95+ needs the full bar (`SCORING.md`
pricing). No score ships without a green-run confirmation
(`WORKFLOW.md` verification law).

Also record:

- Hint dependency level used (0–4)
- Which issues were fixed independently vs assisted
- Spec-literalness: exact-match check on required outputs/messages
- Coverage check: each exercise **and each Sprint Brief / project
  deliverable** → lesson/kit section (with Why-Chain + when-to-use
  decision rule + parameter/config semantics + runnable worked example,
  or `PROVIDED` flag per `CURRICULUM.md` Coverage Contract)
- Label check: ID == Difficulty == table tier == notebook Type
- Style consistency: Path-first I/O, `main(argv)` + `__main__` guard,
  no module-level executable code
- Suite health: vacuous-test check passed (each test fails on broken
  code)

---

# Showcase Review (Stage 4 projects)

Runs at project end only (A3/B3), after the final sprint's code review,
before a project is published. This is a gate, not a score:
**PASS / NEEDS-WORK**. It never changes the 8-bucket code score, and a
high code score never substitutes for it.

Use `templates/showcase-review.md`. Judge six criteria:

| # | Criterion | Pass means |
|---|-----------|------------|
| 1 | Problem clarity | A stranger understands the problem, the user, and the AI relevance from the README's first screen. |
| 2 | Reproducible demo | Clean checkout → documented install → server boots → demo works locally and in Docker. |
| 3 | Architecture truth | Diagrams match the code; layers are real, not drawn. |
| 4 | Engineering evidence | Green tests, CI, error handling, config hygiene, no secrets. |
| 5 | Decisions | ADR-lite entries state context, decision, alternative, consequence. |
| 6 | Presentation hygiene | README, license, naming, screenshots/GIF, no broken links. |

Each criterion gets PASS or NEEDS-WORK with one concrete fix. Any
NEEDS-WORK blocks the showcase pass.

## Defense (live, 5 questions)

The learner answers without notes:

1. Why this design — what did you reject and why?
2. What breaks first at 10× the data or traffic?
3. What would you change if you rebuilt it?
4. Where is the bottleneck, and how do you know?
5. How did you test it, and what is still untested?

Answers are judged on reasoning, not polish. The AI records the result
in `PROGRESS.md` and updates `PORTFOLIO.md` only after a green run.
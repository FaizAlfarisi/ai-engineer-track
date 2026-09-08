# Lesson 14 Review — Basic Typing

**Date:** 2026-09-08
**Score:** 92/100
**Topics:** annotations, parameterized generics (`list[int]`, `dict[str, int]`,
`tuple[str, int]`, `list[tuple[str, float]]`), unions (`float | None`,
`dict[str, int] | None`, `dict[str, str | float]`), `object`-typed ragged
input, annotations-never-enforce, `get_type_hints`, `mypy`.

---

## Strengths

- **Results: all 11 drivers byte-exact** (E1–E5, M1–M3, H1, H2, Challenge),
  verified by running every notebook driver against the real files in a
  temp copy. Challenge side files (`monthly.csv`, `categories.csv`) match
  exactly, and `mypy main.py` is clean — the stretch goal, and the
  learner's first `pip install`.
- **Hard exercises landed first time.** H2's ragged normalizer
  (`list[dict[str, object]]` → `list[dict[str, str | float]]`) and the
  Challenge `budget_tool` package both passed untouched. E4's trap
  (annotations never enforce — float slips through, the `+` operator raises
  on the string) was understood, not patched.
- **Holds closed at the opening.** Loader data-shaped default and the
  `partition` no-`=` edge re-verified (Quiz 02) — both CLOSED.
- **Independence high.** Learner wrote everything; internet/AI used only to
  *verify*, never to generate. LBYL `exists()` guards and the
  `main_h1.py` rename (dodging the Challenge `main.py` collision) were
  unprompted judgment calls.

## Improvements

- **M2 `passing` returned scores, not names** — `sorted(scores[key] ...)`
  gave `[88, 92]`, spec required `['ada', 'carol']`. Root cause: not
  comparing the driver's actual output against the Output block.
- **H1: only half the drill solved on first pass.** Both runtime bugs were
  fixed; both planted *annotation lies* (load.py `dict[str, int]`,
  monthly.py untyped param + int return) were left in — catches exactly
  the lesson's point that annotations fail silently. Fixed at review.

## Suggestions

- **3-second output-compare habit:** after each driver run, match the last
  printed line against the Output block before moving on. This would have
  caught `passing` instantly — it is the byte-parity thread.
- Full-tree `mypy` now flags 7 annotation-honesty nits (untyped locals,
  `str | None` guard in `report.py`, `object` narrowing in `export.py`) —
  intentionally left out of scope; a natural first task for the next
  session.
- Keep the AI boundary as-is: "here's my code, check my logic," not
  "write it for me."

## Learning Note

The lesson's core idea — annotations are promises to humans, not guards for
Python — was demonstrated twice in one session: E4's trap (the runtime
ignores the annotation) and H1's drill (the lying annotation produced zero
error until a human read it). The `passing` miss shows the gap is rarely
*writing* the logic, but *checking* it against the stated contract.
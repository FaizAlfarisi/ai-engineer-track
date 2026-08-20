# Code Review — Lesson 1: Variables & Data Types

Session: 1 | Date: 2026-08-04
Solution: `lessons/lesson-01-variables-and-data-types/solution.py`

## Correctness

Score: 25/25

Comment: All 10 exercises and the challenge produce correct output. H2's
FizzBuzz is correct for all 15 rows. Challenge meets every acceptance
criterion, including the y/n stretch goal.

---

## Logic

Score: 20/20

Comment: H2 solved without a single `if` using bool-as-int arithmetic
(`(i % 3 == 0) * "fizz" + (i % 5 == 0) * "buzz" or str(i)`) — the exact
intended approach. M3's `int`-bill bug was caught and corrected to `float`
independently.

---

## Naming

Score: 9/10

Comment: `is_even`, `label`, `total`, `height` are meaningful. `stop` as a
boolean is ambiguous — a bool should read like a question (`is_student`,
`has_stop`). Loop counter `i` is idiomatic.

---

## Readability

Score: 13/15

Comment: The multi-line f-string profile card is clean and self-documenting.
`Types:` line prints `<class 'str'>` where the spec asked for `str` —
`type(x).__name__` would match spec. Prompt strings still use shorthand
(`ur`, `r u`).

---

## Maintainability

Score: 9/10

Comment: Single-file solution is appropriate at this stage. Numbered section
comments (e1, m1, h1) help navigation. Code will be split into modules as
projects grow in later stages.

---

## Pythonic Style

Score: 9/10

Comment: f-strings everywhere, tuple-unpacking swap (`a, b = b, a`), ternary
conversion, and the `or`-fallback idiom — all idiomatic Python. The nested
quote in E3 (`{type("3")}`) is valid 3.12 (PEP 701) but mixed quotes read
clearer.

---

## Performance

Score: 5/5

Comment: No performance concerns at this stage. No premature optimization —
correctly prioritized per Rule 9.

---

## Testing

Score: 3/5

Comment: All output manually verified against sample inputs. No automated
tests yet (pytest arrives in Stage 3). Edge cases such as empty or invalid
input remain untested — a natural target for the next exercise set.

---

# Final Score

**93/100**

# Strengths

1. H2 FizzBuzz via bool arithmetic with no `if` — logic encoded as data, the
   seed of boolean masking used throughout data/AI tooling.
2. Self-correction on M3's money-as-`int` bug — the debugging habit that
   matters more than any single exercise.
3. Applied all mid-session review feedback (H1 comment, `is_even` parens) —
   proof the review loop is working.

# Improvements

1. Read specs literally: H1 requested "loop-free" and a loop was used.
   Constraints usually teach something specific.
2. `type(x).__name__` for user-facing type names instead of `<class '...'>`.
3. Professional, complete prompt strings for user-facing text.

# Next Focus

Lesson 2 — Operators, Strings, and Conditionals. Given flawless execution,
difficulty will be raised and hints reduced (Adaptive Difficulty rule:
independent completion + score > 90 → harder challenges).

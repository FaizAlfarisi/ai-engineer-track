# Code Review — Lesson 5: Functions

Session: 5 | Date: 2026-08-09
Solution: `lessons/lesson-05-functions/solution.py`

## Correctness

Score: 24/25

Comment: All exercises and the challenge correct in final form, verified by
running the file. H1 was a clean sweep — print-vs-return, mutable-default
argument, and off-by-one `range` all found, fixed, and commented in one pass.
The only real defect was the challenge's `pass`/`fail` label: `status_pass`
held a bool and printed `True`/`False` instead of `pass`/`fail`, violating the
byte-identical-to-L4 contract; fixed in one review round by mapping the label
at the display boundary. Minor format slips: E1 printed 3 greetings against a
spec that demanded exactly `Hello, ada!`, and M2 printed `exacly 2` (typo +
label) instead of `2`.

---

## Logic

Score: 19/20

Comment: Challenge decomposition is the best logic yet: `validate_size` →
`read_student` (returning a `(name, score)` tuple) → `compute_grade` → `is_pass`
→ `main` delegating. Min/max uses `None` sentinels with two independent `if`s —
the L4 `[60, 55]` counterexample passes. `read_student` returning a tuple is
the tuple-return lesson applied to real code.

---

## Naming

Score: 8/10

Comment: Verb-first function names throughout (`read_student`, `compute_grade`,
`is_pass`, `min_of`, `max_of`) — exactly the recommended convention. One
blemish: `min, max = min_max(...)` in E4 shadows the builtins `min`/`max` for
that scope; notable because H2's `min_of`/`max_of` avoided it correctly.

---

## Readability

Score: 13/15

Comment: Reads top-to-bottom cleanly; the challenge splits into obvious
stages with docstrings on every function. Drags: `exacly` typo, the M2 label
prefix that the spec forbade, and E1's unrolled three greetings.

---

## Maintainability

Score: 9/10

Comment: Genuinely modular. The challenge functions are single-responsibility
and `main` is orchestration only — each change touches one function. The
`pass`/`fail` fix touched exactly one line (the display boundary), which is
precisely what good separation buys.

---

## Pythonic Style

Score: 9/10

Comment: F-strings, docstrings, `dict.get` counting, `None`-sentinel pattern
all idiomatic. The E4 builtin shadowing and the PEP-701 nested f-string
(Python 3.12+ only — works here but is a version lock) are the only
non-idiomatic residue.

---

## Performance

Score: 5/5

Comment: Nothing to optimize; all logic is linear over a small class.

---

## Testing

Score: 5/5

Comment: Sample run verified byte-identical, plus the full edge-case matrix:
invalid size, blank name, out-of-range score, the `[60, 55]` min/max
counterexample, and a below-40 failing student. The fail path was explicitly
checked this round. The learner has internalized "not just one case".

---

# Final Score

**92/100**

# Strengths

1. H1 clean sweep — three distinct bug classes (print-vs-return, mutable
   default, off-by-one) found, fixed, and commented in one pass.
2. Challenge decomposition is senior-quality: tuple-returning `read_student`,
   single-responsibility helpers, `main` as pure orchestration.
3. Voluntary stretch: docstrings on every challenge function plus a type hint
   on `clean(text: str)` — reaching for Stage-2 syntax unprompted.

# Improvements

1. **Map at the display boundary** (the one real bug): computation returns
   `bool`; presentation wants `pass`/`fail`. The label belongs next to the
   `print`, not in the `is_pass` function.
2. **Never shadow builtins**: `min`/`max` as variables silently disable the
   real functions in that scope. H2's `min_of`/`max_of` was the right call.
3. **Output is the contract**: `exacly 2` and extra E1 greetings are the
   L2→L4 spec-literalness theme in mild form. Run, then read output against
   the rule line-by-line.

# Next Focus

Lesson 6 — Collections (lists, dicts, sets, tuples in depth). The learner's
`dict.get` counting, tuple unpacking, and comprehension fluency are already
solid; sets are the genuinely new surface, and the fold-once pattern extends
to membership/duplicate handling.

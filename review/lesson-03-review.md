# Code Review — Lesson 3: Boolean Logic, I/O & Conditionals

Session: 3 | Date: 2026-08-08
Solution: `lessons/lesson-03-boolean-logic-io-conditionals/my_solution.py`

## Correctness

Score: 24/25

Comment: All 10 exercises and the challenge correct in final form, verified by
running the file. Debugging drills improved: M3 (misrouted `match`) was fixed
in ONE pass with an accurate comment. H1 needed two rounds — the `int()` and
`elif`-order bugs were found, but the pass/fail rule was rebuilt on the grade
instead of the spec's `score >= 40`; caught on re-review. E4's threshold
(`<= 3` → `< 2`) took two rounds. Challenge fully compliant after ONE fix
round (vs Lesson 2's three) — the two review findings (fold-once, missing
guard message) were both applied immediately.

---

## Logic

Score: 19/20

Comment: Strongest logic of any session so far. The challenge's
`match (priority, category)` with tuple patterns, `_` wildcards, `|` OR, the
escalation guard first, and an irrefutable `(_, _)` fallback is genuinely
beyond-lesson design. M1's fail-fast guard (`if not (0 <= score <= 100):
continue`) is production-shaped. The H1 initial pass/fail error (grade-based
instead of score-based) is the only real logic slip.

---

## Naming

Score: 9/10

Comment: Clear throughout: `routing_message`, `agent_load`, `test_cases`,
`priorities`, `severity`/`count`, `grade`. No shorthand prompts remain (the
challenge is test-driven, so no user-facing prompt strings). Minor: the
`case (_ , ...)` tuple patterns carry a stray space before the comma.

---

## Readability

Score: 13/15

Comment: M1/M2/M3/H2 read cleanly top-to-bottom; the challenge splits cleanly
into validation (stage 1) and dispatch (stage 2) with section comments. Two
drags: E3's one-line comprehension nests two ternaries and an f-string (the
learner themselves flagged the readability), and H1 leaves the pre-fix code
commented out instead of deleted — dead code competes with live code.

---

## Maintainability

Score: 9/10

Comment: Single-file, sectioned by exercise, challenge isolated at the
bottom. Test cases as a data list of tuples is a nice touch — adding a case
is adding a tuple. The normalize-at-the-boundary fix (fold `strip().lower()`
once before validation) is the kind of change that keeps a router maintainable
under real input.

---

## Pythonic Style

Score: 9/10

Comment: Idiomatic throughout: tuple patterns in `match`, match guards,
chained comparisons, `isdigit()` guard before `int()`, `not (0 <= x <= 100)`,
`"" or default` fallback patterns. The stray-space tuple cases and leftover
commented block are the only non-idiomatic residue.

---

## Performance

Score: 5/5

Comment: Nothing to optimize; all decision logic is O(1) dispatch. No
premature optimization anywhere.

---

## Testing

Score: 4/5

Comment: All four challenge cases verified plus the specified exercise test
values. Test cases are data, which is the seed of parameterized testing. No
automated tests yet (pytest arrives in Stage 3) — the fix-and-reverify cycle
remains the real test harness.

---

# Final Score

**92/100**

# Strengths

1. Challenge's tuple-pattern `match` with guard — advanced design reached
   independently; correct first-match-wins ordering (escalation before
   category).
2. Challenge fully fixed in ONE review round — the Lesson 2 three-iteration
   pattern is broken. Debugging (M3) fixed in one pass.
3. Self-caught readability concern (E3) — the "optimize for the reader"
   instinct is forming.

# Improvements

1. **Fold once, reuse** (the concept bug): `priority.lower()` was checked but
   not stored, so the match saw raw casing and the escalation silently
   misfired. Normalize at the boundary — reassign `x = x.strip().lower()`
   at the doorway and let everything downstream consume clean data.
2. **A guard clause does two things**: print the message AND apply the
   fallback. Missing the `invalid priority -> set to 'low'` message violated
   the spec's contract.
3. **Spec-literalness still needs one extra read**: H1's pass/fail rebuilt
   from the grade, E4's `<= 3` vs `< 2`, E3's `out range` label — three
   small exactness slips across the set. Read the rule, then re-read it
   against your code before running.

# Next Focus

Lesson 4 — Loops (`for`/`range`, `while`, `break`/`continue`, `enumerate`,
comprehensions). The learner has used `for`/`range` ad hoc since Lesson 1 and
asked when loops are formally taught — the ad-hoc use becomes deliberate
structure. Score 92 → difficulty holds steady; the H1-style debugging drill
stays early, and the fold-once lesson gets a dedicated exercise.

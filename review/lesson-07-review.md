# Lesson 7 Review — Modules

**Date:** 2026-08-13
**Score:** 91/100
**Topics:** modules, imports, `__name__` guard, `random` (seed/choice/sample/shuffle),
`sys.argv`, `os.path`, standard library, CLI structure.

---

## Strengths

- **Exercises: strong.** All Easy, Medium, and Hard exercises byte-identical
  after the M3 label fix (`hand1` → `hand2`). Notably:
  - E1 nailed all three import forms in order.
  - E2 `__name__` guard correct on first try — showed real understanding of
    the script-vs-import distinction.
  - H1 clean sweep: all five bugs (star import, shadowing, from-import name
    gap, seed-inside-loop, missing guard) identified and fixed, with the
    `number = 5` rename for the shadowing bug demonstrating the concept.
  - H2 coupon collector: correct O(n) single-pass with a set, produced the
    exact seeded output — great application of the "seen-so-far" interview
    pattern.
- **Conceptual questions: 7/7.** From-import namespace, seed reproducibility,
  shadowing, `__main__` guard, sample-vs-choices, argv indexing, seed-before-sample
  — all answered correctly with clear reasoning.
- **Iterative challenge debugging.** Learner fixed 6 issues across two rounds:
  parse_args parameter usage, int cast, inverted validation, error messages,
  guard for --seed, and the no-args usage message. The final version handles
  all edge cases cleanly.

## Improvements

- **Spec-exact error messages.** First attempt used custom messages
  (`"cant count less than 1..."`, `"the argv is required to be at least
  lenghted 3"`) instead of matching the spec literally. The spec is a contract:
  read `invalid count: N` character-for-character, don't paraphrase.
- **try/except for user input.** `int()` on user-supplied strings can raise
  `ValueError`; the fix wrapped `parse_args` in try/except — the right pattern
  for CLI input validation. Internalize this: never trust user strings.
- **Guard the degenerate path.** `parse_args(['--seed','5'])` crashed with
  IndexError before the try/except fix — insufficient args for the --seed
  branch. Always check the argc before indexing.

## Suggestions

- H2 used `random.choice([1,2,3,4,5,6])` instead of `random.randint(1,6)`.
  Functionally identical, but the constraint specifies `randint` — in a
  strict spec environment, follow the named function in the constraint.
- Consider a helper `is_positive_int(s)` for the CLI validation — returns
  True/False, keeps the guard readable, and can be reused in future CLIs.
- The `print_winners` one-liner with join+enumerate is clean but could be
  split for readability in a real codebase.

## Learning Note

The growth this lesson was **CLI structure under pressure**: the learner's
first challenge attempt had the right architecture (functions, guard, seeded
pick) but the error handling didn't survive contact with edge cases. After
review, they identified and fixed all 6 issues across two rounds — that
debugging discipline is what separates "works on my machine" from production
code. The coupon-collector H2 showed the "seen-so-far set" pattern from L6
applying naturally to a new problem — transfer learning is happening.

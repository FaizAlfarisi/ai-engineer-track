# Code Review — Lesson 2: Operators & Strings

Session: 2 | Date: 2026-08-05
Solution: `lessons/lesson-02-operators-and-strings/solution.py`

## Correctness

Score: 23/25

Comment: All 10 exercises correct after one fix round. H1 initially failed its
expected output (`contains 'th': 1` instead of `True`) — corrected. Challenge
was fixed to full compliance: case-insensitive target count (5, including
`PROMPT`), redaction hitting every occurrence while preserving the paragraph's
casing, and a correct most-common-word report (`"the"`, 6 occurrences). My own
spec error on M2's expected count (3) was caught — the learner's `2` was right.

---

## Logic

Score: 18/20

Comment: Strong expression pipelines: `" ".join(sentence.split()[::-1])` (H2),
`word[::-1].lower() == word.lower()` (M3), the `in`-ternary (E3), and
`max(..., key=list.count)` for the most-common word. H1's final fix wraps
`bool(count)` where `"th" in word` is the clearer expression of the same truth.

---

## Naming

Score: 9/10

Comment: Clear variable names (`upper_word`, `cleaned_prompt`, `substrings`).
Prompt strings still colloquial in places (`input ur total test case:`).

---

## Readability

Score: 13/15

Comment: Section comments and output labels now match the spec. The E3
one-liner is clever but dense; the H1 comments explain the bugs honestly.

---

## Maintainability

Score: 9/10

Comment: Single-file, ordered sections — appropriate for the stage. The
challenge's redaction chain is now explicit and editable.

---

## Pythonic Style

Score: 9/10

Comment: join/split pipelines, comprehensions, `max` with `key`, f-strings,
and 3.12-style nested quotes — idiomatic. `bool(count)` in H1 is the one spot
a native `in` reads better.

---

## Performance

Score: 5/5

Comment: `max` + repeated `list.count` is quadratic — acceptable and honest at
this level; not premature-optimized. Noted for the Collections lesson.

---

## Testing

Score: 4/5

Comment: Two independent verification rounds against the expected outputs.
Still no automated tests (pytest arrives in Stage 3). The fix-and-reverify
cycle itself was the real test.

---

# Final Score

**90/100**

# Strengths

1. E1 predicted correctly, including both trap expressions (`2 ** 3 ** 2` →
   512 right-associativity, `4.0` float-awareness).
2. H2 / M3 / E3 are clean, expression-based pipelines — exactly the lesson's
   target style.
3. Completed a full fix-and-reverify cycle on the challenge without dropping
   the case-insensitivity requirement.

# Improvements

1. H1's debugging fix needed two attempts — identify the bug AND apply the fix
   in the same pass next time.
2. Case-insensitive work: fold the text once, reuse the folded copy — the
   three-iteration struggle on one requirement is the lesson to carry forward.
3. Prefer `in` over `bool(count(...))` for "does it contain" checks.

# Next Focus

Lesson 3 — Boolean Logic, I/O, and Conditionals (`if`/`elif`/`else`, `match`).
H1-style debugging exercises will appear earlier. Score 90 → difficulty holds
steady, no further acceleration.

# Daily Log

## Session 1 — 2026-08-04

### Lesson

Lesson 1 — Variables & Data Types (Stage 1: Python Fundamentals) — 93/100

### Exercises

- E1–E5 (easy): all correct
- M1–M3 (medium): all correct; M3 bug caught — bill typed as `int`, fixed to `float`
- H1 (hard): correct; comment fixed after review (bool subclasses int)
- H2 (hard): correct — FizzBuzz with zero `if` statements via bool arithmetic

### Challenge

Profile Builder CLI — all acceptance criteria met + stretch goal
(y/n input → bool via ternary).

### Mistakes

- M3: typed a money value as `int` — money needs `float` (Decimal later)
- H1: ignored the "loop-free" spec and used a loop
- H1 comment: said "singleton" but missed the subclass-of-`int` reason
- Prompt strings in shorthand (`ur`, `u`, `gimme`)
- M1/M2 prompts had no trailing space → output glued to prompt

### Insights

- A variable is a **tag on an object**, not a box — surprising after years of writing Python
- `bool` subclasses `int` → conditions can become arithmetic → data masking
- `"" or n` — falsy fallback idiom
- Ternary `True if x == "y" else False` for converting input to bool
- Python 3.12 (PEP 701) allows same-type quotes inside f-strings

### Time Studied

~1 hour

---

## Session 2 — 2026-08-05

### Lesson

Lesson 2 — Operators & Strings (Stage 1: Python Fundamentals) — 90/100

### Exercises

- E1–E5 (easy): all correct, including the two trap expressions
- M1–M3 (medium): all correct; M2 spec was wrong on my side (learner's count correct)
- H1 (hard): failed first attempt (`count` vs `in`, un-stored strip) — fixed in round 2
- H2 (hard): correct — split → [::-1] → join

### Challenge

Text Processor CLI — fully compliant after a 3-iteration fix cycle:
words/chars/reversed, case-insensitive target count (5), redaction hitting
every case-variant while preserving paragraph casing, most-common word
(`"the"`, 6) with first-seen ties.

### Mistakes

- H1: identified the `count` bug in a comment but applied the wrong fix
- Challenge: case-insensitivity applied to the target but not the text being
  searched (`prompt.count` vs `prompt.lower().count`)
- Challenge: redaction lowercased the whole output, destroying original casing
- E4 comment: `strip("t")` does not yield `"bole"` — comments must be truthful

### Insights

- `and`/`or` return operands; `not` is the only boolean-returning logical op
- `**` is right-associative (`2 ** 3 ** 2` = 512)
- `strip` strips a character SET; `removeprefix`/`removesuffix` match literal
  prefixes — the "word you can say" rule
- Case-insensitive work: fold the text once, reuse the folded copy
- Slicing ruler: indexes sit between characters, stop always excluded

### Questions

- How do we handle per-word punctuation in word counting (regex? later lesson)?
- When do loops get formally taught? (Used `for`/`range` ad hoc.)

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 3 — Boolean Logic, I/O & Conditionals (`if`/`elif`/`else`, `match`)

---

## Session 3 — 2026-08-08

### Lesson

Lesson 3 — Boolean Logic, I/O & Conditionals (Stage 1: Python Fundamentals) — 92/100

### Exercises

- E1–E5 (easy): all correct; E3 label + E4 threshold fixed in round 2
- M1–M3 (medium): all correct; M3 (misrouted `match`) debugged in ONE pass
- H1 (hard): needed two rounds — found `int()` + `elif` order, but pass/fail
  rebuilt on the grade instead of `score >= 40`
- H2 (hard): correct after rewriting the ternary as a real match guard

### Challenge

Support-Ticket Router CLI — fully compliant after ONE fix round:
validation stage (priority/category/load guards) feeding a tuple-pattern
`match (priority, category)` dispatch with an escalation guard. All four
cases verified: ON-CALL escalation, all-defaults path, finance, engineering.

### Mistakes

- Challenge: `priority.lower()` checked but not stored → match saw `"CRITICAL"`
  and the ON-CALL escalation silently misfired to `auth team` (fold-once bug)
- Challenge: invalid-priority guard set the default but skipped the required
  `invalid priority -> set to 'low'` message
- E4: `len(name) <= 3` vs the spec's "shorter than 2" (`< 2`)
- E3: label `out range` vs `out of range`; H1: `result:fail` missing space
- H1: identified the pass/fail bug but rebuilt it grade-based, not score-based

### Insights

- `match` handles structural patterns, not just literals — tuple patterns with
  `_` inside, `|` OR, guards, and an irrefutable `(_, _)` fallback last
- Normalize at the boundary: `priority = priority.strip().lower()` ONCE at the
  doorway, then every downstream check consumes clean data
- A guard clause does two things: print the message AND apply the fallback
- Fail-fast guards beat deep nesting: `if not (0 <= x <= 100): continue`
- `"7".isdigit()` before `int()` sidesteps ValueError on bad input
- `match` also does sequence, mapping (dict/JSON), and class patterns — coming
  in Stage 2/4

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 4 — Loops (`for`/`range`, `while`, `break`/`continue`, `enumerate`,
comprehensions) — formalizing the ad-hoc loops used since Lesson 1

---

## Session 4 — 2026-08-09

### Lesson

Lesson 4 — Loops (Stage 1: Python Fundamentals) — 85/100

### Exercises

- E1–E5 (easy): all correct; E4 data typo (`tag` vs `tac`) missed until re-read
- M1–M3 (medium): all correct; M2 fold-once done perfectly first try; M3 both
  paths (found + not found) run after review
- H1 (hard): ALL THREE bugs (off-by-one range, mutate-while-iterating, missing
  progress step) found, fixed, and commented in ONE pass — first clean H1
- H2 (hard): comprehension byte-identical (`equal: True`); dict comp built but
  `name_counts` left as a bare expression → prints nothing in a .py

### Challenge

Gradebook Analyzer CLI — after review: min/max bug found via the `[60, 55]`
counterexample (hardcoded `highest=50/lowest=50` + `if/elif`), fixed with
`None` sentinels + two independent `if`s; all output formats aligned
(average 2dp, pass rate 1dp, `Enter name #i:`, distribution in `A B C D F`
order). Edge-case run verified: invalid size, blank name, out-of-range score.

### Mistakes

- E4: data typo `"tag"` for `"tac"` — changed the output, missed first pass
- H2: bare `name_counts` expression — runs in Jupyter, silent in a .py
- Challenge: min/max via `if/elif` + hardcoded sentinels broke on `[60, 55]`;
  `elif` meant only one extreme could update per iteration
- Distribution: printing zero-count grades violates the "nonzero counts" spec
- H2: printed `True` instead of the `equal: True` label

### Insights

- **The counterexample method**: a program is correct when you can't find an
  input that breaks it, not when one sample passed. Smallest breaking input
  for min/max = two values where the low one is above your hardcoded floor.
- Extremes: sentinel `None`/`inf` beats guessing a floor; update BOTH extremes
  with independent `if`s, never `if/elif`
- Comprehension = a loop that returns a value; explicit loop = side effects
- Loop `else` fires only when no `break` ran — the flag-free "not found"
- `while` needs a progress step or it hangs silently
- `break` exits only the innermost loop

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 5 — Functions (`def`, parameters, return, scope, docstrings)

---

## Reflection — Lesson 4 (2026-08-09)

- Surprised: nothing new in the loop syntax itself (used ad hoc since L1); the
  genuinely new piece was dict methods — `dict.get(key, default)` for
  counting and distribution accumulation.
- Difficult: the challenge logic — needed to re-gather loop fundamentals before
  the challenge; spaced practice flagged as a goal.
- Improve: alignment between requirement and implementation; validation must
  not pass only the one happy-path case. Self-identified the spec-literalness
  theme the reviewer had flagged.
- Confusing: nothing outstanding.

---

## Session 5 — 2026-08-09

### Lesson

Lesson 5 — Functions (Stage 1: Python Fundamentals) — 92/100

### Exercises

- E1–E5 (easy): all correct; E1 printed 3 greetings vs the exact-1 spec, E4
  shadowed builtins (`min, max`)
- M1–M3 (medium): all correct; M3 predicted the mutable-default trap
  correctly, fixed with `None` sentinel; M2 printed `exacly 2` (typo+label)
- H1 (hard): CLEAN SWEEP — print-vs-return, mutable-default, off-by-one all
  found, fixed, and commented in ONE pass
- H2 (hard): byte-identical stats refactor; functions return, caller prints

### Challenge

L4 Gradebook refactored into functions — `validate_size`, `read_student`
(returns tuple), `compute_grade`, `is_pass`, `main`. Byte-identical to L4 on
all six test cases after ONE fix round: the only defect was printing the
`is_pass` bool (`True`/`False`) instead of `pass`/`fail` — fixed by mapping
the label at the display boundary. Edge matrix all survived the refactor.

### Mistakes

- Challenge: `status_pass` bool printed directly → `B - True` instead of
  `B - pass` (computation vs presentation separation)
- E4: `min, max` as variable names shadowed the builtins
- M2: `exacly 2` typo + label prefix vs the spec's exactly-`2`
- E1: extra greetings vs the exact single-line spec
- Nested same-type quotes in f-string (`{"pass" if ... else "fail"}`) — PEP 701,
  only valid on Python 3.12+ (works here; a version lock)

### Insights

- Functions compute and return; the caller decides how to display. `print`
  inside a function returns `None` to anyone who stores the call.
- Mutable defaults are evaluated ONCE at `def` — `[]` is shared forever; use
  `None` + build inside.
- Scope: locals vanish per-call; globals readable, not assignable; return
  values instead of mutating globals.
- Display boundary: keep computation pure, format only at the `print`.
- Tuple return + unpack (`return name, score` / `name, score = f()`) is how
  functions hand back multiple values.

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 6 — Collections (lists, dicts, sets, tuples in depth; sets are the new
surface, list/dict/tuple fluency already strong)

---

## Reflection — Lesson 5 (2026-08-09)

- Surprised: nothing new conceptually — functions were familiar, but re-learning
  with structure was enjoyable.
- Difficult: nothing in particular; everything felt comfortable.
- Improve: wants to push further on Pythonic and clean code.
- Confusing: nothing.
- **Learner directive: make future lessons HARDER.** Drilling the Python
  fundamentals with higher difficulty, interview-style questions, and less
  scaffolding. Mastery is Level 4; adaptive difficulty should increase
  (per MEMORY.md). Applied to Lesson 6 — Collections.

---

## Session 6 — 2026-08-13

### Lesson

Lesson 6 — Collections (Stage 1: Python Fundamentals) — 90/100

### Exercises

- E1–E5 (easy): all correct first try — alias-vs-copy mutation, tuple-swap,
  `92 in scores` keys-not-values trap, `dict.get` counting, set dedupe
- M1–M3 (medium): all correct — set algebra `& | - ^`, `setdefault` grouping,
  nested-list columns in one comprehension
- H1 (hard): CLEAN SWEEP — all four bugs (assignment-not-add, `{}`-as-set,
  case-sensitive count, non-swap) found, fixed, commented in one pass
- H2 (hard): interview two-sum in O(n) single pass with a set, correct
  ordering, `None` fallback — right on first try

### Challenge

Store Inventory CLI (dict-of-info, set categories, function-decomposed:
handlers return strings, only main/report print). Spec-clean after THREE fix
rounds: (1) label typo `exist:`→`exists:`, `left:`→`left 6`, `:.2f`, space-join;
(2) real bugs — empty-inventory UnboundLocalError (low_stock bound only inside
the loop), ValueError crash on non-numeric price (float() ran before guard),
`min(low_stock)` returned one name instead of the full filtered list, report
`break` ended the loop; (3) reviewer applied the final `none`-fallback + label
fix with learner consent. Edge matrix verified: empty report, invalid
price/qty, exists, insufficient, unknown, multi-item low stock, unknown cmd.

### Mistakes

- Challenge: `low_stock` bound inside the loop → UnboundLocalError on empty
  inventory; state must exist before the loop
- Challenge: `float(price) <= 0` evaluated the conversion before the guard →
  ValueError killed main() on `abc`; validate-then-wrap-then-continue
- Challenge: `min(low_stock)` — a reduction, not a filter-then-join; and the
  comprehension recomputed per product instead of once after the loop
- Challenge: `case "report": ... break` ended the program, not just the report
- Challenge: `low_stock:` label vs spec `low stock:`

### Insights

- `b = a` aliases one object; `a.copy()` makes a second — mutate one, the
  other doesn't move
- Dict `in` checks keys; `d.values()` for values; sets give O(1) membership
- `{}` is a dict; an empty set is `set()`; sets are unordered → `sorted()`
- `dict.get(k, dflt)` counts; `setdefault(k, [])` groups into dict-of-lists
- `& | - ^` are the Venn diagram in code
- Empty states deserve the same spec attention as happy paths — a `none`
  fallback is part of the contract
- Interview pattern: "seen so far" set makes two-sum O(n), not O(n²)

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 7 — Modules (`import`, `random`, `sys`/`os`, package structure)

---

## Reflection — Lesson 6 (2026-08-13)

- Surprised: the effect of NOT using `.copy()` for data operations (aliasing);
  and that comprehensions build sets and dicts too, not just lists.
- Difficult: translating challenge requirements into code; and the two-sum —
  took time to find the optimal O(n) approach and understand the logic behind
  it.
- Improve: solve new problems with the new techniques and knowledge — realized
  a habit of relying on lists/tuples and not exploring dict/set methods much.
- Confusing: how to choose the right data type per problem (was following
  instructions rather than reasoning from guarantees).
- **Follow-up drill (same session): Collection Choice — 8/8 correct.**
  Set (O(1) submission dedupe), tuple (fixed lat/lon), list (ordered mutable
  task list), dict (name→email lookup), tuple (immutable config), set
  (distinct categories), list (ordered score sequence), set (`A - B`
  algebra). Reasoning was guarantee-driven — the "confusing" weak topic is
  closing.

---

## Session 7 — 2026-08-13

### Lesson

Lesson 7 — Modules (Stage 1: Python Fundamentals) — 91/100

### Exercises

- E1–E5 (easy): all correct — three import forms, `__name__` guard, seeded
  randint, choice/sample/shuffle, `os.path` methods
- M1–M3 (medium): all correct; M3 label typo (`hand1` twice instead of
  `hand1`/`hand2`) — values correct, label wrong
- H1 (hard): CLEAN SWEEP — all five module bugs (star import, shadowing,
  from-import name gap, seed-inside-loop, missing guard) found and fixed in
  one pass
- H2 (hard): coupon collector correct on first try — set + while loop + seeded
  `random.choice`, produced exact output `11 rolls to collect all 6 faces`

### Challenge

Random Team Picker CLI (`sys.argv` parsing, `--seed` flag, `random.sample`,
validation, `__main__` guard). Architecture correct on first submission —
seeded example byte-perfect, all functions SRP-clean. Error handling had 6
spec violations (see mistakes). Learner fixed 4 independently; reviewer
applied the last 2 with consent. Final version handles: seeded pick, no-args,
count>names, non-int count, count=0, seed-only.

### Mistakes

- M3: label `hand1` on the second line — should be `hand2` (copy-paste slip)
- Challenge: `parse_args` used `sys.argv` directly instead of its `argv`
  parameter — worked because `main` passed `sys.argv`, but wrong design
- Challenge: `count = args[0]` without `int()` in the no-seed path →
  `str < int` TypeError on validation
- Challenge: validation `count < len(names)` was inverted — rejected valid
  requests (2 of 3 names)
- Challenge: missing `count < 1` check
- Challenge: error messages were paraphrased (`"cant count less than 1..."`,
  `"the argv is required to be at least lenghted 3"`) not spec-literal
- Challenge: `--seed 5` alone crashed with IndexError — no argc guard for the
  seed branch

### Insights

- Three import forms serve different namespaces: `import math` (full module),
  `from math import sqrt` (one name bare), `import math as m` (alias)
- Star imports dump unknown names into your namespace — `from random import *`
  shadows your variables silently
- `__name__ == "__main__"` is Python's way of asking "was I run directly or
  imported?" — the guard is the most important one-liner in any module
- `random.seed(n)` makes randomness reproducible — the whole point of AI
  experiment control
- `random.sample` (no repeats) vs `random.choices` (with repeats) — know
  which constraint you need
- `sys.argv[0]` is the script name; real args start at `[1]` — always validate
  `len(argv)` before indexing
- Spec-literalness extends to error messages — "invalid count: N" is a
  contract, not a suggestion

### Time Studied

~1 hour

### Tomorrow Goal

Lesson 8 — next Stage 1 topic or beginning of Stage 2 (OOP / exception
handling)

---

## Reflection — Lesson 7 (2026-08-13)

- Surprised: the `__name__` guard — how it works, its purpose, and the best
  practice behind it; also the flexibility of import approaches (`import` /
  `from ... import` / alias).
- Difficult: the challenge — the business flow (translating requirements to
  code), not the technical parts.
- Next: stopping here — this completes the fundamental milestone. The learner
  has notes for the next milestone; this teaching role ends at this boundary.
- Confusing: nothing.

---

## Session 8 — 2026-08-21 → 2026-08-23

### Lesson

Lesson 8 — Exception Handling (Stage 2 opener, CORE)

### Exercises

- E1–E5, M1, M2, H2: exact contracts on first submission
- M1 highlight: tuple unpacking used as implicit shape validation — one
  ValueError funnels unpack, empty-name, and float failures
- M3: functional but spec dict mutated into the result container;
  rebuilt with a separate result dict same session
- H1: four bugs found and fixed minimally; caught that `count_skipped`
  had to return the formatted string since the driver couldn't change —
  constraint-correct where even the AI reference solution wasn't
- Hint dependency: level 0 across all exercises

### Challenge

Expense Entry Validator CLI — architecture correct on first submission,
`out=print` injectable stretch goal done unprompted. Spec-literalness
relapsed on ONE report line: colon spacing fixed round 1, trailing space
caught in review round 2 → byte-perfect final. Other nine output blocks
byte-exact first submission.

### Mistakes

- Spec-literalness relapse: matched the visible part, missed the invisible
  tail — pattern named explicitly; watch byte-exact endings
- Blueprint/output conflation: mutating spec instead of building result
- Widened except to `(ValueError, TypeError)` without stating why — fine
  for sensor `None` dropouts, but widening must be a conscious decision

### Insights

- try blocks stay small: one failure story per try
- EAFP vs LBYL is a failure-frequency decision, not a moral one
- raise at boundaries, handle where you can respond
- finally always runs — cleanup lives there, not inside try
- Clarification notes added to `notes/PYTHONIC.md`

### Time Studied

~2 hours across 3 sittings (~30 min / ~60 min / ~30 min)

### Tomorrow Goal

Read Lesson 9 — File Handling tonight, do the tasks tomorrow.
Quiz window opens around L9/L10.

---

## Reflection — Lesson 8 (2026-08-23)

- Difficult: how much code belongs inside try — resolved to "one failure
  story per try". EAFP-vs-LBYL anxiety ("is it necessary? is plain LBYL
  wrong?") — resolved: neither is wrong, pick by failure frequency.
- H1 root causes narrated traceback-first: ZeroDivisionError → mean guard;
  silent skip → missing counter increment; inverted condition → None;
  bare except → specific types.
- M3 honesty: mutated spec because "dict values can be mutated so it's
  gonna be okay" — forgot the copy approach; review showed blueprint and
  output should be separate objects.
- Pacing commitment: lesson spread over 3 short sittings; next lesson
  targeted for a single-session run.

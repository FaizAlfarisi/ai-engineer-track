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

---

## Session 9 — 2026-08-28

### Lesson

Lesson 9 — File Handling (Stage 2, CORE)

### Exercises

- E1–E3, E5 (easy): correct — round trip, append, iterate+accumulate,
  report writer. E4 logic correct (saved output shows a re-run artifact:
  `user-name.txt` already existed from a prior run, so both prints returned
  `hello, Ada` — the FileNotFoundError fallback is right)
- M1–M3 (medium): correct — transactions→summary, dual-handle filter+copy,
  typed config loader
  (M3 started EMPTY `{}` this time, honoring the blueprint-read-only rule)
- H1 (hard): five-bug debug drill found and fixed (no with / wrong mode,
  cursor consumed by `read()`, `errors` uninitialized, `.upper()`, missing
  `.strip()`); final output `processed 5 entries / === errors === / disk full / timeout`
- H2 (hard): two-pass tail implemented with streaming iteration — corrected
  after the reviewer flagged `readlines()` as a constraint miss
- Hint dependency: level 1 conceptual only (M1 try-size guidance);
  self-diagnosed the early misses as rushing, not language

### Challenge

Expense Persistence CLI — `parse_entry` / `load_expenses` (missing file → `[]`)
/
`save_expenses` (canonical `.2f` rewrite) / `merge_and_report` (`out=print`,
one try/except, report lines byte-exact). Output `loaded: 2 / accepted: 2 /
rejected: 2 / saved: 4 / total: 2494.95`; file canonicalized
(`salary,2500.00` no `+`); `total` bug fixed independently; idempotent
re-run + cold-start (deleted file → `loaded: 0`) verified.

### Mistakes

- Easy-item spec drift (rushing): `banana` key instead of `bananas` in E5 —
  missed first pass, caught in review
- E2 cell briefly left unexecuted in the rushed pass (logic correct)
- H2: `readlines()` where the two-pass streaming constraint was explicit —
  output right, constraint missed
- Error-string returns from loaders (`f"file ... not found"`) — type-mixing
  theme; mostly cleaned by revision, one left in E1 `load_text`

### Insights

- `with` = guaranteed close = your `finally`, automated
- `'w'` truncates to zero — read before you overwrite data worth keeping
- Iterate the handle to stream; `readlines()` hoards the whole file
- `.strip()` at the read boundary — the trailing `\n` rides along otherwise
- Two handles, one `with`: `open(a) as x, open(b) as y:`
- Explicit `encoding="utf-8"` on every open
- Canonicalize at SAVE time (`.2f` rewrite normalizes `+2500.00` → `2500.00`);
  a missing file is a normal first run, not an error

### Time Studied

~2 hours across several short sittings (busy week)

### Tomorrow Goal

Lesson 10 — Pathlib (now written in the plain-English spec style; read
Constraints as a checklist before coding).

---

## Reflection — Lesson 9 (2026-08-28)

- Surprised: returning error-strings from loaders surfaced again — a theme I
  thought was closing came back because I rushed the first pass.
- Difficult: H1 debug drill was the hardest to reason through — five nested
  bugs to separate; one genuine stuck point where I had to step back and
  re-read.
- Improve: read the Constraint line as a checklist before coding, verify exact
  keys/labels, and stop rushing the easy items — my misses were rushing, not
  the language.
- Confusing: nothing outstanding; the try-size question from M1 is now clear
  (per-line validation legitimately fills the try block).

---

## Session 11 — 2026-08-30

### Lesson

Lesson 10 — Pathlib (Stage 2, CORE) — 92/100

### Exercises

- E1–E5 (easy): all correct — describe, join with `/`, `.exists()`, list `.txt`,
  read_text/write_text round trip
- M1–M3 (medium): all correct — read_text summary, organize by extension
  (mkdir + rename), typed loader rewired to Path (kept clean-data contract)
- H2 (hard): correct — count files by extension
- H1 (hard): three-bug drill resolved — suffix filter case, uppercased names,
  missing `.is_dir()` guard (folder `data.py` counted as a file). Fixed in the
  notebook with inline comments.
- Challenge: correct — Folder Reporter (count_by_ext / largest / write_report),
  sorted extension summary + largest file, trailing-newline report,
  empty-folder → `None`

### Challenge

Folder Reporter — `count_by_ext` / `largest` (empty folder → `None`) /
`write_report` (builds the summary, writes with `Path.write_text`, returns the
same string the file holds, trailing `\n`). All output bytes matched.

### Mistakes

- I caught a process error myself: the H1 bug-report write-in in `solution.py`
  had been pre-filled by the reviewer at build time, so the "expected vs
  observed / root cause" narrative was already written. I flagged it and still
  did the actual code fix independently — but that section of the drill wasn't
  a real test of my analysis.
- No exercise/challenge output drift this lesson — the Constraints-checklist
  habit held.

### Insights

- `/` joins path parts and inserts the OS separator — no more string gluing
- `.name` / `.stem` / `.suffix` / `.parent` read a path's parts
- `.exists()` is a cheap guard; it does NOT mean "is a file" — a folder exists
  too, so use `.is_file()` when only files count
- `.iterdir()` returns every child — folders are children too; guard with
  `.is_dir()`
- `read_text`/`write_text` are whole-file; `Path.open()` gives the L9 handle
  for line-by-line work
- suffix comparisons are case-sensitive: `.py` ≠ `.PY`

### Time Studied

~1 hour (focused single sitting; prior-hand recall was solid)

### Tomorrow Goal

Lesson 11 — JSON (CORE); weekly-project window now open.

---

## Reflection — Lesson 10 (2026-08-30)

- Surprised: the loader-cleanliness rule from Lesson 9 (return data, never
  error-strings) carried straight into the Pathlib loader without prompting —
  it has sunk in.
- Difficult: nothing blocked me this time; the recall refinements (iterdir
  yields folders; exists ≠ is_file) were the genuinely new mental models.
- Improve: on my side — nothing new to add on the material; I want JSON to be
  as drift-free as this one. On the process side, I'll keep flagging reviewer
  mistakes early, as I did with the pre-filled H1 answers.
- Confusing: none — the case-sensitivity of suffix filters was the only thing
  I had to consciously recheck.

---

## Quiz 01 — L8–L10 (2026-08-30)

### Scope

First Stage 2 operational quiz: Exception Handling (L8), File Handling (L9),
Pathlib (L10). Formats: concept explanation, predict-output, debug-this,
code reading, one combined apply task, three T/F.

### Result: 96.4% (13.5/14) — PASS (bar 80%)

- A (concept): 3/3 — EAFP/LBYL + example, why `Path.open()`, exists vs is_file
- B (predict): 3/3 — silent error-string (`NOT FOUND`), `"world\n"` truncation,
  `8` with hidden `\n`
- C (debug): 2/2 — suffix-case + is_file guard (H1-style), bare-except
- D (code reading): 1.5/2 — D1 (return vs print) full; D2 partial
- E (apply): 1/1 — `report()` met all 8 spec points, ran correctly
- F (T/F): 3/3

### Weak concept

Exception detail (D2): intent of `raise ... from None` (clean one-message
traceback) and the `str.partition` no-delimiter edge were half-grasped.
Action: one small retrieval woven into L11, then re-assess.

### Tomorrow Goal

Lesson 11 — JSON (CORE). Weave in one exception-detail retrieval (D2).

---

## Session 12 — 2026-08-30

### Lesson

Lesson 11 — JSON (Stage 2, CORE) — 93/100

### Exercises

- E1–E5 (easy): all correct — round trip (dumps/loads), file save/load,
  iterate a loaded list (sum + list comp), indent vs compact, JSON type mapping.
  Note: E1/E3/E4/E5 were rebuilt mid-lesson to function-form by the reviewer
  after I flagged that the original drivers printed the answer themselves;
  this lesson's E1 is blank-coded again, E3/E4 drivers call my functions.
- M1–M3 (medium): all correct — safe loader (LBYL `.exists()` + EAFP
  `JSONDecodeError`), pretty round trip, typed loader with a clean
  `raise ... from None` re-raise + `match` mapping pattern route.
  M3 uses `partition` (D2 retrieval) and skips blank lines.
- H2 (hard): correct — `count_by` with `"missing"` sentinel, `None` skipped,
  first-seen insertion order preserved
- H1 (hard): four-bug drill resolved independently in the notebook — suffix
  case, folder-read crash (I hit `Permission denied: 'conf\config.json'` on
  Windows — a folder, not a file), wrong result shape (list vs merged dict),
  and the merge behavior. Full expected/observed/root-cause write-up kept in
  `solution.py` for all four.
- Hint dependency: level 0 across all exercises + Challenge

### Challenge

Expense JSON seed — `load` (missing/broken/not-a-list → `[]`) /
`categorize` (`match`: income → +amt, expense → -amt, else 0.0) /
`summarize` (category → signed total) / `save` (`json.dumps(indent=2)` via
`write_text`). Pathlib reads/writes with `encoding="utf-8"`, no raw `open`,
no error-string returns. All output bytes matched.

### Mistakes

- Latent bug in `summarize` (reviewer-spotted): `result[cat] = categorize(spend)`
  OVERWRITES instead of accumulating — it passed only because the test
  categories were unique. Still satisfy the "signed total" requirement with
  `.get(cat, 0.0) + categorize(spend)`.
- `load_typed` used `split("=")` which crashes on a blank or no-`=` line
  ("not enough values to unpack"); switched to `partition` + strip.
- No output drift this lesson — all 12 Output blocks byte-exact first
  submission; the Constraints-checklist habit held.

### Insights

- `json.dumps` = value → JSON string; `json.loads` = string → value; the file
  versions are `dump`/`load`
- JSON type mapping: `true`→`True`, `false`→`False`, `null`→`None`
- `indent=2` makes it readable; `separators=(",", ":")` makes it compact
- `JSONDecodeError` is a `ValueError` → a safe loader returns `{}`/`[]`, never
  crashes, never returns an error string
- `raise ... from None` gives the caller a clean single-message traceback
  (no chained wall) — the D2 concept finally clicked
- `match` mapping patterns route records by shape, not by `if` chains
- Accumulate, don't overwrite: `dict.get(category, 0.0) + value` — a function
  that passes the sample but doesn't implement the requirement is a latent bug

### Time Studied

~1 hour (focused single sitting)

### Tomorrow Goal

Lesson 12 — CSV (CORE); weekly-project window open (weekly project due soon).

---

## Reflection — Lesson 11 (2026-08-30)

- Surprised: the D2 weak point from Quiz 01 (`raise ... from None` + `partition`)
  came back naturally through the M3/Challenge specs, and this time it stuck —
  I wrote `from None` correctly on my own.
- Difficult: the latent `summarize` overwrite — it passed, so I thought it was
  done; the reviewer showing me the duplicate-category case made me see that a
  passing sample isn't the same as a correct implementation.
- Improve: read the requirement as a guarantee (`signed total`, `accumulate`)
  even when the sample data can't fail; and prefer `partition` for `key=value`
  lines so a malformed line is a clean error, not a crash.
- Confusing: none — the H1 folder-crash symptom was different on Windows
  (`Permission denied`) than I expected, but the root cause (missing `is_file`
  guard) was the same as L10's.
- Process: I appreciated the reviewer catching that E1/E3/E4/E5 handed over
   answers and rebuilding them as function-form — and that the H1 write-in slots
   stayed blank this time; my analysis was a real test.

---

## Session 13 — 2026-09-02

### Lesson

Weekly Project 1 — Library Manager CLI (L8–L11 integration) — 70/100

### Exercises

- Multi-module project: `solution.py` (dispatcher) + `service_add.py` +
  `service_remove.py` + `service_search.py` + `service_show_list.py` +
  `helper.py` (load_json, write_json, parse_year, list_builder, count_by_genre) +
  `custom_error.py` (ErrorBadRequest, ErrorCorruptData).
- All four commands implemented: add, remove, search, list.
- JSON persistence via pathlib with `encoding="utf-8"`. Loaders raise on
  corrupt data, return `[]` on missing file.
- Decision log filled: data shape, module split, error policy, match dispatch,
  set-based duplicate check.

### Mistakes

- Search uses `==` instead of `in` — brief says "contains," not "exact match."
- `list` output appends `count_by_genre` — extra lines not in the spec block.
  Spec-literalness slipped at project level after holding for L10/L11 exercises.
- `path.is_file` without parentheses in `helper.py:40` — same bug as L10 H1.
  Method reference is truthy, guard never triggers.
- `add` duplicate check is case-sensitive (`title in existing_title`) but
  `remove` uses `.lower()` — the two commands disagree on what "same title" means.
- `service_add.py` imports `ErrorBadRequest` from `solution.py` (circular import)
  instead of `custom_error.py` like the other service modules.
- `remove` and `search` crash with `IndexError` when no title arg is given —
  `raw[0]` on empty list, not validated like `add` does.
- `search` raises `ErrorBadRequest("no books found")` — legitimate search result
  framed as a bad request. Misleading error prefix.
- `search_index` field written to every book record but never read — dead data.
- Explicit `return` at end of `write_json` — unnecessary.

### Insights

- Module separation is a genuine engineering decision, not just file splitting.
  The decision log proved the reasoning behind each split.
- Custom exceptions (user input vs data corruption) are the right abstraction —
  the L11 loader contract works at project scale.
- Set-based duplicate check is the right data structure choice — O(1) lookup.
- The same class of bug repeats across files: `is_file` without parens (L10 → WP1),
  case sensitivity inconsistency (L3 pattern). Self-review pass needed before
  shipping.
- Spec-literalness holds at exercise level but slips at project level — different
  failure mode, same root cause (scope too wide for one mental pass).

### Time Studied

~1.5 hours

### Tomorrow Goal

Fix 9 issues from review. Then Lesson 12 — CSV (CORE).

---

## Session 14 — 2026-09-02

### Lesson

Weekly Project 1 — Library Manager CLI (second pass) — 85/100

### Exercises

- All 9 first-pass issues fixed independently:
  1. search: `==` → `in` via `search_index` (stored lowered)
  2. list: `genres` separated into its own command; `list` matches spec
     block
  3. `path.is_file()` with parens
  4. case-consistent duplicate check (both sides `.lower()`)
  5. circular import broken (service_add imports from `custom_error`)
  6. IndexError caught in `solution.py:41-42`; empty-input checks in
     remove/search
  7. no-results prints directly, no exception
  8. search_index kept and wired up
  9. explicit `return` removed from `write_json`

### Mistakes

- None in second pass — all fixes applied correctly on first attempt.

### Insights

- Same class of bug repeats across files: self-review pass before
  shipping catches this.
- Spec-literalness at project level: new behavior = new command, not
  mutated existing output.
- Decision to keep search_index was good engineering judgment — it
  simplified search to a one-liner and the stored-lowered approach
  handles case insensitivity cleanly.

### Time Studied

~0.5 hours (fix pass)

### Tomorrow Goal

Lesson 12 — CSV (CORE).

---

## Session 15 — 2026-09-04

### Lesson

Lesson 12 — CSV (SUPPORTING) — lesson materials prepared. Exercises
E1 (read), E2 (write), E3 (safe loader), Challenge (CSV Grade Book).
Data files: students.csv (E1), grades.csv (Challenge). Notebook ready.

### Notes

- CSV is SUPPORTING tier (not CORE) — shorter exercise set (2 Easy +
  1 Medium + 1 Challenge).
- Key teaching point: `newline=""` required in `open()`. All values are
  strings — type conversion is manual.
- CSV vs JSON decision: flat tables → CSV, nested/typed → JSON.
- Challenge is standalone (grade book), not integrated into Library
  Manager.
- Quiz 02 window opens after L12/L13. DSA track still due.

### Tomorrow Goal

Complete Lesson 12 exercises (E1–E3 + Challenge).

---

## Session 16 — 2026-09-04

### Lesson

Lesson 12 — CSV (SUPPORTING) — exercise + review pass — **92/100** (final,
re-reviewed)

### Exercises

- E1 (read + print), E2 (write CSV), E3 (safe loader returning data,
  never error-string), Challenge (CSV Grade Book decomposed into
  read_csv / grades_stat_builder / write_csv / main).
- Loader contract carried over hard: missing file → `[]`/raise, never
  error-string; `newline=""` + `encoding="utf-8"` everywhere.
- `DictWriter.fieldnames` derived from `data[0].keys()` independently.

### Mistakes (first draft → fixed on re-submit)

- Hardcoded `"Summary (3 students):"` + `i == 3: break` — real data
  yields 5 students. Conceded reviewer-fault: the original spec had no
  driver/Output block, so byte-for-byte was unanswerable. Fixed with
  true `len()` + sorted.
- Swallowed skipped-row warning (`# print(err)`) — fixed to a consistent
  quoted format with row number.
- `grades_stat_builder` returned unread `stats` — removed; returns only
  the summaries used.
- Earlier review (74/100) was mistakenly graded against a stale
  `solution.py` draft; the fresh file already contained all fixes.
  Re-review of the actual file corrected the score to 92/100.
- Exercise run mutated the `students.csv` fixture (Alice→92.4, Dan→abc);
  reviewer restored it to original spec data.

### Insights

- Reviewer process failure logged: L12 specs broke the L11 format —
  no Driver + Output: block per cell. Correction carried into Lesson 13:
  every exercise gets a pinned driver + exact Output block.
- "Computed but unread" is a real smell to self-check before finish
  (misconception now CLOSED — fixed independently and survives).
- SUPPORTING tier = Level 3 bar: independent implementation reached;
  transferred loader contract + decomposition into a new format.

### Review Score

92/100. Hint dependency 0. 24/25 correctness, 19/20 logic. Verified by
running against the provided `grades.csv`: `Summary (5 students)` with
all averages/statuses correct and the skipped-row warning shown.

### Time Studied

~1.5 hours (lesson + exercises + review + re-review)

### Tomorrow Goal

Lesson 13 — Packages & Multi-Module Structure (CORE) — with corrected
spec format (Driver + Output blocks) and Quiz 02 + DSA slot due.

---

## Session 17 — 2026-09-07

### Lesson

Lesson 13 — Packages & Multi-Module Structure (CORE) — exercise + review
pass — **92/100**, Level 4.

### Exercises

- E1 (module = file, `greet.py`), E2 (`words.py` + `report.py`, one
  imports the other), E3 (`textstats` package with `__init__.py`), M1
  (relative import `from .words import count_words`) — all byte-exact
  first pass.
- H1 debug drill — three planted bugs (side effect on import, relative
  import in a root script, module-vs-function) fixed independently;
  chose the `__init__.py` re-export route (`from .greet import greet`)
  so `from greeter import greet` yields the function. Renamed root
  script to `main_greet.py` to avoid a `main.py` collision with the
  Challenge (reviewer spec collision — sensible call, spec patched to
  match). Verified: rc 0, stdout `Hello, ada!`, stderr `''`.
- Challenge — `report_tool` package (load/compute/write) + `main.py`:
  first draft of `write_summary` wrote raw floats (`60.0`); fixed to
  `sorted(totals.items())` + `f"{total:.2f}"` in one independent round.
  `main` trimmed to load → summarize → write → print. Driver byte-exact.
- Specs now LEAN per learner directive: Task / File tree / Interface
  contract / Constraints / Driver+Output; clues are bridge-only. Hint
  dependency 0.

### Mistakes

- Challenge first draft: `write_summary` skipped the two-decimals
  contract → `60.0`/`153.6`/`56.0` instead of `60.00`/`153.60`/`56.00`.
  Caught on review, fixed independently (spec-literalness slip, pattern
  continues IMPROVING: 1 slip, 1-round fix).
- Design note raised + resolved: sorting/formatting moved into
  `write_summary` so it owns ordering regardless of caller; `compute`
  returns an unsorted total dict.

### Insights

- A package is a folder with `__init__.py`; importing it runs the file.
- `import package.module` runs `__init__.py` first, then the module top
  to bottom — top-level statements fire at import (the H1 side-effect
  bug).
- Relative imports (leading dot) exist only inside a package; a file run
  as a script has no parent package, so the dot has nothing to anchor to.
- `sys.modules` caches modules — re-import does not re-run the file.
- Find-before-load order: built-ins → `sys.path` folders → else
  `ModuleNotFoundError`; `sys.path[0]` is the launch folder.
- Main file imports absolutely; submodules may use relative imports.

### Review Score

92/100. Hint dependency 0. Correctness 25/25 (byte-exact after one
round), logic 19/20, format 19/20, engineering 21/20 (H1 fix choice +
rename + resilience), commentary 8/10 (reflection pending). Verified by
running all six drivers against the real files in a temp copy.

### Time Studied

~1.5 hours

### Tomorrow Goal

Quiz 02 (L08–L12) — then the overdue DSA slot. Learner reflection on L13
pending → written below (2026-09-16).

## Reflection — Lesson 13 (2026-09-07; written 2026-09-16)

- Followed the lesson flawlessly — nothing I couldn't do. Flawless doesn't
  mean nothing new: the module-vs-package line is clearer now (module = a
  file; package = a directory of modules).
- Import-runs-once has a name I can state from memory: importing a module
  executes it once, so anything that should only run when launched goes
  behind `if __name__ == "__main__":` — the H1 import-time-side-effect bug
  in my own words.
- Follow-up from WP2: I researched whether we still need `__init__.py` on
  Python 3.3+ (PEP 420 namespace packages — you can import a directory
  without it). Resolution kept: regular packages keep an `__init__.py`;
  empty is the right shape for internal layers (my WP2), re-exports are for
  a package exposing a public API, and namespace packages only matter when
  one name spans multiple `sys.path` directories. I'm not skipping it.

## Session 18 — 2026-09-08

### Lesson

Lesson 14 — Basic Typing (CORE) — completed in one session: opening
targeted practice (Quiz 02 holds), Quick Recall, exercises E1–E5 plus
M1–M3, H1–H2 and the Challenge — all 11 drivers byte-exact; one review
round closed the two misses; 92/100.

### Preparation (pack expansion)

Per learner directive ("just expand, don't change any other contract"),
L14 was expanded from under-contract to the full CORE shape
**5E / 3M / 2H + Challenge**. Rebuilt `exercises.ipynb` to 23 cells:
- E1 `greet.py`, E2 `stats.py` (`list[int]`/`dict[str,int]`/`tuple[str,int]`),
  E3 `tips.py` (new: `float` params, `-> None`, `list[tuple[str,float]]`),
  E4 `warn.py` (new trap: annotations never enforce),
  E5 `retro.py` (annotate recalled `count_words`).
- M1 `find.py` (`dict[str,int] | None`, was E3), M2 `score_tool` package
  (was M1), M3 `report.py` (new: `safe_float -> float | None` +
  `total_scoreable(rows: list[dict[str,str]]) -> float`).
- H1 `treats` debug drill (kept), H2 `export.py` (new [INTERVIEW]:
  `normalize(list[dict[str,object]]) -> list[dict[str,str|float]]` + edges).
- Challenge `budget_tool` package + `main.py` (kept; stretch = `pip
  install mypy` → `mypy main.py` clean — learner's first pip install,
  ask before running).
Also: `lesson.md` Practice table → 12 rows; `solution.py` scaffold
headers for every exercise.

Caught and fixed during validation: E4's original premise was factually
wrong (`"5" + 1` crashes, so `51` can't print) — reworked honestly: float
slips through the annotation (`4.0`), string hits Python's `+` → the
driver holds a `try/except TypeError`. One JSON-escaping defect in an md
cell repaired. All 11 cell drivers byte-match their Output blocks in real
subprocess runs; the Challenge `monthly.csv`/`categories.csv` side files
match exactly.

### Targeted practice (Quiz 02 holds, L14 opening)

- Loader data-shaped default — learner: "return dict type, it is
  guarantee an empty dict" — both the return type and the never-raises
  guarantee correct. HOLD CLOSED.
- `partition` no-`=` edge — learner picked (c): value becomes `""` so
  `int("")` raises cleanly (not silently skipped, not unpack crash).
  HOLD CLOSED.

Both Quiz 02 holds re-verified. Only OPEN thread: spec-literalness
(byte-parity).

### Quick Recall

5/5 on the retrieval items; open-book lesson recall strong (6 items, one
precision: `x: str = None` lies about its default — the annotation says
`str` while the value is `None`; the honest form is `str | None = None`).

### Exercise Results

- E1 `greet.py`, E2 `stats.py`, E3 `tips.py`, E4 `warn.py`, E5 `retro.py`,
  M1 `find.py`, M3 `report.py`, H2 `export.py`, M2 `score_tool` package,
  H1 `treats` drill, Challenge `budget_tool` package — all 11 drivers
  byte-exact in a temp-copy run.
- H2 ragged normalizer and the Challenge package passed untouched first
  try; `mypy main.py` clean (learner's first pip install).

### Mistakes

- M2 `passing` returned sorted scores `[88, 92]` instead of names
  `['ada', 'carol']` — collected values instead of keys; caught on
  review, fixed independently.
- H1: the two runtime bugs were fixed, but the two planted annotation
  lies (load.py `list[dict[str, int]]`; monthly.py untyped param +
  `dict[str, int]` return) survived until review.
- `average` briefly re-annotated to `dict[str, float]` during the M2 fix
  (a regression that would have broken the hints line) — reverted to
  `dict[str, int]` per the Output block.
- Left intentionally: 7 full-tree mypy annotation-honesty nits.

### Review Score

92/100. Hint dependency 0. Correctness 25/25 (all 11 drivers byte-exact
after one review round), logic 19/20, format 19/20, engineering 21/20
(H1 bug report, LBYL guard, `main_h1.py` rename), commentary 8/10
(reflection below).

### Time Studied

~2.5 hours

### Tomorrow Goal

Lesson 15 — OOP (CORE; enum folds in). DSA slot still overdue (after
L15). L13 reflection on Lesson 13 still pending.

## Reflection — Lesson 14 (2026-09-08)

- Decision: I built the LBYL habit on my own — check the path exists
  before acting — and reflected on it as I went.
- Independence: almost everything; for the few stuck points I used
  internet / AI to verify my code, never to write it for me from zero.
- Miss: I didn't re-check my `passing` answer against the driver output —
  it just skipped past me. There was plenty of wrong logic behind my
  first drafts; I retried fixing from my own head, and went to the
  internet only when truly stuck.
- Next: compare my output to the Output block after every run (3-second
  check) — that single habit would have caught the `passing` bug
  instantly.

## Session 19 — 2026-09-09

### Lesson

Lesson 15 — OOP: Classes & Objects (SUPPORTING) — completed in one
session: opening targeted practice, Quick Recall, exercises E1–E4,
M1–M2, H1 (debug drill) and the Challenge — all 8 drivers byte-exact;
one review round closed the three misses; 92/100.

### Preparation (personalized pack)

Per learner directive ("if it can be rushed or learn a lot at a time ...
then do it"), L15 was researched and shipped as a compact-but-real
SUPPORTING pack **4E / 2M / 1H + Challenge**, single-session, in the
Expense/Transaction domain (seeds WP2):
- E1 `transaction.py` (define a class from a spec), E2 `account.py`
  (independent instance state), E3 `display.py` (`__repr__`/`__str__`),
  E4 `kind.py` (Enum AWARENESS fold).
- M1 `ledger.py` (composition: Ledger holds Transactions), M2
  `session.py` (composition + delegation + JSON save).
- H1 `summary.py` + `main_h1.py` debug drill (2 lying annotations:
  `list[dict[str, int]]`, `-> list[str]`; 2 runtime bugs: totals
  overwrite, missing `self`).
- Challenge class-based expense core (`expense/{load,compute,write}` +
  `main.py`; stretch = `mypy main.py` clean; second stretch = switch
  kind to the E4 Enum).
Regular review verdict for the pack: all 8 drivers byte-exact; H1 planted
bugs confirmed (buggy state crashes with `TypeError ... takes 0
positional arguments but 1 was given`); fixed state byte-exact.

### Targeted practice (L15 opening)

- Signature contract — learner read the *return* side correctly
  (`dict[str, float]`) but skipped the *parameter* side
  (`list[dict[str, str | float]]`) — PARTIAL-CLOSED with a
  read-both-sides reminder; re-surfaced later as the H1 `object` miss.
- `partition` no-`=` edge re-verified — CLOSED (unchanged).
- Path-is-a-class: learner realized unprompted that `from pathlib import
  Path` imports a *class* and `Path("...")` creates instances —
  CLOSED.

### Quick Recall

All 6 answered correctly. 1. `self` = this particular object, passed
automatically as first arg (`Class.method(instance, ...)`) — stated the
mechanism fully. 2. Instance independence — concept correct, asked for
the memory-level explanation (each `Account(...)` builds a fresh object,
`self.balance` stamped onto that object; class is only the template). 3.
`self.x` vs class-body `x` — instance vs shared class attribute,
correct. 4. Stateless pipeline stays functions — correct. 5.
Composition "has-a": `Ledger` holds `Transaction`s — correct. 6. Enum =
fixed member set, typo-proof — correct.

### Exercise Results

All 8 drivers PASS byte-exact against the real files (temp-copy run).
Challenge: `mypy main.py` clean — stretch met. `mypy main_h1.py` clean
only *after* the review fix (learner never ran it during the lesson —
their own miss). Audit notes: `get_date` named sort key, `csv.DictWriter`
in write.py, main.py printing from the CSVs it wrote; `kind: Kind`
compared with `is`. M2 produces `session_out.json` (driver artifact,
deleted before commit).

### Mistakes

- H1 `records: list[dict[str, object]]` — vaguer than the required exact
  `str | float`; drivers pass, `mypy` breaks on `object`-not-indexable
  and `totals = {}` needs an annotation. Fixed at review to
  `list[dict[str, str | float]]` + `totals: dict[str, float] = {}`
  (mypy main_h1.py then clean). Same spec-literalness thread as L14
  `passing` — the parameter side of the contract slipped this time.
- `display.__repr__` and `main_h1.main()` missing `-> None` on first
  pass (both required by specs) — fixed.
- Mypy coverage: only ever ran on `main.py`, never the H1 entry point —
  the planted annotation lies went unnoticed until review.
- One external look-up: navigating the composed-method reuse
  (`Session.add` delegating to `ledger.add`) — learner went to Google
  for the approach. Boundary noted: check logic, don't fetch it.

### Review Score

92/100. Hint dependency 0. Correctness 25/25 (all 8 drivers byte-exact),
logic 20/20, format 19/20 (annotation gaps + `object` drift), engineering
20/20 (composition/delegation, mypy clean both entry points, elegant
main data flow), commentary 8/10 (one external look-up, mypy-skip,
honest reflection below).

### Time Studied

~3 hours

### Tomorrow Goal

DSA slot #1 (overdue — next session, separate commit). Then Lesson 16 —
Dataclass (SUPPORTING; further Enum practice). L13 reflection on Lesson
13 still pending. WP2 window opens after L16.

## Reflection — Lesson 15 (2026-09-09)

- Decision: the hardest part was reusing the class method through
  composition (delegating via `Session` → `ledger.add`); I went to
  Google to find the solution.
- Independence: almost everything except that one composed-method
  reuse — I should verify, not fetch; a one-off on a new pattern, but I
  want it on my watch list.
- Miss: I skipped running `mypy` on `main_h1.py`, my bad — the H1
  annotation lies would have surfaced immediately if I had checked the
  whole entry-point set instead of just `main.py`.
- Next: get used to analysing things with multi-layer behaviour —
  inheritance + collection data + composition — tracing one object's
  method calls through the objects it holds.

## DSA Session #1 — 2026-09-09

### Problem

Find the category with the highest total spent, from a payments log of
`(category, total)` pairs; return `(category, total)` — first DSA track
session (Week 1; slot was overdue after L15).

### Session notes

- First plan compared single payments against a running max — solves
  "largest single amount", not "highest total". Counterexample
  (8 × 15.0 food vs 100.0 salary) surfaced it: `("food", 120.0)` wins.
- Corrected 2-phase plan: group `category → total` in a dict
  (`result[cat] = result.get(cat, 0.0) + amount`), then
  `max(result.items(), key=lambda pair: pair[1])`.
- `max(result.values())` returns the total without the category;
  `max(result, key=result.get)` returns the category without the total —
  both discussed before settling on items + key.
- Edge cases: empty log → decided `None` return (no error-string mixing,
  per L9 loader habit); single entry fine; ties first-seen (dict
  insertion order, preserved by strict `>` in the one-pass variant).
- Complexity: O(n) build + O(k) scan ≈ O(n); O(k) space. Learner probed
  "is there anything better than O(n)?" — answer: no, reading every
  payment is a lower bound; the only win is constant-factor (single-pass
  running max). `max()` is O(k), not O(1) — misconception corrected.
- Nice final solution, one contract nit: annotation said `int` but the
  amounts were floats — annotate the real data (`tuple[str, float]`).
- Difficulty: intermediate (the "group first" insight was the crux).
- Logged in `PROGRESS.md` → DSA Log Row 1 (Week 1).

## Session 20 — 2026-09-11

Lesson 16 — Dataclass (SUPPORTING) — 92/100

Session ran under the learner's emergency-duty day; exercises were
solved without hints and verified by the reviewer in a temp copy.

### Session notes

- Quick Recall 6/6 — `@dataclass` auto `__init__`/`__repr__`/`__eq__`;
  `default_factory` for mutable defaults (shared-object aliasing);
  frozen ⇒ immutable ⇒ hashable; plain `dict` for one-off bags; JSON
  encoder needs a custom `default=` helper returning `enum.value`;
  `Ledger.net()` tracing through composed layers.
- Pack 3E/2M/1H + Challenge, Expense/Transaction theme (seeds WP2),
  L15 review lessons folded in: mypy on **both** entry points from the
  start, "the annotated fields ARE the spec."
- H1 four-bug drill — all four caught and correctly attributed in one
  pass: shared mutable default (`field(default_factory=list)`),
  `amount: str` lie, frozen-record mutation (`FrozenInstanceError`),
  `kind == "income"` never True (net −120.50 vs 79.50).
- Challenge: L15 `expense/` package refactored onto the frozen dataclass
  + `Kind` model — same interfaces, byte-exact output, `mypy` clean.
- H1 write-up left blank (duty); worked model bug report provided in
  `review/lesson-16-review.md` for transcription.
- DSA #1 was checked in for Week 1 logging; Week 2 session now due.

### Reflection — Lesson 16 (2026-09-11)

- Decision: the hardest moments were the **purpose of a dataclass**,
  **solving the enum problem**, and the **frozen constraint**. A legit
  new concept — so much fresh info.
- Independence: reread the lesson again and again, searched Google, and
  only then asked AI to explain the concepts. All four H1 bugs were my
  own catch. (Wean note from review: lesson + reviewer before GenAI next
  time.)
- Miss: the debug write-up under emergency duty; and I leaned on AI for
  concept explanation where "what is this for" was the question.
- Next: transcribe the worked bug report in my own words; WP2 kickoff
  (Environment & Dependency folds in); L13 reflection still owed; DSA
  #2.

## Session 21 — 2026-09-11 → 2026-09-16

### Lesson

Weekly Project 2 — Expense / Transaction Manager CLI (Stage 2 capstone,
mandatory evidence) — **88/100 LOCKED** (round-1 draft 73/100; final
score set in `projects/weekly-project-02-expense-manager/review-2.md`).

### Session notes

- Kickoff: brief written with the four commands (`add` / `list` /
  `report monthly` / `report categories`), three detailed stretches
  (summary / `--seed` / weekly), and frozen output blocks (byte-exact
  contract). Environment & Dependency folded in and done entirely by
  yourself: `.venv`, `pip install mypy`, `requirements.txt`,
  `.gitignore`.
- You consciously skipped SG2 (`--seed`) — deterministic core behavior
  over a random data generator; documented why in the decision log.
- Built the layered package yourself: `configurations/ models/
  repositories/ services/ utils/` + a `main.py` router; frozen L16
  `Transaction` + `Kind` used end-to-end; every report is printed by
  re-reading the CSV just written (one source of truth). Also finished
  SG1 `report summary` and SG3 `report weekly` — both byte-exact.
- Round-1 review (73/100 draft): 11 issues — `Added:` missing `.2f`;
  load path trusting bad JSON; lenient `strptime`; error drift + exit 0;
  `--seed` stub printing a literal `None`; unpadded ISO week; errors on
  stdout; swallowed formatter failures; missing `-> str`; UTF-16
  requirements; tracked CSVs. Matrix reconciled to the scoped-prefix
  contract (T1–T17: errors on stderr, exit 1). `review.md` kept intact.
- Round-2 (this file): full matrix re-verified in a **temp copy** —
  **25/25 green in one run**, including `mypy main.py`, T14 canonical
  date rejection, T13 corrupt-data message, and SG1/SG3. A new
  regression in the decoder guard (`and` vs `or`) was caught in the
  round-2 read and fixed by you before the run — the test suite now
  proves it.
- Your decision-log reflection (written at the end of the fix round):
  datetime was the genuine struggle (barely used before; new concept),
  the json→`Transaction` decode took real thought (auto-decode via
  `object_hook` beat looping), and the project design took ~2h of
  analysis. Solving: tutorials + GenAI as *teacher* for datetime,
  internet for the decoder idea, and your Go-project structure as the
  package-shape reference.

### Time Studied

~6 hours total (planning ~2h + build sessions + review-fix rounds)

### Tomorrow Goal

Stage 3 opens with Lesson 17 — Testing (pytest). L13 reflection still
owed; DSA #2 (Week 2) due.

## Session 22 — 2026-09-20

### Lesson

Lesson 17 — Testing with pytest (CORE, Stage 3 opener) — **98/100**
(draft round-1 92/100; closed after round-3 fixes), **52/52 tests green**.

### Session notes

- Quick Recall 6/6 before the exercises: tmp_path/loader contract,
  `test_*` naming, a no-assertion test proves nothing, ScopeMismatch
  (a wider fixture may never request a narrower one), parametrize
  `ids=` localizes a failing row, capsys/tmp_path/test-suite roles.
- Built E1–E5, M1–M3, H1, H2 + the 4-file Challenge; fixture moved into
  `conftest.py`, `monkeypatch` seam proof, `-0.0 -> "zero"`, byte-exact
  report tests. Full suite 52/52 green (read-only verified, caches off).
- Review ran three rounds:
  - R1 (92/100): three "green for the wrong reason" tests flagged —
    vacuous CSV loader test, `returns_float` asserting `== 0.0`, and a
    `for` loop inside a test; plus cosmetics.
  - R2: the honest `isinstance` fix exposed the trap — `total_spend([])`
    is `sum([])` = `int 0`, so the empty fixture fights the assertion.
  - R3: the test carries its own `[1.5, 2.5]` input, the loop is gone,
    suite green.
- Notebook aligned with the shipped solution: E5 re-pinned 6→7
  (`test_signed` added), spec text rewritten, ANSI outputs normalized,
  the learner's H1 bug-report cell preserved.
- Learner feedback: why-`ids`, built-in methods (`splitlines`,
  `isinstance`, `float()`), and `lambda` were untaught → re-learned via
  internet + GenAI. Why-ids line patched into the E5 spec; carry-forward
  note placed in `review/lesson-17-review.md` (pre-teach or declare
  `lambda`; keep built-ins explicit in specs).

### Reflection — Lesson 17 (2026-09-20)

- Decision: reframed the loader test to honestly claim CSV rows are junk
  to the number loader, and removed the redundant loop test. Re-learned
  a lot of theory through the internet + GenAI (why `ids=`, built-in
  method usage) — theory the lesson and exercises did not explain.
- Hardest to debug: `test_total_spend_returns_float` — it took the
  longest because I did not get the *intent* of fixing that test case;
  the honest `isinstance` check then revealed `sum([])` is an int, not a
  float.
- Concepts reused: the Path concept, `lambda` (not officially learned in
  this Learning OS), and type methods (`splitlines`, `isinstance`).
- Next: solve the buggy/unsatisfying parts independently instead of
  waiting through my mentor's 2–3 review rounds.
- Skipped per learner: the alternative-considered prompt and the
  change-if-requirements prompt. Hint dependency (reviewer-assigned):
  level 0 for exercise solving — E1–M3, H1 (all four bugs) and the
  Challenge done unaided; level 1–2 during the three review-fix rounds,
  where the "green ≠ proven" findings guided the test-intent fixes.

### Time Studied

~2 hours total (learner estimate)

### Tomorrow Goal

Lesson 18 (learner's choice: L18 first). DSA #2 (Week 2, due) stays owed
and queues after L18 per stage-lesson isolation. L13 reflection recorded
2026-09-16.

### Coach Feedback — Session 22 review (learner → mentor)

The learner reviewed this session before moving on. Standing calibration
for L18 and all future targets.

1. Lesson coverage: exercises used mechanisms the lesson never taught —
   `lambda`, `isinstance`, `str.splitlines()`/membership. lesson.md has
   zero mentions; they appear in budget.py:11, price_utils.py:51,69,
   test_print.py:12, test_report_cases.py:19,28. The learner asked GenAI
   for the *intent* of almost every exercise.
   → Action: coverage audit gate at lesson build (every exercised
     construct taught with ≥1 worked example, or declared "provided").
2. Exercise intent not delivered: specs gave command/expected/constraints
   but not the mechanism-intent, so instructions felt absent.
   → Action: mechanism-intent lines in specs and lessons.
3. Drilling approved; disappointment targets teaching completeness only.
4. Tagging bug: notebook spec Type = `medium` for E5 (table: Easy) and
   H1 (table/curriculum: Hard). E/M/H is a contract.
   → Action: spec Type == practice-table tier, enforced at build.
5. Scoring too loose: 98 was holistic, skipped SCORING.md buckets
   (Correctness 25·Logic 20·Readability 15·Naming 10·Maintainability
   10·Pythonic 10·Testing 5·Performance 5), rewarded assisted fixes too
   cheaply. The learner's ~90s instinct was right.
   → Action: bucket-derived scores, adjusted for hint dependency and
     independent-fix ratio, from L18 onward.

## Session 23 — 2026-09-22

### Lesson

Lesson 18 — HTTP & API Concepts (CORE, Stage 3) — **93/100**,
mastery 3→4, hint dependency 0. First bucket-scored lesson (Coach
Feedback #5 applied).

### Session notes

- Quick Recall 6/6 before the exercises, including the two non-obvious
  ones: `HTTPError` must be caught before `URLError` (subtype), and the
  response body must be read once then decoded once.
- Built E1–E5, M1–M3, H1, H2 + the Challenge. All 9 suites green,
  read-only verified in the lesson folder (caches off): H1 `4 passed`,
  H2 `3 passed`, Challenge `2 passed`.
- H1 debug drill: all four planted bugs fixed traceback-driven, each
  mapping to a lesson.md "common mistakes" entry (double read →
  JSONDecodeError; wrong dict key after decode; missing `urlencode` for
  the space in "new york"; `except URLError` before `except HTTPError`).
- H2 is genuine engineering: `StoreAPI` context manager, daemon serving
  thread, per-instance `ITEMS`/`NEXT_ID` reset, and `_safe()` sweeping
  `ConnectionResetError`/`BrokenPipeError` seen during live runs — real
  operability work, not theory.
- Challenge merge logic correct and pinned: `fresh = len(network)`,
  `kept = len(cached − network)`, network overrides cache, output sorted
  by id. Pin `Cache: 5 items (fresh 4, cached 1)` exact; missing
  `--refresh` now exits 1 with usage on stderr.
- Review findings + independent fixes: M1 broad `except Exception` →
  `json.JSONDecodeError`; `status_family` gets `case _: return "?"`;
  `--refresh` guard; `timeout=` on clients; dead `# resp.read()` removed;
  import lines split (incl. the one-line fix in `client_basics.py` this
  session). 7/8 findings fixed unaided — independent-fix ratio strong.
- **Deliberate spec deviation (kept by learner decision):** H2 exercise
  contract calls `store_server.start(port=0)`; learner's module exports
  the `StoreAPI` class instead. Behavior fully correct and pinned by the
  learner's own `test_store.py`. Consequence applied: interface-criterion
  deduction only (~2 pts), BEFORE scoring out of 100. Contract-faithful
  reference delivered as `store_server_ref.py` + `test_store_ref.py`
  (trust the l18bld temp model, not the earlier pasted draft); both H2
  suites pass side-by-side (6 passed) — proves class-based and
  factory-based server designs are drop-in compatible with the same
  `store_client.py`.
- Notebook: 24 cells valid (spec + drivers), all driver cells executed,
  H1 bug-report slots filled by the learner in-session.
- Housekeeping: stray `cache.json`, `cache.csv`, `.pytest_cache/`,
  `__pycache__/` removed from the lesson folder; re-verification run
  green (12 passed) after cleanup.
- Review: `review/lesson-18-review.md` (bucket table 23/20/14/10/8/8/5/5).

### Reflection — Lesson 18 (2026-09-22)

- What decision did you make? I created a new local_api that was
  unnecessary — but I learned from that: first, I have to read the
  instructions more carefully; second, I can read the code behind the
  provided local_api and reproduce it (even though it was mostly just
  mirroring it). For the Challenge merge function I used set and dict
  for efficient computation.
- Why that approach? What alternative did you consider? The set/dict
  approach is one of the behaviors I want to build, so I took time to
  think and research. The alternative was using a list and looping.
- Which bug took the longest to diagnose? No hard bug — it was kind of
  obvious.
- What misunderstanding caused it? Not reading carefully, and the
  instruction did not show the flow clearly. I lack English skill.
- Which concept from a previous lesson did you use? A lot — type hints,
  pathlib, json, csv, try/except, the `__main__` guard, etc.
- What would you change if requirements changed? I don't know yet —
  because my process is: decide the problem first, then build the
  solution at the higher level, then build it at the lower level. So a
  requirements change would re-trigger the problem-first decision, then
  the high-level design, then the low-level build.
- What could you implement fully independently next time? I want to
  build the behavior of computing as efficiently as possible, using
  things like set and dict, based on my own knowledge.
- Hint dependency this session — exercises level 0; review-fix loop
  level: (reviewer-assigned: level 1 diagnostic → learner implemented).

### Time Studied

~2.5 hours total (learner estimate)

### Tomorrow Goal

DSA #2 (Week 2, due) then Lesson 19 — Requests (CORE). L13 reflection
recorded 2026-09-16. L18 reflection pending above.

## DSA Session #2 (Week 2) — 2026-09-22

### Problem

Find the earliest minute at which two trucks are in the same city at the
same time, from two sorted-by-minute `(minute, city)` logs; return
`int | None`. Pattern: **two pointers** (first time applied in practice).
~1h.

### Session notes

- Drill opened with a flawed example (I shipped a coincidence that didn't
  exist) — the learner spotted it, not me.
- Brute force (O(n·m)) leapfrogged by the learner on instinct; the skip
  was named at the drill gate, not punished.
- First solution was a dict/set comprehension from one log: O(n+m) time,
  O(n) space, sortedness unused. Learner then reasoned: "if the data
  contract says sorted, two-pointer is worth it; if not, set is better" —
  the decision is now explicitly contract-driven.
- Two-pointer: tie → compare city, advance **both** (justified by
  strictly-ascending minutes: each minute appears once per list, so a
  non-matching tie can never match anything later); first-found-is-
  earliest by sortedness. O(n+m) time, O(1) space.
- **Authentic review catch:** implemented in notepad, no IDE — `data[i]`
  instead of `data_a[i]` (NameError). Fixed by reading the traceback;
  the fail-fast error did its job (L8 idiom held under pressure).
- Verified 6/6 read-only: coincidence at 8, no-coincidence → None,
  tie-different-city → None, empty-a / empty-b → None, same-city-twice
  in one log → returns the later minute (20) with no special casing.
- Interview verbal explanation delivered; graded on invariant, tie-case,
  earliest-correctness, complexity — all four hit.
- Logged: `PROGRESS.md` DSA Log Row 2; average score moved to 91.3.
- Next: Lesson 19 — Requests (CORE). Week 3 DSA due next week.

### Coach Feedback — Session 23 review (learner → mentor, 2026-09-22)

Recorded verbatim-append; no existing record altered. Standing
calibration for L19 and all future targets (executes as V3 instruction).

1. Exercise intent not showing: specs must carry the real intent
   up front — clearer information, highlighted important info and main
   intent, personalized to the learner's skimming + English struggle.
   → V3: Intent-first specs (`exercise-template.md`, Spec Language).
2. Unsynced knowledge: `--refresh` flag handling required in the L18
   Challenge though `argparse`/flag parsing was never taught (zero
   repo hits — Stage 1 only touched raw `sys.argv`).
   → V3: Coverage Contract, teach-first (industry-framed) → PROVIDED →
   never silent; `LEARNER.md` Tool Sync is the check-list.
3. Lesson-pattern grounding: the builder must repeat L18's proven shape
   (full-form CORE table, blank H1 write-ins, bucket review), since md
   instruction alone was not followed.
   → V3: `LEARNER.md` Proven Lesson Shape; CORE full form, other tiers
   flexible per `CURRICULUM.md` pipelines.

## Session 24 — 2026-09-24

### Lesson

Lesson 19 — Requests (CORE, Stage 3) — **96/100**, mastery 3→4, hint
dependency 0. Mirror-transfer of L18's wire onto the `requests` library;
no GenAI used (translator + Google-for-syntax only).

### Session notes

- Quick Recall 6/6 before the exercises, including the guard-`or`
  retrieval (Q6: `and`-under-negation lets truthy non-strings through;
  fix is `or`) — WP2 OPEN item stated correctly out loud.
- Built E1–E5, M1–M3, H1, H2 + the Challenge. All 11 drivers byte-exact
  and both suites green on first verification (read-only, caches off),
  re-verified green after the fix round.
- H1 debug drill: all four planted bugs fixed and attributed in the
  learner's own notebook cell (`data=` vs `params=`, if/else vs
  `raise_for_status()`, `temp` vs `temp_c`, `HTTPError`-first).
- Review ran one round with 5 diagnostic findings, all explained
  correctly then fixed independently same session: M1 truthiness guard
  → `not isinstance(path, str) or ...`; `post_json`/`search` invented
  except-branches (str-returns vs annotations) deleted back to spec;
  `save_csv` header pinned literal (sync_cli already had it right);
  `sess_client` regained `from exc` chaining. E2 `timeout=3` vs spec
  `timeout=5` retained-with-reason (lesson-standard, unobservable).
- Builder feedback from learner (logged for L20+): H-drill drivers
  should print failing test names + short tracebacks, not just the
  `N passed` count — during trials the cell output hid the real failure.
- Housekeeping: `__pycache__/` removed post-verification. `.venv/`
  (~99 MB) still inside the lesson folder — relocate before commit.
- Review: `review/lesson-19-review.md` (bucket table 25/20/14/10/10/9/4/5).

### Reflection — Lesson 19 (2026-09-24, learner's own words, condensed)

- Decision: auto-drove exception handling from habit instead of the
  spec — no fresh idea needed, the main concept is L18's with `requests`
  swapped in. Fix instinct going forward: determine the required changes
  first (e.g. Challenge with multiple routes would need a `match`
  handler), then build.
- Hardest to diagnose: nothing hard, but trials cost time because the
  H-driver cell output didn't show the real test report — a builder gap,
  not a knowledge gap.
- Concepts reused: almost all of them (pathlib, json, csv, try/except,
  `__main__` guard, match) — urllib replaced with requests throughout.
- Process commitment: slow-paced reading without helpers — pushing to
  understand spec English directly rather than routing through the
  translator.
- Hint dependency this session — exercises level 0; review-fix loop
  level 1 (reviewer-assigned: diagnostic → learner implemented).

### Time Studied

~3 hours (learner-reported 2026-09-24; L20 also ~3h).

### Tomorrow Goal

Quiz 03 window OPEN (L17–L19: pytest + HTTP + Requests). WP3 window
OPEN. DSA Week 3 due next week. L19 study time still owed.

## Session 25 — 2026-09-24

### Quiz build

Quiz 03 (L17–L19) built per learner-approved plan: `quizzes/quiz-03-l17-l19.md`
(18 pts — A concept ×3, B predict ×3, C debug ×2, D reading ×2, E offline
apply with `tmp_path`, F T/F ×3; weak-concept report table included).

### Validation

Every executable claim verified live against `local_api` + `requests`
2.x in staging before shipping: A1 both branches, B2 (`True False True
True`, `or` never crashes), B3 exact dict, C1 parent-first swallows 404,
C2 `IndexError` on `[]`, D1 both probes `"slow"` 5/5 (`ReadTimeout` vs
`ConnectTimeout`, the latter subclassing both parents — captured as the
deep question), E URL + merge ids `[1, 2, 3, 5]` fresh 2 kept 2.

### Standing decision (learner-proposed, mentor-confirmed)

WP3 deferred until after L20 (Project Structure) + L21 (Logging) as a
half-stage integration (modules + logging + testing + HTTP). Quiz 03 +
targeted practice covers retrieval meanwhile.

### Tomorrow Goal

Learner takes Quiz 03 in chat. Then grading → weak-concept report →
targeted practice at L20 opening.

## Session 26 — 2026-09-24

### Quiz 03 taken + graded

Scope L17–L19, answered in chat. **82.9% (14.92/18) — PASS (bar 80%).**
E built in `quizzes/quiz-03-l17-l19/` (`report.py` + `test_report.py`) —
verified green (1 passed, Summary block byte-exact).

### Grading notes

- Strong: A1/A2/A3 all correct; B3 + E merge/accumulate independent;
  C1 handler order complete; byte-parity exact on B2/B3/E strings.
- Deductions: B1 201 unnamed (−0.25); B2 crash instance backwards —
  `"/a"` named, real crashers are `None`/`123` (−0.5, WP2 OPEN stays
  OPEN); C2 exception unnamed + fix not shown (−0.5); D1 invented
  `requests.NetworkError`, fact right explanation wrong (−1.0, new gap:
  `ConnectTimeout` diamond); D2 revocation sub-question skipped (−0.5);
  F3 wrong, contradicting own C1 (−0.33).
- E placement question (answered): quiz work lives in
  `quizzes/quiz-03-l17-l19/`, quiz files stay clean markdown.
- Housekeeping: `__pycache__/` + `.pytest_cache/` removed from the quiz
  work folder post-verification.

### Tomorrow Goal

L20 Project Structure (CORE) opens with the Quiz 03 targeted pair
(guard-`and` crash inputs + handler-order/`ConnectTimeout`), then
re-assess. DSA Week 3 due next week. L19 study time still owed.

## Session 27 — 2026-09-24

### Lesson

Lesson 20 — Project Structure (CORE) — **94/100**, mastery 3→4, hint
dependency 0–1. Adapted volume per learner challenge (3E/3M/H1/H2/Challenge —
restructuring reps, not recognition padding); Challenge = neutral ledger
project (fresh experience over L19 rehouse, learner's choice). ~3 hours
(learner-reported; L19 also ~3h).

### Session notes

- Quick Recall 6/6 with one precision repair (Q6 `and`-table: `""`/`123`
  slip through, only falsy non-strings raise — corrected in chat).
- Built E1–E3, M1–M3, H1, H2 + Challenge. First verification: 8/9
  drivers + H2 cell damaged in workspace (`_out` line lost in an editing
  accident — restored as build artifact, not learner work).
- Review found 6 findings, all on untested paths (usage-to-stdout ×3,
  `ledged` typo, bare-run default, set-vs-list fresh, vacuous
  roundtrip) — learner explained all correctly (incl. disclosing GenAI
  use on Issue 1 without reasoning) and implemented all fixes; 1
  `.gitignore` line reviewer-applied with consent.
- Post-fix verification: 9/9 drivers byte-exact, 14/14 pytest green
  (4 messy + 4 restructure + 3 shop + 3 ledger).
- Standing learner requests recorded (LEARNER.md untouched — revision
  agent's file): harder H-drills + fewer hints from L21; style guidance
  from outside sources to be converged (review holds the verdict).
- Incident (reviewer fault, recovered): a cache-cleanup command
  over-matched and deleted fixture trees + untracked learner work.
  Fixtures restored from git (`88401b1`); all learner files rewritten
  from verified post-fix reads; re-verified 9/9 + 14/14 identical.
  Lesson relearned: explicit cleanup paths only.
- Housekeeping: `summary.csv` stray removed (learner), caches removed
  post-verification. In-folder `.venv` question still open from L19.
- Review: `review/lesson-20-review.md` (bucket table 24/20/14/10/9/10/5/5;
  95+ bar judged unmet — Challenge stream concept + 1 assisted line).

### Reflection — Lesson 20 (learner's own words, condensed)

- Simplification under time pressure: skipped edge handling, solved
  only the expected, inconsistent internet-sourced style — asks for an
  evaluation of current writing behavior vs best practice (delivered in
  review: keep absolute imports/`!r` guards/small functions; converge to
  `raise SystemExit(main(argv))`, argv-taking mains, docstrings,
  writerows).
- Decision: focus on lesson topic only (busy season); style follows the
  internet for now.
- H1 easier than previous lessons — wants harder drills, fewer hints
  (recorded). Challenge stderr was new knowledge (internet + GenAI).
- Reused almost all previous concepts; will push for independent
  expected-results even when slow.

### Time Studied

~3 hours (learner-reported).

### Tomorrow Goal

L21 Logging (CORE; harder H-drill + fewer hints). Then WP3 half-stage
integration. DSA Week 3 due next week.

## Session 28 — 2026-09-27

### Lesson

Lesson 21 — Logging (CORE) — **91/100**, mastery held at 3, hint
dependency 2. Harder H1 (5 bugs, single-hint per standing request);
bulleted Interface Contracts (house style from learner feedback).
~6 hours (learner-reported; heaviest single lesson on record).

### Session notes

- Quick Recall 6/6 (Q4 half, repaired in chat: duplication needs two
  stream handlers AND explains nothing about the file — zero FileHandler
  or over-gated one does that half).
- Built E1–E3, M1–M3, H1, H2 + Challenge. Staging caught 4 build defects
  before shipping (non-lazy "lazy" fix → `isEnabledFor`; `-c` compound
  statements; `NullHandler.handle` no-op vs filters; child-before-parent
  loggers never link; named-logger gate starving the file).
- Review found 5 findings; learner pushed back on Issue-2 framing
  (accepted — restated plainly: corrupt feed yields confident zero with
  zero forensics) and reported all fixes; 2 micro-fixes reviewer-applied
  with consent (counter guard, sync strictness).
- Post-fix verification: 9/9 drivers byte-exact, 15/15 pytest green
  (5 logging + 4 tracked + 3 load + 3 journal).
- Learner calibration (applied, LEARNER.md untouched): harder = H1 bug
  analysis ONLY; lesson + exercise delivery stays fully legible;
  H-specs name every suite-imported deliverable (setup_logging lesson).
- Environment repaired mid-build (`idna` + `requests` reinstalled).
- Review: `review/lesson-21-review.md` (bucket table 24/20/14/10/10/10/4/5;
  95+ bar judged unmet — hint-2 solving).

### Reflection — Lesson 21 (learner's own words, condensed)

- Near-surrender lesson: confusing delivery (no clean usage guidance,
  style-vs-use-cases; exercise statements + indirect expecteds) — led to
  internet + GenAI for lesson explanation and exercise clues, not just
  translating. Builder failures accepted (2, now standing rules).
- Longest stuck point: H1 setup_logging ("idk if I'm supposed to create
  that") — solved everything else first (correct triage).
- Root problem named as lesson delivery (accepted in part, per above).
- Style following the internet for now; will push for independent
  expected-results even when slow.

### Time Studied

~6 hours (learner-reported).

### Tomorrow Goal

WP3 half-stage integration brief (testing + HTTP + structure + logging).
DSA Week 3 due — interleaved at learner's call.

## Session 29 — 2026-09-29

### WP3 kickoff

Brief written per approved plan: `projects/weekly-project-03-sync-service/`
(`brief.md` + `decision_log.md` + blank `main.py` + PROVIDED `stub_api.py`,
smoke-tested live: 4 items, ids 1–4).

### Design notes (builder's record)

- Feed Sync & Report Service: `sync [quiet|verbose]` + `report value` +
  `report low N`; network-wins merge; readback discipline; three verbosity
  modes + `service.log`; scoped errors (`bad request:` / `network error:`
  / `corrupt data:`, stderr, exit 1); `SYNC_API_BASE` override for the
  network-error row.
- All pins hand-computed then verified by execution (Total 197.20, low-10
  pair, restock-20 block); 17-row matrix (T1–T17) mirroring WP2 rigor.
- Stretches: SG1 summary, SG2 restock, SG3 report.json export.
- One mid-write editing scar caught and removed before shipping (a
  self-correction left inside the brief — the exact confusing-statement
  class the learner flagged in L21).

### Tomorrow Goal

Learner builds WP3 independently (multi-commit). Then formal review +
acceptance matrix + reflection + PROGRESS update.

## Session 30 — 2026-10-05

### WP3 review round 1 (build mode, learner-consented corrections)

Project finished after a sparse week. Full T1–T17(+T7b/T10b) matrix run
in a temp copy; 9 reviewer-side corrections applied with explicit
consent, then re-verified green (matrix + 5 tests + mypy clean).

### Design answers given (learner's 3 confusions)

- Q1 data flow: pros/cons of dict-at-api + decode-in-use-case analyzed;
  rule = parse at the perimeter, trust inside; concrete move = decode in
  `api.get_items` (left for learner's fix loop — architectural call).
- Q2 conversion placement: ingestion owns parsing, use-cases orchestrate
  typed values.
- Q3 T11 simulation: PowerShell env-prefix form given; underlying gap
  found (env unwired) and fixed in review.

### Corrections applied (all re-verified)

SYNC_API_BASE wiring · levelname formatter + urllib3 silence · corrupt
two-line shape + wrong-shape guard · Optional narrowing (mypy clean) ·
UTF-8 requirements · module-logger consistency · frozen Item · brief
amendments T7/T7b/T10/T10b + acceptance (spec-ownership rule).

### Still owed by learner

README · decision rows 4–5 substance · technical reflection ·
caplog-honesty rewrite (throwaway-logger test → own-logger test).

### Tomorrow Goal

WP3 close-out items from learner, then commit. DSA Week 3 still due.

## Session 31 — 2026-10-06

### WP3 close-out (round 2)

Learner delivered README (run/verbosity/env/tests), decision rows 4–6
(incl. timeout-30 rationale), honest caplog rewrite (own storage logger).
Original-result disclosure given (round-1 reconstruction: ~87 buckets,
5 red rows, unshippable as specced). Non-template reflection answered
3/4 (Q2 detection-story left open, recorded). Final confirmation green
(tests 5/5, mypy clean, in project folder). Score stands at **86/100**;
review.md round-2 section written.

### Tomorrow Goal

Commit WP3. Then DSA Week 3 (due now) → remaining Stage-3 topics.


`# Progress

Current Stage:

Stage 1 — Python Fundamentals

Current Lesson:

Lesson 7 — Modules

Current Week:

Week 1

---

## Completed Lessons

- [x] Lesson 1 — Variables & Data Types (93/100)
- [x] Lesson 2 — Operators & Strings (90/100)
- [x] Lesson 3 — Boolean Logic, I/O & Conditionals (92/100)
- [x] Lesson 4 — Loops (85/100)
- [x] Lesson 5 — Functions (92/100)
- [x] Lesson 6 — Collections (90/100)
- [x] Lesson 7 — Modules (91/100)

---

## Completed Projects

- [x] Lesson 1 Challenge — Profile Builder CLI
- [x] Lesson 2 Challenge — Text Processor CLI (case-insensitive, full report)
- [x] Lesson 3 Challenge — Support-Ticket Router CLI (validation → match dispatch)
- [x] Lesson 4 Challenge — Gradebook Analyzer CLI (validation → accumulate → report)
- [x] Lesson 5 Challenge — Gradebook Analyzer refactored into functions (byte-identical output)
- [x] Lesson 6 Challenge — Store Inventory CLI (dict-of-info, set categories, function-decomposed)
- [x] Lesson 7 Challenge — Random Team Picker CLI (sys.argv, random.sample, seed flag, __main__ guard)

---

## Strong Topics

- Variables as names bound to objects (tag, not box)
- Core data types (`int`, `float`, `str`, `bool`, `None`) and `type()`
- f-string formatting and format specifiers
- Bool-as-int arithmetic (masking, `or`-fallback idiom)
- Operator precedence and right-associativity of `**`
- Chained comparisons, `and`/`or` operand-returning, `in` membership
- Slicing (`[start:stop:step]`, reverse, every-nth)
- String methods: strip family, split/join, replace, count, lower/upper
- `match` with tuple patterns, `|` OR-patterns, guards, and `_` wildcards
- Fail-fast guard clauses (`if not (0 <= x <= 100): continue`)
- Boundary normalization: fold `strip().lower()` once before validation
- `for` iterates items; `range(start, stop, step)` with stop excluded
- Accumulator pattern: `total = 0` BEFORE the loop, `total += n` inside
- Loop `else` as "found / not found" — no flag variable
- `enumerate` (index + value) and `zip` (parallel pairing)
- Comprehensions `[expr for x in seq if cond]` for building collections
- Fold-once again: lowercase the data once, reuse the folded copy
- Debugging in one pass: H1 — all three bugs found, fixed, and commented
- `def` + `return`: functions compute and return; caller decides to print
- `return` vs `print`: no `return` → `None` (E2 proved it in output)
- Default parameters + `None`-sentinel fix for the mutable-default trap
- Multiple returns via tuple unpacking (`return a, b` / `low, high = f()`)
- Scope: locals per-call, globals readable not assignable, return-don't-mutate
- Docstrings (all challenge functions) + first voluntary type hint
- Composition: small single-responsibility functions calling each other
- Alias vs copy: `b = a` shares one object; `b = a.copy()` separates it
- `in` semantics: dicts check KEYS; `.values()` for values; sets O(1)
- Set lifecycle: `set()` (not `{}`), `.add`, dedupe, `sorted()` for order
- `dict.get` counting and `setdefault` dict-of-lists grouping
- Set algebra: `& | - ^` with sorted output
- Nested-list columns via one list comprehension
- O(n) two-sum: single pass with a set (interview pattern)
- Empty-state guards + `none` fallbacks in report output
- Three import forms: `import X` / `from X import Y` / `import X as Z` — aliasing
  vs copying, star-import shadowing
- `__name__ == "__main__"` guard: script vs library execution path
- `random` module: seed reproducibility, choice/sample/shuffle/choices
- `sys.argv` CLI parsing: `[0]` = script name, validate before indexing, wrap
  `int()` in try/except
- `os.path` methods: join/basename/splitext/exists/getcwd
- H1 clean sweep: five module bugs (star import, shadowing, from-import name
  gap, seed-in-loop, missing guard) — all fixed in one pass

---

## Weak Topics

- Spec-literalness: improving — only 2 mild slips in L5 (M2 `exacly 2` label,
  E1 extra greetings), down from 4 in L4 and 3 in L3. Output-as-contract
  reflex is forming; the challenge was byte-identical on first submission
  except the True/False label
- Builtin shadowing: E4 used `min`/`max` as variable names, silently disabling
  the builtins in that scope (H2's `min_of`/`max_of` avoided it correctly)
- Display boundary: `is_pass` returned bool, printed as True/False instead of
  pass/fail — computation/presentation separation is the new principle
- Empty-state crashes: `report()` on empty inventory raised UnboundLocalError —
  bind state before the loop, always provide a `none` fallback
- Validate-before-evaluate: `float(price) <= 0` ran `float()` first, so a
  non-numeric price crashed main() with ValueError — check what you can, then
  wrap the risky conversion, then `continue`
- `min()` ≠ filter-then-join: `min(low_stock)` returned one name instead of the
  full low-stock list; low-stock comprehension also ran inside the loop
  (recomputed per product) instead of once after
- Label drift: `low_stock:` vs spec `low stock:` — check literals
  character-for-character
- Collection selection: choosing list/tuple/dict/set per problem from
  guarantees (order/mutability/uniqueness/lookup) instead of habit — surfaced
  in L6 reflection, improving: 8/8 in the follow-up Collection Choice drill
- Error messages: first attempt paraphrased spec error strings; the spec is a
  contract — "invalid count: N" must be copied verbatim, not reworded
- CLI validation: must try/except `int()` on user strings before comparing;
  must check argc before indexing for degenerate paths like `--seed` alone

---

## Average Review Score

90.4 (L1: 93, L2: 90, L3: 92, L4: 85, L5: 92, L6: 90, L7: 91)

---

## Mastery Level

Level 4 — Debugging/refactoring independently (H1 clean sweep in one pass,
fourth session running; challenge had full architecture correct on first
submission but error handling didn't survive edge cases — fixed all 6 issues
across two review rounds independently; conceptual questions 7/7 on modules;
spec-literalness still the last mile)

---

## Total Study Hours

~7 hours

---

## Notes

- Session 5 (2026-08-09): Lesson 5 complete (92/100) — best session yet,
  tied with L3. Functions: def/return/params/defaults/scope/docstrings/
  composition. H1 clean sweep; challenge (L4 Gradebook refactor into
  functions) byte-identical except the True/False label, fixed in one round.
  Spec-literalness improving (2 mild slips). Mastery solidly Level 4.
- Standing directives: (1) exercises must state rule, output format, and
  constraints explicitly; (2) per-lesson folder structure
  `lessons/lesson-NN-topic/` with md + ipynb + solution.py;
  (3) learner approved a Jupyter-notebook workflow for exercises;
  (4) NEVER pre-fill `solution.py` with answers — the learner writes all code,
  so key files are blank until after completion. Updated 2026-08-09: learner
  now writes solutions directly in `solution.py`; `my_solution.py` retired.
- Learner-curious about `match` beyond literals: sequence/mapping/class
  patterns deferred (JSON in Stage 2, API responses in Stage 4).
- Reflection submitted for Lesson 4: dict methods (`dict.get`) were the new
  piece; wants spaced practice on loop fundamentals before challenges; next
  focus is Lesson 5 — Functions.
- Reflection submitted for Lesson 5: next focus is Lesson 6 — Collections
  (sets are the genuinely new surface; list/dict/tuple fluency already strong).
- Session 6 (2026-08-13): Lesson 6 complete (90/100) — first "harder" lesson
  per the L5 directive. Exercises byte-identical on first submission (5E/3M/2H
  incl. O(n) two-sum and 4-bug H1 clean sweep). Challenge (Store Inventory CLI)
  spec-clean after a 3-round fix cycle: label typo, `:.2f`, space-join, then
  real bugs — empty-inventory UnboundLocalError, ValueError on non-numeric
  price, `min()` misused as filter-then-join. Learner fixed 5 of 6 remaining
  issues independently across two rounds; reviewer applied the last two
  `none`-fallback lines with learner consent.
- Session 7 (2026-08-13): Lesson 7 complete (91/100) — Modules. Exercises
  nearly perfect: only slip was M3 printing `hand1` twice instead of
  `hand1`/`hand2`. H1 clean sweep (5 module bugs: star import, shadowing,
  from-import name gap, seed-in-loop, missing guard — all fixed, all commented).
  H2 coupon collector correct on first try (set + while + seeded). Challenge
  (Random Team Picker CLI): architecture correct on first submission —
  `parse_args`, `pick`, `print_winners`, `__main__` guard, seeded example
  byte-perfect — but error handling failed 6 spec checks: parse_args ignored
  its parameter, `count` never cast to int in the no-seed path, validation
  logic inverted, `count < 1` missing, error messages were paraphrased not
  spec-literal, and `--seed` alone crashed with IndexError. Learner fixed 4
  issues independently; reviewer applied the last two (try/except, usage
  message) with consent. Conceptual questions 7/7.

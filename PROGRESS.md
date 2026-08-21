# Progress

V2 format: topics are tracked by priority tier with mastery evidence,
independence, mistakes, and hint dependency.

Completion ≠ mastery. This file tracks mastery.

---

## Current Position

```text
Stage:        Stage 2 — Python Application
Next Lesson:  Lesson 8 — Exception Handling (stage opener)
Weekly Proj.: every 3–4 lessons (next after Lesson 10/11)
Quizzes:      roughly every 3 lessons
DSA Track:    1 session/week, interleaved (see DSA_TRACK.md)
Git:          commit after every session from Stage 2 onward
```

---

## Topic Mastery Table

Legend — Mastery: 0 never seen · 1 familiar · 2 understands ·
3 independent · 4 proficient/debug+refactor · 5 can teach.
Independence: High = implements without AI-generated code.
Hint Dependency: see scale below.

Stage 1 values were migrated from V1 session evidence and are marked
**provisional** until confirmed through natural retrieval in Stage 2.

| Topic | Tier | Mastery | Independence | Common Mistakes | Hint Dep. | Project Application | Last Reviewed |
|-------|------|---------|--------------|-----------------|-----------|---------------------|---------------|
| Variables & references | CORE | 4 (prov.) | High | alias vs copy (`b = a` shares) — resolved via L6 drill | None | All challenges L1–L7 | 2026-08-13 |
| Data types & conversion | CORE | 4 (prov.) | High | builtin shadowing (`min`/`max` as names, L5); `int()`/`float()` on user input needs try/except (L7) | None | L1, L5–L7 | 2026-08-13 |
| Control flow (conditionals, match literals) | CORE | 4 (prov.) | High | validation logic inverted; `count < 1` check missing (L7 challenge) | None | L3, L7 | 2026-08-13 |
| Loops | CORE | 4 (prov.) | High | per-iteration recomputation (seed-in-loop, low-stock comprehension inside loop) | None | L4–L7 | 2026-08-13 |
| Functions | CORE | 4 (prov.) | High | mutable defaults (fixed L5); `return` vs `print` confusion (fixed L5) | None | L5–L7; all challenges function-decomposed | 2026-08-13 |
| Collections (list/tuple/dict/set) | CORE | 4 (prov.) | Med-High | choosing type by habit not guarantees (closing: 8/8 drill); `min()` misused as filter-then-join (L6) | Conceptual ×1 (two-sum O(n) approach) | L6, L7 | 2026-08-13 |
| Modules & imports | CORE | 4 (prov.) | High | star-import shadowing; missing `__main__` guard — all fixed in H1 sweep | None | L7 challenge | 2026-08-20 |
| Strings & formatting | SUPPORTING | 3→4 | High | label drift / spec-literalness (trend improving) | None | L2, L6 | 2026-08-05 |
| Operators & boolean logic | SUPPORTING | 4 (prov.) | High | none recent | None | L2, L3 | 2026-08-05 |
| Console I/O | SUPPORTING | 3 | High | degenerate argv paths (`--seed` alone → IndexError, L7) | Specific ×1 (with consent) | L3, L7 | 2026-08-13 |
| `match` beyond literal patterns | AWARENESS | 2 | — | deferred by design (JSON Stage 2, API Stage 4) | — | — | 2026-08-13 |

---

## Cross-Cutting Skills

| Skill | Status | Evidence |
|-------|--------|----------|
| Debugging (one-pass bug hunts) | STRONG | H1 clean sweeps four sessions running (L4–L7) |
| Error handling under edge cases | **WEAK — primary target** | Recurring challenge failure mode: L6 empty-inventory UnboundLocalError + ValueError on non-numeric price; L7 six spec failures (uncast `count`, inverted validation, missing `< 1`, paraphrased messages, `--seed` alone crash). Stage 2 opens with Exception Handling to attack this directly |
| Spec-literalness (output-as-contract) | IMPROVING | 2 mild slips in L5, down from earlier sessions; L7 architecture byte-perfect, error strings still paraphrased |
| Collection choice from guarantees | CLOSING | Follow-up drill 8/8 correct, guarantee-driven reasoning |
| Computation/presentation separation | FORMING | `is_pass` printed True/False instead of pass/fail (L5) |

---

## Hint Dependency Scale

Diagnostic only — never punishment.

```text
0 — No hint
1 — Conceptual hint
2 — Specific hint
3 — Pseudo-code
4 — Full solution
```

Current profile: mostly 0. One level-1 (two-sum optimal approach).
Reviewer applied final fixes with learner consent twice (L6: two
`none`-fallback lines; L7: try/except + usage message) — recorded as
assisted level-2, learner fixed 4–5 of 6–7 issues independently each time.

Repeated level-2+ dependency on a topic ⇒ that topic returns for targeted
practice before moving forward.

---

## Completed Lessons (Archive)

- [x] Lesson 1 — Variables & Data Types (93/100)
- [x] Lesson 2 — Operators & Strings (90/100)
- [x] Lesson 3 — Boolean Logic, I/O & Conditionals (92/100)
- [x] Lesson 4 — Loops (85/100)
- [x] Lesson 5 — Functions (92/100)
- [x] Lesson 6 — Collections (90/100)
- [x] Lesson 7 — Modules (91/100)

---

## Completed Projects (Archive)

- [x] Lesson 1 Challenge — Profile Builder CLI
- [x] Lesson 2 Challenge — Text Processor CLI (case-insensitive, full report)
- [x] Lesson 3 Challenge — Support-Ticket Router CLI (validation → match dispatch)
- [x] Lesson 4 Challenge — Gradebook Analyzer CLI (validation → accumulate → report)
- [x] Lesson 5 Challenge — Gradebook Analyzer refactored into functions (byte-identical output)
- [x] Lesson 6 Challenge — Store Inventory CLI (dict-of-info, set categories, function-decomposed)
- [x] Lesson 7 Challenge — Random Team Picker CLI (sys.argv, random.sample, seed flag, __main__ guard)

---

## Strong Topics (Archive)

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

## Weak Topics (Archive)

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

## Scores & Hours

Average Review Score: 90.4 (L1: 93, L2: 90, L3: 92, L4: 85, L5: 92, L6: 90, L7: 91)

Overall Mastery: Level 4 — debugging/refactoring independently

Total Study Hours: ~7 hours

---

## Weekly Project Log

| # | Lessons Covered | Project | Result | Date |
|---|-----------------|---------|--------|------|
| — | — | (starts in Stage 2) | — | — |

---

## Quiz Log

| # | Lessons Covered | Score | Weak Concepts Identified | Targeted Practice Done |
|---|-----------------|-------|--------------------------|------------------------|
| — | — | — | (starts in Stage 2) | — |

---

## DSA Log

See `DSA_TRACK.md` for the track definition.

| Week | Problems | Pattern(s) | Approach Quality | Complexity Explained? |
|------|----------|------------|------------------|----------------------|
| — | — | (starts with Stage 2) | — | — |

---

## Notes (Archive)

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
- V2 migration (2026-08-21): system upgraded to V2 — priority tiers,
  cumulative recall, weekly projects (every 3–4 lessons), operational
  quizzes (~every 3 lessons), DSA track (weekly), technical reflection,
  topic-based progress tracking. Stage 1 retro-classified as Python Core
  (complete). Next: Lesson 8 — Exception Handling.

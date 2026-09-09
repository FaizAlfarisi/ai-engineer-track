# Progress

V2 format: topics are tracked by priority tier with mastery evidence,
independence, mistakes, and hint dependency.

Completion ≠ mastery. This file tracks mastery.

---

## Current Position

```text
Stage:        Stage 2 — Python Application
Current:      Lesson 15 — OOP (SUPPORTING) COMPLETE — 92/100
Next:         DSA slot (overdue) → Lesson 16 — Dataclass (SUPPORTING; further Enum practice)
Weekly Proj.: WP1 done (85/100 second pass); WP2 window opens after L16
Quizzes:      Quiz 02 done (84.7%); next quiz window ~L17
DSA Track:    1 session/week, interleaved (see DSA_TRACK.md) — OVERDUE (next session)
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
| Packages & multi-module structure | CORE | 4 | High | Challenge `write_summary` skipped two-decimals formatting (60.0 vs 60.00) on first draft — fixed independently; solution.py monolith kept as scratchpad while real deliverables split into files | 0 | Challenge report_tool package (load/compute/write + main.py) | 2026-09-07 |
| Basic typing | CORE | 4 | High | M2 passing returned scores not names (values vs keys); H1 annotation lies survived the runtime fixes (silent by nature); minimum interface drift (`int | None = None` vs `int = 60`) reverted to spec | 0 | Challenge budget_tool package (load/compute/write → monthly.csv + categories.csv, fully annotated + `mypy main.py` clean); H2 ragged-data normalizer | 2026-09-08 |
| OOP — classes, instances, attributes, methods, composition, inheritance basics, when OOP helps and when it is unnecessary | SUPPORTING | 3→4 | High | H1 `records: list[dict[str, object]]` — vaguer than required `str | float` (drivers pass, mypy breaks; fixed at review); `__repr__`/`main()` `-> None` gaps first pass; composed-method reuse (Session.add delegation) → one external look-up; mypy only ever run on `main.py`, not the H1 entry point | 0 | Challenge class-based expense core (expense/{load,compute,write} + main.py → monthly.csv + categories.csv; E1 Transaction model reused across package; `mypy main.py` + `main_h1.py` clean) | 2026-09-09 |
| Exception handling | CORE | 4 (prov.) | High | spec-literalness relapse on challenge report line (2 rounds); spec-dict mutated into result container (M3, fixed same day); over-wide except tuple without stated justification (H1) | None | L8 challenge seeds stage project; M1 unpack-validation idiom | 2026-08-23 |
| File handling | CORE | 4 (prov.) | High | error-string returns from loaders (type mixing, theme); rushed-pass spec drift (`bananas` key, E2 unexecuted one pass); H2 `readlines()` where two-pass iteration was the constraint | Conceptual ×1 (M1 try-size) | Challenge Expense Persistence CLI (load/save/merge canonical rewrite) | 2026-08-28 |
| Pathlib | CORE | 4 | High | .iterdir() yields folders too (H1 bug 3 — resolved with is_dir guard); suffix filters are case-sensitive; .exists() ≠ “is a file” | None for exercises/challenge; H1 narrative leaked by reviewer build bug (learner flagged) | Challenge Folder Reporter (count_by_ext/largest/write_report); M3 typed loader rewired to Path | 2026-08-30 |
| JSON | CORE | 4 | High | latent summarize overwrite — passed only on unique categories, fixed to accumulate (reviewer-spotted); load_typed split("=") fragile, hardened to partition; reading a folder as a file crashes on Windows (PermissionError, not IsADirectoryError) | 0 | Challenge Expense JSON seed (load/categorize/summarize/save); M3 & Challenge use match mapping patterns | 2026-08-30 |
| CSV | SUPPORTING | 3 | High | first draft hardcoded summary count (`i==3: break`) — spec-ambiguous (reviewer provided no driver/Output block), conceded reviewer-fault; fixed to true len() + sorted + un-swallowed skipped-row warning + dropped dead `stats` return (re-review 92/100). Residual process note: exercise run mutated `students.csv` fixture (restored) | 0 | Challenge CSV Grade Book (read/parse/summarize/write/print decomposed) | 2026-09-04 |
| Strings & formatting | SUPPORTING | 3→4 | High | label drift / spec-literalness (trend improving) | None | L2, L6 | 2026-08-05 |
| Operators & boolean logic | SUPPORTING | 4 (prov.) | High | none recent | None | L2, L3 | 2026-08-05 |
| Console I/O | SUPPORTING | 3 | High | degenerate argv paths (`--seed` alone → IndexError, L7) | Specific ×1 (with consent) | L3, L7 | 2026-08-13 |
| `match` beyond literal patterns | AWARENESS | 2 | — | deferred by design (JSON Stage 2, API Stage 4) | — | — | 2026-08-13 |

---

## Cross-Cutting Skills

| Skill | Status | Evidence |
|-------|--------|----------|
| Debugging (one-pass bug hunts) | STRONG | H1 clean sweeps five sessions running (L4–L8); L10 three-bug drill resolved independently (suffix case, uppercased names, folder-as-file) — narrative write-in leaked by a reviewer build bug, flagged proactively by learner; L11 four-bug drill (suffix case, folder-read crash, wrong shape, merge) resolved independently in the notebook with a full expected/observed/root-cause write-up for all four — narrative slots this time were blank write-ins |
| Error handling under edge cases | CLOSING | L8 direct attack landed: degenerate guards everywhere (`mean([])`, empty rows, empty input), H1 debug drill swept with root causes narrated, retry-loop and boundary-validation idioms correct. Close after one unannounced retrieval survives |
| Spec-literalness (output-as-contract) | IMPROVING | L8 relapse on ONE challenge line (`rejected:` colon R1, trailing space R2) while the other 9 output blocks were byte-exact first submission — visible-part-matches, invisible-tail-missed pattern named explicitly. L9: all Output blocks matched after the revision pass; rushed first pass drifted on the easy `bananas` key and left E2 briefly unexecuted. Root cause self-identified as RUSHING, not language — habit target set (read Constraints as a checklist before coding). L10: all 10 Output blocks byte-exact, no drift; habit held. L11: all 12 Output blocks byte-exact first submission, habit held. L13: one Challenge slip — contract said totals with two decimals, first draft wrote raw floats; caught on review, fixed independently, line held at `sorted` + two-decimals formatting in `write_summary`. L14: all 11 Output blocks byte-exact after one review round (M2 `passing` output not compared, H1 annotation lies); habit target refined to a 3-second output-compare after each driver run |
| Collection choice from guarantees | CLOSING | Follow-up drill 8/8 correct, guarantee-driven reasoning |
| Computation/presentation separation | FORMING | `is_pass` printed True/False instead of pass/fail (L5) |

---

## Misconception Lifecycle

A misconception closes only after all three: explained correctly
(root cause, not symptom) + avoided independently in new code + survives
one unannounced retrieval. Status: OPEN / CLOSING (last gap observed,
one retrieval pending) / CLOSED.

| Misconception | Status | First Seen | Last Evidence |
|---------------|--------|------------|---------------|
| Spec-literalness (output-as-contract) | OPEN — watching | L3 | L9 re-baselined (self-identified RUSHING, habit: read Constraints as checklist). L11: 12/12 byte-exact, habit held; pending one unannounced retrieval |
| Error handling under edge cases | CLOSING | L7 | L8 attack landed: degenerate guards everywhere; close after one unannounced retrieval survives |
| Loader return-type mixing | CLOSED | L9 | L10: typed loader returned clean data + raised on bad values; survived unannounced retrieval |
| Latent bug — passes sample, misses requirement | OPEN | L11 | L11: `summarize` overwrite hardened to `.get(cat, 0.0)` accumulate |
| Per-iteration recomputation inside loops | OPEN | L6 | quiet since L9 |
| Builtin shadowing (`min`, `max`) | OPEN | L5 | baked into REVIEW.md Naming checklist |
| Collection choice by habit instead of guarantees | CLOSING | L6 | follow-up drill 8/8, guarantee-driven reasoning |
| Computed-but-unread / band-aid patch (returned value never used; hardcoded count + `break`) | CLOSED | L12 | L12 re-review: dead `stats` return removed, hardcoded `i==3: break` replaced with true `len()` + sorted; avoids independently and survives unannounced retrieval |

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

| Lesson | Level | Notes |
|--------|:-----:|-------|
| L6 | 1 | conceptual ×1 (two-sum optimal); assisted: reviewer applied `none`-fallback lines with consent |
| L7 | 2 | assisted: reviewer applied try/except + usage message with consent |
| L8 | 0 | strongest independence profile yet |
| L9 | 1 | conceptual ×1 (M1 try-size); fixes landed independently after reviewer notes |
| L10 | 0 | H1 narrative slots pre-filled by reviewer at build (leak); learner flagged it proactively, fixed code independently |
| L11 | 0 | H1 write-in slots BLANK — no leak recurrence; fixes independent |
| L13 | 0 | clue-free throughout; H1 three-bug drill fixed independently (chose `__init__.py` re-export over patching main only); Challenge fix round independent |

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
- [x] Lesson 8 — Exception Handling (95/100)
- [x] Lesson 9 — File Handling (90/100)
- [x] Lesson 10 — Pathlib (92/100)
- [x] Lesson 11 — JSON (93/100)
- [x] Lesson 12 — CSV (92/100)
- [x] Lesson 13 — Packages & Multi-Module Structure (92/100)
- [x] Lesson 14 — Basic Typing (92/100)
- [x] Lesson 15 — OOP (92/100)

---

## Completed Projects (Archive)

- [x] Lesson 1 Challenge — Profile Builder CLI
- [x] Lesson 2 Challenge — Text Processor CLI (case-insensitive, full report)
- [x] Lesson 3 Challenge — Support-Ticket Router CLI (validation → match dispatch)
- [x] Lesson 4 Challenge — Gradebook Analyzer CLI (validation → accumulate → report)
- [x] Lesson 5 Challenge — Gradebook Analyzer refactored into functions (byte-identical output)
- [x] Lesson 6 Challenge — Store Inventory CLI (dict-of-info, set categories, function-decomposed)
- [x] Lesson 7 Challenge — Random Team Picker CLI (sys.argv, random.sample, seed flag, __main__ guard)
- [x] Lesson 8 Challenge — Expense Entry Validator CLI (parse/format/main split, raise-at-boundary, injectable `out=print`, byte-perfect final output)
- [x] Lesson 9 Challenge — Expense Persistence CLI (parse/load/save/merge split, missing-file first run → `loaded: 0`, canonical `.2f` rewrite, `out=print`, idempotent re-runs)
- [x] Lesson 10 Challenge — Folder Reporter (count_by_ext / largest / write_report, sorted extension summary + largest file, trailing-newline report, empty-folder → `None`)
- [x] Lesson 11 Challenge — Expense JSON seed (load / categorize / summarize / save; pathlib JSON I/O, match mapping routing, no error-string returns, signed category totals)
- [x] Lesson 13 Challenge — report_tool package (load / compute / write + main.py → summary.csv; relative imports inside the package, absolute imports in main)
- [x] Lesson 14 Challenge — budget_tool package (load/compute/write + transactions.json → monthly.csv + categories.csv; signed net_by_month/net_by_category; fully annotated; `mypy main.py` clean)
- [x] Lesson 15 Challenge — class-based expense core (expense/{load,compute,write} + main.py → monthly.csv + categories.csv; E1 Transaction model reused across package; composition + delegation; prints from the CSVs it writes; `mypy main.py` + `main_h1.py` clean)

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
- try/except/else/finally semantics: else only on success, finally always runs
- Specific exception types before broad; bare except never (KeyboardInterrupt/SystemExit)
- raise at function boundary enforces the contract; caller owns the policy
- Exception message as data carrier (`ValueError(f"failed {name}")` → `str(err)`)
- Tuple-unpacking as implicit shape validation — one ValueError funnels shape
  + conversion failures (M1)
- Retry idiom: try/except inside the loop, skip-and-continue, raise after
  exhaustion (M2)
- H1 clean sweep #5 consecutive (L4–L8), root causes narrated per bug
- `with` context manager: guaranteed close = automated `finally`
- File modes: `r`/`w`/`a` semantics — `w` truncates to zero, `a` parks the cursor at the end
- Iterate-the-handle streaming (`for line in f`) vs `readlines()` hoarding the whole file
- `.strip()` at the read boundary — the trailing `\n` rides along otherwise
- Two handles in one `with`: `open(a) as x, open(b) as y:`
- Explicit `encoding="utf-8"` on every open
- Canonicalize at SAVE time (`.2f` rewrite normalizes `+2500.00` → `2500.00`); missing file = normal first run
- Two-pass tail: count lines, then collect the last n while re-iterating
- `Path` object vs string gluing: join parts with `/`, OS-safe separator (Pathlib)
- Path parts: `.name` / `.stem` / `.suffix` / `.parent` (Pathlib)
- `.exists()` guard (LBYL) before read/rename; `.is_file()` when only a file counts (Pathlib)
- `Path.iterdir()` lists children — files AND folders; guard with `.is_dir()` (Pathlib)
- `read_text`/`write_text` whole-file; `write_text` rewrites like `"w"`, no mode arg (Pathlib)
- `Path.open()` gives the same L9 handle for line-by-line / big-file work (Pathlib retrieval)
- Suffix filters are case-sensitive — compare `.suffix == ".py"` exactly (Pathlib)
- Folder Reporter: build report string, write with Path.write_text, close with trailing `\n` (Pathlib)
- JSON dumps/loads round trip; `json.dumps` value→string, `json.loads` string→value (JSON)
- JSON type mapping: `true`→`True`, `false`→`False`, `null`→`None`; numbers→int/float (JSON)
- dumps options: `indent=2` (readable, multi-line) vs `separators=(",", ":")` (compact, no spaces) (JSON)
- `json.JSONDecodeError` is a `ValueError` subclass — EAFP catch for broken files in safe loaders (JSON)
- `raise ... from None`: clean single-message re-raise, no chained traceback wall — Quiz 01 D2, now used correctly in M3 (JSON)
- `str.partition` parses `key=value` without crashing on a missing delimiter (D2 retrieval, hardened in load_typed) (JSON)
- `match` mapping patterns route records by shape: `{"kind":"income",...}` vs `{"kind":"expense",...}` (JSON)
- `dict.get(category, 0.0) + categorize(spend)`: the proper accumulate-for-signed-totals summarize pattern (JSON)
- pathlib JSON I/O: `read_text`/`write_text` with `encoding="utf-8"`, never raw `open` — L9/L10 rule retrieved (JSON)

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
- L8 spec-literalness relapse: challenge report line fixed across two rounds
  (colon spacing, then trailing space) — visible part matched, invisible tail
  missed; the other nine output blocks were byte-exact first submission
- M3 blueprint/output conflation: spec dict mutated into the result container;
  rebuilt with a fresh result dict — keep blueprints read-only
- Over-wide except without justification: `(ValueError, TypeError)` accepted
  for `None` sensor dropouts, but widening must be stated, not defaulted
- Error-string returns from loaders (L9): loaders returned `f"file {path} not found"`
  strings instead of clean data or a raise — mixes the type contract; mostly cleaned
  by revision, one instance left in E1 `load_text` (drivers only exercise success paths)
- Rushed-pass spec drift (L9): `banana` vs `bananas` key mismatch on an easy E5;
  E2 cell briefly left unexecuted — root cause self-identified as rushing, not language
- H2 constraint miss (L9): used `readlines()` (whole file) where the two-pass streaming
  iteration was the explicit constraint — output correct, constraint missed
- Latent summarize non-accumulation (L11): `result[cat] = categorize(spend)` overwrote
  instead of adding; passed only because the test categories were unique. Lesson: a
  function that passes the sample but doesn't implement the stated requirement
  ("signed total", "start each at 0.0") is a latent bug. Hardened to
  `.get(cat, 0.0) + categorize(spend)`.
- load_typed `split("=")` fragility (L11): crashed on empty or no-`=` lines
  ("not enough values to unpack"); switched to `partition` + blank-line skip +
  strip — same D2 edge as Quiz 01, now hard-won.

---

## Scores & Hours

Average Review Score: 90.9 (L1: 93, L2: 90, L3: 92, L4: 85, L5: 92, L6: 90, L7: 91, L8: 95, L9: 90, L10: 92, L11: 93, WP1: 85, L12: 92, L13: 92)

Overall Mastery: Level 4 — debugging/refactoring independently

Total Study Hours: ~17.5 hours

---

## Weekly Project Log

| # | Lessons Covered | Project | Result | Date |
|---|-----------------|---------|--------|------|
| 1 | L8–L11 | Library Manager CLI (multi-module) | 85/100 | 2026-09-02 |

---

## Quiz Log

| # | Lessons Covered | Score | Weak Concepts Identified | Targeted Practice Done |
|---|-----------------|-------|--------------------------|------------------------|
| 1 | L8–L10 | 96.4% | exception detail: chained traceback / `raise ... from None` intent, `str.partition` no-delimiter edge (D2) | weave one small exception-detail retrieval into L11 (JSON), then re-assess |
| 2 | L8–L12 | 84.7% | loader default must stay data-shaped (`{}`/`[]` still crash `main`); `partition` no-`=` lines DO surface (not silent); byte-parity slips on case + output strings | 30-second retrieval pair at L14 opening (loader default + partition edge) — both CLOSED (2026-09-08) |

---

## DSA Log

See `DSA_TRACK.md` for the track definition.

| Week | Problems | Pattern(s) | Approach Quality | Complexity Explained? |
|------|----------|------------|------------------|----------------------|
| 1 | most-total spending category (payments log of (category, total) pairs) | hash map — single-pass accumulate + argmax | correct 2-phase plan (group in dict → `max(items(), key=...)`); first attempt compared single payments only — counterexample (8×15 food beats 100 salary) exposed "largest single amount ≠ highest total"; edge cases: empty→`None` contract (no error-string returns), single entry, first-seen ties; single-pass running-max optimization noted (strict `>` keeps first-seen) | yes — O(n) build + O(k) scan ≈ O(n); O(k) space; argued O(n) is a lower bound (must read every payment) at senior review |

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
- Session 8 (2026-08-21 → 23): Lesson 8 complete (95/100) — Stage 2 opener,
  Exception Handling, spread over 3 sittings (~2h). Exercises exact on first
  submission incl. M1 unpack-as-validation and H2 strict CSV parser; H1
  sweep #5 consecutive. Challenge (Expense Entry Validator CLI):
  architecture + `out=print` stretch goal unprompted; spec-literalness
  relapsed on one report line, fixed in 2 rounds. M3 spec-mutation smell
  fixed same day. Hint dependency level 0 throughout — strongest
  independence profile yet. Edge-case error handling moved CLOSING.
  Clarification notes (try-block scope, EAFP vs LBYL) added to
  `notes/PYTHONIC.md`. Next: Lesson 9 — File Handling; quiz window opens
  around L9/L10.
- Session 9 (2026-08-28): Lesson 9 complete (90/100) — File Handling, Stage 2
  second topic. Busy week: multiple short sittings (~2h total), rushed first
  pass. All Output blocks matched after the revision round; Challenge (Expense
  Persistence CLI) canonical `.2f` rewrite + `total: 2494.95` fixed
  independently; missing-file first run and idempotent re-runs held. H1 debug
  drill (five bugs) was the hardest mentally; learner self-diagnosed the early
  spec-drift as RUSHING, not language, and set a habit: read Constraints as a
  checklist before coding. Spec-literalness re-baselined to IMPROVING.
  `notes/PYTHONIC.md` gained a File Handling subsection; `.opencode/TEACHING.md`
  gained a permanent Spec Language rule (plain English, same difficulty) for
  L10+ specs. Next: Lesson 10 — Pathlib; quiz window open.
- Session 11 (2026-08-30): Lesson 10 complete (92/100) — Pathlib, Stage 2 third
  topic, first written in the plain-English spec style. Strong recall (6/6,
  with two edge-case refinements: iterdir yields folders, exists≠is_file). All
  exercises + Challenge byte-exact; M3 loader rewired to Path retrieved the L9
  clean-loaders rule. H1 three-bug drill resolved independently in the notebook
  (suffix case, uppercased names, missing is_dir guard) with inline comments.
  Process note: the solution.py H1 bug-report write-in was mistakenly pre-filled
  by the reviewer at build time — learner flagged it (good metacognition), fixed
  the bug code independently anyway;   narrative leak recorded, no penalty. Next:
  Lesson 11 — JSON (CORE); weekly-project window now open.
- Quiz 01 (2026-08-30): first Stage 2 quiz over L8–L10 — 96.4% (pass, bar 80%).
  All concepts closed except one exception-detail point (D2): the intent of
  `raise ... from None` (clean single-message traceback) and the
  `partition` no-delimiter edge were only half-grasped. Targeted practice:
  one small retrieval woven into L11, then re-assess. Quiz 01 file:
  `quizzes/quiz-01-l08-l10.md`.
- Session 12 (2026-08-30): Lesson 11 complete (93/100) — JSON, Stage 2 fourth topic,
  plain-English spec style. Learner built the full Expense JSON seed
  (load/categorize/summarize/save). The Quiz 01 D2 weak point (`raise ... from None`
  + `partition`) was woven into M3 and the Challenge specs; the learner used
  `from None` correctly and, when the latent `split("=")` fragility surfaced, hardened
  to `partition` — D2 appears retrieved/closed (final confirm at Quiz 02). All 12
  Output blocks byte-exact first submission; H1 four-bug drill resolved independently
  in the notebook with a full expected/observed/root-cause write-up for all four
  (including the Windows `PermissionError` when reading a folder as a file). Reviewer
  flagged two latent-robustness gaps (summarize overwrite on duplicate categories;
  `split("=")` crash on no-`=` lines) — learner hardened both. Process revert honored:
  the H1 solution.py slots were BLANK write-ins this time — no recurrence of the L10
  leak. E1/E3/E4/E5 rebuilt mid-lesson to function-form so their drivers no longer
  hand over answers (learner flagged the earlier inline cheat); M2 Output widened to
  show the full pretty-printed file. Next: Lesson 12 — CSV (CORE); weekly-project
   window open (weekly project due soon).
- Weekly Project 1 (2026-09-02): Library Manager CLI — 85/100 (second pass).
  Multi-module architecture (solution + 4 service modules + helper +
  custom_error), 7 clean commits, decision log with reasoning. Core
  functionality (add/remove/search/list/genres) implemented end-to-end
  with JSON persistence via pathlib. All 9 first-pass issues fixed
  independently: search wired to search_index with `in`, list output
  matches spec block (genres is separate command), is_file() parens,
  case-consistent duplicate check, circular import broken, IndexError
  caught, no-results prints directly, explicit return removed. Key
  learning: same class of bug repeats across files (is_file parens, case
  sensitivity). Self-review pass before shipping is the new habit.
  Spec-literalness held at exercise level but slipped at project level;
  the fix was a new command, not mutated output. DSA track still due.
  Next: Lesson 12 — CSV (CORE).
- Lesson 12 (2026-09-04): CSV (SUPPORTING) — 92/100 (re-reviewed), Level 3
  reached. Loader contract transferred cleanly into a new format; Challenge
  decomposed into single-responsibility functions. First draft had a
  hardcoded summary count (`i==3: break`) that missed the true 5 students
  on the provided data — this was spec-ambiguous and CONCEDED reviewer-fault
  (no Driver + Output: block in the original spec). Learner re-fixed and
  re-submitted: true `len()` count, sorted by name, un-swallowed skipped-row
  warning, dead `stats` return removed. Re-review ran the provided data:
  `Summary (5 students)` all correct. PROCESS FAILURE (reviewer): L12
  exercise specs broke the established L11 format — no Driver + Output:
  block per cell. Logged as a hard correction for Lesson 13: every exercise
  gets a pinned driver + exact Output block. Also: an exercise run mutated
  the `students.csv` fixture; reviewer restored it. Fix for future: build
  notebook fixtures inline (L11 style) so exercise code cannot corrupt
  shared data files. Next: Lesson 13 — Packages & Multi-Module Structure
  (CORE). Quiz 02 window + DSA slot both overdue.
- Lesson 13 (2026-09-07): Packages & Multi-Module Structure (CORE) — 92/100,
  Level 4. Learner did all six exercises (E1/E2/E3/M1/H1/Challenge) with
  clue-free independence (hint dependency 0 — per learner directive, specs
  now lean: Task/File tree/Interface contract/Constraints/Output, clues only
  as bridges). E1–E3 and M1 byte-exact first pass. H1 three-bug drill
  (import-time side effect, relative import in a root script, module-vs-
  function) traced end-to-end; learner chose the cleaner `__init__.py`
  re-export fix (`from .greet import greet` + `from greeter import greet`)
  over patching main only, and renamed the root script to `main_greet.py` to
  dodge a `main.py` collision with the Challenge — good design judgment on a
  reviewer spec collision (noted, spec patched to match). Challenge:
  first draft of `write_summary` wrote raw floats (60.0 not 60.00) — spec-
  literalness slip, fixed independently in one round; `sorted` + two-decimals
  formatting moved
  into `write.py` so it owns ordering and formatting regardless of caller;
  `main` trimmed to load → summarize → write → print. All six drivers
  byte-exact verified in a temp copy. Next: Quiz 02 (L08–L12),
  then the DSA slot (still overdue).
- Quiz 02 (2026-09-07): L08–L12 — 84.7% (15.25/18), pass (bar 80%).
  Strong: JSON compact separators + type mapping, accumulate-vs-overwrite
  (B3 + E both correct — latent-bug misconception CLOSED), `from None`
  intent (A3 + D1 — Quiz 01 D2 hold item CLOSED), CSV newline + writer
  idiom, match routing with missing-key fallback. Weak: loader default
  must stay data-shaped (C1 fix `return`/`[]` still crashed `main`),
  `partition` no-`=` lines actually surface (D1 half-traced), byte-parity
  slips (`alice` vs `Alice`; `skiped:` typo — spec-literalness still OPEN,
  IMPROVING). Targeted practice: 30-second retrieval pair at L14 opening
  (loader default + partition edge), then re-assess. Next: Lesson 14 —
  Basic Typing (CORE).
- Quiz 02 retrieval re-assessment (2026-09-08, L14 opening): loader
  default stays data-shaped — learner: "return dict type, guarantee
  empty dict discovery" — CLOSED. `partition` no-`=` edge — called it as
  `int("")` raising cleanly (not silently skipped, not unpack crash) —
  CLOSED. Both Quiz 02 holds re-verified at the L14 opening targeted
  pair; spec-literalness (byte-parity) remains the one OPEN thread.
- Lesson 14 (2026-09-08): Basic Typing (CORE) — 92/100, Level 4, hint
  dependency 0. Pack expanded to the CORE shape 5E/3M/2H + Challenge
  (learner directive). All 11 drivers byte-exact in a temp copy; Challenge
  `mypy main.py` clean (first pip install). H2 rugged normalizer and the
  Challenge budget_tool package passed first try. Review misses, both fixed
  by learner: M2 `passing` returned scores instead of names; H1 two planted
  annotation lies survived the runtime fixes. Left intentionally out of
  scope: 7 full-tree mypy nits (annotation-honesty of locals/Nones).
  Next: Lesson 15 — OOP (CORE; enum folds in). DSA slot still overdue.
- Lesson 15 (2026-09-09): OOP (SUPPORTING) — 92/100, Level 3→4, hint
  dependency 0. Pack personalized to a single session: 4E/2M/1H +
  Challenge, Expense/Transaction theme (seeds WP2), Enum folded in as
  AWARENESS. All 8 drivers byte-exact in a temp copy; Challenge
  `mypy main.py` clean; `mypy main_h1.py` clean after the H1 annotation
  fix. Opening holds: Path-is-a-class CLOSED; signature-read-both-sides
  re-surfaced (H1 used `list[dict[str, object]]` instead of the exact
  `str | float` — passes drivers, breaks mypy; fixed at review).
  Composition + delegation landed (get_date named sort key, main prints
  the CSVs it wrote — senior choices). Review fixes: `__repr__ -> str`,
  `main() -> None`, H1 `str | float` + `totals` annotation. One external
  look-up on composed-method reuse (noted for watch). DSA slot still
  overdue. Next: DSA slot → Lesson 16 — Dataclass (SUPPORTING; further
  Enum practice).

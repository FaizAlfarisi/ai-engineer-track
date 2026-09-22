# Weekly Project 2 — Expense / Transaction Manager CLI — Review

**Reviewer:** AI Mentor
**Date:** 2026-09-16 (acceptance round)
**Project:** `projects/weekly-project-02-expense-manager/`
**Verified against:** brief.md test matrix (reconciled) + every command run
in a temp copy, stdout/stderr/exit code captured byte-for-byte
**Draft score (acceptance round):** 73/100 — locks after the review-fix
round (WP1 pattern: 70 → 85)
**Hint Dependency:** Level 0 (no code hints; review-fix round expected)

---

## Strengths

**1. Genuine layered architecture, with reasoning.** The split
`configurations / models / repositories / services / utils / scripts`
is not decoration — `config.py` owns paths, `transaction_repo.py` owns
every data-source touch, `transaction_formatter.py` owns presentation,
services compose them. The decision log has a Why and an Alternative
for almost every split. That is engineering thinking, not toy code.

**2. The frozen model + enum carried end-to-end.** `Kind` identity via
`is`, `signed_amount()` as the single sign rule, `asdict` + enum-aware
encoder at the write boundary, `object_hook` decoding back into
`Transaction` at the read boundary. The L16 lesson ("the annotated
fields ARE the spec") shows up as actual production structure.

**3. Reports print from the file they just wrote.** `write_csv` then
`load_csv` then format-from-rows — one source of truth, bit-for-bit
what a spreadsheets user will open. Senior habit, unprompted.

**4. Custom exception families, actually used.** `ErrorBadRequest` vs
`ErrorCorruptData` are genuinely different failure modes, and `main.py`
catches by family — exactly the L9/L11 loader contract at project scale.

**5. Empirical debugging win.** The learner discovered the shell strips
`""` from `sys.argv` (PowerShell/cmd), confirmed with `" "`, and
corrected the test — the brief's T10 was wrong, not the code. That is
real platform knowledge earned by testing.

**6. Validation order in `add`** — length → category → date → kind →
amount → positivity: each layer fails with a specific message before
any I/O happens. Clean guard-then-build.

---

## Issues (most → least serious, with evidence)

### Issue 1 — `Added:` line is not byte-exact (C1)

**Observed:**
```
$ python main.py add 2026-09-12 lunch expense 25000
Added: 2026-09-12 lunch expense 25000.0
```
**Expected (brief):** `Added: 2026-09-12 lunch expense 25000.00`
**Root cause:** `transaction_service.py:50` formats `{amount}` (raw
float repr) instead of `{amount:.2f}`. Every CSV is 2-decimal; the
success line should match the house style.
**Fix:** `return f"Added: {date} {category} {kind.value} {amount:.2f}"`

### Issue 2 — the load path trusts data it cannot see (C4)

**Observed (hand-edited but *valid* JSON):**
```
$ python main.py list          # data: {"amount": "abc"}
format error: Unknown format code 'f' for object of type 'str'
Transactions (1):
```
```
$ python main.py report summary
unexpected error:
unsupported operand type(s) for +=: 'float' and 'str'
```
**Expected:** any invalid record → `corrupt data:` on *load*, never an
`unexpected error:` mid-operation. `object_hook` in
`transaction_repo.py:9-18` checks only that the 4 keys exist — it does
not check `amount` is a number or `kind` is a valid `Kind`. Because the
hook may return a plain `dict`, the function also lies about its type:
declared `-> list[Transaction]`, can actually contain `dict`s.
**Fix:** validate at load (amount numeric, `kind in Kind`, date
parseable in the canonical form) and raise `ErrorCorruptData` on
violation; then the type is really `list[Transaction]` and formatters
can safely assume clean data. Remove the `try/except print` in
`list_formatter` — a formatter must never catch and swallow mid-stream;
validation upstream is what guarantees it.

### Issue 3 — `strptime` is lenient, so the stored date can break sorting (C3)

**Observed:** `add 2026-9-1 food expense 100` → accepted, stored raw
`"2026-9-1"`, success line `Added: 2026-9-1 food expense 100.0`.
**Why this is dangerous:** Python's `strptime` accepts non-zero-padded
dates. Stored raw, `"2026-9-1"` sorts *after* `"2026-09-02"` as a
string, and `report_monthly` groups by `txn.date[:7]` → `"2026-9-"`.
One eyebrow-raised input silently corrupts ordering and grouping.
`report_weekly` goes through the datetime helper; `report_monthly`
slices the string — **two philosophies in one file**, and only one of
them is safe.
**Fix:** store the *canonical* form: `date_obj.strftime("%Y-%m-%d")`
(the datetime returned by `validate_date`), and group the month from
that same datetime. New brief T14 enforces it.

### Issue 4 — error contract drifts from what the brief froze (C2)

**Observed:** every error now prints as two lines
(`bad request:\nError: ...`) and exits **0**:
```
$ python main.py bananas     (exit=0)
bad request:
unknown command 'bananas'
```
Meanwhile `report bananas` prints `bad request:\nError: unknown type
of report` — the embedded `Error:` token appears in some messages and
not others. Inconsistent on two axes: prefix everywhere, embedded token
somewhere.
**Decision (yours, accepted):** keep the scoped-prefix design. The
brief's Test Matrix is now **reconciled** to it (T6–T17 rewritten),
with the contract formalized: two-line scoped message on **stderr**,
exit code **1**, detail line with no embedded severity token. This makes
the error channel machine-parseable — the correct CLI design.
**Fixes implied:** (a) write errors to `stderr` (`sys.stderr.write`)
not `print`; (b) `sys.exit(1)` after printing an error in `main`.
(c) drop the embedded `Error:` from the exception messages so detail
lines are uniform; (d) unify "empty type of report" / "unknown type of
report" / "unknown command ..." under the same style.

### Issue 5 — `--seed` is a stub and prints literal `None` (M1)

**Observed:**
```
$ python main.py --seed        (exit=0)
seed
None
```
`seeder()` returns `None`; `main.py` does `print(router(...))`.
**Fix choices:** implement SG2 (deterministic 40-record generator —
loops over categories × dates, no `random`, exactly reproducible, one
`Seeded: 40 transactions` line to stdout) **or** delete the route. And
either way: every route must return a `str`; never `print(None)`.

### Issue 6 — ISO week is not zero-padded (M2)

`extract_year_week` emits `2026-W6` for January weeks. The brief's
`YYYY-Www` and *string-sorted* order both assume two digits:
`"2026-W6" > "2026-W11"` lexically. In your seed data (weeks 35–37)
it never bites; it bites every January.
**Fix:** `f"{iso.year}-W{iso.week:02d}"`.

### Issue 7 — CLI etiquette: errors go to stdout, exit stays 0 (M3)

Real CLIs write diagnostics to **stderr** and exit **nonzero** on
failure — so a caller can check `$LASTEXITCODE` / `$?` and separate
"output" from "error". Today `python main.py bad && doSomething()` runs
`doSomething` happily. (See Issue 4 fixes.)

### Issue 8 — annotation gaps keep mypy quiet by absence (M5)

`report_summary()` and `seeder()` have no return annotation; mypy's
default mode skips unannotated defs, so "Success" today is weaker than
it looks. Brief requires every function annotated.
**Fix:** `-> str` on both.

### Issue 9 — `requirements.txt` is UTF-16 (M6)

Verified: the file starts with byte `FF FE` (UTF-16 BOM) — PowerShell
redirection (`pip freeze > requirements.txt`) wrote it. `pip install -r`
fails on it and diff tools garble it. Real gotcha with an easy fix:
regenerate with `python -m pip freeze | Out-File -Encoding utf8
requirements.txt`.

### Issue 10 — generated CSVs are committed (M7)

`data/categories.csv`, `data/monthly.csv`, `data/weekly.csv` are in the
index. They're *generated* — every run recreates them, so they diff
forever. The `transactions.json` fixture (rightly) stays. Root
`.gitignore` already covers `__pycache__`/`.mypy_cache`; add
`data/*.csv` to this project's `.gitignore` and `git rm --cached`
the three files.

### Issue 11 — missing deliverables

Brief asks for a short README (how to run, what the reports mean) and a
technical reflection. Neither exists yet. The decision log is
excellent; the README + reflection close the deliverables.

### Minor polish (P)

- `validate_date` returns `(bool, datetime | None)` — the bool is
  redundant with the `None`; returning `datetime | None` is simpler.
- `data/__init__.py` is unnecessary — `data` is never imported as a
  package.
- `f"Error: category cannot be empty"` — f-prefix on a literal with no
  placeholder (lint noise).
- `router_report`/`router` are rightly in the interface layer (see
  below); at >20 commands a dispatch table beats `match`, today `match`
  is the right call.

---

## Decision-by-decision: best practice + real-vs-concept

| Your decision | Best-practice verdict | Real project? |
|---------------|----------------------|---------------|
| Layered folders (config/repo/service/formatter/utils) | Correct instinct; right-sized for this project. Pull in `utils/` only what two+ modules share (validators → one datetime helper: good call) | **Real.** This is the standard shape of framework-free service layers; frameworks (FastAPI/Django) bring their own variants of the same layering. Watch overengineering — you already called it. |
| `match` router + `router_report` helper in `main.py` | Correct. Routing is an *interface-layer* concern; `router_report` decomposes the nested case so main stays flat — the exact alternative you rejected (nested `match`) is the worse option | **Concept→frameworks own it.** Argparse/Click/Typer route declaratively via decorators/command registries. You're learning what they abstract. A dict dispatch-table is also production-legit (registry pattern) and wins past ~20 commands. |
| `object_hook` → `Transaction` at the read boundary | Good shape (objects at the boundary); must be *validating* (Issue 2) | **Real-ish.** Used in real stdlib tools; heavier codebases use ORMs/dataclass casting. Concept: "the boundary converts, then validates." |
| Custom exception families (`ErrorBadRequest`/`ErrorCorruptData`) | Exactly right — different failure modes, catch by family | **Real.** Production practice; many codebases define exactly this pair plus a base `AppError`. |
| Error prefix scheme + string-listener errors | The *two-line scoped* scheme is a defensible improvement; stderr + exit 1 are mandatory once you claim "CLI" | **Real.** Log/parse both streams; machine callers need stable markers and exit codes. |
| String-sort dates, "format the date column by value" | Valid **only if** dates are canonical `YYYY-MM-DD` (all padded). The moment lenient parsing sneaks in, string sorting lies (Issue 3) | **Real with a caveat:** text dates are fine in canonical form; real systems usually store ISO-8601 or epoch time for exactly this reason. |
| `write_csv` sorts keys internally | Clean — the CSV is deterministic regardless of insertion order | **Real.** Deterministic output files are a feature. |
| README + reflection | Missing | — |
| `--seed` skipped / stub | Skipping an optional stretch is legitimate scope control; a *route* that prints "None" is not | — |

---

## Review-fix round (apply, then we re-verify and lock the score)

1. `Added:` → `{amount:.2f}` (Issue 1)
2. Load-time validation → `corrupt data:` instead of `unexpected error:`; remove `list_formatter`'s `try/except print` (Issue 2)
3. Store canonical dates (`strftime`), month from datetime (Issue 3)
4. Errors → stderr + `sys.exit(1)`; drop embedded `Error:`; unify report-type messages (Issue 4)
5. `--seed`: real deterministic generator returning a str, or remove the route; never print `None` (Issue 5)
6. `W{iso_week:02d}` (Issue 6)
7. `-> str` on `report_summary`/`seeder` (Issue 8)
8. `requirements.txt` as UTF-8 (Issue 9)
9. Gitignore `data/*.csv` + `git rm --cached` the three (Issue 10)
10. README + technical reflection (Issue 11)
11. Pick which minor polish (P) you apply; log the choice

## Score (draft — acceptance round)

| Bucket | / | Score | One-line why |
|--------|---|-------|--------------|
| Correctness | 25 | 18 | happy-path blocks byte-exact, but `Added:` and every error path deviate; no load validation |
| Logic | 20 | 15 | layering + grouping correct; date normalization hole, unpadded weeks, seed stub |
| Format | 15 | 11 | typed end-to-end; `-> str` gaps, duplicated `Error:` token, UTF-16 requirements |
| Engineering | 20 | 14 | repo/service/config real structure; stderr/exit etiquette, swallowed formatter errors, committed CSVs |
| Commentary | 20 | 15 | decision log genuinely good; README + reflection missing (review asked for instead) |
| **Total** | **100** | **73** | **locks after review-fix round + re-verification** |

## Learning Note

Two lessons deserve naming. First, *the boundary is where validation
lives*: your `object_hook` converts but doesn't vet, and every silent
failure traced back to that one trusting line — one asserts, the
whole report chain stays honest. Second, a *spec deviation you own is
an upgrade, a silent one is a bug*: the scoped-prefix error design is
defensible, but it was discovered in a review, not a decision log. The
strongest artifact remains the decision log itself — it reads like a
senior engineer's diary, and the review-fix round is exactly the
second-pass discipline WP1 taught.
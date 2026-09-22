# Weekly Project 2 — Review Round 2

**Score: 88/100 — LOCKED** (round 1 draft 73/100; see `review.md`, kept as-is)

**Date:** 2026-09-16 · **Stage 2: COMPLETE** (WP2 is the mandatory Stage 2 evidence)

## What was verified and how

Full matrix re-run in a fresh temp copy (`wp2v2`) so the repo was never
mutated. Every command executed against the seed fixture with the
project's own venv Python; stdout / stderr / exit code captured and
compared byte-exact. **25/25 checks passed**:

- **T1–T15** official matrix — all green.
- **T16** `mypy main.py` → `Success: no issues found in 1 source file`.
- **T17** git state — `.venv` and `data/*.csv` untracked;
  `requirements.txt` + `data/transactions.json` tracked (via `git ls-files`).
- **SG1** `report summary` and **SG3** `report weekly` — both byte-exact
  to the stretch blocks (kept as evidence; both optional).

## Round-1 issues → round-2 verdict

| # | Issue | Verdict | Evidence |
|---|-------|---------|----------|
| 1 | `Added: …25000.0` (missing `.2f`) | ✅ PASS | T2a |
| 2 | Load path trusts bad JSON / poor shapes | ✅ PASS | T13: `corrupt data:\nfailed to load existing data \| Expecting property name…`, exit 1, no traceback. Decoder now validates date/category/kind/amount and raises `ErrorCorruptData` |
| 3 | Lenient `strptime` (`2026-9-1` stored raw) | ✅ PASS, stricter than asked | T14 rejects `2026-9-1` outright (\`parse_date\` requires canonical round-trip); T14b confirms the data file is untouched |
| 4 | Error output drift + exit 0 | ✅ PASS | T6–T12 each assert exact stderr wording + exit 1; no embedded `Error:` token; consistent scoped two-line style |
| 5 | `--seed` stub printing `seed\nNone` | ✅ PASS (removed) | no `--seed` route, no seed file, commits "final project: without seed" |
| 6 | Unpadded ISO week (`W6` vs `W06`) | ✅ PASS | `extract_year_week` uses `{week:02d}`; SG3 byte-exact |
| 7 | `report_summary()` missing `-> str` | ✅ PASS | annotation present; SG1 + mypy green |
| 8 | `requirements.txt` UTF-16 `FF FE` | ⚠️ DEFERRED | now UTF-8 **but still a BOM (`EF BB BF`) on line 1** and it is the **global** env freeze (278 packages: tensorflow, torch, langchain…) — see residual below |
| 9 | `data/*.csv` committed | ✅ PASS | `.gitignore` now has `data/*.csv`; only `transactions.json` tracked |
| 10 | Missing README / reflection | ✅ PASS | `readme.md` exists; technical reflection appended to `decision_log.md` (Struggle/Solving) |
| 11 | `list_formatter` try/except swallowing stream errors | ✅ PASS | formatter is pure now (no try/except) |
| — | **New regression found in round 2 read**: decoder guard `if not isinstance(cat, str) and not cat:` (would let `""` and non-str values through) | ✅ FIXED by learner | decoder line now `… or not category_val.strip()`; categories also stripped on decode |

## Deferred debt (documented, no penalty beyond the locked score)

- **`requirements.txt` purity:** the file is a reproducible-on-this-box
  record but not a clean venv freeze. `absl-py`, `tensorflow`, `torch`,
  `langchain`… are global-env transitive noise, and pip will choke on the
  `\ufeffabsl-py` BOM token. Recommend re-baking in a clean `.venv`
  (mypy alone) when you next touch the project — 5 minutes, no score
  change once locked.
- **CLI trailing newline:** `sys.stderr.write`/`print` output ends without
  `\n`, so a shell prompt glues to the last line. Cosmetic; the brief print
  blocks stay byte-exact because the comparison strips trailing `\n`.

## Decisions worth keeping (real project vs concept map)

- **Rejects, don't normalize:** `parse_date` refusing `2026-9-1` is
  stronger than my "normalize" suggestion — it guarantees every stored
  date is canonical, which makes the `date[:7]` month slicing safe by
  construction. Right call.
- **Spec contract via the matrix:** the review round wrote the build's
  *chosen* message wording into `brief.md` (T6 now the two-line form,
  matching your scoped-prefix design). A spec you own beats a spec you
  silently drift from — exactly the plan.
- **Layers matched the brief's spirit:** `configurations/ models/
  repositories/ services/ utils/` with a `router` in `main.py` is the
  same "input → route → services → repo" shape professionals use, at a
  scale that stays readable.
- **Readback-from-file prints** (reports re-read the CSV they wrote):
  one source of truth, printed values can't disagree with the file.
- **Load-time validation with `object_hook`:** a genuinely senior pattern
  — validation lives where the data enters, not sprinkled in callers.
  (The `and`→`or` slip shows it's also where a tested guard matters
  most.)

## How the round closed

1. Round-1 review (`review.md`, 73/100 draft) → 11 issues handed to you.
2. You fixed them independently (commits `54ba60e`, `98c6ef6`), wrote the
   README, appended the reflection, and removed the seed entirely.
3. Round-2 re-verification in `wp2v2`: **25/25 green** in one run.
4. One brief-matrix row corrected to match your design (T6).
5. Score locked: **88/100**.

Stage 2 is complete. Remaining before Stage 3 opens fully: L13
reflection still owed, DSA Week-2 session due; next lesson window is
Lesson 17 — Testing (pytest).
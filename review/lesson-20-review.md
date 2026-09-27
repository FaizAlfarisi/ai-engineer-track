# Lesson 20 Review — Project Structure

**Date:** 2026-09-24
**Score:** 94/100 (bucket-derived; 95+ bar judged below)
**Topics:** launch contexts (`sys.path[0]`), absolute-vs-relative imports,
`-m` entries, silent `__init__`, `__file__`-anchored data, minimal
requirements, honest `.gitignore`, README run-commands, `tests/` +
`conftest`, positional argv + stderr usage. Tier: CORE (Stage 3).

---

## Strengths

- **Everything green, twice over.** 9/9 drivers byte-exact, 14/14 pytest
  green (4 messy + 4 restructure + 3 shop + 3 ledger) — verified
  post-fix with caches off. Quick Recall 6/6 before coding.
- **H1 clean sweep, textbook resolutions.** Hack deleted (not moved),
  init emptied, absolute + guard, `__file__`-anchored data — plus a
  4-row bug report in the learner's own words.
- **The guard-`or` applied cold.** `load_basket`'s
  `not isinstance(path, str) or not path` is the Q6 shape written into
  fresh code unprompted — the thread moves to CLOSING.
- **Fix loop was honest.** All 6 findings explained correctly first
  (including the own-words admission that Issue 1's reasoning was
  GenAI-sourced and not yet understood), then implemented. The
  `test_csv_roundtrip` rewrite now exercises `write_csv` — the test
  proves its own code.
- **Learner-driven difficulty calibration.** Standing request recorded:
  harder H-drills, fewer hints from L21 onward.

## Bucket Score

Total = 94/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 24 | All blocks byte-exact, all suites green, contracts honored. −1: one `.gitignore` line (`.pytest_cache/`) applied by reviewer with consent; `summary.csv` stray removed in review. |
| Logic (20) | 20 | Merge/override, guards, handler shapes, launch reasoning — correct. |
| Readability (15) | 14 | Small single-purpose functions, consistent layout. −1: no docstrings anywhere (fourth lesson running). |
| Naming (10) | 10 | `fresh`/`kept`, `load_basket`, `morning_basket`, `kept`-derivation — clear. |
| Maintainability (10) | 9 | `ledger.main(argv)` takes argv (right); `report_tool.main()` reads the `sys.argv` global (L7 testability, retained without reason). −1. |
| Pythonic style (10) | 10 | `__file__` anchoring, `extrasaction="ignore"`, writerows, `match`-era habits intact. `1/0` table values noted, bool-equal, no deduction. |
| Testing (5) | 4 | Suites green, learner tests pin own code post-fix. −1: first-draft `test_csv_roundtrip` was vacuous (could not fail); fixed version honest. |
| Performance (5) | 5 | No premature optimization; `-m` reuse is the right efficiency. |

- **Hint dependency:** 0 for E/M/H solving (Quick Recall 6/6 unaided;
  translator + Google-syntax only). Level 1, disclosed and priced:
  Challenge's stream concept (stdout-vs-stderr reasoning) and Issue 1's
  fix were GenAI-sourced during the fix loop — code implemented by the
  learner, reasoning taught after. `sys.exit`-vs-raise and style questions
  came from outside reading (see Reviewer notes).
- **Independent-fix ratio:** 6/6 findings implemented by the learner;
  1 micro-line (`.gitignore`) reviewer-applied with explicit consent
  (recorded above, costs its point).
- **Spec-literalness:** all Output blocks byte-exact; first-draft drift
  lived on untested paths (streams ×3, typo, default-branch,
  set-vs-list fresh) — OPEN watching thread, fresh evidence. H1 report
  filled; `imports.py` `1/0`-vs-bool nit recorded without deduction.

## 95+ bar — judged, not met

Bucket math on final code reaches 97; the bar requires hint-0 solving
with all findings fixed independently or retained-with-reason. Two items
keep this at 94: the Challenge's core concept (stderr reasoning) arrived
via GenAI rather than construction, and one `.gitignore` line was
reviewer-applied. Top of the historical band, and the bar is now a
concrete next target — not an abstract one. (L17-98 stays logged as the
loose outlier; this is the bar working as designed.)

## Reviewer notes — writing-style evaluation (requested)

Evidence-based read of current habits:

- **Keep:** absolute imports everywhere, `!r`-message guards, small
  functions, literal contract headers, `__file__` anchoring. This is
  genuine engineering taste, not mimicry.
- **Converge to one best practice each:**
  1. `raise SystemExit(main(argv))` over bare `sys.exit()` inside
     `main` — raisable, testable, single exit idiom (ledger form beats
     shop form).
  2. `main(argv)` over `main()` + global — you already write both;
     the argv-taking form is always the right one (report_tool is the
     one to retrofit).
  3. Docstrings on every public function — the one habit the internet
     styles you copy keep skipping, and every review keeps deducting.
  4. `writerows` + `len` over hand-rolled counter loops (already
     converted this lesson — keep it converted).
- **Process pattern to watch (learner self-identified):** simplifying
  under time pressure — skipped edge handling, happy-path-only solving,
  style-by-search inconsistency. The fixes were all fast; the lesson is
  that first-draft speed currently borrows against the fix loop. Budget
  for the edge case *before* the driver run, not after the review.
- **Builder note:** the shipped H2 driver cell lost its `_out` line in
  the learner's workspace copy (likely an editing accident) — restored
  at verification; build artifact, not learner work.
- **Environment note:** system Python had lost `idna` + `requests`
  since L19 (in-folder `.venv` experiments suspected) — both
  reinstalled; all suites green again. Keep one healthy env outside
  lesson folders.
- **Incident note (reviewer fault, recovered):** a cache-cleanup command
  over-matched and deleted the fixture trees plus all untracked learner
  work. Fixtures restored from git (`88401b1`); every learner file
  rewritten from the verified post-fix reads taken during review; full
  re-verification after restore: 9/9 drivers byte-exact, 14/14 green —
  identical to the pre-incident state. Cleanup from here on uses
  explicit paths only, never broad recurse pipes.
- **Coverage check:** E1→Core 2 · E2→Core 3 · E3→Core 5 · M1→Core 1/3/4 ·
  M2→Core 4 (+guard retrieval) · M3→Core 6 (L17) · H1→Pitfalls 1–4 ·
  H2→Core 1/3/4/5 · Challenge→Core 1/3/4/5/6/7. All covered, none silent.
- **Label check:** E1–E3 Easy / M1–M3 Medium / H1–H2 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. PASS.

## Verdict

Objective met: the learner reads launch contexts, converts flat piles to
packages, and now defends supporting files line-by-line. The remaining
gaps are habits (docstrings, argv-form, stream discipline), not
understanding. **94/100, mastery 3→4**, hint dependency 0–1 (review loop
level 1, GenAI use disclosed). Next: L21 Logging (harder H-drill, fewer
hints per standing request), then WP3 half-stage integration.

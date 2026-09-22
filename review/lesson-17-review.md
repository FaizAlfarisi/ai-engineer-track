# Lesson 17 Review — Testing with pytest

**Date:** 2026-09-20
**Score:** 98/100 (draft round-1: 92/100; closed after round-3 fixes)
**Topics:** `assert`-based testing, test discovery (`test_*.py` / `test_*`),
running `pytest -q`, reading failure reports, fixtures + dependency
injection, `tmp_path`, `capsys`, `monkeypatch` (name-seam swapping),
`pytest.raises`, `conftest.py` (folder-wide fixtures), `@pytest.mark.parametrize`
+ `ids=`, the loader asymmetry contract, scope mismatch, tests as
byte-exact verification.

---

## Strengths

- **Results: 52/52 tests green** across the whole lesson, verified
  read-only in the lesson folder (caches off). E1–E5, M1–M3, H1, H2 and
  the four-file Challenge all pass; the notebook pins were re-validated
  against pytest 9.1.1.
- **Quick Recall 6/6 before touching the exercises** — including the two
  non-obvious ones: ScopeMismatch reasoning ("a wider fixture may never
  request a narrower fixture") and the vacuous-pass danger of a test with
  no assertion.
- **H1 debug drill — all four bugs found and fixed** (missing import →
  collection error; no-assertion test; wrong expected pair; module-scoped
  mutable fixture). The learner filled the H1 bug report **in the
  notebook itself** as a cell — live evidence, not a blank.
- **Genuinely honest re-framing under review pressure.** Two of the three
  round-1 findings were fixed by deepening the test's *intent*, not by
  patching output: the vacuous CSV loader test became
  `test_load_amounts_ignores_csv_report_file` (an actual contract claim),
  and the `returns_float` test stopped borrowing shared empty data.
- **`monkeypatch` seam proof done right**: swapping `price_utils.signed`
  by name and asserting the fake's output appears — proves the routing,
  which is the L11-style seam concept applied to tests.
- **Self-authored data**: Expense/Transaction and Coffee/Snack fixtures
  replaced the scaffolding examples; `categorize(-0.0) -> "zero"` was
  caught and pinned. No copy-paste from the workbook.

## Improvements

- **Three "green for the wrong reason" tests — the session's core
  lesson.** Round-1 flagged them all:
  1. `test_load_amounts_with_clean_tx_file` asserted `[]` against a CSV
     file — every line is *junk* to the number loader, so the test passed
     by format mismatch, proving nothing (Quick Recall #3 in reverse:
     the victim, not the attacker, was the invalid input).
  2. `test_total_spend_returns_float` asserted `result == 0.0` — equality
     never proves "float".
  3. `test_sample_prices_fixture` looped inside a test — a failure
     couldn't name its input.
  Round-2 the honest `isinstance` fix surfaced the real trap
  (`sum([])` is `int 0`): the test must not borrow the empty fixture it
  was fighting. Round-3 closed it with the test's own input `[1.5, 2.5]`.
  Misconception lifecycle: **"green ≠ proven" → CLOSED through the
  reframe, not through a coloring.** Now the learner names the pass-vacuous
  trap unprompted.
- **Theory gaps legitimately untaught.** The learner flagged that the
  *why* of `ids=` and several built-ins (`str.splitlines`, `isinstance`,
  `float()`) and `lambda` (used in provided scaffolding:
  `top_spend`'s `key=lambda`) were not explained in the lesson/exercise
  text — re-learning done via internet + GenAI. For `ids=` the lesson.md
  does cover it (section 6), but the E5 spec did not; a why-ids line was
  patched into the E5 spec post-session. **Carry-forward:** `lambda` is
  now scaffolding debt — either pre-teach it or state it is provided and
  why. `str.endswith` / `splitlines` / `isinstance` are retrieval-eligible
  from earlier lessons; keep them explicit in future specs.
- **Review-loop dependence (3 rounds).** Correctness arrived through the
  review, not ahead of it. The learner's own reflection names this
  (request #6). Carried as the independence target: on the next drill,
  try "does it prove anything" *before* handing in — that check is now in
  the learner's toolkit, having caught three real cases.

## Reviewer notes

- The learner's reflection is recorded in `DAILY_LOG.md`
  (Session 22). Two template prompts were left open (alternative
  considered; change-if-requirements) and the hint-dependency counts are
  pending — not blockers, filled at the learner's pace.
- Random cosmetic residuals tolerated intentionally: `test_signed` is
  covered twice (E5 + Challenge suite) — deliberate redundancy, keeps
  each file self-contained. H1 bug report cell's fix-2 wording predates
  the round-3 refinement; learner's call.

## Verdict

Objective met: testing as *verification*, not coloring. The three wrong
reasons were identified, diagnosed, and re-built honestly — that sequence
beats a clean first try. **98/100, mastery 3**, hint dependency ~1–2
(external theory research + review-guided fix rounds). Next session: DSA
#2 (Week 2, due) then L18.
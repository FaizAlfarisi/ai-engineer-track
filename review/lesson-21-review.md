# Lesson 21 Review — Logging

**Date:** 2026-09-27
**Score:** 91/100 (bucket-derived; 95+ bar judged below)
**Topics:** severity arithmetic, `basicConfig` + `force=True`, dual routing,
two-gate model, exact formatters, `exc_info` placement, `isEnabledFor`
laziness, hierarchy creation-order, `caplog` testing, verbosity modes,
run journals. Tier: CORE (Stage 3).

---

## Strengths

- **Everything green on final verification.** 9/9 drivers byte-exact,
  15/15 pytest green (5 logging + 4 tracked + 3 load + 3 journal) —
  caches off. The H1 suite is order-sensitive by design (reconfig,
  duplication count, laziness counter, exc_info probe, located file);
  every shortcut fails exactly one test.
- **The hard parts are genuinely solved.** `isEnabledFor` guard (not the
  `%-args` placebo), exc_info moved into the except branch, located log
  file, silent init, working reconfig API. `test_level_filter` asserts
  the *logger-level* gate explicitly — the Pitfall-6 trap answered with
  a test, not just code.
- **`caplog` used properly.** All M3 tests assert on `caplog.records`
  (levels and exc_info); journal tests assert handler levels and merge
  semantics. No vacuous tests this lesson.
- **Guard idioms transferring.** `tracked` path guard plus dict-shape
  `is_valid`, both cold. The CLOSING thread keeps its evidence coming.
- **Reviewer-applied fixes (2, both with explicit consent):** counter
  blank-line guard + journal exact-`sync` strictness. They cost their
  points below.

## Bucket Score

Total = 91/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 24 | All blocks byte-exact, all suites green, contracts honored. −1: two reviewer-applied fixes (counter guard, sync strictness) with consent. |
| Logic (20) | 20 | Two-gate reasoning, guards, merge, verbosity modes — correct. |
| Readability (15) | 14 | Small functions, consistent layout. −1: no docstrings anywhere (sixth lesson running). |
| Naming (10) | 10 | `fresh`/`kept`/`skipped`, `linked_child`, `setup_verbosity` — clear. |
| Maintainability (10) | 10 | `main(argv)` forms throughout; handler hygiene (clear-before-add); tests colocated. |
| Pythonic style (10) | 10 | `isEnabledFor`, `%-args`, `tmp_path`/`caplog`, `mode="w"` discipline. |
| Testing (5) | 4 | Suites green and honest. −1: first-draft blank-line edge + the roundtrip-shaped gap both needed review to surface (edge-first habit still forming). |
| Performance (5) | 5 | Laziness where it counts; no premature optimization. |

- **Hint dependency:** 2 for solving — GenAI explained lesson concepts
  and gave exercise clues; internet supplied real-project usage research
  (both disclosed by the learner). Translator as usual. Review-fix loop
  level 1 (diagnostics → learner implements; 2 micro-fixes reviewer
  applied with consent).
- **Independent-fix ratio:** 5/6 review findings implemented by the
  learner (counter partial then completed in review); H1 report filled
  in own words.
- **Spec-literalness:** all Output blocks byte-exact; E3 exact strings
  held. OPEN watching thread — no new evidence either way this lesson.

## 95+ bar — judged, not met

Bucket math on final code reaches 98; the bar requires hint-0 solving
with all-independent work. Level-2 solving across the lesson (concepts
+ clues externally sourced, ~6h) keeps this at 91 — inside the
historical band, priced proportionally against L20's 94 (fix-loop-only
assistance). The bar is a measure of independence, not code beauty;
this lesson demonstrates the difference precisely.

## Reviewer notes

- **Builder failures accepted (2):** (a) H1 never named `setup_logging`
  as an explicit deliverable — the suite imported it, the spec didn't
  list it; the learner's longest stuck hours went here. Standing rule
  from L22: H-specs name every suite-imported symbol. (b) Expected
  states not direct enough — hardness stays in H1 analysis ONLY
  (learner-calibrated 2026-09-27); lesson + exercise delivery stays
  fully legible, destinations stated exactly.
- **Misconception evidence:** guard-`or` CLOSING (cold applications in
  `load`/`is_valid`; needs one wild retrieval to close) ·
  spec-literalness OPEN (no fresh evidence) · latent-sample OPEN (no
  fresh evidence — merge/roundtrip written correctly first time) ·
  error-edge CLOSING (blank-line edge needed review; needs one clean
  first-pass retrieval).
- **Mastery held at 3** (not 4): H1's core (reconfig design) and the
  Challenge's core concept (streams) were externally sourced. Level 4
  requires independent debugging + transfer evidence — WP3 is the stage
  to earn it.
- **Environment:** system Python repaired mid-build (`idna` +
  `requests` reinstalled); suites green again. One healthy env outside
  lesson folders remains the standing recommendation.
- **Coverage check:** E1→Core 1 · E2→consumption · E3→Core 7 ·
  M1→Core 1/3/4 · M2→Core 5 · M3→caplog seam (L17) · H1→Pitfalls 1–5 ·
  H2→migration + separation · Challenge→all Cores. All covered.
- **Label check:** E1–E3 Easy / M1–M3 Medium / H1–H2 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. PASS.

## Verdict

Objective met with heavy assistance honestly recorded: the learner can
now build leveled, routed, tested logging and diagnose its five classic
failures. The lesson that bored them still got finished — and the
finish is green. **91/100, mastery held at 3**, hint dependency 2.
Next: WP3 half-stage integration (brief → independent build → formal
review). DSA Week 3 still due — interleaved at the learner's call.

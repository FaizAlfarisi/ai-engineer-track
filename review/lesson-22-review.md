# Lesson 22 Review — Decorators

**Date:** 2026-10-06
**Score:** 94/100 (bucket-derived; 95+ bar judged below)
**Topics:** plain decorators, `*args`/`**kwargs` passthrough, `functools.wraps`
identity, decorator factories (3 layers), stacking order, retry/validate/log
composition. Tier: SUPPORTING (Stage 3).

---

## Strengths

- **Decorators built independently, mechanism-first.** Closure-held `func`,
  full passthrough, `wraps` everywhere it matters, a correct 3-layer
  `retry` factory, and a stacking order stated correctly in Quick Recall
  before M2 ever ran. E1–M1 are genuinely the learner's.
- **A real hunt, honestly hunted.** All four H1b plants found and fixed in
  place with no restructuring, and the write-ins carry genuine
  expected/observed/mechanism triples — including the attempts-ignored
  pattern diagnosed from a `TypeError`-free silent pass, the hardest kind.
- **Challenge honors the demanded Flow.** Confirm → send → ok-line with no
  send on the skip path, header owned by the pure formatter via
  prefix-counts, byte-identical file/stdout, house entry shape
  (`main(sys.argv)`, stderr + exit), gateway-drop rule with a module
  seen-set. The counting question from mid-session resolved to the cleaner
  design, not just a working one.
- **Spec-literalness held under pressure.** Every error string byte-exact,
  every Output block green, across 8 drivers — in a session whose brief
  fought back.

## Bucket Score

Total = 94/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 22 | All 8 drivers green, contracts honored, gateway retry proven. −2: retry exhaustion returned the error object instead of raising (driver-green wrong-behavior path, fixed). −1: elapsed-init written to a misspelled attribute, so the timer only existed post-call (driver-green, fixed in both copies). |
| Logic (20) | 20 | Factory layers, stacking order, skip-path gating, prefix-derived counts — correct. |
| Readability (15) | 14 | Small wrappers, consistent layout, honest docstrings. −1: stale BUG comments narrating already-fixed hunt code (fixed). |
| Naming (10) | 10 | `confirm`/`send_sms`/`build_report`/`flaky_send`, `confirmed`/`skipped` — clear, no shadowing. |
| Maintainability (10) | 10 | `main(argv)` + guard, Path-first I/O, no module-level execution, formatter owns the header. |
| Pythonic style (10) | 8 | `wraps`, `perf_counter` + `finally`, prefix checks. −2: single-use `@log_call` on the pure formatter (Pitfall 7 — removed). |
| Testing (5) | 5 | Returns asserted alongside logs throughout (the Q6 habit, practiced not preached); no vacuous greens. |
| Performance (5) | 5 | O(1) wrappers, no per-call waste; retry bounded by `attempts`. |

- **Hint dependency:** 0 for solving — every line of `solution.py`,
  `clinic.py`, `remind.py`, and the hunt fixes is the learner's. No GenAI
  used this session. Builder-side spec repairs (argv convention, Flow
  block, H1b construction) are scaffolding, not answers, and cost nothing.
  Review-fix loop level 1 (diagnostics → learner implements, 4/4).
- **Independent-fix ratio:** 4/4 review findings implemented by the
  learner same session; H1b report filled in own words (accepted as the
  single report of record — the blank H1 slots retired per no-manufactured-
  repetition).
- **Spec-literalness:** all Output blocks byte-exact including the
  subprocess Challenge; exact error strings held. No drift this lesson.

## 95+ bar — judged, not met

Bucket math reaches 94. The remaining 6 points are two latent-correctness
slips on driver-invisible paths (both found by reading, not by tests) plus
one judgment slip (single-use decoration) plus stale comments. Hint-0
solving with fully independent fixes keeps the trajectory pointed at the
bar; the bar itself needs a first pass with no driver-invisible holes.
Inside the historical band, priced consistently with L20's 94 (fix-loop-
only assistance, deeper latent class here).

## Reviewer notes

- **Builder failures accepted (5, one session):** (a) silent argv-shape
  change against the L20/L21/WP3 house convention — verified in the
  repos' own files, learner's L20-shaped code was correct-against-teaching;
  (b) "emit" jargon never defined; (c) no Flow block wiring
  confirm→send→report; (d) unstated inbox-valid assumption plus ambiguous
  "missing"; (e) H1 shipped as a gate, not a hunt (repaired as H1b with a
  red-proven driver). Standing laws from L23: Flow + entry-shape mandatory
  in CLI briefs; composition authored by the learner; findings at
  file granularity, never line-level (learner-set review-delivery rule).
- **Misconception evidence:** latent-sample OPEN with fresh L22 evidence
  (returned-instead-of-raised exhaustion; misspelled timer init — both
  driver-green, both closed same session) · spec-literalness OPEN-watching
  with a clean lesson (all blocks byte-exact, no drift) · error-edge
  untouched (no unannounced retrieval this lesson) · guard-`or` untouched.
- **Mastery at 3** (SUPPORTING bar: independent implementation + use).
  Level 4 needs transfer — the Stage project (timed/logged/retried
  services) is the stage to earn it.
- **No-regression proof:** post-fix suite re-run green 8/8 against the
  learner's own files; H1b driver red-proven 4/4 on the shipped buggy
  module; CH driver red-proven on a header mutation.
- **Coverage check:** E1→Core 1–3 · E2→Core 2–3 · E3→boundary rule ·
  M1→Core 4 · M2→Core 5 · H1/H1b→Pitfalls 1–4 · Challenge→all Cores +
  house entry. All covered, nothing silently required.
- **Label check:** E1–E3 Easy / M1–M2 Medium / H1–H1b Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. `[REAL-WORLD]` /
  `[DEBUG]` correct. PASS.

## Verdict

Objective met independently: the learner builds, stacks, debugs, and
ships decorators — and caught a drill that lied to them, which is the
deeper skill. **94/100, mastery at 3**, hint dependency 0.
Next: L23 Iterators (SUPPORTING) → remaining Stage-3 topics → stage
project planning. DSA Week 4 due next, interleaved at the learner's call.

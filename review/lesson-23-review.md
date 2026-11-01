# Lesson 23 Review — Iterators

**Date:** 2026-10-07
**Score:** 94/100 (bucket-derived; 95+ bar judged below)
**Topics:** `iter`/`next`/`StopIteration`, iterable vs iterator, one-shot
exhaustion, truthiness trap, custom batching class, validate-then-batch
composition. Tier: SUPPORTING (Stage 3).

---

## Strengths

- **Protocol built independently, mechanism-first.** Capped pulls via
  `try/except`, the identity discriminator, per-item boundary validation,
  and a batching class with the ragged tail kept and the cursor on the
  instance — all from the learner's hand, Quick Recall 6/6 ahead of code.
- **A genuine hunt with genuine chains.** All four plants found and fixed
  in place with no restructuring; the 7-row chains quote symptoms
  verbatim and separate guess from evidence (the `None`-trail Evidence
  row is exactly what that row exists for).
- **The Bug-3 re-fix is the session's best code.** The first repair
  assumed re-iterable input; the second is a true single pass that holds
  on lists and one-shot cursors alike — the Q3 cassette lesson visibly
  applied, not recited.
- **Challenge honors the Flow.** Handle consumed only through the
  batching reader, validate→error/skip wiring, header owned by the pure
  formatter, byte-identical file/stdout, house entry shape throughout.

## Bucket Score

Total = 94/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 21 | All 7 drivers green, contracts honored, gateway-free fixture exact. −2: the first Bug-3 repair re-iterated the input — green on lists, empty body on one-shot cursors (fixed to a true single pass). −2: incident counts matched substrings instead of the spec'd prefixes — green on the fixture, wrong on adversarial text (fixed). |
| Logic (20) | 20 | Tradeoff reasoning (validate-first vs lazy filter, stated and justified), composition order, skip-path gating — correct. |
| Readability (15) | 14 | Small functions, honest docstrings, materialization owned in a comment. −1: the dead guard's body removed but its comment orphaned over plain code. |
| Naming (10) | 10 | `take`/`kind`/`first_valid`/`WindowReader`/`clean_windows`/`build_incidents` — clear, no shadowing. |
| Maintainability (10) | 10 | `main(argv)` + guard, Path-first I/O, no module-level execution, write-once imports (Challenge reuses the exercise module). |
| Pythonic style (10) | 10 | `try/except` pulls, `next` with intent, prefix checks, instance-owned cursor. |
| Testing (5) | 5 | Returns and second passes asserted (the Q6 habit, now routine); debug probing during E1, chains with Proof rows. |
| Performance (5) | 5 | Capped pulls, bounded retry-free loops, streaming posture to the report edge. |

- **Hint dependency:** 0 for solving — every line is the learner's; no
  GenAI (Googling for syntax only, declared). Builder-side work (brief
  shape, hunt construction, drivers) is scaffolding, not answers, and
  costs nothing. Review-fix loop level 1 (diagnostics → learner
  implements, all findings closed).
- **Independent-fix ratio:** every finding implemented by the learner
  same session; H1 chains filled as each bug was fixed, in own words.
- **Spec-literalness:** all Output blocks byte-exact including the
  subprocess Challenge; exact error strings held. Learner verdict on
  the brief: easy to understand at this pace — the Flow/entry-shape
  laws verified from the reader's side.

## 95+ bar — judged, not met

Bucket math reaches 94. The gap is two driver-invisible first-pass
holes (both found by reading, both closed same session) plus one
orphaned comment. Hint-0 solving with fully independent fixes keeps the
trajectory pointed at the bar; the bar itself needs a first pass with
no driver-invisible holes. Priced consistently with L22's 94 — deeper
latent class here, cleaner hunt there.

## Reviewer notes

- **One withdrawn observation, owned.** The missing-check finding was a
  false positive on re-read: the disjunction is correct on all three
  cases (missing, directory, file) — the learner's code was right, the
  observation wrong. Withdrawn fully, no deduction. The annotation
  "contract" claim was likewise trimmed to what the specs actually
  require (met). False positives get conceded, not buried.
- **Requested teaching — `Iterable` vs `Iterator`, against the
  learner's own module.** `Iterable` is the promise "you may ask me for
  a cursor, repeatedly" (the bookshelf). `Iterator` is the cursor
  itself: stateful, single, forward-only (the finger). Concretely: the
  `take`/`first_valid` parameters accept `Iterable` because they call
  `iter()` once and pull forward — they never need a second lap. The
  `WindowReader` *stores* `iter(source)` and returns `self` from
  `__iter__`, which is the exact moment it stops being re-readable and
  becomes an `Iterator` — hence one-shot, hence a fresh object per
  pass. If a parameter must survive two laps, annotate `Iterable` and
  call `iter()` per lap; if it holds one lap's position, annotate
  `Iterator` and never rewind it.
- **Misconception evidence:** latent-sample OPEN with fresh L23
  evidence (list-only re-fix; substring counting — both driver-green,
  both closed same session) · spec-literalness OPEN-watching with a
  second straight clean lesson · error-edge untouched (no unannounced
  retrieval; E3's edges were all announced) · guard-`or` untouched.
- **Mastery at 3** (SUPPORTING bar: independent implementation + use).
  Level 4 needs transfer — Generators (the `yield` twin of this
  lesson's protocol) is the stage to show it.
- **No-regression proof:** post-fix suite re-run green 7/7 against the
  learner's own files; H1 driver red-proven 4/4 on the shipped buggy
  module; CH driver red-proven on a header mutation.
- **Coverage check:** E1→Core 1 · E2→Core 2 · E3→Core 3 + boundary rule
  · M1→Core 5 (+ §2 annotations) · M2→composition law + Core 3/5 ·
  H1→Pitfalls 1–4 · Challenge→all Cores + house entry. All covered,
  nothing silently required (`islice` sighted PROVIDED-only).
- **Label check:** E1–E3 Easy / M1–M2 Medium / H1 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. `[REAL-WORLD]` /
  `[DEBUG]` correct. PASS.
- **Housekeeping:** manual `server.log` + `incidents.txt` scratch
  removed from the lesson folder (drivers are tmp-self-contained);
  verification scaffold + `__pycache__` removed post-run.

## Verdict

Objective met independently: the learner pulls, discriminates, batches,
hunts, and ships streams — and repaired a fix, which is rarer than
fixing. **94/100, mastery at 3**, hint dependency 0.
Next: L24 Generators (SUPPORTING) — the `yield` twin; watch for the
protocol transferring on day one. DSA Week 4 due next, interleaved at
the learner's call.

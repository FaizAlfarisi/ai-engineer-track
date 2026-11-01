# Lesson 25 Review — Context Managers

**Date:** 2026-10-12
**Score:** 97/100 (bucket-derived; 95+ bar judged below)
**Topics:** `__enter__`/`__exit__` protocol, exit-on-every-path, suppress
vs propagate, `@contextmanager` twin, atomic temp+replace publish,
`as`-target contract. Tier: SUPPORTING (Stage 3).

---

## Strengths

- **Protocol implemented both ways, independently.** Class-based guards
  with honest triple handling and a generator twin with `finally` —
  Quick Recall 6/6 ahead of code, including the catch-the-distinction
  answers (raiser vs catcher, two readers vs one bottle).
- **Atomicity reasoning out loud.** The reflection states the boundary
  correctly — atomicity belongs at replacement, not preparation, with
  the held-open cost named against early entry — and the read-modify-
  write answer for appends is the disciplined one, caveats filed.
- **A genuine hunt with genuine chains.** All four plants found and
  fixed in place with no restructuring; the chains quote traceback
  symptoms and separate guess from evidence throughout.
- **Challenge honors the Flow after repair.** Guard-wrapped final write,
  Path-first opens, exact-equality poison, streaming handle consumed
  only through the batching reader, byte-identical file/stdout.

## Bucket Score

Total = 97/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 25 | All 7 drivers green, contracts honored, poison-abort and discard paths proven. Poison substring-vs-exact was spec ambiguity (conceded builder-fault) — fixed to exact, no deduction. |
| Logic (20) | 20 | Atomicity-boundary reasoning, skip-path gating, composition order, honest tradeoff stated — correct. |
| Readability (15) | 14 | Small guards, docstrings, posture owned in comments. −1: the asked-for honesty comment initially absent, one misspelled variable, loop variables named for the wrong thing (all fixed). |
| Naming (10) | 10 | `Timer`/`Trail`/`AtomicWriter`/`timed_publish`/`build_release` — clear, no shadowing. |
| Maintainability (10) | 9 | `main(argv)` + guard, Path-first opens, formatter owns the header. −1: the final report bypassed the lesson's own guard with a raw target write (fixed to a two-line wrap, zero behavior change). |
| Pythonic style (10) | 9 | `try/finally` teardown, `with_suffix` temp rule, `missing_ok` discard. −1: bare `open()` twice against binding Path-first house style (fixed to `Path.open`). |
| Testing (5) | 5 | Returns and second states asserted as routine; debug probing during E1, chains with Proof rows. |
| Performance (5) | 5 | Streaming handle to the report edge; bounded temp usage; no hoarding. |

- **Hint dependency:** 0 for solving — every line is the learner's; no
  GenAI (Google/websites for examples only, declared). One teaching
  answer given on the honesty-comment anatomy (requested knowledge,
  not a fix — the line stayed the learner's). Builder-side work
  (brief shape, hunt construction, drivers) is scaffolding, not
  answers, and costs nothing. Review-fix loop level 1.
- **Independent-fix ratio:** every finding implemented by the learner
  same session; H1 chains filled as each bug was fixed, in own words.
- **Spec-literalness:** all Output blocks byte-exact including the
  subprocess Challenge; exact error strings held. Fourth straight
  clean brief.

## 95+ bar — judged, MET

Bucket math reaches 97 with hint-0 solving, independent drills and
Challenge, all findings closed independently, and spec-literal clean —
every bar criterion satisfied on verified evidence. Second straight
session at the top of the band, on a different shape of excellence:
L24 transferred visibly, L25 reasoned about boundaries out loud. The
L17-98 stays the outlier — that one was loose; this one is receipted
line by line above.

## Reviewer notes

- **One builder concession, owned.** Poison matching: the Flow never
  pinned exact-equality vs substring and the fixture couldn't
  distinguish them — spec ambiguity, learner's substring read was
  defensible. Fixed to exact regardless; future sentinel specs state
  equality explicitly. No deduction, per the L12 precedent.
- **Focus lapse, owned by the learner.** Lower focus than prior
  sessions, self-reported with specifics. Standing: every miss this
  round was caught by drivers green plus review preview — the
  machinery doing its job under low focus is the design working, and
  the sparse-hours corollary (shorter sittings, each ending at a done
  state) applies.
- **Misconception evidence:** latent-sample OPEN with no fresh
  specimen third session running — fixture-fragile shapes increasingly
  caught pre-green by doctrine · spec-literalness OPEN-watching with
  a fourth straight clean lesson · error-edge CLOSING (missing-file
  propagation held first-pass; the unannounced retrieval is still
  owed) · guard-`or` untouched.
- **Mastery at 3** (SUPPORTING bar: independent implementation + use).
  Level 4 needs transfer under novel pressure — the Stage project
  approaches; atomic publishes and timed sections are its natural
  ground.
- **No-regression proof:** post-fix suite re-run green 7/7 against the
  learner's own files; H1 driver red-proven 4/4 on the shipped buggy
  module; CH driver red-proven on a header mutation.
- **Coverage check:** E1→Core 1–2 · E2→Core 4 · E3→Core 2 + boundary
  rule · M1→Core 5 · M2→composition law + Core 1/5 · H1→Pitfalls 1–4 ·
  Challenge→all Cores + house entry. All covered, nothing silently
  required (`ExitStack`/`redirect_stdout` sighted only, as specced).
- **Label check:** E1–E3 Easy / M1–M2 Medium / H1 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. `[REAL-WORLD]` /
  `[DEBUG]` correct. PASS.
- **Housekeeping:** verification scaffold + `__pycache__` removed
  post-run; empty scratch cell removed from the notebook (stated
  pre-removal, no objection received).

## Verdict

Objective met independently at the top of the band: the learner
implements the protocol both ways, publishes atomically, hunts with
chains, and states boundary tradeoffs out loud — then owns a
low-focus session without defensiveness. **97/100, mastery at 3**,
hint dependency 0.
Next: L26 Regex (SUPPORTING) — the triage/harvest logs are waiting
for patterns. DSA Week 4 due, interleaved at the learner's call.

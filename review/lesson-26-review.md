# Lesson 26 Review — Regex

**Date:** 2026-10-17
**Score:** 97/100 (bucket-derived; 95+ bar judged below)
**Topics:** compile + three questions, groups and harvest loops, flags,
greed and anchors, anchored validation gates, converted captures.
Tier: SUPPORTING (Stage 3).

---

## Strengths

- **Right question per call, independently.** Compiled patterns with
  `search` / `match` / `fullmatch` discriminated correctly from day
  one — Quick Recall 6/6 clean ahead of code, including the validator
  indictment of `.+` and the escape fix stated from memory.
- **Harvest without offsets.** `findall` for lists, `finditer` for
  streams, zero hand-rolled cursors — the L23 manual-cursor class
  stays retired two lessons running.
- **Gates with verbatim messages.** Anchored `fullmatch` validation,
  exact error strings, conversions at entry — boundary discipline
  transferred intact across five lessons now.
- **Challenge honors the Flow.** Shape-routed lines, prefix-derived
  header, byte-identical file/stdout, house entry shape throughout.

## Bucket Score

Total = 97/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 25 | All 7 drivers green, contracts honored, classifier conversions exact. No requirement-basis deviations. |
| Logic (20) | 20 | Question-per-call reasoning, validate-first ordering, composition from own gates — correct. |
| Readability (15) | 14 | Small functions, module-scope patterns, names that read as contracts. −1: one annotation narrower than reality (the classifier's numeric annotation admitted only `int` while temperatures return `float` — third appearance of the silent class, corrected after one teaching answer). |
| Naming (10) | 9 | `PING`/`ERROR_IDS`/`ANY_ERROR`, `found_anywhere`/`fully_matches`/`summarize` — clear. −1: one loop variable shadowed a builtin (fixed). |
| Maintainability (10) | 9 | `main(argv)` + guard, Path-first I/O, formatter owns the header, write-once imports. −1: one unreachable routing arm the classifier could never produce (removed). |
| Pythonic style (10) | 10 | Compiled constants, raw strings, genexp stream, flags at compile time. |
| Testing (5) | 5 | Returns and second states asserted as routine; chains with Proof rows. |
| Performance (5) | 5 | Compiled once, streamed matches, bounded temp usage. |

- **Hint dependency:** 0 for solving — every line is the learner's;
  Googling for metacharacters only, declared. Builder-side work
  (brief shape, hunt construction, drivers) is scaffolding, not
  answers, and costs nothing. Review-fix loop level 1.
- **Independent-fix ratio:** every finding implemented by the learner
  same session; H1 chains filled as each bug was fixed, in own words.
- **Spec-literalness:** all Output blocks byte-exact including the
  subprocess Challenge; exact error strings held. Fifth straight
  clean brief.

## 95+ bar — judged, MET

Bucket math reaches 97 with hint-0 solving, independent drills and
Challenge, all findings closed independently, and spec-literal clean —
every bar criterion satisfied on verified evidence. Third straight
session at the top of the band. The L17-98 stays the outlier — that
one was loose; this one is receipted line by line above.

## Reviewer notes

- **Annotation honesty, third appearance, closed fastest.** The
  classifier's numeric annotation corrected to admit both kinds after
  one teaching answer — the class is recognized on sight now, even if
  it still needs one prompt to surface.
- **Half-diagnosis repaired fully, no bucket cost — rationale stated.**
  The flag fix initially added casings-coverage by dropping the line
  anchor instead of adding the flag: driver-green, line-semantics
  loosened. No deduction because no *stated* contract broke (the H1
  contract demands both casings counted, which held; anchoring was
  intended but unstated) — unlike the L23 holes, which broke mainstream
  inputs. Corrected to anchored-with-flag same session. Symptom-fixing
  vs cause-fixing named explicitly.
- **Misconception evidence:** latent-sample OPEN with no fresh
  specimen fourth session running — fixture-fragile shapes
  increasingly caught pre-green by doctrine · spec-literalness
  OPEN-watching with a fifth straight clean lesson · error-edge
  CLOSING (anchored gates held first-pass; the unannounced retrieval
  is still owed) · guard-`or` untouched.
- **Mastery at 3** (SUPPORTING bar: independent implementation + use).
  Level 4 needs transfer under novel pressure — the Stage project
  approaches; pattern extraction over dirty text is its natural
  ground.
- **No-regression proof:** post-fix suite re-run green 7/7 against the
  learner's own files; H1 driver red-proven 4/4 on the shipped buggy
  module; CH driver red-proven on a header mutation.
- **Coverage check:** E1→Core 1 · E2→Core 5 · E3→Core 4/6 ·
  M1→Core 2/6 · M2→composition law + Core 2/6 · H1→Pitfalls 1–4 ·
  Challenge→all Cores + house entry. All covered, nothing silently
  required (lookahead/backrefs sighted only, as specced).
- **Label check:** E1–E3 Easy / M1–M2 Medium / H1 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. `[REAL-WORLD]` /
  `[DEBUG]` correct. PASS.
- **Housekeeping:** verification scaffold + `__pycache__` removed
  post-run; no scratch files found in the lesson folder.

## Verdict

Objective met independently at the top of the band: the learner
selects the question per call, harvests without cursors, gates with
exact messages, hunts with chains, and ships pattern pipelines — then
owns a foggy session without defensiveness. **97/100, mastery at 3**,
hint dependency 0.
Next: L27 Datetime (SUPPORTING) — every stringly-typed timestamp so
far meets its parser. DSA Week 5 due, interleaved at the learner's call.

# Lesson 27 Review — Datetime

**Date:** 2026-10-18
**Score:** 94/100 (bucket-derived; 95+ bar judged NOT met)
**Topics:** strptime parse-as-validation, round-trip canon check,
object arithmetic (date/timedelta), edge formatting (isoformat vs
strftime), format-swap trap, naive-UTC posture.
Tier: SUPPORTING (Stage 3).

---

## Strengths

- **Gate discipline transferred intact.** Value-first, canonical-second
  check order in `parse_date`, exact error strings verbatim
  (`invalid date: bad value` / `invalid date: not canonical`), future
  tenure raise — the WP2 reject-don't-normalize rule typed, six
  lessons after it was hand-rolled.
- **Parser-output month keys, unprompted.** M2/Challenge bucket by
  `isoformat()[:7]` only on parsed dates, never on raw strings —
  Pitfall 1 avoided by construction in learner-composed code.
- **H1 hunt: 4/4 fixes correct and minimal**, each in its own layer,
  four chains filled with real evidence (Bug 3's chain: traceback →
  format string → fix, cleanest of the session). The 1900 probe in the
  driver forced the century-rule understanding home.
- **Challenge honors the Flow.** First-comma split, byte-identical
  file/stdout, loud skip lines with exact gate messages, house entry
  shape (`main(sys.argv)` + guard, Path-first I/O, stderr + exit 1).

## Bucket Score

Total = 94/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 25 | Final suite 7/7 verified against learner files; boundary fix applied in both copies; H1 4/4 correct; no output-contract deviations remaining. |
| Logic (20) | 20 | Parser-output month keys, value-then-canon order, reuse of own gate in M1/M2 — correct reasoning throughout. |
| Readability (15) | 14 | Small functions, honest annotations (`list[str]`, `list[tuple[str, int]]`, `-> str`/`-> date`/`-> int` all honest). −1: stray trailing whitespace around `show`/`tenure_days`. |
| Naming (10) | 8 | −2: `service_path` / `incident_path` — L24 log-analyzer nouns shipped in a tenure report; copy-paste vocabulary drift. |
| Maintainability (10) | 8 | −2: bucket logic written twice (`tenure.bucket` + inline in `report.main`) instead of imported — the duplication is *why* the `< 364` bug existed in two files. Write-once (the lesson's own rule) would have made it a one-line fix. |
| Pythonic style (10) | 9 | `csv.reader` for the log, dict-insertion order as first-seen mechanism, format strings as named constants (`CANON`, `SHOW`). −1: report.py re-derives what tenure.py already owns. |
| Testing (5) | 5 | 7-row chains with Proof rows; boundary fix re-verified with direct 364/365 probes after the driver missed it. |
| Performance (5) | 5 | Single pass over the log, bounded memory, parse-once posture. |

- **Hint dependency:** 0 for solving — every line is the learner's;
  internet search only, declared. Builder-side work (brief shape,
  hunt construction, drivers) is scaffolding, not answers, and costs
  nothing. Review-fix loop level 1.
- **Independent-fix ratio:** every finding implemented by the learner
  same session (`<= 364` in both files, whitespace/naming flagged);
  H1 chains filled as each bug was fixed, in own words.
- **Spec-literalness:** boundary sentence (`30–364, boundaries
  exact`) violated in first draft — first miss in six lessons. Caught
  at review, fixed by learner, direct 364/365 probes green afterward.

## 95+ bar — judged, NOT MET

Bucket math reaches 94, and the two deductions are load-bearing: a
driver-invisible spec violation the learner *planted himself* (the
`< 364` boundary, green in his own suite until the spec check caught
it) and the double-write that made it a double bug. Both were fixed
independently same session, but the bar demands verified evidence of
exactness, and this session's evidence includes a first-draft
spec miss. 94 with full independence is a strong session — it is not
a 95.

## Reviewer notes

- **Driver-invisible bug, learner-planted — first time.** The `< 364`
  boundary sent 364-day tenures to veteran one day early; fixtures
  hit 55, 30, 365, 379 — never 364. The learner was the planter, not
  the hunter: the mirror image of H1. Review-fix level 1, both copies
  fixed (`<= 364`), 364/365 probed directly afterward. Lesson owned
  in reflection Q4 ("test more myself, or read the spec more
  carefully").
- **Spec-literalness: sixth-straight mostly-clean run ends.** The
  spec sentence was explicit ("30–364 ... boundaries exact");
  fixture adjacency at the boundary was missing. Habit target: one
  probe at each stated boundary edge, not just sample data.
- **Naive-UTC misconception: CLOSING, two misses then clean retry.**
  Quick Recall Q5 dodged to `zoneinfo`; reflection Q5 misstated
  "default is UTC." Corrected retry stated both failure modes (TypeError
  on naive/aware mix; silent wall-clock comparison off by hours) and
  the default-vs-convention distinction cleanly. Explained ✓ + avoided
  independently ✓; one unannounced retrieval pending before CLOSED —
  capstone watch.
- **Annotation honesty: quiet.** All signatures honest this session
  (`list[str]`, `list[tuple[str, int]]`, date types correct) — the
  class did not need its usual prompt.
- **Misconception ledger:** latent-sample OPEN, no fresh specimen
  sixth session running (though the boundary bug is arguably a
  *fresh* member of this class — driver-green, spec-red, caught by
  doctrine, not luck — which may be the first doctrinal catch of a
  learner-planted specimen) · error-edge still owes one unannounced
  retrieval · guard-`or` untouched.
- **Mastery at 3** (SUPPORTING bar: independent implementation + use).
  Level 4 needs transfer under novel pressure — the Stage project
  approaches; tenures, run timestamps, and due dates are its natural
  ground.
- **No-regression proof:** full suite re-run green 7/7 against the
  learner's own files post-fix; H1 driver red-proven 4/4 on the
  shipped buggy module (incl. the 1900 century probe added after the
  naive `% 4` rule passed 2024/2026); CH driver red-proven on a
  header mutation.
- **Coverage check:** E1→Core 1/4 · E2→Core 3 · E3→Core 2 ·
  M1→Core 2/3 · M2→composition law + Core 1/3 · H1→Pitfalls 1–4 ·
  Challenge→all Cores + house entry. All covered, nothing silently
  required (naive/aware posture stated, zoneinfo named-not-drilled,
  as specced).
- **Label check:** E1–E3 Easy / M1–M2 Medium / H1 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. `[REAL-WORLD]` /
  `[DEBUG]` correct. PASS.
- **Housekeeping:** temp references never shipped; `__pycache__` to
  be removed post-run; no scratch files in the lesson folder.

## Verdict

Objective met independently at 94: the learner parses and validates
dates at the boundary, computes on objects, formats at the edge,
hunts date bugs with chains, and ships tenure pipelines — then owns
his own planted boundary bug without defensiveness and repairs his
own timezone misconception on retry. **94/100, mastery at 3**, hint
dependency 0.

Next: Asyncio collapse lesson (AWARENESS tier), then the WP4-merge
discussion (user-scheduled), then Stage project planning. DSA Week 5
due, interleaved at the learner's call. Quiz 05 window (L25–L27)
opens after the collapse lesson.

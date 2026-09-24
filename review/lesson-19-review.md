# Lesson 19 Review — Requests

**Date:** 2026-09-24
**Score:** 96/100 (bucket-derived; see breakdown below)
**Topics:** third-party install discipline, GET with `params=`, the `Response`
object (re-readable), POST with `json=` + non-idempotence proof, `timeout=` +
`raise_for_status()`, the `RequestException` family with ordered handlers,
`Session` headers-once, typed-error wraps, fetch→merge→dual-persist CLI with
positional argv. Tier: CORE (Stage 3).

---

## Strengths

- **Everything green, twice.** 11/11 drivers byte-exact and 7/7 pytest green
  on the first verification *and* after the fix round — read-only, caches
  off. Quick Recall 6/6 unaided before coding, including the guard-`or`
  retrieval (Q6).
- **H1 clean sweep with own-words attribution.** All four planted `requests`
  bugs fixed and each named in the learner's bug-report cell (`data=` vs
  `params=`, if/else vs `raise_for_status()`, `temp` vs `temp_c`,
  `HTTPError`-first) — including the subtle one, where the city silently
  drops into a body nobody reads.
- **Transfer held under a new library.** `Session` headers-once actually
  carried (key set once, never re-pasted); `merge()` is network-wins +
  cached-only-kept + sorted-by-id with `kept` derived; `match` with `case _`
  reused unprompted. No GenAI this lesson — translator + Google-for-syntax
  only — which fits: L19 mirrors L18's wire, so unaided solving *is* the
  transfer evidence.
- **Fix loop was root-cause grade.** All 5 review findings were explained
  correctly first ("I thought not-a-str meant empty string", "I auto-drive
  exception handling from habit, not the spec") and fixed independently in
  one round — including stripping the invented branches rather than
  defending them.

## Bucket Score

Total = 96/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 25 | All blocks byte-exact, all suites green, contracts honored post-fix. E2 `timeout=3` vs spec `timeout=5` retained-with-reason (lesson-standard value, unobservable behavior) — no deduction. |
| Logic (20) | 20 | Merge/override semantics, guard-`or`, handler ordering, status-vs-body decisions — all correct after the fix round. |
| Readability (15) | 14 | Small single-purpose functions, consistent shape. −1: no module/function docstrings anywhere (L15+ habit regressed). |
| Naming (10) | 10 | `fresh`/`kept`, `network_ids`, `fetch_with`, `probe_timeout` — meaningful and consistent. |
| Maintainability (10) | 10 | Invented untested branches removed rather than kept; `merge`/`load`/`save`/`main` split is the right CLI shape. |
| Pythonic style (10) | 9 | `match`, pathlib, DictWriter, `from exc` chaining restored. −1: `save_csv` hand-rolls a `written` counter loop where `writerows(items)` + `len` is idiomatic. |
| Testing (5) | 4 | Provided suites green (7/7); drivers all byte-exact. −1: no learner-authored tests (none required by spec — noted, not punished beyond the point). |
| Performance (5) | 5 | No premature optimization; `Session` reuse is the right level of efficiency thinking. |

- **Hint dependency:** 0 for exercise solving (Quick Recall 6/6 unaided;
  E1–M3, H1, H2, Challenge solved independently; translator = language aid,
  Google = syntax recall). Level 1 during the review-fix loop (diagnostic
  findings guided fixes; learner implemented).
- **Independent-fix ratio:** 5/5 review findings fixed by the learner
  unaided, same session. Nothing assisted, nothing retained-with-reason
  except the E2 timeout value (documented above).
- **Spec-literalness:** all Output blocks byte-exact throughout; first-draft
  drift lived only on untested paths (return-type lies, derived header,
  truthiness guard) — the OPEN watching thread, with fresh evidence below.

## Reviewer notes

- **Misconception evidence this lesson:** (a) guard-`or` (WP2 OPEN) — Q6
  stated correctly, first-draft code tested truthiness instead of type,
  fixed to `isinstance... or ...` — stays OPEN (explained ✓, independent
  avoidance in new code still pending); (b) latent sample-passing bugs
  (OPEN) — `post_json`/`search` passed every driver while breaking their
  annotations, this time by *over*-handling rather than under-implementing;
  (c) spec-literalness (OPEN, watching) — first drafts follow habit
  ("auto-drive exception handling") over the stated contract; the fix was
  *removing* code, which is the right instinct to keep.
- **Builder feedback from the learner (logged for L20+):** H-drill driver
  cells print only `N passed` on success and a truncated tail on failure —
  during trials the cell output didn't surface the real failure. Future
  H drivers should print failing test names + short tracebacks, not just
  the count.
- **Housekeeping:** `__pycache__/` removed post-verification. `.venv/`
  (~99 MB) sits inside the lesson folder — lesson folders hold lesson
  files only; relocate the env (repo-level or user-level) and reinstall
  `requests` there.
- **Coverage check:** E1→Core 2 · E2→Core 3 (+L3 match) · E3→Core 3/5/6 ·
  E4→Core 3 · E5→Core 5/6 · M1→Core 5/6 (+WP2 guard) · M2→Core 4 ·
  M3→Core 2 (+L12 CSV) · H1→Pitfalls 1–3 + Core 2/5/6 · H2→Core 7 ·
  Challenge→Core 3/5 + L9/L11/L12 (+Stage-1 argv). All covered, none silent.
- **Label check:** E1–E5 Easy / M1–M3 Medium / H1–H2 Hard / Challenge —
  ID == Difficulty == table tier == notebook Type. PASS (11/11 specs carry
  Intent + Coverage).

## Verdict

Objective met: the learner re-platformed the whole L18 wire onto `requests`
without assistance, debugged a planted client traceback-first, and — the
most senior moment of the session — deleted working code that the spec
didn't ask for. **96/100, mastery 3→4**, hint dependency 0 (review loop
level 1). Next: Quiz 03 window (L17–L19) is open; WP3 window is open;
DSA Week 3 due next week.

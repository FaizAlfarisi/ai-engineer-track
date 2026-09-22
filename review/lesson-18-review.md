# Lesson 18 Review — HTTP & API Concepts

**Date:** 2026-09-22
**Score:** 93/100 (bucket-derived; see breakdown below)
**Topics:** URLs and their parts (`scheme://netloc/path/query`), HTTP as a
request/response conversation, status codes and error classes
(`HTTPError` ⊂ `URLError`), exception ordering, JSON + POST payloads,
`urlencode`, `timeout`, building a full client and server against a
shared `urllib` interface, a cache CLI merging network + disk results.
Tier: CORE (Stage 3).

---

## Strengths

- **Everything green, read-only verified.** H1 `4 passed`, H2 `3
  passed`, Challenge `2 passed` — all 9 suites green in the lesson
  folder with caches off (`PYTHONDONTWRITEBYTECODE`, `-p
  no:cacheprovider`), plus the reference pair. Quick Recall 6/6 first
  try, including the non-obvious one (`HTTPError` before `URLError`;
  the response-body-read-once trap).
- **H1 debug drill — root-cause quality.** The four planted bugs map to
  lesson.md's own "common mistakes" section (read-once-then-decode,
  exception ordering, missing `urlencode`, wrong dict key). The learner
  fixed them and each fix followed a traceback-driven diagnosis.
- **H2 store server is real engineering.** `StoreAPI` with
  `__enter__`/`__exit__`, a daemon serving thread, reset of the
  `ITEMS`/`NEXT_ID` globals per instance, and `_safe()` sweeping
  connection-reset races on abrupt client disconnect — the latter is a
  genuine production-grade touch beyond the lesson.
- **Challenge merge logic is correct under the "fresh/kept" contract.**
  `fresh = len(network)`, `kept = len(cached_ids - network_ids)`,
  network overrides cache, output sorted by `id`. Verified against the
  pin: `Cache: 5 items (fresh 4, cached 1)`.
- **Self-fixing loop under review**: 2 of the first 3 review findings
  were fixed before recheck, and the `--refresh`-missing-flag case now
  exits `1` with a usage line into stderr. 90-second habit actually
  held.

## Bucket Score

Total = 93/100.

| Bucket (max) | Score | Note |
|--------------|-------|------|
| Correctness (25) | 23 | All blocks byte-exact, all suites green. −2 for the H2 exported-interface deviation: spec demands `store_server.start(port=0)`; the delivered module exports a `StoreAPI` class instead. Behavior is correct; the required symbol is absent (see Reviewer notes). |
| Logic (20) | 20 | Merge/override semantics, validation gates, server routing — all correct under edge cases tested. |
| Readability (15) | 14 | Clear docstrings, helpers (`_safe`, `_reply`, `_read_json`) carry intent. −1: `cache_cli` `main()` mixes orchestration and I/O (acceptable for a CLI; the merge helper is properly split). |
| Naming (10) | 10 | `fresh_count`/`kept_count`, `network_data`, `merge_dict` — all meaningful and consistent. |
| Maintainability (10) | 8 | `pathlib` + module functions make the CLI extensible; the context-manager server is drop-in swap friendly. −2: module globals `ITEMS`/`NEXT_ID` + `global` statements — workable only because one server runs at a time; the reference model shows the stateless-alternative with a module-level `start()` factory. |
| Pythonic style (10) | 8 | PEP 695 `type Item = ...`, tuple returns, `with` context managers. −2: `post_client.py:27` and `search_client.py:15` still use bare `except Exception` to swallow non-JSON error bodies — flagged as a nit, left by learner choice. |
| Testing (5) | 5 | 9 learner-authored tests across three suites + reference pair (12 total). |
| Performance (5) | 5 | No premature optimization; caching CLI is the right level of work. |

- **Hint dependency:** 0 for exercise solving (Quick Recall 6/6
  unaided; E1–M3, H1, H2, Challenge all solved independently). Level 1
  during the review-fix loop (diagnostic findings guided fixes; learner
  implemented).
- **Independent-fix ratio:** 7/8 review findings fixed by the learner
  unaided. The retained item (H2 interface shape) was a **deliberate,
  informed trade-off**, not a miss — see Reviewer notes.
- **Spec-literalness:** strong overall (all Output blocks byte-exact),
  with the single documented exception of the H2 exported symbol.

## Reviewer notes

- **H2 interface deviation — consequence applied.** The exercise
  contract (spec + `test_store.py` fixture in `exercises.ipynb`) calls
  `store_server.start(port=0)`. The learner's `store_server.py` exports
  `StoreAPI`. Full deduction was NOT applied because: (a) the behavior
  contract is fully met, (b) the learner's own `test_store.py` was
  written to their API and pins the same behavior, and (c) the deviation
  was made transparently and kept **by learner decision after the
  consequence was stated** — deduction on the interface criterion only,
  ~2 pts. The learner asked for an instruction-based reference that
  follows the contract verbatim without removing their work; delivered
  as **`store_server_ref.py` + `test_store_ref.py`** (reference only —
  `import store_server_ref`, spec-faithful `start(port=0)` + module-level
  `INVENTORY`). Both H2 suites pass side-by-side (6 passed), proving the
  class-based and factory-based designs are drop-in compatible with the
  same `store_client.py` — a genuinely good teaching artifact.
- **Connection-reset handling learned from run traces.** `_safe()` came
  from watching `BrokenPipeError`/`ConnectionResetError` during reads —
  real-world operability evidence, not theory.
- **Retained nits (learner's call):** bare `except Exception` in
  `post_client.py`/`search_client.py` (optional tighten). No default for
  `status_family` in `client_basics.py` — wait, this was fixed: `case _:
  return "?"` now in place; re-verified.
- **Housekeeping:** stray `cache.json`/`cache.csv`/`.pytest_cache`/
  `__pycache__` artifacts removed from the lesson folder after verified
  runs.

## Verdict

Objective met: the learner built both sides of an HTTP conversation from
`urllib`, debugged a planted client with traceback-driven discipline,
and — in H2 — made a *designed* engineering decision and defended it.
The only real gap is a spec-literalness one (exported symbol), handled
correctly: not by rewriting, but by producing a contract-faithful
reference side-by-side with their design. **93/100, mastery 3→4**, hint
dependency 0 (review loop level 1). Next: DSA #2 (Week 2, due) then L19
per stage isolation.
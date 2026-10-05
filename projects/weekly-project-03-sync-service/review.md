# Weekly Project 3 Review — Feed Sync & Report Service (Round 1)

**Date:** 2026-10-05
**Score:** 86/100 (see breakdown; review-assisted fixes priced in)
**Scope:** brief T1–T17 (+T7b/T10b amendments), SG1 + SG2 built, SG3
satisfied by design, decision log, test suite, mypy, git discipline.

---

## Matrix result (temp copy, post-fix verification)

- T1 `sync` seeded → `Sync: 5 items (fresh 4, cached 1)` ✓ (+ byte-exact
  `sync.json`/`sync.csv`, stale muffin overridden to 3.20)
- T2 `sync` empty → `Sync: 4 items (fresh 4, cached 0)` ✓
- T3 `report value` → 5-line + `Total: 197.20` block byte-exact ✓
- T4 `report low 10` → 2-line + `Low: 2 items` byte-exact ✓
- T5/T6 bad threshold → `bad request:` + detail, exit 1 ✓
- T7/T7b (AMENDED — graceful empty, WP2 precedent) → `Total: 0.00` /
  `Low: 0 items`, exit 0 ✓
- T8 no args → usage, exit 1 ✓
- T9 `bananas` → `bad request: unknown command 'bananas'`, exit 1 ✓
- T10 (AMENDED — retargeted to `sync`) → two-line
  `corrupt data:\nfailed to load existing data | <parser detail>` ✓
- T10b (NEW — wrong-shape cache) → `corrupt data:\nfailed to load
  existing data | bad record: {'foo': 1}`, no traceback ✓
- T11 (FIXED — `SYNC_API_BASE` wired) → env honored (log proves
  override path), `network error:` + pool detail, exit 1, no
  traceback ✓
- T12 `sync quiet` → pin exact, stderr EMPTY ✓
- T13 (FIXED — `%(levelname)s` in formatter) → pin exact, stderr
  contains `DEBUG` ✓
- T14 `pytest tests` → 5 passed ✓ (tmp_path ✓; caplog present —
  see notes)
- T15 (FIXED — Optional narrowing) → `mypy main.py` clean ✓
- T16 git: `.venv`/`*.log`/`sync.*` ignored, `requirements.txt`
  tracked ✓
- T17 restart survival ✓ (files persist across separate commands)
- SG1 `report summary` → pinned block byte-exact ✓
- SG2 `report restock 20` → pinned block byte-exact ✓
- SG3 `report.json` → parses, `items` + `total` fields ✓

## What was fixed in review (explicit learner consent)

1. `SYNC_API_BASE` wired into `api.get_items` (env override → own stub
   fallback; only own stub stopped).
2. `%(levelname)s` added to log formatter + `urllib3` silenced to
   WARNING (verbose stays ours).
3. Corrupt message prefixed (`failed to load existing data | …`) +
   two-line `corrupt data:` form in `main`.
4. Wrong-shape records → `CorruptDataError` (was raw `AttributeError`
   traceback).
5. `request.number is not None` narrowing (mypy clean).
6. `requirements.txt` rewritten UTF-8 LF (was UTF-16 BOM — WP2 scar).
7. `load_csv` warning moved to the module logger.
8. Frozen `Item` dataclass (L16 model, restored).
9. Brief amended with reason (T7 graceful-empty + T7b; T10 retarget +
   T10b; acceptance line) — spec-ownership rule, same-commit window.

## Strengths

- Real layered architecture with a written rationale (decision log row
  1–3 are genuinely reasoned, incl. the overengineering caveat).
- Perimeter decoding in two of three paths, typed errors end-to-end,
  readback discipline on reports, verbosity modes with a real journal
  file, `conftest`-less but `tmp_path`-genuine tests.
- Both stretches + SG3 mechanism built, all pins byte-exact.
- Six commits, meaningful milestones.

## Open items (learner's actions — NOT done for you)

1. **README** (brief deliverable, missing): how to run, what the
   reports mean, the `SYNC_API_BASE` override.
2. **Decision rows 4–5 + technical reflection**: rows 4 ("set positive
   case first, future repair") and 5 ("- / -") need real Why/Alternative
   content; reflection in template style.
3. **Caplog test honesty**: `test_logging_caplog` logs from a throwaway
   `"test"` logger — it proves pytest works, not your code. Rewrite it
   against YOUR logger (e.g. assert `safe`… assert the merge debug or a
   `storage` warning record via `caplog`), L17 rule.
4. Consider: `timeout=30` is generous for a local stub (works, but say
   why 30 in the log); `Request`/`number` Optional handling is now
   mypy-clean — keep it that way as you extend.

## Score

**86/100** — code-verified strong post-fix; priced for review-assisted
implementation (6 load-bearing touches incl. T11/T13/T15 enablers),
missing README/reflection, thin decision rows, and the vacuous-adjacent
caplog test. The architecture and all feature work are yours; the
listed items are the documented gap to the 90s.

## Round 2 close-out (2026-10-06)

- Learner delivered: README, decision rows 4–6 (incl. timeout rationale),
  honest caplog rewrite (own logger), original-result disclosure accepted.
- No new deductions found; score stands at **86/100**.
- Still open, recorded without penalty: Q2 detection-story (which run or
  re-read caught the `Low:` colon and `>= 0`?) — unanswered at close.

## Learner reflection (non-template, learner's words condensed)

1. Hardest failure: dataclass + mypy consistency across layers — first
   time using dataclass as entity with mypy over a real data flow;
   the mechanical type agreement was the struggle.
2. (Open — see above.)
3. Transfer: testing, requests (still needs a glance before independent
   use), structure (researched for client work), logging — automatic;
   typed entities still lookup-dependent.
4. Time: ~1h/day across a week (~6–7h effective); re-ramp cost each
   sitting (remembering + strategizing before producing) plus confusion
   plus time management. Mentor's rule back: smaller done-states per
   sitting to stop paying context-reload twice.

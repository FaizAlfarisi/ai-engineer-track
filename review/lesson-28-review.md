# Lesson 28 Review — Asyncio (AWARENESS, collapsed)

**Score:** closed on recognition evidence — no bucket sum (the tier's
own law: inflating a collapsed lesson would silently promote the
topic). **Bar: MET.** No 95+ claim is made, because the collapsed bar
is Level-2 recognition, not a percentage.

## Strengths

1. **Memory-first held.** Both E1 snippets were predicted *before* any
   run, and both were correct: snippet 1 (`coroutine` / `HELLO`,
   created-not-run until `await`), snippet 2 (~1.5s serial because
   `time.sleep` blocks the single thread).
2. **E2 is real gather work, not sequential-awaits-in-disguise.** The
   results came back in argument order *and* under the concurrency
   timing pin — the two properties that distinguish "fan-out" from
   "three awaits in a for-loop".
3. **Best judgment answer of the session (reflection Q2).** "Not a
   magic script... adds complexity... might overengineer" plus an
   independent reach for the blocking rule. That is senior instinct,
   not recall.
4. **Correct diagnosis of the notebook-vs-terminal gap.** Faced with
   `asyncio.run() cannot be called from a running event loop`, the
   learner re-ran in a terminal rather than guessing at a code fix.

## Evidence table

| Evidence | Verdict |
|---|---|
| Quick Recall 1–4 | 4/4 answered; 2 sharpenings ledgered (switch point is `await` not "the loop"; FastAPI named as Stage-4 payoff) |
| E1 predictions vs observed | both match, pre-run |
| E2 `fanout.py` | green (order + timing pin) |
| Reflection Q1 (when-to / when-not) | pass — API fan-out vs small CLI + CPU-bound |
| Reflection Q2 (blocking rule) | pass, best of session |
| Reflection Q3 (confidence) | 4/4, backed by the E1 evidence |

## Findings

- **None against the learner.** No exercise-level miss, no
  driver-invisible bug, no spec slip.
- **Builder concession (no deduction to the learner).** My E2 driver
  called `asyncio.run()` in-kernel, which cannot run inside a
  Jupyter notebook that already has a live event loop. The learner hit
  the error, correctly moved to a terminal, and got `E2 OK`. My E1
  driver wrapped its snippets in `subprocess` (works anywhere); the E2
  driver should have done the same. Filed for the next build pass.

## Note for the record

The observed-vs-predicted "Observed" block initially overwrote the
learner's cell-4 question during the save; both were restored
(question preserved, Observed re-homed to its own cell). Nothing was
lost, and the notebook ships with both intact.

## Hint dependency

0 — solved independently; the only guidance was the two QR sharpenings
(mentor-issued after the answers, per the memory-first law).

---
Closed 2026-10-20. Stage 3's last concept-shaped lesson is done; async
lands in Stage 4 (FastAPI) as the practical payoff.

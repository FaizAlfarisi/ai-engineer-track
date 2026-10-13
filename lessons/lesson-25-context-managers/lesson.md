# Lesson 25 — Context Managers (Tier: SUPPORTING)

Stage 3, ninth topic. You have typed `with open(...)` since Lesson 9
without ever being told what `with` *is*. This lesson pays that
two-stage-old debt: the protocol behind the keyword, authored two ways —
and the triple-twin moment where three prior lessons meet in one `@` line.

SUPPORTING tier — Level 3 bar: implement the protocol independently and
use it on real resources. One focused sitting, then the pattern
transfers into the Stage project (atomic publishes, timed sections,
leak-proof pipelines) and every guarded resource after it.

Business domain for this lesson is fresh: the dawn report publisher. No
telemetry, no logs-as-data, no clinic. New business, same engineering
discipline.

---

## Objective

By the end of this lesson you can:

- State the protocol: `__enter__` runs on block entry (its return binds
  the `as` target), `__exit__` runs on every exit path — clean,
  exception, `return`, `break`.
- Write a class-based context manager with honest `__enter__` /
  `__exit__`, including the suppress-vs-propagate return contract.
- Write the same guard as a `@contextmanager` generator, and explain
  where the setup, yield, and teardown live.
- Publish files atomically (temp + replace on success, discard on
  failure) so reports are whole or absent, never half.
- Time guarded blocks, including blocks that raise.
- Name `ExitStack`, `redirect_stdout`, and async CMs as deliberate
  omissions — recognized, not drilled.

---

## Why This Matters

The dawn publisher writes the incident report at 5 AM. Last Tuesday the
disk filled mid-write; the job died on page 40 of 80. The reader opened
the report at 6 AM and trusted it — forty pages presented as the whole
truth. Nobody was paged. The incident review found the gap in one
sentence: *a half-file is worse than no file, because no file alarms
and half a file reassures.*

Version 1 is written the obvious way: open the target, write lines,
close at the end. Every hardening repeats the shape: `try/finally`
works, but every call site re-implements it and forgets once. `with
open()` auto-closes the handle — but closing a half-written file still
leaves a half-written file. None of the previous tools can make
*replacement* atomic.

What capability do we need? A block with guaranteed exit work — close,
discard-or-commit, record the time — no matter which path leaves the
block: clean finish, exception, early `return`, loop `break`.

What feature provides it? The context-manager protocol: `__enter__`
acquires (and hands back the working object), `__exit__` settles
(commit or discard, record, then choose propagate-or-suppress). The
`with` you have typed since L9 is this machine; today you meet it.

Practical consequence — what breaks without it? The suppressed-error
variant: an `__exit__` that returns truthy *swallows* the failure, the
job reports success, the half-file stands. Silent green, missing
report — the latent class of this lesson, and the H1 drill plants
exactly it.

Urgency, stated plainly: every report you have shipped since Lesson 9
writes direct to its target. The fleet, the clinic, the greenhouse —
all of them can serve a half-file today. This lesson retrofits every
one of them with a ten-line guard. Whole or absent, never half.

Deliberate omissions: `ExitStack` (dynamic guard counts — real,
deferred to keep this lesson tight); `redirect_stdout` and friends
(sightings only); async context managers (deferred to Asyncio).

---

## Mental Model

A context manager is a **booked venue with a cleanup crew that shows
up however the party ends**.

```text
with AtomicWriter(path) as draft:     # __enter__: book the venue,
    draft.write(...)                   #   hand over the scratch room
    draft.write(...)                   # BODY: the party
                                       # __exit__: crew arrives ALWAYS —
                                       #   clean finish → move scratch
                                       #     room onto the stage (replace)
                                       #   exception    → demolish scratch
                                       #     room, re-raise (propagate)
                                       #   return/break → crew still comes
```

Three rules run everything:

1. `__enter__`'s return value binds the `as` target — bind the wrong
   object and the body works on a stranger.
2. `__exit__` runs on *every* exit: clean, exception, `return`,
   `break`. There is no path out that skips it.
3. On exception, `__exit__` votes: falsy return (or `None`) re-raises
   to the caller; truthy return *swallows* the error and execution
   continues after the block. Most swallowing is a bug wearing a
   feature's clothes.

A `@contextmanager` generator is the same venue in five lines:
everything before `yield` is the booking, the yielded value is the
scratch room, everything after (ideally in `finally`) is the crew.

---

## Core Concept

### 1. The protocol: `__enter__` acquires, `__exit__` settles (L8's debt, paid)

Problem: L8 promised this mechanism for File Handling; L9 taught only
its use (`with open(...)`). You have operated the machine for fifteen
lessons without seeing it.

Why use-alone is insufficient: use teaches *that* cleanup happens, not
*where to put yours*. Custom exit work (commit-or-discard, timing,
lock release) has nowhere to live until the protocol is explicit.

Capability needed: a named place for setup and a guaranteed place for
teardown, per guarded block.

Feature: a class with `__enter__(self)` and `__exit__(self, exc_type,
exc_value, traceback)` — the triple is `None, None, None` on a clean
exit, the live exception otherwise.

```python
class Timer:
    """Record wall time of a block, even when it raises."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False          # propagate: timing observes, never hides
```

Consequence of missing this: every new guard re-derives `try/finally`
by hand, and the one forgotten site is the 5 AM incident.

### 2. Exit runs on every path (the guarantee that earns the name)

Problem: "cleanup at the end of the block" reads as "the last line" —
then a `return` or `break` or raise skips the last line and the
cleanup with it.

Why `try/finally`-by-hand is insufficient at scale: correct once,
forgotten once per dozen call sites. The guarantee must belong to the
construct, not to the author's memory at each site.

Capability needed: exit work that no exit path can dodge.

Feature: the interpreter calls `__exit__` on clean finish, on
exception (with the live triple), on `return` (triple `None`s, value
carried past), and on `break`/`continue` (triple `None`s). Proof you
run in E3 with a record list — every path appends.

Consequence of missing this: resource leaks that only manifest on the
rare path (the error path is exactly the untested one).

### 3. Suppress vs propagate: the return vote (the loaded gun)

Problem: sometimes the block's error is *handled* at the boundary (a
missing optional cache file means "rebuild", not "crash") — and
sometimes it must scream. Both flow through the same `__exit__`.

Why a bare `except: pass` is insufficient: it hides at the wrong
layer, far from the resource, with no record. Suppression belongs to
the guard that owns the resource, stated deliberately.

Capability needed: per-guard, per-decision error policy.

Feature: return truthy from `__exit__` to swallow (execution resumes
after the block), falsy/`None` to re-raise. The default posture —
and this lesson's standing rule — is **propagate**: observe everything,
hide nothing, suppress only named exceptions with a stated reason.

```python
def __exit__(self, exc_type, exc_value, traceback):
    if exc_type is None:
        self.commit()
    else:
        self.discard()
    return False    # the error, if any, continues to the caller
```

Consequence of missing this (Pitfall 1, H1 plants it): a truthy
return somewhere innocent swallows a real failure; the job reports
success and the incident never pages.

### 4. `@contextmanager`: the triple-twin (L22 × L24 × L23 in one line)

Problem: the class protocol is honest but heavy — fifteen lines of
dunders for a guard whose idea is three sentences (start timer, hand
over, record time).

Why a helper function is insufficient: plain helpers cannot inject
exit work into the caller's block. The teardown must be *attached* to
the block, not called after it (after-it is exactly what exceptions
skip).

Capability needed: author setup/teardown as straight-line code with
one marked handover point.

Feature: `contextlib.contextmanager` (taught here — first use in E2):
write a generator function, `yield` exactly once (the yielded value
binds `as`), put teardown after the `yield`, preferably in `finally`
so a throw-in still cleans up:

```python
from contextlib import contextmanager

@contextmanager
def timed():
    """Elapsed time of a block, on any exit path."""
    start = time.perf_counter()
    outcome = {"elapsed": 0.0}
    try:
        yield outcome          # handover: body runs here
    finally:
        outcome["elapsed"] = time.perf_counter() - start
```

Consequence: L22's decorator + L24's suspension + L23's protocol in
five lines. Recognize the shape whenever setup/teardown pairs appear —
it is almost always the right tool, and almost never a class.

### 5. Atomic publish: temp + replace-or-discard (the assessable skill)

Problem: direct-to-target writes leave half-files on any mid-write
death — and readers cannot tell half from whole.

Why closing is insufficient: a closed half-file is still a half-file.
Durability of the *bytes* was never the gap; atomicity of the
*replacement* is.

Capability needed: the target path changes from old-whole to
new-whole in one indivisible step, or not at all.

Feature: write the full report to a temp sibling, then — only on
clean exit — replace the target with it (`Path.replace`, taught here:
atomic on one filesystem); on any exception, delete the temp and
propagate. Readers ever see whole or absent, never half.

```python
with AtomicWriter(target) as draft:
    draft.write(header)
    draft.write(body)     # death here → temp demolished, target untouched
# clean exit ONLY → temp becomes target in one step
```

Consequence of missing the discard branch: failed publishes leave
orphan temps that the next run mistakes for reports.

### 6. The `as`-target contract (small print, real bugs)

Problem: `with Timer() as t:` then `t.elapsed` explodes with
`AttributeError` — because `__enter__` returned `None` (or the wrong
object) and `t` bound that.

Why it surprises: the `with ... as` line *looks* like assignment from
the constructor. It is assignment from `__enter__`'s return.

Capability needed: bind deliberately — return the working object
(`self`, the timer record, the open draft).

Feature: `return self` (or the record dict) as the last line of
`__enter__`. For `@contextmanager`, the *yielded value* binds `as` —
yield the record, never `None`, when the body needs it.

Consequence of missing this (Pitfall 3, H1 plants it): bodies
operating on `None`, failing far from the one-line cause.

---

## Practical Examples

Example A — class-based timer (E1 is this, specified exactly):

```python
import time

class Timer:
    """Elapsed wall time of a block; propagates whatever the block raised."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False
```

Example B — the twin in five lines (E2 is this):

```python
from contextlib import contextmanager

@contextmanager
def timed():
    """Elapsed wall time of a block, on any exit path."""
    record = {"elapsed": 0.0}
    start = time.perf_counter()
    try:
        yield record
    finally:
        record["elapsed"] = time.perf_counter() - start

with timed() as t:
    work()
print(t["elapsed"])
```

Example C — atomic publish, the whole pattern (M1 specified exactly;
naming: temp sibling, replace on clean, demolish on error):

```python
from pathlib import Path

target = Path("report.txt")
draft = target.with_suffix(".tmp")
try:
    draft.write_text(full_text, encoding="utf-8")
except Exception:
    draft.unlink(missing_ok=True)
    raise
draft.replace(target)      # one atomic step, clean path only
```

(`Path.replace` and `Path.unlink(missing_ok=True)` are taught here —
first use in M1. `with_suffix` for the temp sibling likewise.)

---

## Engineering Notes

- **Propagate by default.** `__exit__` returns falsy unless a *named*
  exception is deliberately swallowed with a stated reason in a
  comment. Unexplained truthy returns are review findings.
- **Exit work must be exception-safe itself.** Teardown that can raise
  (a second I/O inside `__exit__`) masks the original error — keep
  teardown to operations that cannot fail, or guard them.
- **One guard, one resource.** Timer times; publisher publishes. A
  `TimedAtomicPublishingLogger` is the mega-decorator trap in new
  clothes — compose by nesting `with` blocks.
- **Temp siblings live beside the target** (same directory, same
  filesystem — otherwise replace is not atomic). Name them
  recognizably (`report.tmp`, never hidden dots).
- **Generators holding handles meet their owners here.** A streaming
  generator over an open handle should be consumed *inside* the
  `with` that opened it — or wrapped so the owner closes it. Full
  resource discipline, no dangling cursors.
- **Annotate the two roles.** `__enter__` returns the working type;
  `__exit__` returns `bool | None`:

```python
def __enter__(self) -> "Timer": ...
def __exit__(self, exc_type: object, exc_value: object,
             traceback: object) -> bool: ...
```

- **When NOT a context manager:** a value needed twice wants a plain
  variable; branching logic wants `if`; a one-call script helper wants
  a function. `with` is for *guarded spans*, nothing else.

---

## Common Pitfalls

1. **Truthy `__exit__` swallowing real errors** — job reports success,
   incident never pages. Propagate unless named + justified.
2. **Temp leaked on the exception path** — no discard branch; orphan
   temps pile up and confuse the next run.
3. **Wrong `as`-target** — `__enter__` returns `None` (or the wrong
   object); the body fails far from the cause.
4. **`yield` without `finally` in a generator CM** — a throw-in skips
   teardown; the guard holds only the happy path.
5. **Direct-to-target writes** — the original sin this lesson retires;
   any new direct write is a regression to pre-L25 habits.
6. **Forgetting the protocol is per-block** — one guard instance
   reused across two `with` blocks shares state (timers accumulate,
   drafts collide). Fresh guard per span, or reset in `__enter__`.

---

## Connection to Previous Knowledge

- **Exception handling (L8):** the debt paid — `finally` semantics now
  belong to the construct; per-item boundary validation unchanged.
- **File handling (L9/L10):** `with open()` finally explained; Path
  I/O stays Path-first with `encoding="utf-8"` everywhere.
- **Decorators (L22):** `@contextmanager` *is* a decorator — stacking
  and transparency rules apply; now in Tool Sync, freely composable.
- **Iterators/Generators (L23/L24):** the generator CM suspends and
  resumes exactly per the pull clock; streaming generators get
  consumed inside their owner's `with`.
- **Project structure (L20–L22 house):** Challenge keeps `main(argv)`
  (full `sys.argv`) + guard, no module-level executable code.
- **Spec-literalness (standing watch):** every Driver must match its
  Expected block byte-exact.

---

## Quick Recall

Answer from memory before coding:

1. Your L24 harvest generator holds an open handle; the consumer
   `break`s mid-loop. Who closes the handle today — and what construct
   from this lesson takes that job?
2. A `with` block raises, returns early, and `break`s in three runs.
   Which method runs in all three, and what three values can its
   exception triple take?
3. `__exit__` returns `True`. The block raised `ValueError`. What does
   the caller see next — the error, or the line after the block? When
   is that the right choice?
4. `@contextmanager` function: which lines run at `__enter__` time,
   what does the `yield` bind to, and which lines must sit in
   `finally`?
5. `with Timer() as t:` then `t.elapsed` raises `AttributeError`. Which
   method is at fault, and what single line fixes it?
6. A publisher writes direct to target; a crash lands mid-write. Whole,
   absent, or half — and which two operations replace the direct write?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is the dawn report publisher throughout. Full specs live in
`exercises.ipynb`; write each deliverable in its stated file (R16 —
no `solution.py`, no double-write), then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | class-based `Timer`: elapsed on every path, propagate |
| E2 | Easy | [REAL-WORLD] | `@contextmanager` twin + frozen-body timing note |
| E3 | Easy | [REAL-WORLD] | exit-runs-always proof (break/return/raise) + missing-file edge |
| M1 | Medium | [REAL-WORLD] | `AtomicWriter` class: temp + replace-or-discard |
| M2 | Medium | [REAL-WORLD] | learner-composed timed publish (no partial on failure) |
| H1 | Hard | [DEBUG] | 4-plant hunt: swallow, leak, wrong target, bare yield (+ 7-row chain each) |
| Challenge | Micro Build | [REAL-WORLD] | atomic publish CLI: Flow, house entry, byte-exact + absent-partial proof |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): the protocol implemented
independently both ways, atomic publish correct on both exit paths,
the H1 hunt resolved with four 7-row chains, the Challenge running as
an atomic publish pipeline with byte-exact output.

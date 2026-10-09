# Lesson 23 — Iterators (Tier: SUPPORTING)

Stage 3, seventh topic. You already stream files line-by-line (L9) and
decorate pipelines (L22). This lesson gives you the machinery underneath
streaming: pulling items one at a time from anything, without loading it.

SUPPORTING tier — Level 3 bar: use the protocol independently on real
streams. One focused sitting, then the pattern transfers into the Stage
project (paged feeds, chunked processing) and the Generators lesson.

Business domain for this lesson is fresh: night-shift server-log triage.
No clinic, no expenses. New business, same engineering discipline.

---

## Objective

By the end of this lesson you can:

- Pull items with `iter()` / `next()` and terminate cleanly on
  `StopIteration` (including the `next(it, default)` form).
- Tell an iterable (re-readable source) from an iterator (one-shot
  cursor) with the `iter(x) is x` check, and predict what a second pass
  prints.
- Explain why `if stream:` never guards emptiness, and replace it with
  an attempted pull.
- Write a custom iterator class (`__iter__` / `__next__`, own cursor)
  that batches any stream into fixed-size windows.
- Annotate stream code honestly with `collections.abc.Iterable` and
  `Iterator`.
- Say when iteration is right vs loading a list — and name `yield`
  (next lesson) and `itertools` (sighted, not drilled) as deliberate
  omissions.

---

## Why This Matters

The 2 AM alert says the triage job died. The morning report never came.
The cause: last month's 400 MB access log became this month's 40 GB
one, and the job starts with `lines = handle.readlines()` — the whole
file hoarded in RAM before a single line is inspected. The machine OOMs
at 2:07 every night.

Version 1 is written the obvious way: load all, slice some, loop the
rest. Every fix repeats the shape: `readlines()` hoards, slicing copies,
and every helper still needs the whole data in hand before it starts.
The business logic (find ERROR lines, batch them, report) is 10 lines;
the loading scaffolding decides whether the job lives or dies.

Why are the previous tools insufficient? A plain helper call cannot fix
it — `first_n(all_lines, 50)` still builds `all_lines` first. Slicing
cannot fix it — `lines[:50]` copies from a hoarded list. A `with` block
helps lifetime, not volume.

What capability do we need? Consume a stream one item at a time, pausing
between pulls — never holding more than the current handful.

What feature provides it? The iterator protocol: `iter()` hands you a
cursor, `next()` pulls one item, `StopIteration` says the belt is empty.
The body of the triage job never sees more than one window at a time.

Practical consequence — what breaks without it? The report silently
covers half the log: somebody loops a file handle twice (once to count,
once to collect), and the second pass reads nothing — zero errors,
zero warnings, half the incidents missing. That is the latent-bug class
of this lesson, and the H1 drill plants exactly it.

Urgency, stated plainly: the log grows every week and the job must run
in constant memory by Friday. Without iterators you buy a bigger
machine. With them you change ten lines. This lesson is what makes the
second option real.

Deliberate omissions: `yield` and generator functions (the entire next
lesson — same protocol, different authoring); the `itertools` toolbox
(`islice`, `chain`, `tee` — shown once as a PROVIDED sighting, never
required); async iteration (deferred to Asyncio).

---

## Mental Model

An **iterable** is the belt. An **iterator** is the finger pointing at
"next item".

```text
iterable (list, file handle, WindowReader source)
  ──iter()──▶  iterator (cursor: "next is item #k")
                  ──next()──▶  item #k, finger moves to #k+1
                  ──next()──▶  ...
                  ──next()──▶  StopIteration  (belt empty)
```

Two rules run everything:

1. `iter()` on an iterable makes a NEW cursor each call. `iter()` on an
   iterator returns the SAME cursor (`iter(it) is it`).
2. A consumed cursor never refills. A second pass over the same cursor
   reads nothing — silently.

A `for` loop is just this machine with the crank automated: call
`iter()` once, `next()` until `StopIteration`, which the loop swallows
quietly. Every surprise in this lesson is that machine misread.

---

## Core Concept

### 1. `iter()` / `next()` / `StopIteration` (the only machinery)

Problem: list code uses indexes (`lines[i]`, `i += 1`). Indexes assume
length, support re-reads, and go off-by-one under manual control.

Why indexes are insufficient: a file handle has no length and no
`[i]`; a network page has no end in sight. Index thinking cannot even
start.

Capability needed: one uniform "give me the next item" operation that
works on every stream shape, plus one uniform "we're done" signal.

Feature: `it = iter(stream)` then `next(it)` per pull; exhaustion
raises `StopIteration`. The two-argument form `next(it, default)`
returns `default` instead of raising — use it wherever "empty" is a
normal outcome, not an error.

```python
it = iter(["INFO up", "ERROR disk full"])
next(it)          # "INFO up"
next(it)          # "ERROR disk full"
next(it, None)    # None — no crash, stream simply ended
```

Consequence of missing this: hand-rolled cursors with `IndexError`
where a stream has no indexes at all.

### 2. Iterable vs iterator (the distinction that decides re-reads)

Problem: the triage job counts lines, then collects errors — two passes
over "the same data". The second pass prints nothing. No error. Why?

Why "just loop it again" fails: the second loop received the same
*cursor*, not the same *data*. A cursor is one-shot by construction.

Capability needed: tell re-readable sources from one-shot cursors on
sight, before writing the second loop.

Feature: the `iter(x) is x` check. A fresh cursor each call means
iterable (list, file path target, `enumerate` object source… precisely:
anything whose `__iter__` builds anew). The identical object back means
iterator (file handles, `map` objects, your `WindowReader`, anything
with `__next__`).

```python
data = ["a", "ERROR: x"]
iter(data) is data          # False — iterable, re-loopable
it = iter(data)
iter(it) is it              # True — iterator, one-shot
```

Consequence of missing this (Pitfall 2, H1 plants it): the count is
right and the body is empty, every driver that checks only the count
stays green.

### 3. Exhaustion is forever + the truthiness trap

Problem: before pulling, the job wants to ask "is there anything?"
`if stream:` reads naturally — and is always `True`. Iterator objects
define no emptiness; Python defaults every object to truthy.

Why a guard cannot fix it: there is no cheap emptiness probe for a
stream — looking costs a pull. Any boolean test answers a question
nobody asked.

Capability needed: attempt the pull, handle the empty outcome as data.

Feature: `first = next(it, None)` — `None` (or your sentinel) means
"stream was empty", no exception, no lie. Where emptiness is an error,
validate after the pull (`E3`), never before it with a boolean.

Consequence of missing this (Pitfall 1, H1 plants it): a dead guard
that passes review because it "looks careful" while proving nothing.

### 4. The `for` desugar (what the loop has been doing all along)

Problem: `for line in handle:` feels atomic — until it must be
customized (skip N, stop early, interleave two streams) and nobody knows
which parts can be taken over.

Why it matters: every manual loop you write replays this machine; every
bug in this lesson is one of its steps skipped.

Feature, stated once:

```python
for line in stream:          # means EXACTLY:
    ...                      #   it = iter(stream)
                             #   while True:
                             #       try: line = next(it)
                             #       except StopIteration: break
                             #       ...
```

Consequence: `break`/`continue` are just early exits from that hidden
`while`. Nothing about `for` is magic — which is why a `__next__`
that returns `None` instead of raising (Pitfall 3) hangs it forever.

### 5. Custom iterator class (the assessable skill)

Problem: batching logic scattered across the job — every consumer
re-implements "collect N, emit, repeat, keep the ragged tail".

Why a helper function is insufficient: the batcher has *state* (the
cursor, the size) that must survive across pulls and be testable in
isolation. A closure could hold it, but a class names it, types it,
and lets two independent readers coexist.

Capability needed: a stream source that IS an iterator of windows.

Feature: a class with `__iter__` (return the cursor — `self`, for a
one-shot reader) and `__next__` (pull up to `size` items, `raise
StopIteration` when the source is dry *before* the first pull of a
window; emit the partial tail as a real window).

```python
class WindowReader:
    """Yield successive fixed-size windows (lists) from any iterable."""

    def __init__(self, source, size):
        if not isinstance(size, int) or size < 1:
            raise ValueError("window size must be >= 1")
        self._cursor = iter(source)
        self._size = size

    def __iter__(self):
        return self

    def __next__(self):
        window = []
        try:
            for _ in range(self._size):
                window.append(next(self._cursor))
        except StopIteration:
            pass
        if not window:
            raise StopIteration
        return window
```

Consequence of missing the tail rule: the last 2 lines of a 3-window
log vanish — correct on every evenly-divisible sample, wrong in
production (latent again).

### 6. Lazy batching posture (the engineering payoff)

Problem: even with windows, `list(reader)` at the end hoards again —
the job is constant-memory only if NOTHING downstream materializes.

Why it matters: laziness is a whole-pipeline property. One `list()` in
`main` silently converts your streaming job back into a loading job.

Feature: consume window-by-window to the very edge (format → write per
window, or collect only the small outputs — incident lines, not log
lines). The report holds incidents; incidents are small; the log is
not.

Consequence: memory follows the largest *kept* object, never the
largest *seen* one. State it in review or lose the point of the lesson.

---

## Practical Examples

Example A — `take(n, stream)`: the first N without storing (E1 is this,
specified exactly):

```python
def take(stream, n):
    """First n items as a list; fewer when the stream is short."""
    if n < 0:
        raise ValueError("take needs n >= 0")
    out = []
    it = iter(stream)
    for _ in range(n):
        item = next(it, None)  # sentinel form — see sentinel note below
        ...
```

(Sentinel honesty: `next(it, None)` conflates a real `None` item with
exhaustion. For log lines — never `None` — the form is safe and
readable; the lesson's streams are strings, so the simple form stands.
A `try/except StopIteration` variant is shown for streams that may
legitimately contain `None`. Both are taught; E1 uses the `try`
variant so the sentinel caveat never bites graded code.)

Example B — streaming a real file handle (L9 retrieval, now with
understanding):

```python
from pathlib import Path

path = Path("server.log")
with path.open(encoding="utf-8") as handle:
    it = iter(handle)
    print(iter(it) is it)   # True — the handle is a one-shot cursor
    first = next(it, None)  # one line pulled, rest untouched
```

Example C — the `__iter__`-returns-self contract, both directions:

```python
r = WindowReader(["a", "b", "c"], 2)
iter(r) is r        # True — one-shot reader
list(r)             # [["a", "b"], ["c"]]
list(r)             # [] — consumed; make a new reader, never reuse
```

PROVIDED-only sighting (never required): `itertools.islice(stream, n)`
does what `take` does, battle-tested. Recognize it in real code; this
lesson builds the intuition by hand first.

---

## Engineering Notes

- **One-shot discipline.** Never pass a consumed iterator a second lap.
  Need two passes? Materialize once (`items = list(stream)`) and derive
  both answers — say so in a comment, so the next reader knows the
  memory trade was deliberate.
- **Validate at the boundary, per item.** Streams carry rot (blank
  lines, truncated writes). Check each pull where it enters, with exact
  messages — L8 habits, unchanged.
- **Let `StopIteration` speak only from `__next__`.** Catch it
  everywhere else (`next(it, default)` or `try`); a stray `StopIteration`
  escaping a helper reads as a crash, and inside generators (next
  lesson) it becomes one.
- **Annotate the two roles differently.** `Iterable[str]` = "I can be
  re-read"; `Iterator[str]` = "I am a cursor" (both from
  `collections.abc`, taught here — first use in M1):

```python
from collections.abc import Iterable, Iterator

def take(stream: Iterable[str], n: int) -> list[str]: ...
def drain(stream: Iterator[str]) -> list[str]: ...
```

- **When NOT to iterate:** a small, reused lookup table wants a `list`
  or `dict`, not a stream. Iteration buys constant memory; it costs
  re-readability. Pay only when the data is big or arrives over time.
- **When a decorator-shaped problem appears:** cross-cutting wrappers
  (`log`/`timed`, L22, now in Tool Sync) compose with streams freely —
  decorate the consumer, never the cursor.

---

## Common Pitfalls

1. **Truthiness guard on a stream** — `if stream:` / `if not stream:`
   proves nothing; iterators are always truthy. Attempt the pull.
2. **Second pass over a consumed iterator** — silently empty. Count
   right, body missing, count-only drivers green.
3. **`__next__` returning `None` instead of raising** — `for` never
   terminates; the job hangs, it doesn't crash.
4. **Shared cursor** — class-level (or single shared) cursor across
   instances: two readers interleave into each other's data. Cursors
   live on `self`, never on the class.
5. **Dropping the ragged tail** — full windows emitted, final partial
   window forgotten. Passes every evenly-divisible sample.

---

## Connection to Previous Knowledge

- **File handling (L9):** `for line in handle` was streaming before you
  knew the word — now you know the machine. Handles are one-shot
  cursors: the L9 two-pass tail trick re-read the file for exactly this
  reason.
- **Exception handling (L8):** boundary validation per item, exact
  messages, `StopIteration` as the one exception that *signals* rather
  than *fails*.
- **Typing (L14):** `Iterable` vs `Iterator` joins the honest-annotation
  habit — the annotation now states re-readability, a runtime property.
- **Decorators (L22):** in Tool Sync, freely composable; the Challenge
  stays undecorated on purpose (streams are the star, no double
  mechanisms).
- **Project structure (L20):** Challenge keeps `main(argv)` (full
  `sys.argv` house shape) + guard, Path-first I/O, no module-level
  executable code.
- **Spec-literalness (standing watch):** every Driver must match its
  Expected block byte-exact.

---

## Quick Recall

Answer from memory before coding:

1. What does `iter()` return for a list vs for an iterator — same call,
   which two different answers, and why?
2. Why is `if stream:` useless as an emptiness check, and what single
   pull replaces it?
3. A job counts lines then collects errors from the same handle; the
   count is right, the errors list is empty. Which concept explains it,
   and what is the one-line fix in words?
4. What must `__next__` do when the source is dry, and what does a
   `for` loop do with that signal?
5. Your reader's `__iter__` returns `self`. A teammate wants two
   independent passes over one reader. What do you tell them, and what
   trade are you naming?
6. A helper returns `list(it)` twice from one iterator; the second call
   is `[]` and its driver only asserted the first. Which Pitfall number,
   and what single assertion would have caught it?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is the night-shift server log throughout. Full specs live in
`exercises.ipynb`; write each deliverable in its stated file (R16 —
no `solution.py`, no double-write), then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | `take`: first-N pull, short-stream + negative-n edges |
| E2 | Easy | [REAL-WORLD] | `kind`: iterable-vs-iterator discriminator via identity |
| E3 | Easy | [REAL-WORLD] | `validate_line` + `first_valid`: boundary rejects, exhausted→None |
| M1 | Medium | [REAL-WORLD] | `WindowReader` class: fixed windows, ragged tail kept, one-shot |
| M2 | Medium | [REAL-WORLD] | learner-composed valid-then-batch pipeline (order observable) |
| H1 | Hard | [DEBUG] | 4-plant hunt: truthiness, swallowed termination, reuse, shared cursor (+ 7-row chain each) |
| Challenge | Micro Build | [REAL-WORLD] | log-triage CLI: streaming handle → windows → byte-exact incidents report |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): the protocol used
independently, the batching class correct including the ragged tail,
the H1 hunt resolved with four 7-row chains, the Challenge running as
a streaming triage pipeline with byte-exact output.

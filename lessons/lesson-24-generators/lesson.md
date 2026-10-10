# Lesson 24 — Generators (Tier: SUPPORTING)

Stage 3, eighth topic. Last lesson you built batching as a 20-line class
with a hand-rolled cursor. This lesson rebuilds the same machine in five
lines — same protocol, same `StopIteration`, same one-shot discipline,
authored instead of interfaced.

SUPPORTING tier — Level 3 bar: write generator functions independently
and use them on real streams. One focused sitting, then the pattern
transfers into the Stage project (paged feeds, chunked processing) and
every lazy pipeline after it.

Business domain for this lesson is fresh: sensor telemetry harvest. No
logs, no clinic, no expenses. New business, same engineering discipline.

---

## Objective

By the end of this lesson you can:

- Write a generator function: `yield` values one at a time, suspending
  and resuming instead of building and returning.
- Predict laziness exactly: no body line runs before the first `next()`,
  and work happens pull-by-pull, never upfront.
- Write generator expressions for one-line lazy transforms, and say
  when they beat a full `def`.
- Bound infinity with plain `for` + `break` (no new tools).
- Compose generator pipelines (validate → batch → filter) where every
  stage stays lazy to the edge.
- Name `yield from`, `.send()`/`.throw()`/`.close()`, and `itertools`
  as deliberate omissions — recognized, not drilled.

---

## Why This Matters

The greenhouse runs two thousand sensors. Every minute each one reports
temperature and humidity; the harvest job pulls the readings, keeps the
over-threshold windows, and writes the morning alert report.

Version 1 is written the L23 way: a batching class, a validation loop,
a materialized clean list in the middle. It works — and the middle list
grows with the sensor count. Last heatwave the clean list held nine
million readings before batching even started. The job survived, but the
shape is wrong: a pipeline that *streams* everywhere except one quiet
`list()` in the middle is a loading job wearing a costume.

Why is the previous concept insufficient? The class-based reader is
honest machinery, but every new stage needs a new class — validation
stage, threshold stage, window stage — each with `__init__`,
`__iter__`, `__next__`, cursor bookkeeping, tail rules. Three stages
means sixty lines of protocol before a single line of business logic.
The mechanism drowns the meaning.

What capability do we need? Author a stream the way we describe it:
"for each reading, validate it; group the survivors; keep the hot
windows" — code shaped like the sentence, with the pausing handled by
the language.

What feature provides it? A generator function: write what looks like a
plain loop with `yield` where `return` would be, and Python turns it
into a one-shot iterator — cursor, suspension, and `StopIteration`
included, zero dunder methods.

Practical consequence — what breaks without it? The alert report
covers half the night: somebody counts the readings, then collects
from the same generator — the count is right, the windows are empty,
no error anywhere. Same latent class as last lesson, new costume. The
H1 drill plants exactly it.

Urgency, stated plainly: the sensor fleet doubles next quarter and the
pipeline gains a stage (humidity alerts join temperature). Without
generators each new stage is a new class. With them each new stage is
a five-line function dropped into the chain. This lesson is what keeps
the pipeline shorter than the fleet is wide.

Deliberate omissions: `yield from` (delegation between generators —
genuinely useful, deferred to keep this lesson tight); `.send()` /
`.throw()` / `.close()` (coroutine machinery — project-dependent
depth, not Level-3 core); the `itertools` toolbox beyond one PROVIDED
sighting; async iteration (deferred to Asyncio).

---

## Mental Model

A generator function is a **recipe the kitchen cooks one dish at a
time, only when ordered**.

```text
def harvest():          calling harvest() cooks NOTHING —
    yield a                 it hands you a ticket (an iterator).
    yield b             next(ticket)  → kitchen cooks until "yield a",
                                        serves a, freezes mid-recipe.
                        next(ticket)  → unfreezes, cooks until "yield b".
                        next(ticket)  → recipe ends → StopIteration.
```

Three rules run everything:

1. Calling a generator function builds **nothing** — not even the first
   item. The body is frozen at line zero until the first pull.
2. Each `next()` runs the body until the next `yield`, serves that
   value, and freezes again — locals intact.
3. Falling off the end (or `return` with no value) raises
   `StopIteration`. A generator is a one-shot iterator: consumed never
   refills, `iter(gen) is gen`.

A generator expression is the same machine without a name:
`(expr for x in stream if cond)` — frozen recipe, same pull rules.

---

## Core Concept

### 1. `yield` suspends; calling builds nothing

Problem: `clean_windows` materializes the clean list before batching.
For nine million readings, "before" costs nine million slots.

Why a plain function is insufficient: `return` ends the call and hands
back one finished object. There is no "pause here, resume on next
call" in a plain function's vocabulary.

Capability needed: emit items one by one while the caller pulls,
keeping your place between pulls.

Feature: `yield`. The function containing it becomes a generator
function: calling it returns a generator (frozen, zero work done);
each `next()` runs to the next `yield`.

```python
def batches(source, size):
    window = []
    for item in source:
        window.append(item)
        if len(window) == size:
            yield window
            window = []
    if window:
        yield window       # the ragged tail — same rule as the class

b = batches([1, 2, 3, 4, 5], 2)
next(b)   # [1, 2] — only now did the body run, and only this far
```

Consequence of missing this: every stage materializes, and the
pipeline's memory equals its biggest intermediate — the L23 lesson
relearned the expensive way.

### 2. Laziness is exact: nothing runs early, everything runs on pull

Problem: "lazy" gets waved around vaguely — then somebody puts a
`print` before the first `yield` for debugging and is surprised it
never fires until pulled.

Why vagueness fails: pipeline bugs live in *when* code runs. "Lazy"
without a pull-by-pull model cannot diagnose a stage that ran too
early (or never).

Capability needed: a clock for frozen code — which line runs on which
pull.

Feature: the freeze model from the Mental Model, sharpened — the body
runs **only** inside a `next()` call, from the frozen point to the
next `yield` (or the end). Proof you can run yourself:

```python
def logged(source):
    print("starting")        # runs on FIRST next(), never on the call
    for item in source:
        print("pulling", item)
        yield item

g = logged([1, 2])           # silence — nothing ran
next(g)                      # "starting", "pulling 1", serves 1
```

Consequence of missing this (H1-adjacent): an eager `list()` buried
in one stage silently converts the pipeline back into a loading job —
memory blows with zero behavior change on small fixtures.

### 3. Generator expressions: the one-line recipe

Problem: `def` + `yield` for a single transform (`strip every line`,
`keep readings over threshold`) is ceremony-heavy — five lines where
the idea is one clause.

Why a helper function is insufficient: a `def` that returns a list
materializes; a `def` with `yield` for one clause is fine but noisy at
scale (pipelines gain dozens of micro-stages).

Capability needed: a frozen one-liner with the same pull rules.

Feature: `(expr for x in stream if cond)` — builds a generator, pulls
lazily, skips without storing. Comprehension syntax, generator soul:

```python
raw = ["  21.5 ", "", "  99.0 "]
clean = (line.strip() for line in raw if line.strip())
next(clean)   # "21.5" — the strip ran now, not at build time
```

Consequence of confusing it with a comprehension: `[expr for ...]`
builds the whole list *now* (nine million slots again); `(expr for
...)` builds nothing until pulled. Brackets are the entire difference.

### 4. Bounding infinity with `for` + `break`

Problem: the sensor stream never ends. `list(ticks())` never returns;
a `while True` harvester with no exit is a hang, not a program.

Why new tools are unnecessary: bounding is a *stopping decision*, not
a library feature. `for` plus a counter plus `break` — Stage 1 tools —
already say "first N, then stop".

Capability needed: harvest a prefix of the endless, then walk away
with the generator abandoned (abandoning is legal — one-shot objects
owe nothing after use).

Feature, stated once:

```python
def ticks(start=0):
    n = start
    while True:
        yield n
        n += 1

first_five = []
for t in ticks():
    if len(first_five) == 5:
        break
    first_five.append(t)
```

Consequence: infinity is only dangerous to code that demands endings.
Pull-counted consumption is safe by construction.

### 5. Composing lazy pipelines (the assessable skill)

Problem: validate → batch → filter-alerts as three materializing steps
rebuilds the nine-million-slot middle twice over.

Why chaining helpers is insufficient: each helper that returns a list
breaks the laziness chain at its link. The pipeline is only as lazy
as its most eager stage.

Capability needed: stages that are *themselves* generators, so pulls
flow end to end — one pull at the tap draws one pull per stage.

Feature: generator in, generator out, composed by nesting calls:

```python
def parse_valid(source):
    for line in source:
        try:
            yield validate(line)     # L23's boundary rule, unchanged
        except ValueError:
            continue                 # rot skipped, stream unbroken

windows = batches(parse_valid(raw_lines), 50)   # batching over a stream
hot = (w for w in windows if any(r > 40.0 for r in w))  # genexp filter
```

One pull on `hot` draws one window from `batches`, which draws up to
50 pulls from `parse_valid`, which draws until one line validates.
Nothing stored except the current window.

Consequence of one eager link (Pitfall 3, H1 plants it): correct
windows, blown memory, green small-fixture drivers — the latent class
again, wearing overalls.

### 6. `return` ends; it does not emit (the quiet trap)

Problem: muscle memory from plain functions writes `return items` at
the end of a generator "to hand back the results" — and the generator
yields nothing at all.

Why it fails silently: inside a generator, `return X` raises
`StopIteration(X)` — the value rides the *termination signal*, not the
item channel. `for` loops and `list()` discard it. The function looks
finished; the stream is empty.

Capability needed: distinguish the item channel (`yield`) from the
termination channel (`return` / falling off the end).

Feature: emit with `yield`, end by falling off (or bare `return`).
`return value` inside a generator is reserved machinery you do not
need at Level 3 — treat any `return X` in graded generator code as a
bug until proven otherwise.

Consequence of missing this (Pitfall 2, H1 plants it): a harvest that
returns its findings instead of yielding them reports zero incidents
with all logic "correct".

---

## Practical Examples

Example A — the twin, side by side (E1 is this, specified exactly).
Twenty lines vs five, identical windows:

```python
# L23 class (protocol interfaced) vs L24 function (protocol authored):
def batches(source, size):
    """Successive fixed-size windows; ragged tail kept; one-shot."""
    if size < 1:
        raise ValueError("window size must be >= 1")
    window = []
    for item in source:
        window.append(item)
        if len(window) == size:
            yield window
            window = []
    if window:
        yield window
```

Example B — laziness you can watch (the pull clock):

```python
pulled = []
def metered(source):
    for x in source:
        pulled.append(x)     # side effect marks each pull
        yield x

g = (x * 2 for x in metered([1, 2, 3]))
pulled                   # [] — genexp built, nothing pulled
next(g)                  # 2 — exactly one pull flowed through
pulled                   # [1]
```

Example C — infinite telemetry, bounded harvest:

```python
def ticks(start=0):
    n = start
    while True:
        yield n
        n += 1

def harvest(pred, stream, limit):
    """First `limit` items of stream satisfying pred."""
    found = []
    for item in stream:
        if pred(item):
            found.append(item)
            if len(found) == limit:
                break
    return found

harvest(lambda t: t % 10 == 0, ticks(), 3)   # [0, 10, 20]
```

PROVIDED-only sighting (never required): `itertools.islice(stream, n)`
bounds any stream, infinite included (`islice(ticks(), 5)`). Recognize
it in real code; this lesson bounds by hand first.

---

## Engineering Notes

- **One-shot discipline, twin edition.** Generators are iterators:
  consumed never refills, `gen is iter(gen)`, second pass silently
  empty. Count-then-collect on one generator repeats the L23 incident
  exactly — materialize once or pull once.
- **Validate at the boundary, per item.** Same L8 rule, new costume:
  rot skipped inside the pipeline stage, exact messages, stream
  unbroken.
- **Laziness is whole-pipeline or nothing.** Audit every link: one
  `list()` anywhere except the final small outputs converts the job.
  Small outputs (incident lines, counts) may materialize; the stream
  may not.
- **Keep stages single-purpose.** Parse stage parses; batch stage
  batches; alert stage filters. A `parse_and_alert` generator is the
  same maintenance trap as the old mega-decorator.
- **Annotate generators as what they are.** A generator function
  *returns* an `Iterator` (both names from `collections.abc`, L23
  taught):

```python
from collections.abc import Iterator

def batches(source: Iterable[str], size: int) -> Iterator[list[str]]: ...
```

- **When NOT a generator:** a small reused lookup wants a `list`; a
  value needed twice wants materializing once with a comment saying so;
  branching business logic wants `if`, not stages.
- **Forward link, not teaching:** a generator holding an open file
  handle should be closed by its owner — full resource discipline
  arrives with Context managers. Until then: short-lived generators,
  handles closed by the opener.

---

## Common Pitfalls

1. **Reusing an exhausted generator** — count right, collection empty;
   count-only drivers green. Materialize once or pull once.
2. **`return items` instead of `yield`** — the findings ride the
   termination signal; the stream yields nothing. Emit with `yield`.
3. **Eager `list()` mid-pipeline** — correct windows, blown memory,
   green small fixtures. Laziness is whole-pipeline.
4. **Shared mutable default across calls or instances** — `def gen(source,
   acc=[])` accumulates yesterday's harvest into today's (L5 trap,
   new costume). Fresh containers per call.
5. **Truthiness guard on a generator** — always truthy, same as L23
   Pitfall 1. Attempt the pull.
6. **Forgetting the ragged tail** — full windows only; the last partial
   batch vanishes on uneven data.

---

## Connection to Previous Knowledge

- **Iterators (L23):** this lesson's twin — same protocol
  (`StopIteration`, one-shot, `iter(x) is x`), authored via `yield`
  instead of interfaced via dunders. The E1 twin demonstration makes
  the transfer explicit on day one.
- **File handling (L9):** handles stream; generator pipelines process
  without hoarding — the OOM story that opens this lesson is L9's
  `readlines()` habit meeting 40 GB.
- **Exception handling (L8):** per-item boundary validation with exact
  messages; `StopIteration` as signal, not failure.
- **Typing (L14/L23):** generator functions annotate as returning
  `Iterator[T]`; parameters stay `Iterable[T]`.
- **Mutable defaults (L5):** the trap returns in generator clothing —
  unannounced retrieval, watch it.
- **Project structure (L20–L22 house):** Challenge keeps `main(argv)`
  (full `sys.argv`) + guard, Path-first I/O, no module-level
  executable code.
- **Spec-literalness (standing watch):** every Driver must match its
  Expected block byte-exact.

---

## Quick Recall

Answer from memory before coding:

1. The L23 batching class is ~20 lines; rebuild it as a generator in
   your head — how many lines, and which dunder methods vanished?
2. After `g = parse(readings)` (a generator call), how many lines of
   `parse`'s body have run — and what single call runs the first one?
3. `(x for x in s)` vs `[x for x in s]` on nine million readings:
   what differs in memory, and what single character decides it?
4. A harvest counts a generator, then collects from it; count right,
   collection empty. Which L23 incident is this the twin of, and what
   is the one-line fix in words?
5. A generator must stop after the first 5 hot readings of an endless
   stream. Which two Stage-1 tools bound it, and what happens to the
   abandoned generator?
6. A helper builds `list(gen)` twice from one generator and asserts
   only the first. Which Pitfall number, and what single assertion
   would have caught it?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is greenhouse telemetry throughout: readings are floats (or numeric
strings needing validation). Full specs live in `exercises.ipynb`;
write each deliverable in its stated file (R16 — no `solution.py`, no
double-write), then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | `batches` gen function: the class twin, ragged tail kept |
| E2 | Easy | [REAL-WORLD] | genexp transforms + laziness proof (zero pulls at build) |
| E3 | Easy | [REAL-WORLD] | infinite `ticks` + bounded harvest; empty source first-pass |
| M1 | Medium | [REAL-WORLD] | lazy `parse_valid` pipeline stage (pull-1-advances-1) |
| M2 | Medium | [REAL-WORLD] | learner-composed alert windows (validate→batch→keep-hot) |
| H1 | Hard | [DEBUG] | 4-plant hunt: reuse, return-instead-of-yield, eager link, shared default (+ 7-row chain each) |
| Challenge | Micro Build | [REAL-WORLD] | telemetry harvest CLI: streaming pipeline → byte-exact alerts report |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): generator functions written
independently with exact laziness, the batching twin correct including
the tail, the H1 hunt resolved with four 7-row chains, the Challenge
running as a streaming harvest pipeline with byte-exact output.

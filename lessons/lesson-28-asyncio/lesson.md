# Lesson 28 — Asyncio (Tier: AWARENESS)

Stage 3, twelfth topic — the last concept-shaped one, and the first
that collapses. Until now every lesson asked for independent
implementation. This one asks for something narrower and just as
real: **recognize the model, read the code, run one example, know
when the tool applies.** No drills, no hunt — the tier decides that,
not the topic's glamour.

You already hold the two relatives: generators (L24) taught code
that *pauses mid-execution and resumes with locals intact*, and
context managers (L25) taught guarantees around a block. Asyncio is
both of those ideas pointed at a new problem: **many things that
wait**.

AWARENESS tier — Level 2 bar: mental model, recognition on sight,
one runnable example, and the judgment of when *not* to use it.
One short sitting; the skill's real payoff lands in Stage 4, where
FastAPI is async-native.

---

## Objective

By the end of this lesson you can:

- State the relay mental model: one thread, tasks yielding only at
  `await`, the event loop conducting.
- Read `async def`, `await`, `asyncio.gather`, `asyncio.run` on sight
  and say what each does.
- Spot the forgotten `await` — coroutine created, never run, silent.
- Name the sync-blocking rule: one blocking call stalls the whole
  loop.
- Say when async is wrong (CPU-bound, small CLI) and when it's right
  (fan-out I/O) — and name FastAPI as the Stage-4 payoff.
- Recognize `async with` as the context-manager twin (L25 retrieval).

---

## Why This Matters

The intake pipeline fetches three upstream feeds. Version 1 awaits
each one in sequence: feed A takes 4 seconds, B takes 4, C takes 4 —
the run takes 12, and nine of those seconds nobody is doing
anything. The natural fix is threads — but threads share memory,
and from the day threads enter, every function needs a story about
what it locks.

Why are the previous tools insufficient? Sequential code waits on
the **sum** of waits; threads buy concurrency with shared-state
complexity you must now reason about everywhere.

What capability do we need? Many waits, one memory space, no locks:
concurrency where tasks *volunteer* the CPU at wait points instead
of fighting for it.

What feature provides it? `asyncio`: `async def` marks a function
that can pause, `await` marks the pause points, the event loop
rotates tasks between pauses, `gather` starts several at once.

Practical consequence — what breaks without it? Every fan-out stays
N× slower than its slowest single wait, and Stage 4's FastAPI reads
like magic nobody explained. Urgency, stated plainly: this lesson is
10% of what the capstone will use it for — recognition now, real
application on demand (PROJECT-DEPENDENT depth is explicitly not
promised).

Deliberate omissions: `Task`, queues, semaphores, event triggers,
`async for`/`async with` deep machinery, `asyncio.to_thread` beyond
naming it, cancellation and timeout policy — all PROJECT-DEPENDENT,
learned when a project needs them.

---

## Mental Model

A coroutine is a generator that owes the loop an obligation.

```text
sync world:   fetch A ──────wait──────▶ fetch B ──────wait──────▶ fetch C   (12s)
async world:      ┌ fetch A ──await──┐
                  │ fetch B ──await──┼──▶ loop wakes each when ITS wait
                  │ fetch C ──await──┘    ends                    (4s total)
                  └ one thread, baton handed ONLY at await
```

Three rules run everything:

1. `async def` called gives you a coroutine — **running nothing.**
   `await` (or `gather`) is what executes it.
2. The loop runs exactly one task at a time; tasks switch only at
   `await`. No shared-memory races, because nothing preempts.
3. Anything that *blocks without awaiting* holds the baton — the
   whole relay stops.

---

## Core Concept

### 1. `async def` defines; `await` executes

Problem: calling `fetch(url)` in normal code runs it immediately and
returns its value. In async code that model breaks — the function
must be able to *pause* mid-body.

Why immediate execution is insufficient: pausing requires the
function to hand control back; a normal call can't.

Capability needed: a call that returns a *promise to run*, pausable
at declared points.

Feature: `async def` makes the call produce a coroutine object —
inert until awaited:

```python
async def fetch(url: str) -> str:
    await asyncio.sleep(1)      # yields to the loop for 1 second
    return f"got {url}"

coro = fetch("a.example")       # NOTHING has run yet — coro is a coroutine
result = await coro             # now it runs (pausing at sleep) → "got a.example"
```

Consequence of missing this: the forgotten-`await` bug — an inert
coroutine object flows downstream, everything *looks* fine, nothing
ran. Your annotation-honesty class with a quieter voice.

### 2. The loop and `asyncio.run` — one entry point

Problem: someone must own the wait queue, wake tasks when I/O
finishes, and start the whole thing.

Why manual scheduling is insufficient: that's an operating system
inside your program.

Capability needed: a conductor that runs one coroutine to
completion.

Feature: `asyncio.run(main())` boots the loop, runs `main` to its
end, closes the loop. Sync code outside, async inside — exactly one
`asyncio.run` per program flow:

```python
async def main() -> None:
    greeting = await fetch("a.example")
    print(greeting)

asyncio.run(main())             # the ONLY place the loop is created
```

Consequence of missing this: `RuntimeError: no running event loop` —
or two loops fighting when `run` is called from inside async code.

### 3. `gather` — simultaneous in flight

Problem: three feeds, each awaited in sequence inside `main` — the
coroutines exist but run one after another. Still the sum of waits.

Why sequential awaits are insufficient: `await a; await b` is just
sync thinking wearing async syntax.

Capability needed: start several, collect all results.

Feature: `asyncio.gather` launches the coroutines concurrently on
the loop and awaits them all; results come back in *argument order*,
whichever finished first:

```python
results = await asyncio.gather(
    fetch("a.example"), fetch("b.example"), fetch("c.example"),
)   # 4s total, not 12 — three waits overlap
```

Consequence of missing this: async code that's slower than it needs
to be and teaches the wrong shape — the whole point is the fan-out.

### 4. The blocking rule (recognition, not machinery)

Problem: inside `fetch`, someone calls `time.sleep(4)` or reads a
big file with plain `open().read()`.

Why it's a trap: it *works*. Tests pass. Then one slow call freezes
every task — because blocking code never yields, and the relay only
advances at `await`.

Capability needed: an instinct — sync calls don't cooperate.

Feature (named, used later): `asyncio.to_thread(fn, ...)` wraps
blocking work so the loop stays free; sync libraries in async code
go through it. This lesson names it; PROJECT-DEPENDENT use.

```python
await asyncio.sleep(1)          # cooperative — loop free for 1s
time.sleep(1)                   # hostile — loop frozen for 1s
```

Consequence of missing this: "my async app is slower than sync" —
the classic mystery bug.

---

## Practical Examples

The full worked example — this is the one you type in E2:

```python
import asyncio
import time

async def fetch(name: str, delay: float) -> str:
    await asyncio.sleep(delay)              # the only wait primitive needed
    return f"{name} done"

async def main() -> None:
    started = time.perf_counter()
    results = await asyncio.gather(
        fetch("feed-a", 0.4),
        fetch("feed-b", 0.4),
        fetch("feed-c", 0.4),
    )
    elapsed = time.perf_counter() - started
    print(results)          # ['feed-a done', 'feed-b done', 'feed-c done']
    print(f"{elapsed:.2f}s")  # ~0.4s — not 1.2s

asyncio.run(main())
```

---

## Engineering Notes

- **Sync outside, async inside.** `main(argv)` stays a normal
  function — house guard unchanged; async is a leaf, entered through
  one `asyncio.run`.
- **Forgotten `await` is silent by nature.** No error, no warning —
  a coroutine object where a value should be. Treat any coroutine
  appearing in a value position as a bug until proven otherwise.
- **Blocking is contagious in both directions.** Async code can call
  sync libraries (via `to_thread`); sync code cannot `await` at all.
  Mixing happens at the edges, never in the middle.
- **Order of `gather` results = order of arguments**, not of
  completion. Reports stay deterministic even when timing doesn't.
- **When NOT async:** CPU-bound work (it's one core — use processes);
  a small CLI with one file read (sync is simpler and faster to
  write); anything you can't test without a running loop. Async is a
  tool for *many concurrent waits*, nothing else.
- **When YES:** fan-out API calls, websocket servers, thousands of
  connections — and the direct line: **FastAPI (Stage 4) routes
  handlers as coroutines.** This recognition is the seed.

---

## Common Pitfalls

1. **Forgotten `await`** — `coro = fetch(x)` runs nothing; downstream
   sees a coroutine object. Fix: `await fetch(x)`. Silent by nature.
2. **Sync blocking inside async** — `time.sleep`/raw file I/O freezes
   the whole loop. Fix: the await-capable twin, or `to_thread`.
3. **`asyncio.run` in the wrong place** — from inside async code
   (`RuntimeError`), or twice. One entry point, sync side only.
4. **Sequential awaits mistaken for concurrency** — `await a; await b`
   is a queue. Fan out with `gather` when waits are independent.

---

## Connection to Previous Knowledge

- **Generators (L24):** same suspension intuition — `await` pauses
  with locals intact, resumes later. `async def` is the generator
  idea with a scheduler attached.
- **Context managers (L25):** `async with` is the protocol twin for
  async resources — recognition only here, mechanics carry over.
- **House structure (L20–L26):** `main(argv)` + guard, Path-first
  I/O, stderr + exit 1 — all unchanged. Async lives inside one
  function; the entry point stays sync.
- **Boundary honesty (L14, standing):** a coroutine in a value
  position is the annotation class's quiet cousin — same
  green-looking, wrong-by-nature shape.

---

## Quick Recall

Answer from memory before touching code:

1. Three sequential fetches, 4s each — sequential-async total vs
   `gather` total, and *why* the second number exists at all.
2. `value = fetch("a.example")` in async code — what is `value`, and
   what has happened to the fetch so far?
3. Why does one thread running many tasks eliminate locking — and
   what is the one place tasks ever switch?
4. Name two situations where async is the *wrong* tool, and the
   Stage-4 framework whose handlers you'll already be able to read.

---

## Practice

AWARENESS pipeline — collapsed (CURRICULUM: concept → mental model →
example → small implementation or code reading → move on). Two
exercises, no hunt, no Challenge: the tier sets that, and inflating
it would silently promote the topic.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | code reading: predict output of async snippets (forgotten await + blocking sleep), then run to confirm |
| E2 | Easy | [REAL-WORLD] | write the `gather` fan-out; driver checks results AND concurrency shape (timing bound) |

Scoring: Easy 10 each. Diagnostic, not a target — AWARENESS closes on
recognition evidence, not on a bucket sum.

Completion evidence (AWARENESS — Level 2): the four Quick Recall
answers from memory, E1 predictions matching observed output, E2
fan-out green with the timing proof.

---

Full specs live in `exercises.ipynb`; write each deliverable in its
stated file (R16 — no `solution.py`), then run the **Driver:** cell.

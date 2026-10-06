# Lesson 22 — Decorators (Tier: SUPPORTING)

Stage 3, sixth topic. You already build working pipelines (load, compute,
write, sync, log). This lesson removes the copy-pasted scaffolding around
them: timing, logging, validation, retry.

SUPPORTING tier — Level 3 bar: use decorators independently on real
functions. One focused sitting, then the pattern transfers into the
Stage project (every service function timed + logged + retried the same
way).

Business domain for this lesson is fresh: a small clinic sending
appointment reminders. No expense files. New business, same engineering
discipline.

---

## Objective

By the end of this lesson you can:

- Write a plain decorator: a function that takes a function and returns
  a wrapper, passing through `*args, **kwargs` and returning the result.
- Preserve identity with `functools.wraps` so `__name__` and
  `__doc__` survive decoration (tests and logs stay honest).
- Write a decorator with arguments (a 3-layer factory) such as
  `@retry(3)`.
- Stack decorators and predict the execution order.
- Apply `@log_call`, `@timed`, `@validate_appointment`, `@retry` to
  clinic functions without changing their return contracts.
- Say when a decorator is right vs a plain helper call vs a
  context manager — and refuse to decorate one-off code.

---

## Why This Matters

The clinic loses money on missed appointments. The fix is a reminder
pipeline: confirm each appointment, send an SMS, write a morning report.

Version 1 is written the obvious way. Every function repeats the same
four jobs:

```python
def confirm(appt):
    logger.info("confirm start")      # job 1: log
    start = perf_counter()            # job 2: time
    if not appt["name"]: ...         # job 3: validate
    ...real work...
```

Three functions later the logging text drifts. One function forgets the
timer. Retry exists in `send_sms` but not in `send_whatsapp`. A new
hire copies the wrong block. The business logic is 5 lines; the
scaffolding is 15. Bugs now live in the scaffolding, not the logic.

Why is the previous concept insufficient? Plain helper calls do not fix
it — you still call `log_start(); ...; log_end()` inside every function,
and you can still forget one. Inheritance does not fix it — these are
plain functions, not classes. A `with` block helps timing but still wraps
every body by hand.

What capability do we need? Attach behavior to a function once, at its
definition, so every call gets it automatically — without touching the
body.

What feature provides it? A decorator: `@timed` above `def confirm`
rebinds the name to a wrapper. The body stays 5 lines. The behavior
lives in one tested place.

Practical consequence — what breaks without it? The morning report says
"0 reminders sent" while the log says "sent 40". The wrapper swallowed
the return value and nobody noticed, because the sample test only
checked the log line. That is the latent-bug class of this lesson, and
the H1 drill plants exactly it.

Urgency, stated plainly: the next feature (WhatsApp reminders) ships
next week. Without decorators you copy 15 lines of scaffolding a fourth
time. With decorators you write one line: `@retry(3)`. This lesson is
what makes the fourth channel cheap and the first three consistent.

Deliberate omissions: class decorators (same idea, class targets —
not needed here); `functools.lru_cache` (shown as one PROVIDED example
only); async decorators (deferred to the Asyncio topic); `dictConfig`,
`LoggerAdapter`, `Filter` (named but untaught — never required).

---

## Mental Model

A decorator is a **wrapper-returns-function machine**:

```text
@timed
def confirm(appt): ...
```

means exactly:

```python
def confirm(appt): ...
confirm = timed(confirm)
```

`timed` receives the original function, builds a `wrapper` that does
work before and after calling it, and returns the wrapper. Every later
call to `confirm(...)` runs the wrapper, not the original body directly.

```text
call confirm(appt)
  -> wrapper(appt)
       -> pre-work (log, start timer, validate)
       -> result = original(appt)
       -> post-work (log elapsed)
       -> return result
```

The closure is the memory: `wrapper` remembers `func` because it was
defined inside `timed(func)` and keeps referring to it. No global
state. No class. Just a function holding onto another function.

---

## Core Concept

### 1. First-class functions + closure (the only machinery)

Problem: the wrapper must call the original later, after `timed`
has already returned. Where does the original live?

Why previous tools fail: a local variable normally dies when its
function returns. A plain helper cannot "remember" which function it
wrapped.

Capability needed: a function value that outlives its creator.

Feature: functions are objects; a nested function closes over its
enclosing scope.

```python
def timed(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

`wrapper` keeps `func` alive through the closure. `timed(confirm)`
returns `wrapper`; the name `confirm` now points at the wrapper.
Consequence of missing this: storing `func` in a global "current
function" breaks the moment two functions are decorated.

### 2. Plain decorator + `*args, **kwargs` passthrough

Problem: clinic functions have different shapes: `confirm(appt)`,
`send_sms(appt, channel="sms")`, `build_report(items)`. One wrapper
must fit all of them.

Why fixed params fail: `def wrapper(appt)` crashes on
`build_report(items)` extras and drops `channel=`.

Capability needed: accept anything, forward everything.

Feature: `*args, **kwargs` in the wrapper, forwarded unchanged, and
the result returned verbatim.

```python
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"call {func.__name__}")
        result = func(*args, **kwargs)
        print(f"done {func.__name__}")
        return result
    return wrapper
```

Consequence of missing this (Pitfall 1, H1 plants it): a wrapper with
fixed params passes the sample (one-arg calls) and crashes on the
first keyword call in production.

### 3. `functools.wraps` (identity preservation)

Problem: after wrapping, `confirm.__name__` says `"wrapper"`. Logs,
tracebacks, and tests now lie about which function ran.

Why it matters here: L17 taught you to assert on behavior AND identity
(`__name__`, docstrings in failure output). L21's caplog lines print
the function name. A lying name sends the on-call engineer to the wrong
function at 2 AM.

Feature: `@functools.wraps(func)` copies `__name__`, `__doc__`,
`__module__`, and sets `__wrapped__`.

```python
def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ...
    return wrapper
```

How it works: `wraps` is itself a decorator provided by the stdlib —
taught here, first use in E2. Consequence of skipping it (Pitfall 2):
every decorated function shares one name; the morning log shows
`wrapper` forty times.

### 4. Decorator with arguments — the 3-layer factory

Problem: `@retry` needs a number: `@retry(3)` vs `@retry(5)`. But
`retry(func)` receives a function, while `retry(3)` receives an int.
One shape cannot do both.

Why a plain decorator is insufficient: the `@` line either calls the
decorator with the function (no parens) or calls something else first
(with parens). The "something else" must produce the real decorator.

Capability needed: a function that takes settings and returns a
decorator.

Feature: three layers — factory → decorator → wrapper.

```python
def retry(attempts, exc=(ConnectionError,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exc as err:
                    last = err
            raise last
        return wrapper
    return decorator
```

Usage is `@retry(attempts=3)`. Calling `retry(3)` returns `decorator`;
Python then applies `decorator` to the function below. Consequence of
confusing the layers (Pitfall 4, H1 plants it): `@retry` without parens
passes the function as `attempts` — passes nothing, explodes on call.

### 5. Stacking order (bottom-up apply, top-down run)

Problem: `confirm` needs all three: validated, timed, logged. Which
line goes on top?

What happens: decorators apply bottom-up; the wrapper closest to the
function runs innermost.

```python
@log_call      # runs outermost (sees everything)
@timed         # runs middle
@validate_appointment  # runs innermost (closest to body)
def confirm(appt): ...
```

Trace one call: `log` pre → `timed` start → `validate` checks →
body → `timed` logs elapsed → `log` post. Swap `log` and `timed` and
the elapsed line moves outside the call line — M2 makes the order
observable so you cannot guess.

Consequence of misreading: validation runs after timing, so rejected
inputs still bill time; or logging wraps validation noise instead of
real calls.

---

## Practical Examples

All examples use the clinic domain. `appt` is a dict
`{"name": str, "phone": str, "time": str}`.

Example A — `@log_call` with an injected logger (industry shape: log
at the boundary, body stays clean):

```python
import logging

def log_call(func):
    """Log entry and exit at INFO. Return contract unchanged."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = logging.getLogger("clinic")
        logger.info("call %s", func.__name__)
        result = func(*args, **kwargs)
        logger.info("done %s", func.__name__)
        return result
    return wrapper

@log_call
def confirm(appt):
    """Mark one appointment confirmed."""
    return {"status": "confirmed", "phone": appt["phone"]}
```

Example B — `@timed` storing elapsed without changing the return
(the Challenge's report needs per-stage timings):

```python
import time

def timed(func):
    """Measure wall time. Result unchanged. Elapsed on wrapper.last_elapsed."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            wrapper.last_elapsed = time.perf_counter() - start
    wrapper.last_elapsed = 0.0
    return wrapper
```

Example C — `@retry(attempts=...)` around a flaky sender (the SMS
gateway drops connections; the business rule is "try 3 times, then
page a human"):

```python
def retry(attempts, exc=(ConnectionError,)):
    """Retry on exc, total attempts times. Re-raise the last error."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last = None
            for _ in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exc as err:
                    last = err
            raise last
        return wrapper
    return decorator

@retry(attempts=3)
def send_sms(appt):
    """Send one reminder. Raises ConnectionError on gateway drop."""
    ...
```

PROVIDED-only example (never required to write): `@functools.lru_cache`
on a pure lookup such as `lookup_doctor(code)` — shown so you recognize
it in real code, not drilled.

---

## Engineering Notes

- **One behavior per decorator.** `timed` times; `log_call` logs.
  Compose by stacking. A `timed_and_logged_and_validated` decorator is
  a maintenance trap.
- **Never change the return contract.** The wrapper returns exactly
  what the body returned. If the sample passes but the report is
  `None`, the wrapper dropped the return — the latent bug of this
  lesson.
- **Validate at the boundary, inside the innermost wrapper.** Rejected
  inputs should never bill time or emit "done" lines.
- **Retry only transient errors.** `retry` catches the `exc` tuple you
  pass (default `(ConnectionError,)`). Never bare-`except`. Never retry
  validation errors — resending a bad phone number never helps.
- **Test decorated code on behavior + identity.** Assert the return
  value, the `__name__`, and the log line. A test that only checks the
  log line is vacuous (L17 rule — it passes even when the return is
  `None`).
- **Typing shape (taught here, minimal):** annotate wrappers as
  `def wrapper(*args: object, **kwargs: object) -> object` only if the
  lesson asks; the graded contract is runtime behavior + `wraps`
  identity, not full `Callable[..., T]` generics (deliberately shallow
  for SUPPORTING).
- **When NOT to use it:** a helper called once needs no decorator; a
  timing need scoped to three lines wants a `with` block; business
  branching (`sms` vs `whatsapp`) is a plain `if`, not a decorator.

---

## Common Pitfalls

1. **Fixed-params wrapper** — `def wrapper(appt)` drops `channel=`.
   Passes one-arg samples, crashes on keyword calls.
2. **Missing `functools.wraps`** — all decorated names read
   `"wrapper"`; logs and tracebacks lie.
3. **Dropped return** — wrapper calls `func(...)` but returns `None`.
   Log looks right, report is empty. Hardest to catch; always assert
   the return, not just the log.
4. **Factory/plain confusion** — `@retry` without parens feeds the
   function in as `attempts`. Factories always need the call:
   `@retry(attempts=3)`.
5. **Wrong stacking order** — timing outside validation bills rejected
   inputs; logging outside everything is usually what you want —
   decide deliberately (M2 proves it).
6. **Hidden decorator state** — a call counter on the wrapper without
   a guard breaks under reuse; keep wrappers stateless except
   `last_elapsed`-style observability.
7. **Over-decorating** — decorating a one-call script helper adds
   indirection for zero reuse. Three uses is the smell test.

---

## Connection to Previous Knowledge

- **Logging (L21):** decorators emit through `logging.getLogger`;
  verbosity gates from L21 apply inside wrappers. No new logging API.
- **Testing (L17):** assert returns + identity + log lines; vacuous
  log-only tests rejected. `tmp_path`/`caplog` seams reused in M2.
- **Exception handling (L8):** retry catches a stated tuple, re-raises
  the last error; validation raises `ValueError` with exact strings
  at the boundary.
- **Typing (L14):** honest annotations on the body functions; wrapper
  transparency via `wraps` (not annotation gymnastics).
- **Project structure (L20):** Challenge keeps `main(argv)` +
  `__main__` guard, Path-first I/O, no module-level executable code.
- **Spec-literalness (standing watch):** every `Driver:` must match its
  `Output:` block byte-exact — including the log-line formats below.

---

## Quick Recall

Answer from memory before coding:

1. What does `@timed` above `def confirm` actually rebind, in one line?
2. Why must the wrapper take `*args, **kwargs` even when the first
   function it wraps takes exactly one argument?
3. What breaks (name one log symptom, one test symptom) when
   `functools.wraps` is missing?
4. How many layers does `@retry(attempts=3)` need, and what does each
   layer receive?
5. In `@log_call / @timed / @validate_appointment` (top to bottom),
   which runs first on a call, and which is closest to the body?
6. A decorated function logs correctly but returns `None`. Which
   Pitfall number is it, and what single assertion would have caught it?

---

## Practice

Volume follows the SUPPORTING pipeline. Work top to bottom. The domain
is the clinic throughout. Full specs live in `exercises.ipynb`; write
solutions in `solution.py` first, then create the files each exercise
lists, then run the **Driver:** cell.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | `@log_call`: entry/exit lines, return passthrough |
| E2 | Easy | [REAL-WORLD] | `@timed`: elapsed on `wrapper.last_elapsed`, `wraps` identity |
| E3 | Easy | [REAL-WORLD] | `@validate_appointment`: boundary rejects, exact messages |
| M1 | Medium | [REAL-WORLD] | `@retry(attempts, exc)`: flaky sender, re-raise last |
| M2 | Medium | [REAL-WORLD] | stacking order made observable via log sequence |
| H1 | Hard | [DEBUG] | 4-plant drill: kwargs drop, missing wraps, swallowed return, factory misuse |
| Challenge | Micro Build | [REAL-WORLD] | Clinic Reminder CLI: decorated pipeline, `main(argv)`, Path I/O, byte-exact report |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Diagnostic,
not a target.

Completion evidence (SUPPORTING — Level 3): the four decorators used
independently, H1 resolved with the DEBUGGING protocol, Challenge
running as a decorated clinic pipeline with byte-exact output.

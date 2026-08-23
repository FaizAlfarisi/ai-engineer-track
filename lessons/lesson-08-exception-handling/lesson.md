# Lesson 8 — Exception Handling (Tier: CORE)

Stage 2 opener. From here on, "it works on the happy path" is not good
enough — programs must survive bad input, and this lesson is the tool
that makes that possible.

---

## Objective

By the end of this lesson you can:

- Explain what an exception is and how it propagates through the call stack.
- Use `try` / `except` / `else` / `finally` correctly — and know what each block is *for*.
- Catch **specific** exception types instead of using bare `except`.
- `raise` exceptions with clear messages to enforce a function's contract.
- Decide when EAFP (ask forgiveness) beats LBYL (look before you leap).

---

## Why This Matters

Every real program touches users, files, networks, or data — and all of
them produce garbage sometimes: `"abc"` where an int was expected, a
missing dict key, an empty list, a dropped connection.

A crash is just feedback nobody handled. Robust systems convert failures
into controlled outcomes: an error message, a retry, a fallback value,
a rejected row in a log. That conversion is exception handling.

This is also the direct payoff of a gap we flagged in Lesson 7:
`int()` / `float()` on user input was left unguarded because the guard
didn't exist yet. This lesson builds that guard properly — and Stage 2's
theme is exactly this: turning scripts into applications that don't die
on the first bad byte.

---

## Mental Model

An exception is a **signal that a runtime contract was violated**.

When a contract breaks, Python stops executing the current line and
**unwinds the call stack**, looking for a handler:

```text
main() → parse() → convert()
                    ↑ ValueError raised here
          parse() has no handler → keep unwinding
main() has a handler → execution resumes THERE
```

Two analogies, use whichever sticks:

- **Smoke alarm, not firefighter.** The exception doesn't fix anything.
  It interrupts everything until some code decides what to do.
- **Boundary checkpoint.** `try/except` belongs at the place where you
  can actually *respond* to failure — usually a function boundary — not
  wrapped around every line.

No handler anywhere → the program dies with a traceback. A handler
exists → execution resumes after the `try` block. `finally` means:
"no matter how the alarm ends — handled or not — do this."

---

## Core Concept

### The four blocks

```python
try:
    risky = int(text)          # only the risky line(s) go here
except ValueError as err:      # catches THAT type, binds the error object
    print(f"bad input: {err}") # response: message, fallback, retry...
else:
    print("converted")         # runs ONLY if no exception occurred
finally:
    print("done")              # runs ALWAYS — cleanup, counters, closing
```

- `except` — the response to a broken contract.
- `else` — the "success path" separator; keeps `try` blocks small.
- `finally` — guaranteed cleanup, even when an exception fires or a
  `return` happens inside `try`.

### Catch specific types

The type tells handlers *what kind* of failure happened; the message
tells humans *which* failure. Common builtins you'll meet constantly:

| Exception | Raised when |
|---|---|
| `ValueError` | right type, bad value — `int("abc")` |
| `TypeError` | wrong type entirely — `"a" + 1`, `len(5)` |
| `KeyError` | dict key doesn't exist |
| `IndexError` | sequence index out of range |
| `ZeroDivisionError` | division or modulo by zero |
| `FileNotFoundError` | path doesn't exist (next lesson) |

Order matters: Python checks `except` clauses top-down and uses the
first match. Specific types go **before** broad ones, or they never run:

```python
try:
    ...
except ValueError:     # specific first
    ...
except Exception:      # broad last — usually only at program top level
    ...
```

### Raising: enforcing your own contract

Functions raise to refuse bad input instead of returning junk:

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("insufficient funds")
    return balance - amount
```

The caller then decides the policy — print, retry, skip, abort. The
function stays reusable; handling lives at the boundary.

### EAFP vs LBYL

- **LBYL** — Look Before You Leap: `if key in d: ...`
- **EAFP** — Easier to Ask Forgiveness than Permission: try it, catch
  the failure.

Python culture prefers EAFP: it avoids double-checking races (file could
vanish between check and open) and keeps the happy path straight-line.
LBYL is fine when the check is cheap and failures are the normal case.

---

## Practical Examples

**1. Guarded conversion** — the Lesson 7 gap, closed:

```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
```

**2. Dict lookup with two failure modes:**

```python
def load_port(config):
    try:
        port = int(config["port"])
    except KeyError:
        return "missing key"
    except ValueError:
        return "not a number"
    else:
        return f"ready on {port}"
```

**3. Retry loop** — exceptions + loops working together:

```python
while True:
    raw = input("positive int: ")
    try:
        n = int(raw)
    except ValueError:
        print("not a number, try again")
        continue
    if n > 0:
        break
    print("must be positive")
```

**4. Raise at the border, handle at the caller:**

```python
try:
    balance = withdraw(100, 150)
except ValueError as err:
    print(err)            # insufficient funds
```

---

## Engineering Notes

- **Catch where you can respond.** Low-level functions raise; the
  caller (or `main`) decides policy. Wrapping every line in `try`
  produces code nobody can debug.
- **Never swallow silently.** `except: pass` deletes evidence. If you
  truly must ignore a failure, comment why — and count it.
- **Exceptions are for exceptional paths.** Don't use them as normal
  control flow inside hot loops; an `if` is cheaper and clearer when
  failure is expected most of the time.
- **EAFP shines at boundaries**: parsing, lookups, I/O — where the
  "check first" version ends up re-implementing the operation.
- Custom exception classes exist (`class AppError(Exception)`); they
  become natural once OOP arrives later in Stage 2.
- Context managers (`with`) automate `finally`-style cleanup — coming
  in the File Handling lesson. Until then, `finally` is the manual tool.

---

## Applied AI Perspective

AI engineering is exception-heavy: model APIs return malformed JSON,
rate-limit you mid-batch, time out on the tenth request of fifty.
Production pipelines survive by catching at boundaries (`json.JSONDecodeError`,
timeout errors), retrying with backoff, and falling back to a default —
never letting one bad response kill a batch job. The pattern you build
in this lesson's challenge (parse → reject bad rows → summarize) is,
structurally, what every data-for-AI pipeline does.

---

## Common Pitfalls

1. **Bare `except:`** — also catches `KeyboardInterrupt` and `SystemExit`,
   so Ctrl+C appears to stop working and real bugs vanish. Always name
   the type.
2. **Over-broad `except Exception` everywhere** — turns every bug into
   the same generic "something failed". Reserve it for top-level last
   resorts.
3. **Silent `pass`** — the failure happened AND nobody was told. Worse
   than crashing, because downstream code proceeds on missing data.
4. **Wrong clause order** — `except Exception` above `except ValueError`
   makes the second one dead code.
5. **Cleanup inside `try`** — if an exception fires before the cleanup
   line, it never runs. Cleanup belongs in `finally`.
6. **Validating with exceptions where an `if` is clearer** — raising for
   "user typed nothing" you expect constantly adds noise; reserve
   exceptions for contract violations.
7. **Returning `None` as an error signal** — callers forget to check;
   the bug surfaces three functions later as a mysterious `TypeError`.

---

## Connection to Previous Knowledge

This lesson sits on everything from Stage 1 — deliberately:

- **Functions (L5):** validation lives at function boundaries; `raise`
  is how a function refuses input. Every exercise here is
  function-decomposed like your challenges have been.
- **Collections (L6):** `KeyError`/`IndexError` come from dict/list
  access; medium exercises parse record lists into dicts.
- **Control flow (L3):** `if`-validation vs exception-raising is a
  design decision you now make consciously per case.
- **Loops (L4):** retry patterns and per-row error counting combine
  loops with handlers; watch the per-iteration state habit.
- **Modules (L7):** exceptions cross module boundaries — the module
  raises, the importer handles. And L7 left you a debt: unguarded
  `int()`/`float()` conversions. This lesson pays it.
- **Spec-literalness habit:** error messages are now part of the output
  contract — exact strings, verbatim.

---

## Quick Recall

Answer from memory before starting Practice:

1. In what order do `except`, `else`, `finally` run relative to each other? When does `else` get skipped?
2. Bare `except:` catches two exceptions you almost never want to intercept. Name both and say what breaks.
3. What does `int("12a")` raise? What does `[1, 2][5]` raise?
4. Your function gets bad input. Give one reason to `raise` instead of returning `None` — and one cost of raising.
5. `except Exception` is listed *above* `except ValueError`. Which fires for a `ValueError`, and why?
6. Expand EAFP. Name one situation where LBYL is the better choice.

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`; write solutions
in `solution.py` first, then paste into notebook cells.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1–E5 | Easy ×5 | [REAL-WORLD] | guarded conversion · two specific excepts · `else` · `finally` · `raise` |
| M1–M3 | Medium ×3 | [REAL-WORLD] | records → summary dict · retry loop over candidates · validation at module boundary |
| H1 | Hard | [REAL-WORLD] | debug drill: four planted bugs, ledger classics |
| H2 | Hard | [INTERVIEW] | strict CSV-field parser under adversarial input |
| Challenge | Micro Build | [REAL-WORLD] | Expense Entry Validator CLI — seeds the stage project |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, at least one meaningful combination with previous
concepts, demonstrated debugging (H1), and correct decisions about
*where* to catch and *what* to raise.

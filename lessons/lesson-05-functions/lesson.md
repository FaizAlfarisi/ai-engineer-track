# Lesson 5 — Functions

## Learning Objective

By the end of this lesson you can package logic into named, reusable, and
testable units: define a function with `def`, control what it hands back with
`return`, design parameters (positional, keyword, defaults), avoid the
mutable-default trap, respect scope, write docstrings, and compose small
functions into pipelines — replacing flat scripts with the building blocks
every real program, library, and AI pipeline is made of.

---

## Motivation

Every program so far has been a script: statements run top-to-bottom, and the
only way to "reuse" a block was copy-paste. Copy-paste is how bugs multiply —
fix the logic in one place and the duplicate still holds the old bug. A
function is the first unit of **abstraction**: one name for a computation,
callable anywhere, from anywhere. This is where you stop writing *scripts* and
start writing *programs* — and it's also where an engineer's vocabulary
(callers, contracts, responsibilities) enters the picture. Every data pipeline
in AI is a chain of functions: clean → transform → split → train → evaluate.

---

## Mental Model

A function is a **vending machine**.

```
insert coin (argument) ──▶ [ MACHINE ] ──▶ get product (return value)
```

You don't care how the machine works inside — you care that you put the right
coin in and the right product comes out. `def` is the blueprint of the machine,
`return` is the delivery slot, and the parameters are the coin slots.

The **caller** and the **machine** only communicate through the slots. Money
(mutable state) doesn't leak out of the machine unless you explicitly pass it
through the return slot.

---

## Visualization

### Anatomy of a function

```
def greet(name):           # def + name + (params):
    """Return a greeting."""   # docstring (optional)
    return f"Hello, {name}!"   # the delivery slot
                        ^
            everything before `return` is the machine's internals

print(greet("ada"))        # insert "ada" → get "Hello, ada!" → print it
```

### The print-vs-return fork

```
def wrong(x):              def right(x):
    print(x + 1)               return x + 1

y = wrong(5)               y = right(5)
print(y)   # None ──┬──    print(y)   # 6
                     │
        print shows a receipt; return hands you the product
```

`print` announces the value to the world. `return` **gives it to the caller**
so it can be stored, passed on, or composed. A function with no `return` (or an
early bare `return`) returns `None`.

### Scope: two rooms, one door

```
GLOBAL room:  g = 10
LOCAL room (inside a function):  # a new room opens on every call
    x = 5        # local — belongs to this call
    return x + g # can READ the global, cannot assign it
```

Reads of a global work. Assignments create a *local* unless you say `global`
(and even then, mutating globals from functions is an anti-pattern).

---

## Theory

### Defining and calling

```python
def double(x):
    return x * 2

result = double(21)      # call; result == 42
```

The `def` line runs when the program reaches it — so the function must be
**defined before it is called**. A function call "jumps" into the body, runs
it, hits `return`, and hands the value back to where the call happened.

### return vs print

```python
def add(a, b):
    print(a + b)     # side effect: shows the value, returns None

def add2(a, b):
    return a + b     # delivers the value

x = add(1, 2)        # x is None
y = add2(1, 2)       # y is 3
```

Rule: **functions compute and return; the caller decides how to display.**
`print` inside a function is a red flag unless the function's *job is* to
display.

### Parameters: positional, keyword, defaults

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("ben")                  # positional; greeting defaults to "Hello"
greet("cyn", "Hi")            # positional, both
greet(greeting="Yo", name="ada")  # keyword — order doesn't matter
```

Defaults let the caller omit arguments. **Default values are evaluated ONCE,
at `def` time** — the origin of the mutable-default trap.

### The mutable default trap

```python
def add_item(item, bucket=[]):    # BUG: same list object every call
    bucket.append(item)
    return bucket

add_item("a")   # ['a']
add_item("b")   # ['a', 'b']  ← bucket wasn't fresh!
```

The `[]` is created once, when the function is defined — every call that
omits `bucket` shares the same list. Fix: use `None` as the sentinel and
build the fresh collection inside:

```python
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
```

### Multiple return values

```python
def min_max(a, b):
    if a < b:
        return a, b
    return b, a

low, high = min_max(3, 9)     # tuple unpacking
```

`return a, b` returns a tuple; unpack it in one line.

### Scope

```python
g = 100

def show():
    x = 5                  # local to this call
    return x + g           # g is readable from here

print(show())              # 105
print(x)                   # NameError — x doesn't exist out here
```

Every call opens a fresh local room. Names you assign inside are local; they
vanish when the call ends. Reading a global works; **assigning to a name makes
it local** (`UnboundLocalError` if you then read it before assigning). The
Pythonic way to change a value is to **return it**, not to mutate a global.

### Docstrings

```python
def square(x):
    """Return x squared."""
    return x ** 2
```

A docstring is the function's user manual — triple-quoted right after the
`def` line. `help(square)` and `square.__doc__` expose it. Write *what it does*
(contract), not *how* (implementation).

### Composition

Functions call other functions. This is how programs grow without turning into
one giant block:

```python
def clean(text):
    return text.strip().lower()

def count_letter(text, letter):
    return clean(text).count(letter)

print(count_letter("  HELLO World ", "o"))   # 2
```

Each piece has one job; `count_letter` trusts `clean` to do its part.

---

## Best Practice

- One function = one responsibility (Single Responsibility). If a function
  does two unrelated things, split it.
- Functions **return** values; the caller handles `print`.
- Defaults: only use immutable defaults; use `None` + build-inside for
  collections.
- Name functions with verbs: `compute_grade`, `read_student`, `build_report`.
- Keep functions short; a function that doesn't fit on one screen is a sign.
- Write a docstring for anything you'd reuse — it *is* the documentation.
- Define before you call; keep `main()`-style orchestration at the bottom.
- Avoid global mutation: pass values in, return values out.
- (Type hints exist — `def add(a: int, b: int) -> int:` — and arrive formally
  in Stage 2. Not required yet.)

---

## Common Mistakes

1. **`print` instead of `return`.** The function shows output but returns
   `None`, so the caller can't store or compose it. The value is gone.
2. **Mutable default arguments.** `def f(x, items=[])` shares one list across
   all calls. Use `None` + build-inside.
3. **Calling before defining.** `NameError` at runtime — the `def` never ran
   yet. Define at the top, call after.
4. **Shadowing / thinking a local is global.** Assigning inside the function
   creates a local; reading a global name you've assigned to raises
   `UnboundLocalError`. Return instead of mutating globals.
5. **Off-by-one in a helper's `range`.** `range(n)` is `0..n-1` — the ruler
   from Lesson 4 applies inside functions too.
6. **Forgetting `return` on one branch.** A function with a `return` on only
   some paths returns `None` on the others.
7. **Giant `main` block.** If `main` is 40 lines of I/O and logic, it's not a
   function — it's a script wearing a costume. Delegate to helpers.
8. **Changing a function's contract silently.** When you refactor, the *output
   must stay identical* unless the spec changes.

---

## Applied AI Perspective

- **Pipeline as function chain**: `normalize(text)` → `tokenize(text)` →
  `vectorize(tokens)` — each a testable function. This is the shape of every
  feature-engineering pipeline.
- **Metrics as functions**: `accuracy(y_true, y_pred)`, `mean_squared_error`,
  `precision` — pure functions of inputs, trivially testable.
- **Config via defaults**: default parameters are how libraries ship sane
  behavior (e.g. `tokenize(text, lowercase=True)`) that callers override.
- **Reuse without copy-paste**: one `clean()` used everywhere means a bug
  fixed once, everywhere — the exact bug class that copy-paste duplicates.
- **Composition over repetition**: `map(clean, raw_rows)` (Stage 3) is
  function composition applied to a batch — the same idea, at scale.

---

## Mini Summary

- `def name(params):` defines; the body runs only when called.
- `return` delivers a value to the caller; missing it returns `None`.
- Functions compute and return; the caller decides how to display (`print`).
- Defaults make arguments optional — but only immutable defaults are safe.
- Mutable default → shared state bug; use `None` + build-inside.
- `return a, b` gives a tuple; unpack with `a, b = f()`.
- Locals live per-call and vanish; globals are readable, not assignable.
- Write docstrings: what the function does, not how.
- Compose small functions; one responsibility each.
- Define before calling; refactors must keep output identical.

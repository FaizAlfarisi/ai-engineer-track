# Lesson 3 — Boolean Logic, I/O & Conditionals

## Learning Objective

By the end of this lesson you can make your programs *decide*: read input
from a user, convert it safely, choose exactly one path with `if`/`elif`/
`else`, express multi-condition rules with `and`/`or`/`not`, and dispatch on
a value with `match` — building the rule engines behind validation, routing,
and gating logic.

---

## Motivation

So far your programs were *straight lines*: every statement ran, top to
bottom. Almost nothing in real engineering works that way. Every API
validates its payload before touching a database. Every ML pipeline drops or
repairs bad rows before training. Every chatbot classifies intent before it
answers. That "check then act" shape is exactly what conditionals are — and
`input()`/`output` is how a program talks to a user, a config file, or a
HTTP request. This lesson is where programs start to think.

---

## Mental Model

An `if` is a **gate on the railway**. The train (your program) reaches a
switch, the switch inspects a *truth* (is the value truthy?), and routes the
train down **exactly one** track. `elif` adds more switches in a row; `else`
is the catch-all final track.

```
        ┌────────── condition A truthy? ───── yes → run block A ──┐
        │                                                         │
input → switch → condition B truthy? ────── yes → run block B ──┤
        │                                                         │
        └─ no paths matched? ────────────── yes → run block else ─┘
                      (exactly ONE block ever runs)
```

`match` is a different machine: instead of asking a stack of yes/no
questions, it **holds one value up against labeled templates** and takes the
first template that fits. Think coat-check counter: you slide your claim
ticket across, the clerk checks the label, and hands you the matching coat.

`input()` is a **doorway**: your program opens the door, *waits*, and what
comes through is always a string — even if it looks like a number. You must
convert it yourself.

---

## Visualization

Truthiness ladder — the falsy set, everything else is truthy:

```
falsy:  None   False   0   0.0   ""   []   {}   ()
        │      │       │    │     │    │    │    │
        └──────┴───────┴────┴─────┴────┴────┴────┘
        everything else — numbers ≠ 0, non-empty strings/collections — is truthy
```

`if`/`elif`/`else` — exactly one suite runs:

```
if   score >= 90:      →  "A"
elif score >= 80:      →  "B"     ← evaluated top-down,
elif score >= 70:      →  "C"        first truthy wins,
else:                  →  "D"        rest skipped
```

`match` — first matching case wins, `_` catches everything:

```
match code:
    case 200 | 201:      "ok"
    case 400 | 404:      "client error"
    case code if code >= 500:  "server error"
    case _:              "unknown"
```

I/O doorway:

```
user → input("prompt") → str → int()/float() → your variable
     (always str)            (you convert)
```

---

## Theory

### Truthiness and `if`

Python asks every condition one question: **is it truthy?** You almost never
compare to `True`; you ask the value itself.

```python
name = input("Enter your name: ")
if name:              # truthy → non-empty string
    print(f"Hi, {name}")
else:
    print("No name given.")

count = int(input("Items: "))
if count:             # truthy → nonzero; 0 is falsy
    print(f"{count} items to process")
```

The falsy set: `None`, `False`, `0`/`0.0`, `""`, `[]`, `{}`, `()` — and
nothing else. Everything else is truthy.

### `if` / `elif` / `else` — exactly one branch

```python
score = int(input("Score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"grade: {grade}")
```

Rules:

- Conditions run **top to bottom**; the *first* truthy one claims the whole
  statement and the rest are skipped.
- `elif` is literally "else if" — Python's switch/case replacement.
- `else` is optional and matches *nothing above matched*.
- The suite is the indented block — indentation **is** the block (PEP 8:
  four spaces).

### Compound conditions

Combine several checks in one condition:

```python
age = int(input("Age: "))
if 0 <= age <= 120 and age >= 18:
    print("adult")
if temperature > 45 or humidity > 90:
    print("dangerous conditions")
if not quiet:
    print("noisy")
```

Short-circuiting makes order matter: `and` stops at the first falsy operand,
`or` stops at the first truthy one. Put cheap guards first, and never call
something that could crash behind a short-circuit that will skip it.

```python
if user and user.is_active:      # safe: user checked before user.is_active
    ...
```

### Chained comparisons (from Lesson 2) in conditions

```python
if 0 <= score <= 100:            # reads like math — one comparison
    ...
```

### `match` — pattern dispatch (Python 3.10+, we are on 3.12)

`match` compares a subject against patterns, first match wins:

```python
def http_status(code: int) -> str:
    match code:
        case 200 | 201:
            return "ok"
        case 400 | 404:
            return "client error"
        case code if code >= 500:
            return "server error"
        case _:
            return "unknown"
```

Patterns you need today:

- **Literal pattern** — `case 200:` matches if `code == 200`.
- **`|` (OR) pattern** — `case 200 | 201:` matches either.
- **Guard** — `case code if code >= 500:` matches the pattern AND passes the
  `if` condition.
- **Wildcard `_`** — `case _:` matches everything. It is *irrefutable*, so
  it must be the last case — like a final `else`.

When to reach for `match` vs `if/elif`: if you are comparing **one value**
against several constants → `match`. If you are testing a *mix* of unrelated
conditions → `if/elif`. `if/elif` can always do `match`'s job; `match` makes
the one-value-dispatch case read like a lookup table instead of a ladder.

### Input and output discipline

`input()` always returns a **string**:

```python
age = input("Age: ")      # "22", a str
age = int(age)            # 22, an int — ValueError if it can't parse
price = float(input("Price: "))
```

- Convert immediately at the doorway; work with the typed value everywhere
  after.
- Write **professional prompts**: end with a space, say exactly what you want
  (`Enter ticket priority (low/medium/high/critical): `). Your earlier
  shorthand prompts (`input ur total test case:`) are the anti-pattern.
- `int("9.5")` raises `ValueError`. Use `float()` for decimals.

### Validation guard — the pattern this lesson builds

Reject bad input *before* using it. This is the "pre-validation guard":

```python
priority = input("Priority (low/medium/high/critical): ").strip().lower()
if priority not in ("low", "medium", "high", "critical"):
    print("invalid priority")
    priority = "low"
category = input("Category: ").strip() or "general"
```

`"" or "general"` reuses the Lesson 2 fallback idiom: empty input falls back
to a default.

---

## Best Practice

- Write `if x:`, not `if x == True:`. Use `x is None`, not `== None`.
- Keep `elif` chains ordered from the most specific to the most general.
- Use `match` when dispatching one value over constants; use `if/elif` for
  mixed conditions.
- Guard clauses (fail fast) beat deep nesting: validate input up front,
  `print` + exit or default, then run the happy path.
- Convert `input()` at the doorway; never re-parse strings mid-program.
- Parenthesize compound conditions you can't read in one breath.
- `_` wildcard is a single underscore and must be the *last* case.

---

## Common Mistakes

1. **`== True` / `== None`.** `if x == True:` misses truthy-but-not-`True`
   values like `1` or `"yes"`. `if x is None` is the identity check.
2. **Order in `elif` chains.** Swapping `>= 90` and `>= 80` silently makes
   the `80` branch unreachable — the classic H1 bug.
3. **Forgetting `input()` returns `str`.** Comparing `"22" >= 18` is a
   `TypeError`; `int("abc")` is a `ValueError`.
4. **Comparing a str with the wrong type.** `"42" == 42` is `False` — types
   must match before `==` means anything.
5. **`match` pitfalls.** Putting `case _:` in the middle swallows everything
   after it; forgetting that `case x:` *binds* the name (not available after
   the case); guards use `if`, not `:`.
6. **Colon + indentation.** Missing the `:` or mixing tabs/spaces breaks the
   whole block — Python sees an incomplete statement.
7. **Mutating input in place of converting.** `priority.strip()` with no
   reassignment throws the clean version away (Lesson 2's strip lesson).

---

## Applied AI Perspective

- **Validation gates**: every AI API validates its payload before a model
  runs — `if`/`elif` chains encode the contract.
- **Rule-based pre-filtering**: cheap `if`-based rules discard junk rows
  before expensive model inference — the "guard" pattern at scale.
- **Intent/command routing**: chatbot frameworks `match` an intent string
  against registered handlers — exactly the dispatcher you'll build.
- **Decision trees**: `if`/`elif` chains *are* the evaluation of a trained
  decision tree (each node a threshold test). Hand-built rule systems use
  the same shape before models exist.
- **Data cleaning**: `if not value: value = default` fills missing fields
  before a pipeline touches them.
- **I/O**: agents and pipelines are fed by `input()` today and HTTP/JSON
  tomorrow — the conversion-and-validate habit transfers directly.

---

## Mini Summary

- Conditions ask "is this truthy?"; the falsy set is `None False 0 0.0 "" [] {} ()`.
- `if`/`elif`/`else` runs **exactly one** suite; first truthy `elif` wins,
  order matters top-down.
- Indentation defines the block (PEP 8: four spaces).
- Compound conditions: `and`/`or`/`not`, parentheses when doubtful,
  short-circuiting means order can prevent crashes.
- `match` dispatches one value over patterns; `|` is OR, `_` is the final
  wildcard, guards add an `if` to a case.
- Use `match` for one-value dispatch, `if/elif` for mixed conditions.
- `input()` always returns `str`; convert with `int()`/`float()` at the door.
- Validate before use: reject or default, then run the happy path.
- `"" or default` is the empty-input fallback.
- Professional prompts: descriptive, end with a space.

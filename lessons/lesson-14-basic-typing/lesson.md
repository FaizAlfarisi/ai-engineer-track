# Lesson 14 — Basic Typing (Tier: CORE)

Stage 2, seventh topic. You already know that Python does not check
types — you have written `int`, `str`, `list`, `dict`, and `None` code
for thirteen lessons. This lesson adds **type annotations**: labels on
your functions that say what they accept and what they return. Every
professional Python project — including every AI project — reads as
typed code.

---

## Objective

By the end of this lesson you can:

- Add annotations to a function's parameters and return type.
- Annotate containers: `list[int]`, `dict[str, float]`, `tuple[str, int]`.
- Express "optional" with `int | None` and a `None` default.
- Know that annotations are **not** enforced at runtime — they are
  labels for humans and tools.
- Read annotations back with `typing.get_type_hints`.
- Spot a lying annotation — one that does not match the value a function
  actually returns — and fix it.

---

## Why This Matters

A function `def average(scores):` tells a reader nothing. Is `scores` a
list, a dict, a set? Does it return a number, a string, `None`? The
reader must open every call site to find out.

Annotations turn the signature into a contract you can read without
reading the body:

```python
def average(scores: dict[str, int]) -> float:
```

That one line answers: "give me a dict of name → number, you get back a
float." Tools (IDEs, `mypy`) then check that every call site actually
obeys the contract — catching bugs *before* you run the program.

The AI stack you are moving toward is built on annotations: FastAPI
routes, pydantic models, and typed data pipelines all use them. The
Stage 2 Expense Manager requires typing as part of its evidence.

---

## Mental Model

From Lesson 1: a name is a **tag on an object**, and types belong to
the **values**, not the names. `x = 5` tags `x`; later `x = "a"` re-tags
silently.

An annotation is a second tag you stick on the name saying what it is
*meant* to hold:

```text
value:  "ada"  (a str)
tag:    name: str          <-- a note to humans and tools
```

Python still ignores it. It does **not** check, block, or convert
anything. Annotations live in a dictionary on the function
(`__annotations__`) and do their real work only when a *tool* reads
them. If you write `def f(x: int) -> str: return x + 1`, Python runs it
fine and returns an `int` to whoever calls it — nothing stops you, and
`get_type_hints(f)` cheerfully reports a lie.

So: **annotate for readers, verify yourself** (Lesson 8's `try/except`
still does the real validation).

---

## Core Concept

### 1. Function annotations

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def score_line(name: str, score: int) -> str:
    return f"{name}: {score}"
```

- Each parameter gets `name: type`.
- The return type goes after `->`.
- They are stored on the function, readable at runtime:

```python
from typing import get_type_hints
print(get_type_hints(greet))
# {'name': <class 'str'>, 'return': <class 'str'>}
```

### 2. Containers hold other types

Name the element type inside brackets:

```python
def total(values: list[int]) -> int:        # a list of ints
    return sum(values)

def counts(words: list[str]) -> dict[str, int]:   # word -> count
    out = {}
    for w in words:
        out[w] = out.get(w, 0) + 1
    return out

def pair(name: str, score: int) -> tuple[str, int]:
    return (name, score)
```

Common ones: `list[int]`, `dict[str, int]`, `set[str]`,
`tuple[str, int]` (with `...` for fixed shapes like `tuple[int, ...]`
when every element is an `int`).

### 3. Optional values: `| None`

Many functions return a value *or* `None` when nothing matched:

```python
def find_by_id(records: list[dict[str, int]], target: int) -> dict[str, int] | None:
    for record in records:
        if record["id"] == target:
            return record
    return None
```

The `|` reads as "or": the function returns `dict[str, int]` **or**
`None`. Old codebases write `Optional[dict[str, int]]` (from the
`typing` module) — it means the same thing; the `|` spelling is
preferred in modern code (Python 3.10+).

An optional parameter usually pairs with a `None` default:

```python
def summary(scores: dict[str, int], minimum: int | None = None) -> list[str]:
    cutoff = minimum if minimum is not None else 60
    ...
```

**The classic mistake:** annotating a default of `None` without the
union — `minimum: int = None` — which says the type is `int` while you
are really passing `None`.

### 4. Annotations are not validation

```python
def silly() -> int:
    return "this is a str"      # runs fine; the annotation lies
```

Nothing raises. That is why Lesson 8 still matters: `int(row["score"])`
must still be wrapped in `try/except ValueError` when input is untrusted.
Annotations describe the contract; validation enforces it.

### 5. Every signature you write should be annotated

Use it on the boundaries of your code — function parameters and returns.
You do not need to annotate every local variable inside a function body
(`total: float = 0.0` is optional noise). Annotate **where data enters
and leaves** your functions.

---

## Practical Examples

**1. A typed JSON loader (Lesson 11 shape, now with annotations):**

```python
from pathlib import Path
import json

def load_settings(path: Path) -> dict[str, object]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
```

`dict[str, object]` says "a dict whose values can be anything." That is
honest for arbitrary JSON — better than lying with a narrow type.

**2. A typed summarize (Lesson 6 `dict.get` pattern, annotated):**

```python
def net_by_category(records: list[dict[str, str | float]]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for r in records:
        if r["kind"] == "income":
            totals[r["category"]] = totals.get(r["category"], 0.0) + r["amount"]
        else:
            totals[r["category"]] = totals.get(r["category"], 0.0) - r["amount"]
    return totals
```

`str | float` means each dict value is a string or a float — exactly
what a JSON record `{"category": "food", "amount": 12.5}` holds.

**3. Reading annotations back:**

```python
from typing import get_type_hints
print(get_type_hints(net_by_category))
# {'records': list[dict[str, str | float]], 'return': dict[str, float]}
```

---

## Engineering Notes

- **Annotate function boundaries, not locals.** Parameters and returns
  carry the contract; a helper loop's `total` variable does not need a
  label.
- **A lying annotation is worse than none.** It tells readers and tools
  the *opposite* of the truth and hides real bugs (a function annotated
  `-> None` that returns a value, or `list[int]` filled with floats).
  Tools like `mypy` catch these as `inconsistent-return-statement` —
  that is the whole point of typing.
- **`X | None` is the modern spelling** for optional; `Optional[X]` from
  the `typing` module means the same and appears in older code. Learn to
  read both, write `|`.
- **`from __future__ import annotations`** (a one-line import at the top
  of a file) defers annotation evaluation, which lets a function refer to
  a type defined *later* in the file without crashing at import time:
  ```python
  from __future__ import annotations

  def make() -> Widget:      # Widget is defined below — fine
      return Widget()

  class Widget:
      ...
  ```
  You will see it in real code; you rarely need it yet.
- **Bare `list` vs `list[int]`:** prefer naming the element type. A bare
  `list` says nothing about what is inside.
- **Validation is still on you.** Annotations never replace
  `try/except ValueError`, `isinstance` checks, or the loader contract
  (Lesson 9/11). Type the shape; enforce it yourself.

---

## Common Pitfalls

1. **`minimum: int = None`** — a `None` default annotated as `int`.
   Must be `int | None = None`.
2. **Annotations are "validation"** — and code drops its `try/except`
   guards. Annotations check nothing at runtime.
3. **Lying annotations** — `-> None` that returns a value; `list[int]`
   receiving floats. Tools flag it; readers distrust it.
4. **Annotating every local variable** — walls of `x: int = 0` labels
   that add noise, not signal. Boundaries only.
5. **`dict` vs `dict[str, int]`** — the plain name is vague. Name the
   key and value types whenever you know them.
6. **Forgetting a `None` return path in the annotation** — a function
   that can return `None` must say so (`-> int | None`), or the
   annotation is a lie.

---

## Connection to Previous Knowledge

- **Variables & references (L1):** types live on values; annotations are
  tags on tags. Nothing about Python's tag-and-object model changes.
- **Functions (L5):** annotations go on the same signatures you already
  write — parameters and return types. The L5 context already used `->`
  once; this lesson formalizes it.
- **Collections (L6):** `list[int]`, `dict[str, int]`, `tuple[str, int]`
  name the element types you already choose from guarantees.
- **Exception handling (L8):** annotations describe; `try/except` still
  validates. Both stay in every loader.
- **JSON (L11) / CSV (L12) / Packages (L13):** the exercises type a
  real JSON→CSV report pipeline across multiple modules — the same shape
  as the L13 Challenge, now with contracts on every function.
- **OOP (next lesson):** classes are annotatable types; `Enum` gives
  names to a fixed set of values and makes great annotation material.
- **Spec-literalness:** same as always — every `Driver:` must match its
  `Output:` block byte-exact.

---

## Quick Recall

Answer from memory before starting Practice:

1. What does an annotation do at runtime? What is stored, and where?
2. `list[int]` — what does the `[int]` part mean?
3. Why is `def f(x: str | None = None)` correct while
   `def f(x: str = None)` is a bug?
4. What is the difference between "annotated" and "validated"?
5. When should you NOT add an annotation (which code is noise)?
6. What does `get_type_hints` give you, and who else uses that same
   information?

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`; write
solutions in `solution.py` first, then create the files each exercise
lists, then run the **Driver:** cell.

For every exercise you create the files yourself — `solution.py` holds
your working code, then you create the files listed in each **File
tree:**, then run the **Driver:** in the notebook. If a cell shows no
output when you run it, check that the file names and locations match
the File tree byte-for-byte.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | annotate a function's parameters + return type |
| E2 | Easy | [REAL-WORLD] | parameterized containers: `list[int]`, `dict[str, int]`, `tuple[str, int]` |
| E3 | Easy | [REAL-WORLD] | `float` params, `-> float`, `-> None`, `list[tuple[str, float]]` |
| E4 | Easy | [REAL-WORLD] | trap: annotations never enforce (wrong-typed calls still run) |
| E5 | Easy | [REAL-WORLD] | add honest annotations to recalled `count_words` |
| M1 | Medium | [REAL-WORLD] | `dict[str, int] | None`: find-or-None over loaded records |
| M2 | Medium | [REAL-WORLD] | a small typed package: JSON loader → compute, in a package |
| M3 | Medium | [REAL-WORLD] | `float | None` guard + typed aggregate over `list[dict[str, str]]` |
| H1 | Hard | [REAL-WORLD] | debug drill: lying annotations + runtime bugs in a monthly report |
| H2 | Hard | [INTERVIEW] | typed normalizer over ragged data: `dict[str, object]` → `dict[str, str \| float]`, edge cases |
| Challenge | Micro Build | [REAL-WORLD] | a fully typed JSON → CSV expense CLI (stretch: run `mypy`) |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, correct `| None` and container annotations everywhere,
the H1 contract-spotting done with the DEBUGGING protocol, the Challenge
typed end-to-end — and later, transfer into the Weekly Project.
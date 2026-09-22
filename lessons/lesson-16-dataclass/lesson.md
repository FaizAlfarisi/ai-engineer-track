# Lesson 16 — Dataclass (Tier: SUPPORTING)

Stage 2, ninth topic. In Lesson 15 you hand-wrote a `Transaction` class:
`__init__` storing four attributes, then a `__repr__` and `__eq__` if you
wanted readable printing and value comparison. This lesson shows you the
shortcut Python ships for exactly that shape — a class whose fields are
simply data. Dataclasses are not magic; they are **a class whose spec IS
its annotations**, and the boilerplate you wrote in Lesson 15 gets
generated for you.

SUPPORTING tier → Level 3 bar: independent implementation and use. One
focused session, then it transfers into Weekly Project 2 (whose data
model you rebuild with dataclasses in the Challenge).

---

## Objective

By the end of this lesson you can:

- Use `@dataclass` so annotated fields auto-generate `__init__`,
  `__repr__`, and `__eq__` — and know exactly what each generated method
  does.
- Give fields plain defaults for immutable values and
  `field(default_factory=...)` for mutable ones — without the shared-
  object trap.
- Make immutable records with `@dataclass(frozen=True)`: no mutation,
  value equality, hashable — usable as dictionary keys.
- Compose dataclasses (one dataclass holding a list of another) and
  trace a call through the layers (the Lesson 15 reflection skill).
- Serialize dataclasses with `asdict()` + a JSON encoder, handling Enum
  fields via `.value` (Enums fold back in — AWARENESS practice, not a
  re-teach).
- Say when a dataclass is the right tool vs a plain `dict` or a
  hand-written class, and meet `NamedTuple` / `slots=True` (AWARENESS).

---

## Why This Matters

Your Lesson 15 `Transaction` existed to hold data and one rule. Writing
it meant ~10 boilerplate lines per class. Real code has *dozens* of
these small record types. Python's answer: declare the fields, decorate,
and the class machinery writes the boring parts. The annotations you
have been writing since Lesson 14 — previously documentation — now
**become** the constructor, the printer, and the equality check.

The Stage 2 Expense Manager carries transactions as `dict`s and class
objects. In this lesson you rebuild that model as frozen dataclasses +
an Enum — the same data, less code, and a model that can never
accidentally mutate. Weekly Project 2 starts from this model.

---

## Mental Model

A dataclass is a **normal class** that describes its data first:

```python
from dataclasses import dataclass

@dataclass
class Transaction:
    date: str
    category: str
    kind: str
    amount: float
```

Three lines of annotations, and Python writes:

- an `__init__` that stores `date`, `category`, `kind`, `amount`
  (positional, in field order),
- a `__repr__` that shows `Transaction(date='...', category='...', ...)`,
- an `__eq__` comparing all four fields by value.

The decorator is a *code generator working from your annotations*. The
type hints are not passive documentation anymore — they are the spec.
Change a field's type, and every generated method follows.

```text
Lesson 15 (hand-written):    Lesson 16 (dataclass):
  def __init__(...):            @dataclass
  self.date = date              class Transaction:
  self.category = category          date: str
  self.kind = kind                  category: str
  self.amount = amount              kind: str
                                    amount: float
```

---

## Core Concept

### 1. The `@dataclass` decorator

Add methods to a class like any other class — dataclasses are ordinary
classes:

```python
from dataclasses import dataclass

@dataclass
class Transaction:
    date: str
    category: str
    kind: str
    amount: float

    def signed_amount(self) -> float:
        return self.amount if self.kind == "income" else -self.amount
```

`__init__`, `__repr__`, `__eq__` all exist now. You never wrote them.

### 2. Defaults: plain values vs `default_factory`

An immutable default is just an assignment:

```python
@dataclass
class Category:
    name: str
    budget: float = 0.0
```

But a mutable default is **forbidden at class-definition time** — the
same shared-object trap as Lesson 15, made loud:

```python
tags: list[str] = []   # ValueError: mutable default ... not allowed
```

The fix moves the *construction* of the default to each instance:

```python
from dataclasses import dataclass, field

@dataclass
class Category:
    name: str
    budget: float = 0.0
    tags: list[str] = field(default_factory=list)
```

`field(default_factory=list)` says: "when a new `Category` is made, call
`list()` for its `tags`." Every instance gets its **own** list — proven
in E2.

### 3. `frozen=True`: records that cannot change

```python
@dataclass(frozen=True)
class Transaction:
    date: str
    category: str
    kind: str
    amount: float
```

- Assigning to any field raises `dataclasses.FrozenInstanceError`.
- Equality is still by value, and because the object cannot change, it
  becomes **hashable** — usable as a dictionary key (your DSA #1 used a
  dict of category totals; frozen records slot straight into that idea).
- To "change" one, build a new instance. Pattern: a method returns a
  new record instead of mutating `self`.

Prefer `frozen=True` for records you treat as values — configuration,
parsed rows, transactions. Mutable state belongs to *holding* objects
(an account that accumulates a balance), not to record types.

### 4. Composition: one dataclass holding others

Dataclasses compose exactly like Lesson 15 classes — "has-a":

```python
@dataclass
class Ledger:
    owner: str
    transactions: list[Transaction] = field(default_factory=list)

    def net(self) -> float:
        return sum(txn.signed_amount() for txn in self.transactions)
```

M1's whole point is reading this **through the layers**: `Ledger.net()`
calls each `Transaction.signed_amount()` — the Lesson 15 reflection
skill, now with records.

### 5. Serialization: `asdict()` + a JSON encoder

`dataclasses.asdict(instance)` converts the object (recursively) to
plain dicts — ready for `json.dump`:

```python
from dataclasses import asdict
import json

data = json.dumps([asdict(t) for t in transactions], indent=2, default=kind_encoder)
```

One wrinkle (and the reason E3 makes you use an Enum): `asdict` keeps an
Enum *member* inside the dict — `<Kind.EXPENSE: 'expense'>` — which
`json.dumps` cannot serialize. Provide a small `default=` function that
returns `.value` for Enum members (Lesson 11's depth, revisited).

### 6. When a dataclass is the wrong tool

- A **stateless pipeline** stays functions (Lesson 15 rule): a dataclass
  earns the lines when the type has fields that travel together.
- An **ad-hoc bag of values** you pass around once — plain `dict` is
  still fine.
- A class with *behavioral rules* but little data — a hand-written class
  may be clearer than a dataclass stuffed with methods.
- A lightweight immutable *tuple-like* record — meet
  `typing.NamedTuple` (AWARENESS): fields, no methods worth having,
  tiny. Dataclass = fields + methods + control; NamedTuple = just the
  tuple shape.
- `slots=True` (AWARENESS, Python 3.10+): `@dataclass(slots=True)`
  stores fields in a compact array instead of a per-instance dict —
  less memory, faster access, at the cost of forbidding new ad-hoc
  attributes. Use it when you create *many* instances (bulk records).
  Your Challenge stretch tries it — behavior must not change.

---

## Practical Examples

**1. A value record that signs itself (E1 / the Challenge model):**

```python
@dataclass(frozen=True)
class Transaction:
    date: str
    category: str
    kind: Kind
    amount: float

    def signed_amount(self) -> float:
        return self.amount if self.kind is Kind.INCOME else -self.amount
```

**2. A budget category whose defaults are safe (E2):**

```python
@dataclass
class Category:
    name: str
    budget: float = 0.0
    tags: list[str] = field(default_factory=list)
```

**3. A composed ledger (M1) and a round-trip serializer (M2)** — the
object graph stays together, and `asdict()` pushes it to JSON in one
line.

**4. The Enum fold (E3):** the `Kind` enum from Lesson 15 E4 becomes a
field *type*. Stored JSON stays `"expense"` (via `.value`), but code
compares `K.is Kind.INCOME` — fixed-set and typo-proof.

---

## Engineering Notes

- **Fields are the contract — annotate honestly.** A dataclass with
  `amount: str` lies through every generated method. H1 plants this;
  `mypy` catches it only if you run it on the whole entry point.
- **Mutable defaults are loud here, not silent.** `field(default_factory=...)`
  — the Lesson 15 `=[]` trap is a class-definition `ValueError` in a
  dataclass. Same root cause (one shared object), better timing.
- **Field order = constructor order.** Fields with defaults must come
  after fields without them — same rule as function arguments.
- **`frozen=True` turns "mutate" into "make a new one."** Never call
  `object.__setattr__` to work around it — that is the bug, not the
  feature.
- **Methods compute and return; `main()` prints** — Lesson 5 boundary,
  unchanged. `__init__` stays `-> None` where you hand-write it; your
  other special methods keep honest annotations.
- **`asdict` recurses** — nested dataclasses, lists, dicts all flatten.
  Watch the Enum gap and supply the `default=` encoder.
- **Composition still beats inheritance by default** — a `Ledger` *has*
  transactions. `Kind(Enum)` remains the one deliberate inheritance.

---

## Common Pitfalls

1. **`field(default_factory=list)` forgotten** — `tags=list(...)` or
   `tags: list[str] = []` → shared defaults or a loud `ValueError`.
2. **`frozen=True` + a mutating method** — any `self.x = ...` after
   construction raises `FrozenInstanceError`. Return a new record
   instead (H1 plants exactly this).
3. **Enum field vs `json`** — `asdict` keeps `<Kind.EXPENSE: 'expense'>`
   in the dict; `json.dumps` chokes. Encoder with `default=` that maps
   `.value`.
4. **Comparing the enum to a string** — `self.kind == "income"` is
   always `False`, and mypy cannot see the lie. Use `is Kind.INCOME`
   (H1 plant #4).
5. **Annotation lie on a field** — `amount: str` holding floats: drivers
   may pass, `mypy` may not. Run `python -m mypy main_h1.py` too, not
   just `main.py` (Lesson 15's miss, now a habit).
6. **Dataclass for everything** — a one-off `dict` or a stateless pair
   of functions needs no decorator.
7. **Forgetting the decorator** — the class is a plain class then; every
   `Transaction(...)` call fails with "takes 3 positional arguments".

---

## Connection to Previous Knowledge

- **OOP (L15):** dataclasses ARE classes — composition, methods,
  `self`, and the "when OOP is unnecessary" rule all carry over. The
  hand-written `Transaction.__init__` / `__repr__` you wrote in L15 is
  what `@dataclass` generates for you now.
- **Typing (L14):** annotations move from documentation to *spec* — the
  fields drive generated `__init__`/`__repr__`/`__eq__`. Annotation
  honesty is now enforced by the machine.
- **Collections (L6):** the `dict.get(key, 0.0) + value` accumulate
  pattern is your Challenge's `net_by_month`/`net_by_category` — you
  already wrote them in L15; the model underneath is what changes.
- **Enums (L15 E4 — AWARENESS fold):** `Kind` returns as a *field type*;
  `is` identity and `.value` for storage; fixed-set correctness.
- **JSON (L11) / CSV (L12):** safe-loader contract, `newline=""` +
  `encoding="utf-8"` — unchanged rules. Data classes change the model,
  not the I/O discipline.
- **DSA #1 (Week 1):** freezing a record makes it hashable → usable as a
  dict key — the same hash map idea you used for category totals.
- **Spec-literalness:** every `Driver:` must still match its **Output:**
  block byte-exact.

---

## Quick Recall

Answer from memory before starting Practice:

1. What three methods does `@dataclass` generate from your annotated
   fields?
2. Why is `tags: list[str] = []` rejected, and what replaces it?
3. What does `frozen=True` guarantee, and what is the consequence for a
   dict key (hashability)?
4. When is a plain `dict` still the better answer than a dataclass?
5. What happens if you hand `json.dumps(asdict(record))` a record whose
   field is an Enum member — and what fixes it?
6. In `Ledger.net()`, whose `signed_amount` is called — trace the call
   through the layers.

---

## Practice

Volume follows the SUPPORTING pipeline (Concept → Basic implementation
→ practical exercises → integration exercise → assessment). Work top to
bottom; the theme is the same Expense/Transaction domain, now as data
classes, rebuilding the Lesson 15 model. Full specs live in
`exercises.ipynb`; write solutions in `solution.py` first, then create
the files each exercise lists, then run the **Driver:** cell.

For every exercise you create the files yourself — `solution.py` holds
your working code, then you create the files listed in each **File
tree:**, then run the **Driver:** in the notebook. If a cell shows no
output when you run it, check that the file names and locations match
the File tree byte-for-byte.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | `@dataclass` baseline: auto `__init__`/`__repr__`/`__eq__` from fields + one method |
| E2 | Easy | [REAL-WORLD] | defaults: plain value vs `field(default_factory=...)`; independent mutable state |
| E3 | Easy | [REAL-WORLD] | `frozen=True` + the `Kind` Enum fold: hashable value record, dict-key use |
| M1 | Medium | [REAL-WORLD] | composed `Ledger` dataclass holding a list of records; multi-layer trace |
| M2 | Medium | [REAL-WORLD] | `asdict()` + JSON round trip with an Enum-aware encoder |
| H1 | Hard | [REAL-WORLD] | debug drill: shared mutable default, annotation lie, frozen mutation, enum-vs-string |
| Challenge | Micro Build | [REAL-WORLD] | refactor the Lesson 15 package onto the frozen dataclass model (stretch: `mypy`, `slots`) |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (SUPPORTING → Level 3): independent
implementation of the dataclass model, honest field annotations, the H1
drill resolved with the DEBUGGING protocol — including running `mypy`
on the H1 entry point — and the Challenge running as a frozen-data
Expense Manager core, ready to transfer into Weekly Project 2.
# Lesson 15 — OOP: Classes & Objects (Tier: SUPPORTING)

Stage 2, eighth topic. You have already touched classes three times: you
defined custom exceptions (`class ErrorBadData(Exception)` in Lesson 8),
your library project ships a `custom_error.py`, and every library you
have used (`pathlib.Path`, `json`, `enum`) is built from classes. This
lesson finally teaches the idea directly — *practical, not
syntax-drilled* — because you have been using objects for fifteen
lessons without naming the pattern.

SUPPORTING tier → Level 3 bar: independent implementation and use. One
focused session, then it transfers into Weekly Project 2.

---

## Objective

By the end of this lesson you can:

- Define a class and create **instances** that each carry their own state.
- Write `__init__`, `self`, and methods — and know how a method differs
  from a plain function.
- Annotate every method (the Lesson 14 habit continues):
  `__init__` returns `None`, methods declare their real return type.
- Distinguish instance attributes from class-level constants, and avoid
  the shared-mutable-default trap.
- Implement `__repr__` / `__str__` so objects print readably.
- Compose classes (one object holding others — "has-a") and recognize
  when a plain function would be simpler.
- Use `enum.Enum` as "a class whose members are a fixed set" (AWARENESS
  fold — it feeds the Challenge and Lesson 16).

---

## Why This Matters

You have never written a class yourself, yet you have *used* classes all
along. `Path("data.json")` — what returned it? An **instance** of
`pathlib.Path`. `json.loads(...)` returned a `dict`. `Path.read_text()`
is a **method** — a function that lives on an object and acts on that
object's data.

When you load a transaction, you currently carry its fields around as a
`dict`: `txn["date"]`, `txn["amount"]`. That works. But the moment you
have a *rule* that belongs to a transaction — "an income adds, an
expense subtracts" — that rule is written in a function over here,
while the data sits over there. Classes let you attach the rule to the
data:

```text
dict:           the data  |  the logic  (two places)
Transaction:    the data  +  the logic  (one object)
```

The Stage 2 Expense Manager and Weekly Project 2 are built on exactly
this idea: a `Transaction` that knows how to sign itself, a `Ledger`
that holds many transactions and totals them. Same for your own code
going forward — any domain with "things that have state and rules"
(accounts, sessions, records) is where classes earn their keep.

---

## Mental Model

A class is a **blueprint**; an **instance** is one actual object made
from that blueprint.

```text
class Transaction            Transaction          Transaction
(blueprint)                 /--------------------|--------------------\
                        date="2026-09-04"     date="2026-09-25"   date="2026-10-01"
                        kind="expense"        kind="income"       kind="expense"
                        amount=12.5           amount=100.0        amount=8.0
```

One `class` line, three independent objects. Each instance has its own
copies of the attributes; mutating one never touches the others (that is
the point of E2).

`self` means **"this particular object."** When Python runs
`food.signed_amount()`, it calls `Transaction.signed_amount(food, ...)`
— the instance is passed automatically as the first argument. That is
why every method's first parameter is named `self`, and why you never
pass it yourself.

```text
food.signed_amount()        # Python secretly does:
                            #   Transaction.signed_amount(food)
Transaction.signed_amount   # a plain function taking (self, ...)
food.signed_amount          # a bound method: self is already attached
```

Analogy if it helps: a class is a menu, instances are the plated meals.
The menu lists what exists; each plate is a concrete thing with its own
ingredients.

---

## Core Concept

### 1. Defining a class

```python
class Transaction:
    def __init__(self, date: str, category: str, kind: str, amount: float) -> None:
        self.date = date
        self.category = category
        self.kind = kind
        self.amount = amount

    def signed_amount(self) -> float:
        if self.kind == "income":
            return self.amount
        return -self.amount
```

- `Transaction(...)` calls `__init__` on a brand-new object. `self`
  receives that object; the attributes are stored **on it**.
- `__init__` is the constructor's initializer. It must be annotated
  `-> None` — it does not return the object; the `class` machinery does.
- Methods are functions inside the class. `signed_amount(self)` reads
  *its own* attributes through `self`.

### 2. Creating instances

```python
food = Transaction("2026-09-04", "food", "expense", 12.5)
salary = Transaction("2026-09-25", "salary", "income", 100.0)

print(food.signed_amount())    # -12.5
print(salary.signed_amount())  # 100.0
print(food is salary)          # False — two distinct objects
```

### 3. Instance vs class attributes

Attributes set with `self.` in `__init__` live on **each instance**.
Attributes assigned directly under `class` live on the **class** and are
shared by every instance:

```python
class Account:
    currency = "USD"          # class-level constant, shared

    def __init__(self, name: str, balance: float = 0.0) -> None:
        self.name = name      # instance attribute, per object
        self.balance = balance
```

Reaching for `self.currency` works too (Python finds it on the class),
but the rule of thumb: write `self.` always — except a deliberate
constant that truly never changes, which can sit at class level.

### 4. `__repr__` and `__str__`

Two special methods both produce a string, and Python calls them
automatically when you print an object:

- `__str__` — what `print(obj)` and `f"{obj}"` show (for humans).
- `__repr__` — what `repr(obj)` shows (for developers, debugging).

Use both to buy back readable output — remember Lesson 1's `print`
review, where `<class 'str'>` taught you to give tools a readable
string instead of Python's default.

### 5. Composition: objects that hold other objects

The most useful class pattern in this course is **"has-a"** — one class
holds instances of another:

```python
class Ledger:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.transactions: list[Transaction] = []

    def add(self, txn: Transaction) -> None:
        self.transactions.append(txn)

    def net(self) -> float:
        return sum(txn.signed_amount() for txn in self.transactions)
```

`Ledger` *has* `Transaction`s. No inheritance needed — composition is
preferred by default. Inheritance ("is-a") earns its place when one
class is genuinely a *special case* of another; you already used it:
`ErrorBadData(Exception)` and `Kind(Enum)` are both subclasses.

### 6. Enum — a class with a fixed set (AWARENESS)

A bare string like `"expense"` can be mistyped (`"Expense"`,
`"expences"`) and Python will never complain. `enum.Enum` gives you a
class whose members are a **fixed, named set**:

```python
from enum import Enum

class Kind(Enum):
    INCOME = "income"
    EXPENSE = "expense"

print(Kind.INCOME.value)        # 'income'  — the value you store / compare
print(Kind.INCOME.name)         # 'INCOME'  — the identifier
print(Kind.INCOME is Kind.INCOME)  # True — one object, no typos
```

A wrong name (`Kind.EXPENC`) fails loudly at import time instead of
silently at runtime. One awareness-level exercise (E4), then Lesson 16
gives enum more practice.

### 7. When OOP is unnecessary

OOP is a tool, not a rule. A **stateless pipeline** — data in, data out,
no object holds anything between calls — is cleaner as plain functions:
your Weekly Project 1 stayed class-free on purpose, and it worked.

The signals that say "make it a class": the same data structure appears
with **rules attached to its values** (a transaction that must sign
itself), or you keep passing the *same* group of values into function
after function (a wallet balance crawling through every call). When the
data is just moved around unchanged, a `dict` and functions remain the
simpler answer.

---

## Practical Examples

**1. A transaction that signs itself (used through E1, M1, Challenge):**

```python
class Transaction:
    def __init__(self, date: str, category: str, kind: str, amount: float) -> None:
        self.date = date
        self.category = category
        self.kind = kind
        self.amount = amount

    def signed_amount(self) -> float:
        return self.amount if self.kind == "income" else -self.amount
```

The rule "income adds, expense subtracts" now lives on the object — a
`Ledger` totals a list of them with one line of `sum(...)`.

**2. An account whose report formats itself:**

```python
class Account:
    def __init__(self, name: str, balance: float = 0.0) -> None:
        self.name = name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def status(self) -> str:
        return f"{self.name}: {self.balance:.2f}"
```

```text
>>> alice = Account("alice", 50.0)
>>> alice.deposit(10.0)
>>> alice.status()
'alice: 60.00'
```

**3. A class turning records into a formatted report (M1 ties your L5–L14
muscles to objects):** a `Ledger.report()` that sorts a list of
transactions by date and formats each signed amount to two decimals —
composition (`Ledger` has `Transaction`s) plus the `format`/`sorted`
skills you already own.

**4. A fixed-set state (E4 / Challenge stretch):** `class Kind(Enum)`
replaces the string comparison with a named, typo-proof set while the
stored JSON values stay identical to before — dictionaries and files
still see `"expense"`.

---

## Engineering Notes

- **Annotate every method** — parameter types and return type.
  `__init__` is always `-> None`. This is the Lesson 14 habit, applied
  to classes; the Challenge's `mypy` stretch checks it.
- **Missing `self` is the signature bug of this lesson.** `def
  print_report():` inside a class compiles fine, then explodes with
  `TypeError ... takes 0 positional arguments but 1 was given` the first
  time you call `report.print_report()`. H1 plants exactly this.
- **Never use a mutable class-level default:** `def __init__(self,
  records=[])` shares *one* list across every instance. Use
  `records: list[X] | None = None` and build the list in the body, or
  assign fresh state in `__init__`.
- **Prefer composition (has-a) over inheritance by default.** Reach for
  inheritance when the relationship is genuinely "is-a" (a custom
  exception *is* an `Exception`; `Kind.INCOME` *is* a `Kind`).
- **Keep classes small.** One class = one idea (a `Transaction`, a
  `Ledger`, a `Summary`). A 400-line class is a sign to split.
- **Methods compute and return; the outermost `main()` prints.** This is
  the Lesson 5 boundary kept inside the class — it is what lets your
  drivers call methods and print their results.
- **Supertypes in annotations:** a `list[Transaction]` names the element
  type; `Summary(records)` is not "data of mystery" — it is data you can
  read the type of.

---

## Common Pitfalls

1. **Forgetting `self`** — as a parameter (crashes with `TypeError`) or
   as the prefix (`total = 0` instead of `self.total = 0`, then
   `AttributeError` later). Both are H1 material.
2. **Mutable class-level default** — `records=[]` shared by all
   instances; one object's additions appear in all the others.
3. **`__init__` annotated like a factory** — it returns `None`, not the
   object. Annotate it `-> None`.
4. **Printing instead of returning** in methods — makes the class
   unusable from a driver or another module. Compute and return; the
   caller prints.
5. **OOP for everything** — a stateless two-function pipeline does not
   need a class. Composition of dicts + functions is still the win.
6. **String states that can be mistyped** — `"expense"` vs `"expences"`.
   A `Kind(Enum)` makes the typo a loud, early error.
7. **Annotations drift on classes too** — a method annotated `-> list[str]`
   that returns a dict is the same lying annotation as in Lesson 14,
   only inside a class now. H1 plants two.

---

## Connection to Previous Knowledge

- **Functions (L5):** methods are functions defined inside a class; the
  first parameter (`self`) is filled in automatically by the call
  syntax. Your decomposition habits (`compute and return, main prints`)
  carry straight over.
- **Exception handling (L8):** `class ErrorBadData(Exception)` was your
  *first* inheritance — every custom exception you write subclasses
  something. Inheritance basics here are mostly "recognize what you
  already did."
- **Typing (L14):** every method is annotated — `__init__` `-> None`,
  signatures honest. The H1 "lying annotation" bugs are the same bug,
  moved inside classes.
- **Packages (L13):** classes travel across modules exactly like
  functions — `from transaction import Transaction`; the Challenge
  composes a package of modules around the class model.
- **JSON (L11) / CSV (L12):** loaders still follow the safe-loader
  contract; CSV still uses `newline=""` + `encoding="utf-8"`. Classes do
  not change those rules — they give the data a model.
- **Enum (AWARENESS fold here):** E4 introduces it as a class with a
  fixed member set; Lesson 16 (Dataclass) folds it back in for more
  practice.
- **Spec-literalness:** the driver/Output contract is unchanged — every
  `Driver:` must match its `Output:` block byte-exact.

---

## Quick Recall

Answer from memory before starting Practice:

1. What does `self` refer to, and why do you never pass it in the call?
2. Two accounts made from the same class — what makes their balances
   independent?
3. What is the difference between storing an attribute with `self.x = ...`
   and assigning `x = ...` inside the class body?
4. When is a plain function a better answer than a class?
5. What is composition ("has-a")? Name one object that holds other
   objects in this lesson.
6. Why does `class Kind(Enum)` beat a bare `"expense"` string for
   representing state?

---

## Practice

Volume follows the SUPPORTING pipeline (Concept → Basic implementation
→ practical exercises → integration exercise → assessment). Work top to
bottom; the theme throughout is the Expense/Transaction domain that
seeds Weekly Project 2. Full specs live in `exercises.ipynb`; write
solutions in `solution.py` first, then create the files each exercise
lists, then run the **Driver:** cell.

For every exercise you create the files yourself — `solution.py` holds
your working code, then you create the files listed in each **File
tree:**, then run the **Driver:** in the notebook. If a cell shows no
output when you run it, check that the file names and locations match
the File tree byte-for-byte.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | define a class from a spec: `__init__`, attributes, one method |
| E2 | Easy | [REAL-WORLD] | independent instance state + a mutating method |
| E3 | Easy | [REAL-WORLD] | `__repr__` / `__str__` readable output contract |
| E4 | Easy | [REAL-WORLD] | `enum.Enum` fixed-set members used by a class |
| M1 | Medium | [REAL-WORLD] | composition: `Ledger` holds `Transaction`s; sort/sum/format |
| M2 | Medium | [REAL-WORLD] | composition + delegation: `Session` wraps a `Ledger`, saves JSON |
| H1 | Hard | [REAL-WORLD] | debug drill: 2 lying annotations + 2 runtime bugs in a class |
| Challenge | Micro Build | [REAL-WORLD] | class-based Expense Manager core across a small package (stretch: `mypy`) |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (SUPPORTING → Level 3): independent
implementation of the class model, honest method annotations, the H1
drill resolved with the DEBUGGING protocol, and the Challenge running
as a class-based Expense Manager core — ready to transfer into Weekly
Project 2.
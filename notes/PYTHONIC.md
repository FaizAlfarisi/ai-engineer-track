# Pythonic Thinking

Python is not Java.

Python is not C++.

Python has its own philosophy.

Always prefer writing code the Python way.

---

# The Zen of Python

Run

import this

Read it frequently.

Important principles include:

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Readability counts.
- Errors should never pass silently.

---

# Prefer

Meaningful variable names

List comprehensions (when readable)

Enumerate

Pathlib

Context Managers

Type Hints

Dataclasses

F-strings

---

# Avoid

Deep nesting

Very long functions

Magic numbers

Global variables

Mutable default arguments

Overusing lambda

Overengineering

---

# Working Code vs Good Engineering Code

Working code is the entry ticket, not the finish line.

After it works, ask:

- Are the names honest?
- Is there duplication worth removing?
- Are function boundaries right?
- Is any complexity unnecessary?
- Would a teammate understand it without me explaining?

"The code works. Now improve it." is a normal part of every task.

---

# Idiomatic Python

Prefer

if item in collection

instead of

manual searching loops.

Prefer

for item in items

instead of

for i in range(len(items))

unless index is required.

Prefer

enumerate()

instead of manually incrementing counters.

---

# Exceptions: Scope and Style (Lesson 8)

## Keep try blocks small

Only lines that can fail go inside try.

One try = one failure story.

Same exception type + same response → group them in one try.

Different responses → separate try blocks.

Use else for the success path that must not run when try failed.

Letting tuple unpacking raise counts as validation:

`name, amount = record.split(",")` guards the shape for free.

## EAFP vs LBYL — the decision rule

Neither is wrong. Pick by failure frequency.

EAFP when failure is exceptional:

parsing, dict lookups, file opens, API responses.

Checking first re-implements the operation as a pre-check.

LBYL when failure is the common case and the check is cheap:

`if not line.strip(): continue` beats raising and catching in a hot loop.

If your except fires more often than not,

you wrote LBYL's job in EAFP syntax.

Litmus test: write both.

Whichever happy path reads like prose wins.

---

# File Handling (Lesson 9)

## with closes for you

Open files with `with` — the handle is closed on success, exception,
or early `return`.

It is your `finally`, automated:

`with open(path, "w", encoding="utf-8") as f: ...`

## w truncates — read first

Opening with `"w"` erases the file to zero immediately.

If the data must survive until you have read it, read it before you
reopen it for writing.

## Iterate the handle to stream

`for line in f` yields one line at a time (memory-friendly).

`readlines()` loads the whole file into a list.

Prefer iteration unless you truly need every line at once.

## Strip at the read boundary

A read line keeps its trailing `\n`.

Strip before comparing or splitting cleanly.

(And a second `read()` returns `""` — the cursor is already at the end.)

## Loaders return data — never error strings

A loader returns clean data, or raises, or returns a default.

Do not return a formatted message like "file not found" from a loader —
that mixes the type you promise the caller.

Use `pathlib` for path work (next lesson).

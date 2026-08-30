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
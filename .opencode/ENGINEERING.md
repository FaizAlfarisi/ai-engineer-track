# Engineering Principles

This document defines the engineering standards used throughout the Learning OS.

Every lesson, review, challenge, and project must follow these principles.

They are more important than language syntax.

---

# Philosophy

Programming is not writing code.

Programming is solving problems through software.

Good engineers optimize for maintainability, readability, correctness, and simplicity.

---

# Principle 1 — Readability First

Code is read far more often than it is written.

Always prefer readable code over clever code.

Bad

```python
x=[i*i for i in range(100) if i%2==0]
```

Better

```python
even_squares = [
    number ** 2
    for number in range(100)
    if number % 2 == 0
]
```

---

# Principle 2 — Explicit is Better than Implicit

Avoid hidden behavior.

Prefer obvious code.

Follow the Zen of Python whenever possible.

---

# Principle 3 — Keep It Simple

Simple code is easier to debug.

Simple code is easier to review.

Simple code is easier to maintain.

Avoid unnecessary abstractions.

---

# Principle 4 — Solve Today's Problem

Never build features for imaginary future requirements.

Avoid overengineering.

Follow YAGNI.

---

# Principle 5 — DRY Carefully

Avoid duplicated logic.

Do NOT remove duplication too early.

Duplication is often cheaper than the wrong abstraction.

---

# Principle 6 — Small Functions

Functions should do one thing.

A function that requires many comments is often doing too much.

---

# Principle 7 — Meaningful Names

Variables explain data.

Functions explain actions.

Classes explain concepts.

Avoid

x

data

temp

abc

Prefer

student_name

total_price

is_authenticated

load_dataset()

---

# Principle 8 — Errors Are Information

Never ignore exceptions.

Never hide stack traces during development.

Every error teaches something.

---

# Principle 9 — Optimize Last

Correctness

↓

Readability

↓

Maintainability

↓

Performance

Performance comes last unless profiling proves otherwise.

---

# Principle 10 — Test Your Thinking

Before writing code ask

What is the input?

What is the output?

Edge cases?

Failure cases?

Invalid data?

---

# Principle 11 — Write for Humans

Future teammates are your primary users.

Computers only execute.

Humans maintain.

---

# Principle 12 — Engineering Mindset

Always ask

Why?

What problem does this solve?

What assumptions exist?

Can this fail?

How can it be simplified?

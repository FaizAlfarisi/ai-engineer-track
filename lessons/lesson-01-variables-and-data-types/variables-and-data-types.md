# Lesson 1 — Variables & Data Types

## Learning Objective

By the end of this lesson you can bind names to values, explain the difference
between the major built-in types (`int`, `float`, `str`, `bool`, `None`),
inspect the type of any object, and print formatted output using f-strings.

---

## Motivation

Every program is a machine that transforms data. Variables are how you name that
data so the machine can refer to it. Without them, every calculation would be a
one-off with no memory. Every AI pipeline, API response, and data set you will
touch is built on these five types.

---

## Mental Model

A variable is a **name tag tied to an object**.

In Python, the object holds the value. The name is just a reference to it.
Assignment is "stick this name on that object" — not "store this value in a box".

```
         ┌────────────┐
  age  ──▶│  25        │  ← an int object
         └────────────┘

         ┌──────────────┐
  name ──▶│ "Ada Lovelace"│  ← a str object
         └──────────────┘
```

If you re-assign, you move the name tag to a different object. The old object is
simply dropped (and eventually freed by garbage collection).

---

## Visualization

```
Objects live in memory. Names live in a table (the namespace).

Namespace            Memory
─────────            ────────────────
 age  ───────┐      ┌──────────────┐
             └─────▶│  25 (int)    │
 name ───────┐      └──────────────┘
             └─────▶┌─────────────────┐
                    │ "Ada" (str)     │
                    └─────────────────┘
```

Two names can point at the *same* object. One name can point at *different*
objects over time. This is why "variables don't have types in Python —
objects do."

---

## Theory

### Binding a name

```python
age = 25
name = "Ada"
```

No declaration, no `var`, no type keyword. The first time a name appears on the
left of `=` it is *bound*. Python does not have declarations — the binding
happens the moment the assignment runs.

### Reassignment

```python
age = 25
age = age + 1   # the name `age` now points at a NEW int object (26)
```

### Core types

| Type    | Example literal      | What it is                    |
|---------|----------------------|-------------------------------|
| `int`   | `42`, `-7`, `10**100`| Integer, unlimited precision  |
| `float` | `3.14`, `-0.5`, `2e3`| Double-precision real number  |
| `str`   | `"hello"`, `'hi'`    | Immutable text sequence       |
| `bool`  | `True`, `False`      | Truth value (subclass of int) |
| `None`  | `None`               | The "nothing" singleton       |

### Inspecting types

```python
type(42)          # <class 'int'>
type(3.14)        # <class 'float'>
type("hi")        # <class 'str'>
type(True)        # <class 'bool'>
```

### Division and arithmetic

```python
8 / 5   # 1.6   division ALWAYS returns a float
17 // 3 # 5     floor division
17 % 3  # 2     remainder
5 ** 2  # 25    power
```

### f-strings (formatted string literals)

Since Python 3.6; restrictions on embedded expressions were lifted in 3.12:

```python
age = 25
print(f"I am {age} years old")     # I am 25 years old
print(f"Double: {age * 2}")        # Double: 50
print(f"age = {age}")              # age = 25
```

---

## Examples

```python
price = 9.99
quantity = 3
total = price * quantity
print(f"Total: ${total}")          # Total: $29.970000000000002  (float precision!)
```

```python
first = "Grace"
last = "Hopper"
full_name = first + " " + last     # concatenation
print(full_name)                   # Grace Hopper
```

---

## Best Practice

- `snake_case` for variables and functions (PEP 8).
- `UPPER_SNAKE_CASE` for module-level constants: `MAX_RETRIES = 3`.
- Meaningful names: `tax_rate`, not `t` or `x1`.
- Prefer f-strings over `%`-formatting and `.format()` for readability.
- Use `=` debug specifier in f-strings while developing: `f"{total = }"`.
- Python has no real constants; the convention is the enforcement.

---

## Common Mistakes

1. **Expecting variables to behave like C boxes.** You bind names to objects.
   `a = b` makes both names point at the same object — visible with mutable
   types in later lessons.
2. **Concatenating `str` with numbers** → `TypeError: can only concatenate
   str (not "int") to str`. Use an f-string instead.
3. **Reading an unbound name** → `NameError`. Python resolves names at runtime.
4. **Trusting float equality / arithmetic exactly.** `0.1 + 0.2 != 0.3` because
   floats are binary approximations. Use `round()` or later `Decimal` when exact.
5. **Naming a variable after a builtin** (`type`, `str`, `list`) — shadows the
   builtin and causes confusing errors later.

---

## Applied AI Perspective

- `int`/`float` are the math behind every loss function and gradient step.
- `str` is how models read text; tokenizers split `str` into integer IDs.
- `bool` powers every filter, mask, and early-stop condition in training loops.
- `None` is how APIs signal "no result" (e.g. a missing field in a JSON
  response before you learn about `Optional`).
- `type()` is your first debugging tool when a library returns something you
  did not expect.

---

## Mini Summary

- Assignment binds a name to an object; the object carries the type.
- Core types: `int`, `float`, `str`, `bool`, `None`.
- `type(x)` reveals the object's class.
- `/` returns `float`; use `//` for floor division, `%` for remainder.
- f-strings are the idiomatic way to build output strings.
- `None` is the singleton for "nothing".
- Name variables in `snake_case`; constants in `UPPER_SNAKE_CASE`.
- A `NameError` means a name was used before being bound.
- A `TypeError` often means mixing incompatible types (e.g. `str` + `int`).
- Names in Python are references, not boxes.

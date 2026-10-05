# Engineering Handbook

This handbook contains engineering principles that apply to every project in this Learning OS.

Programming is not about writing code.

Programming is about solving problems in a way that other engineers can understand, maintain, and extend.

---

# Engineering Priorities

Always optimize in this order:

1. Correctness
2. Readability
3. Maintainability
4. Simplicity
5. Performance

Never sacrifice readability for micro-optimizations unless profiling proves it is necessary.

---

# KISS

Keep It Simple.

Avoid unnecessary abstraction.

Avoid clever code.

Prefer boring code.

---

# YAGNI

You Aren't Gonna Need It.

Do not implement features for imaginary future requirements.

Build only what today's requirements demand.

---

# DRY

Don't Repeat Yourself.

Avoid duplicated business logic.

However,

Prefer temporary duplication over the wrong abstraction.

---

# Single Responsibility

Every

- Function
- Class
- Module

should have one clear responsibility.

---

# Separation of Concerns

Business logic

↓

Application logic

↓

Input / Output

↓

Storage

should remain separated whenever possible.

---

# Code Reading

Engineers read far more code than they write.

When reading unfamiliar code:

1. Skim for structure (functions, flow, I/O).
2. Predict what it does before tracing every line.
3. Trace inputs to outputs.
4. Hunt edge cases and failure paths.
5. Judge maintainability: names, boundaries, duplication.
6. Only then suggest refactoring.

Practice this on every debugging drill and code-reading exercise.

---

# Code Review Checklist

Can another engineer understand this?

Can this be tested?

Can this be simplified?

Does this solve the right problem?

---

# Readability Example

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

# Meaningful Names

Variables explain data.

Functions explain actions.

Classes explain concepts.

Avoid: `x`, `data`, `temp`, `abc`

Prefer: `student_name`, `total_price`, `is_authenticated`, `load_dataset()`

---

# Test Your Thinking

Before writing code, ask

What is the input?

What is the output?

Edge cases?

Failure cases?

Invalid data?

---

# Path-First I/O

Paths are `Path` objects, not strings.

- Signatures take `str | Path`; convert first: `path = Path(path)`.
- Open via the object: `path.open(...)`, `path.read_text(...)`,
  `path.write_text(...)` — never bare `open()` on a path.
- Anchor beside the module: `Path(__file__).with_name(...)`.
- Entry points take argv and guard: `def main(argv)` +
  `if __name__ == "__main__":`. No module-level executable code.

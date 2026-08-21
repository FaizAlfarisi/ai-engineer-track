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

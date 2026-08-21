# Code Review Engine (V2)

Review code like a professional senior engineer.

The goal is improvement, not criticism.

Review the learner's REASONING, not just the output. Working output with
broken reasoning is a fail; correct reasoning with a small bug is a win
in progress.

---

# Review Order

1. Correctness

Does the program satisfy the requirements — including edge cases?

---

2. Reasoning

Can the learner explain WHY this approach?
What alternatives were considered?
Ask before telling.

---

3. Logic

Can the algorithm be simplified?

---

4. Readability

Would another engineer understand this?

---

5. Naming

Variables, functions, classes, modules.
Meaningful? Consistent? Shadowing builtins?

---

6. Maintainability

Can this code be extended easily?
Are function boundaries right?
Is duplication controlled?

---

7. Pythonic Style

Idiomatic Python. No Java-style or C-style code.

---

8. Performance

Is optimization necessary? If not, avoid premature optimization.

---

9. Testing & Edge Cases

What should be tested? What edge cases exist?
(Weight grows from Stage 3, when pytest is CORE.)

---

10. Security (when relevant)

Validate input. Avoid unsafe execution. Never leak secrets.

---

# Feedback Format

## Strengths

Three things done well.

---

## Issues

For each issue, use the diagnostic style — do not hand over fixes:

```text
Expected concept:
The function should return a new value without modifying the original.

Observed result:
The original collection is being modified.

Question:
Which operation in your implementation mutates the collection?
```

The learner discovers and fixes the bug. Only apply a fix directly when
the learner has exhausted independent attempts AND consents.

---

## Refactoring Suggestions

Concrete "now improve it" targets: naming, duplication, function
boundaries, complexity, Pythonic style.

---

## Learning Notes

One engineering principle illustrated by this code.

---

## Final Score

Correctness / Logic / Naming / Readability / Maintainability /
Pythonic / Performance / Testing → Overall (0–100)

Also record:

- Hint dependency level used (0–4)
- Which issues were fixed independently vs assisted
- Spec-literalness: exact-match check on required outputs/messages

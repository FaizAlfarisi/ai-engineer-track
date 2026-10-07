# Debugging Handbook

Debugging is a core engineering skill.

Never guess.

Always investigate.

---

# Debugging Protocol

Follow all seven steps, in order. No skipping to the fix.

1. Reproduce the issue.

2. Read the traceback — top line last, but understand every frame.

3. Locate the suspicious area.

4. Form a hypothesis: "I think it fails because..."

5. Test the hypothesis (print, breakpoint(), minimal example).

6. Fix ONE thing. Test again.

7. Explain the root cause in one sentence — not the symptom, the cause.

---

# Debug Report Chain (fill as each bug is fixed)

When stuck, work this chain before asking anything. One job per row —
symptom quotes, never explains; explanation lives only in Cause.

| Step | Content |
|------|---------|
| Symptom | what happened, quoted exactly |
| Trigger | smallest reproduction (command/input) |
| Hypothesis | what you believe, one sentence, labeled as guess |
| Evidence | the probe/test result that confirmed or killed it |
| Cause | the mechanism, one sentence |
| Fix | what changed (diff summary) |
| Proof | suite/test green that verifies it |

---

# Recurring Bug Patterns (personal ledger)

- Per-iteration recomputation inside loops
- Unguarded conversions (`int()`/`float()` on user input)
- Inverted validation logic
- Missing degenerate-path checks (empty input, missing args)
- Paraphrased error messages instead of spec-exact strings

---

# Common Tools

print()

breakpoint()

logging

assert

pytest

---

# Before Asking AI

Can I reproduce it?

Did I read the traceback?

Did I inspect variables?

Can I explain the bug?

---

# Mindset

The computer is almost never wrong.

Your assumptions usually are.

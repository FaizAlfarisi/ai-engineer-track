# Standard Response Format (V2)

Formats for each artifact type. Keep responses natural — a mentor
speaking, not a form being filled.

---

# Lesson

Follows the V2 structure (CURRICULUM.md):

```text
Objective
Why This Matters
Mental Model
Core Concept
Practical Examples
Engineering Notes
Common Pitfalls
Connection to Previous Knowledge   (mandatory)
Quick Recall                       (questions, not answers)
Practice                           (tier-scaled volume)
```

Optional additions ONLY when valuable: visualization, deeper theory,
Applied AI perspective.

---

# Exercise

Each exercise states:

```text
[REAL-WORLD] or [INTERVIEW]
Objective
Rule / Input / Output format       (explicit, standing directive)
Constraints
Hints                              (conceptual only — no code in hints)
```

Volume follows the topic's tier pipeline. Never a fixed 5/3/2 split.

---

# Code Reading Drill

```text
Unfamiliar code block
Questions: what does it do / predict output / find bugs /
           maintainability problems / refactor it / edge cases
```

---

# Debugging Drill

```text
Buggy code + observed misbehavior
Learner runs: Reproduce → Traceback → Locate → Hypothesis → Test → Fix → Explain root cause
AI gives expected-vs-observed framing only, never the fix
```

---

# Weekly Project Brief

```text
Problem (realistic scenario)
Requirements
Constraints
Acceptance Criteria                (checkable)
Stretch Goals                      (optional)
Deliverables
NO step-by-step implementation plan. NO starter code beyond blank files.
```

---

# Stage Project Brief

Same as weekly, plus:

```text
Design decisions the learner must make and justify
Formal review gate at milestones
```

---

# Quiz

```text
Mixed formats: explain · predict output · debug this · code reading · apply
(Multiple choice sparingly)
Then: weak-concept report → targeted practice plan
```

---

# Review

Strengths (3)

Issues (diagnostic style: expected / observed / question — no handed-over fixes)

Refactoring Suggestions

Learning Notes (one engineering principle)

Final Score + hint dependency level + independent-fix ratio

---

# Reflection Prompts

Technical, not generic:

- What decision did you make? Why? What alternative did you consider?
- Which bug took longest to diagnose? What misunderstanding caused it?
- Which concept from a previous lesson did you use?
- What would you change if requirements changed?
- What could you implement fully independently next time?

---

# Progress Update

Topic table rows touched (mastery/hint dependency/last reviewed)

Weekly project log / quiz log / DSA log entries if applicable

Weak concepts needing targeted practice

Next objective

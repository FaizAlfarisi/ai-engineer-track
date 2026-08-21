# DSA Track — Interview Readiness

A lightweight parallel track. One session per week, interleaved with the
main roadmap. Never mixed into stage lessons.

Purpose: interview readiness — not competitive programming mastery.

Every exercise here is `[INTERVIEW]` by definition. Where possible,
problems use real-world-flavored framing (transactions, logs, schedules,
inventory) rather than bare puzzles.

---

# Priority Tiers

## CORE — must become fluent

- Arrays
- Strings
- Hash maps
- Sets
- Two pointers
- Sliding window
- Stack
- Queue
- Binary search
- Basic recursion

Target: recognize the pattern, implement without hints, state time/space
complexity, explain trade-offs verbally.

## SUPPORTING — competent

- Linked lists
- Trees
- BFS / DFS
- Heaps

Target: understand, implement with minimal hints, explain when to use.

## AWARENESS — recognize only

- Advanced dynamic programming
- Advanced graph algorithms
- Advanced tree variants
- Advanced algorithms

Do not drill these. Know they exist and what problems they solve.

---

# Session Pattern (weekly)

```text
1 problem per session (sometimes 2 short ones)
↓
Brute force first (correct beats clever)
↓
Optimize
↓
Complexity comparison (time + space, stated out loud)
↓
Code review (senior-engineer pass)
↓
Explain reasoning verbally (as if in an interview)
```

The verbal explanation is mandatory — interviews are spoken.

---

# Variation Rule

Never repeat the same problem verbatim. Two Sum may be revisited once,
but through variations and new real-world-flavored scenarios. Pattern
recognition across different surface stories is the actual skill.

---

# Difficulty Adaptation

Same rules as the main track:

- Struggling → drop to easier variation of the same pattern.
- Cruising → add constraints, remove hints, raise ambiguity.
- Pattern mastered → move to the next pattern; do not farm easy wins.

---

# Logging

After each session, append a row to `PROGRESS.md` → DSA Log:

| Week | Problems | Pattern(s) | Approach Quality | Complexity Explained? |

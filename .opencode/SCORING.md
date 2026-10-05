# Assessment Engine (V3)

Learning is measured by mastery and transfer — not completion.

---

# Mastery Levels

0 Never seen · 1 Recognizes syntax · 2 Can explain (understands) ·
3 Can implement independently · 4 Can debug and refactor independently ·
5 Can teach someone else.

Completion targets per tier: RULES.md R12. A CORE topic may close its
lesson at Level 3 but stays "in rotation" until Level 4 plus transfer is
observed (concept used unannounced in a later exercise/project).

---

# Exercise Scoring

Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are diagnostic,
not a target to farm. Quiz scored separately; its result feeds the
weak-concept report.

---

# Review Score (bucket-score law — mandatory)

Every review shows the 8-bucket table with each deduction named:

Correctness 25 · Logic 20 · Readability 15 · Naming 10 · Maintainability
10 · Pythonic Style 10 · Testing 5 · Performance 5 → Total 100.

Independent-fix ratio recorded alongside hint dependency level (0–4,
RULES.md R11).

## Assistance Pricing (hint level → bar and buckets)

- Hint-0 solving → eligible for the 95+ bar.
- Hint-1 (conceptual/diagnostic) → bar cap 94.
- Hint-2 (specific) → bar cap 90.
- Reviewer-applied fixes cost their bucket points and are marked
  assisted — never scored as independent.
- **95+ bar:** hint-0 solving, independent H-drills + Challenge, all
  findings fixed independently or retained-with-reason, spec-literal
  clean. Historical band ~90 (`LEARNER.md` anchor) — 95+ is exceptional,
  justified line-by-line.

## Suite Health (vacuous-test detection — mandatory at suite review)

A test that passes on broken code is rejected at build. Every suite
must demonstrate behavior-change sensitivity: break the implementation
on purpose, watch the suite fail, then ship.

---

# Anti-Patterns

Do NOT optimize for: lessons completed, points accumulated, speed.

DO optimize for: independence, transfer, engineering judgment.

Once a topic hits its tier target AND shows transfer — move forward
(RULES.md R6).
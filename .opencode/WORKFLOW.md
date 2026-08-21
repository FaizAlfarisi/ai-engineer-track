# Teaching Workflow (V2)

The workflow is a loop, not a conveyor belt. Steps may be shortened or
skipped when mastery evidence justifies it (see CURRICULUM.md →
Adaptation Rules). What may never be skipped: review of learner code,
reflection, and progress updates.

---

# Session Start (every session)

1. Read `PROGRESS.md` — topic table, weak spots, hint dependency
2. Read `DAILY_LOG.md` — last session, tomorrow's goal
3. Check `ROADMAP.md` — current stage, next topic's tier
4. Determine today's objective:
   - new lesson, OR
   - weekly project session (every 3–4 lessons), OR
   - quiz session (~every 3 lessons), OR
   - targeted practice on a weak concept, OR
   - DSA session (weekly, see `DSA_TRACK.md`)
5. Research the topic per `RESEARCH.md` (effort scales with topic)

---

# New-Lesson Loop

```text
Learn
↓
Recall Previous Knowledge        (quick recall of related topics)
↓
Understand Current Concept       (lesson, questions until understood)
↓
Apply Current Concept            (easy exercises)
↓
Combine With Previous Concepts   (medium exercises)
↓
Debug / Diagnose                 (hard exercises, bug hunts)
↓
Build                            (challenge / micro build)
↓
Review                           (code review, reasoning included)
↓
Assess                           (score + mastery evidence check)
↓
Reflect                          (technical reflection)
↓
Update Mastery                   (PROGRESS.md topic table + DAILY_LOG.md)
```

The volume at each step follows the topic's tier pipeline in
`CURRICULUM.md`. For AWARENESS topics the loop collapses to:
concept → example → small implementation → move on.

---

# Periodic Loops

## Weekly Project (every 3–4 lessons)

```text
Multiple lessons
↓
Project brief (problem, requirements, constraints, acceptance criteria, stretch goals)
↓
Independent build (learner designs and implements)
↓
Formal code review
↓
Assessment against acceptance criteria
↓
Reflection + progress update
```

## Quiz (~every 3 related lessons)

```text
Several related lessons
↓
Quiz (explain / predict output / debug this / code reading / apply)
↓
Weak-concept report
↓
Targeted practice on weak concepts
↓
Re-assess
```

## Stage Project (end of stage)

```text
All stage lessons
↓
Stage project brief
↓
Independent design + build (AI clarifies requirements, reviews only)
↓
Formal review + mastery assessment across stage topics
↓
Stage completion decision (evidence-based, RULES.md Rule 12)
```

## DSA Session (weekly)

Follows `DSA_TRACK.md`. Logged in PROGRESS.md → DSA Log.
Never mixed into a stage lesson.

---

# Session End (every session)

1. Update `PROGRESS.md`: topic table rows touched, hint dependency,
   last-reviewed dates, logs
2. Append `DAILY_LOG.md`: lesson/exercises/challenge/mistakes/insights/
   hints needed/time/tomorrow's goal
3. Git commit (Stage 2 onward): learner runs the commands, AI guides

---

# Spaced Retrieval Rule

When building any exercise set or project brief, check the topic table
for CORE topics not reviewed recently and weave 1–2 of them into the
work naturally — without announcing a review.

---

# When NOT to Teach More

If the learner demonstrates understanding, independent implementation,
successful debugging, and transfer — stop generating exercises for that
topic and move forward. Later lessons will reinforce it implicitly.

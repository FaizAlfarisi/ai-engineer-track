# Teaching Workflow (V2)

The workflow is a loop, not a conveyor belt. Steps may shorten when
mastery evidence justifies it (RULES.md R6). What may never be skipped:
review of learner code, reflection, progress updates.

---

# Session Start (every session)

1. Read `PROGRESS.md` — topic table, weak spots, hint dependency
2. Read `DAILY_LOG.md` — last session, tomorrow's goal
3. Check `ROADMAP.md` — current stage, next topic's tier
4. Determine today's objective:
   - new lesson, OR
   - weekly project (every 3–4 lessons), OR
   - quiz (~every 3 lessons), OR
   - targeted practice on a weak concept, OR
   - DSA session (weekly, see `DSA_TRACK.md`)
5. Research the topic per `RESEARCH.md` (effort scales with topic)
6. Check the topic table for stale CORE topics and weave 1–2 into the
   work unannounced (RULES.md R14)

---

# New-Lesson Loop

```text
Learn → Recall Previous → Understand → Apply Easy → Combine Medium →
Debug / Diagnose Hard → Build Challenge → Review (reasoning included) →
Assess (score + mastery evidence) → Reflect → Update Mastery
```

Volume per step follows the topic's tier pipeline (`CURRICULUM.md`).
For AWARENESS topics the loop collapses to:
concept → example → small implementation → move on.

---

# Periodic Loops

- Weekly Project (every 3–4 lessons): brief → independent build →
  formal review → assessment vs acceptance criteria → reflection +
  progress update.
- Quiz (~every 3 lessons): quiz → weak-concept report → targeted
  practice → re-assess.
- Stage Project (end of stage): brief → independent design + build →
  formal review + mastery assessment → stage completion decision
  (evidence-based, RULES.md R12).
- DSA (weekly): follows `DSA_TRACK.md`; never mixed into stage lessons.

---

# Session End (every session)

1. Update `PROGRESS.md`: topic rows touched, hint dependency,
   misconception lifecycle, last-reviewed dates, logs
2. Append `DAILY_LOG.md`: lesson/exercises/challenge/mistakes/insights/
   hints needed/time/tomorrow's goal
3. Git commit (Stage 2 onward): learner runs the commands, AI guides
4. System files stay frozen during lessons (RULES.md R17) — session data
   goes only into `PROGRESS.md` and `DAILY_LOG.md`
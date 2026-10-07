# Teaching Workflow (V4)

The workflow is a loop, not a conveyor belt. Steps may shorten when
mastery evidence justifies it (RULES.md R6). What may never be skipped:
review of learner code, reflection, progress updates.

---

# Session Start (every session)

1. Environment health check: `python --version`, `pytest --version`,
   key imports for today's topic (`LEARNER.md` Tool Sync). Repair
   before building — never debug the environment mid-lesson.
2. Read `PROGRESS.md` — Current Position block (+ topic rows for
   today's topic only)
3. Read `DAILY_LOG.md` — last session tail + tomorrow's goal
4. Read `LEARNER.md` — profile, queued targets, difficulty knobs
5. Check `ROADMAP.md` — current stage, next topic's tier
6. Determine today's objective:
   - new lesson, OR
   - weekly project (every 3–4 lessons), OR
   - quiz (~every 3 lessons), OR
   - targeted practice on a weak concept, OR
   - DSA session (weekly, see `DSA_TRACK.md`)
7. Research the topic per `RESEARCH.md` (effort scales with topic)
8. Check the topic table for stale CORE topics and weave 1–2 into the
   work unannounced (RULES.md R14)

---

# Sparse-Hours Mode

When sittings are short and sparse:

- End every sitting at a small done-state (green pin, committed).
- Re-ramp via `git log` + last green pin, never by re-reading full logs.
- Split builds across sittings (~40–50 requests each); a sitting that
  overruns context re-transmits everything — stop earlier, resume
  cheaper.

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

# Verification Law

- No score ships without a green-run confirmation (all drivers +
  suites green, read-only where required).
- Projects verify in a temp copy staged with only the files under
  validation.
- Execution is ground truth; reading is hearsay — a read you have not
  executed against is unverified.

---

# Session End (every session)

1. Update `PROGRESS.md`: topic rows touched, hint dependency,
   misconception lifecycle, last-reviewed dates, logs
2. Append `DAILY_LOG.md` (tail-only — anchor on the last ~10 lines):
   lesson/exercises/challenge/mistakes/insights/hints needed/
   Time Studied as `wall / focused / sittings`/tomorrow's goal
3. Retro (3 questions, learner answers): (1) What hurt most — fog or
   difficulty? (2) What rule would have prevented it? (3) Sittings +
   learner-reported token line.
4. Git commit (Stage 2 onward): learner runs the commands, AI guides
5. System files stay frozen during lessons (RULES.md R17) — session data
   goes only into `PROGRESS.md` and `DAILY_LOG.md`
# Teaching Workflow (V5)

The workflow is a loop, not a conveyor belt. Steps may shorten when
mastery evidence justifies it (RULES.md R6). What may never be skipped:
review of learner code, reflection, progress updates.

---

# Session Start (every session)

Run the boot walk in `.opencode/commands/start-session.md` — it is the
single source for load order, state reads, and the environment check.
Then:

1. Determine today's objective:
   - Stage 4 sprint (brief / concept kit / build / review / showcase), OR
   - new lesson, OR
   - weekly project (every 3–4 lessons), OR
   - quiz (~every 3 lessons), OR
   - targeted practice on a weak concept, OR
   - DSA session (weekly, see `DSA_TRACK.md`)
2. Research the topic per `RESEARCH.md` (effort scales with topic).
3. Check the topic table for stale CORE topics and weave 1–2 into the
   work unannounced (RULES.md R14).

---

# Sparse-Hours Mode

When sittings are short and sparse:

- End every sitting at a small done-state (green pin, committed).
- Re-ramp via `git log` + last green pin, never by re-reading full logs.
- Split builds across sittings (~40–50 requests each); a sitting that
  overruns context re-transmits everything — stop earlier, resume
  cheaper.

---

# Model Selection

- Stages 1–3 → New-Lesson Loop (`templates/lesson-template.md`).
- Stage 4 → Sprint Loop + Concept Kit (`templates/concept-kit.md`).
- A Stage 4 concept that is broad enough to need a full lesson may use
  the lesson structure, but the kit is the default.
- `templates/lesson-template.md` is deprecated for Stage 4.

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

# Stage 4 Sprint Loop

A sprint spans several sittings; each sitting is a session with a
single clear objective. **A0 is setup only** — repos, briefs, and
environment — and skips this loop entirely.

```text
Brief → slice plan → Concept Kit → build → verify → code review →
showcase pass → publish checkpoint → retro → next slice
```

1. Read the sprint brief, the current project state (`README.md`,
   `ARCHITECTURE.md`), and `PORTFOLIO.md`. Do not re-read history.
2. Confirm scope + definition of done. The learner writes the slice
   plan; the AI asks questions, never dictates the plan.
3. Teach only the Concept Kit the slice needs (`CURRICULUM.md`).
4. Build — learner writes all code. End every sitting at a green pin or
   a clean stop.
5. Verify tests + demo before review (`Verification Law`).
6. Code review per `REVIEW.md` (8-bucket score still applies).
7. At project end only (A3/B3), after the final sprint's code review:
   showcase pass per `REVIEW.md` + `templates/showcase-review.md` (six
   criteria + five defense questions). Not every sprint.
8. Publish checkpoint: learner updates README/ARCHITECTURE/DECISIONS/
   demo; AI reviews; update `PORTFOLIO.md`; optional LinkedIn draft.
9. Retro + `PROGRESS`/`DAILY_LOG` update.

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
- Stage 4 (portfolio): six sprints across two showcase projects. Each
  sprint ends in a code review; each project ends in a Showcase Pack,
  a showcase gate, and a live defense at project end only (A3/B3)
  (RULES.md R18/R19).
- DSA (weekly): follows `DSA_TRACK.md`; never mixed into stage lessons.

---

# Verification Law

- No score ships without a green-run confirmation (all drivers +
  suites green, read-only where required).
- Projects verify in a temp copy staged with only the files under
  validation.
- Stage 4 showcase projects verify from a clean checkout: tests green,
  server boots, demo command works, `/docs` loads. A screenshot without
  a green run is not evidence.
- Execution is ground truth; reading is hearsay — a read you have not
  executed against is unverified.

---

# Session End (every session)

1. Update `PROGRESS.md`: topic rows touched, hint dependency,
   misconception lifecycle, last-reviewed dates, logs; Stage 4 sprint
   status + showcase gate result
2. Append `DAILY_LOG.md` (tail-only — anchor on the last ~10 lines):
   lesson/exercises/challenge/mistakes/insights/hints needed/
   Time Studied as `wall / focused / sittings`/tomorrow's goal; for
   sprints, the slice shipped + green-run evidence
3. Retro (3 questions, learner answers): (1) What hurt most — fog or
   difficulty? (2) What rule would have prevented it? (3) Sittings +
   learner-reported token line.
4. Git commit (Stage 2 onward; Stage 4: one repo per project): learner
   runs the commands, AI guides. Never commit for the learner.
5. System files stay frozen during lessons (RULES.md R17) — session data
   goes only into `PROGRESS.md` and `DAILY_LOG.md`; Stage 4 may also
   update `PORTFOLIO.md` for status and repo links only.
# Standard Response Format (V5)

Artifact formats live in `templates/` — use the matching template
(lesson, exercise, project/weekly, quiz, review, reflection,
assessment). This file holds the response rules that apply everywhere.

- Respond like a mentor speaking, not a form being filled — but follow
  the requested structure faithfully.
- Exercises open with `## Intent` (what to build + mechanism/why),
  state rule, output format, and constraints explicitly (standing
  directive), labeled `[REAL-WORLD]` / `[INTERVIEW]` / `[DEBUG]`
  (RULES.md R13); **bold the main intent + critical constraints**;
  hints are conceptual only (RULES.md R11); volume and table shape
  follow the topic tier — never a fixed split (RULES.md R6,
  `CURRICULUM.md` pipelines).
- Never announce a review of a previous topic — retrieval is implicit
  (RULES.md R14).
- Projects: no starter code, no step-by-step plans — blank files only
(RULES.md R7/R16). Solutions live where the deliverable lives (no
mandatory solution.py-first, no double-write). CLI briefs carry a Flow
block + house entry shape.
- Code reviews: strengths (3), diagnostic issues (expected/observed/
  question), refactoring suggestions, one learning note, 8-bucket score
  table with named deductions (`REVIEW.md`), plus coverage-check and
  label-check, style, and suite-health lines. Reviewer diagnostics use
  expected/observed/question; learner H1 reports use the 7-row chain
  (`notes/DEBUGGING.md`). The Stage 4 showcase gate is separate and
  never blended into this table.
- Reflection: 4–6 session-grounded prompts + hint + transfer anchors
(`templates/reflection-template.md` bank; `TEACHING.md` Phase 9).
- Notebooks: title-first specs with Type/Coverage/Expected lines;
spec + driver cells, all executed, outputs stripped; no driver
duplication.
- Progress updates: touched topic rows (mastery / hint dependency /
  last reviewed), weak concepts, logs, next objective — honest values.

---

# Visual Communication

Use the cheapest visual that answers fastest; never decorate. Full
cookbook, selection matrix, and anti-overuse rules:
`notes/VISUALIZATION.md`.

## Response ladder

```text
one line → table → ASCII → Mermaid → chart → API docs → screenshot
```

Stop at the first form that answers the question. Escalate only when the
cheaper form genuinely fails.

## When to use what

| Need | Form |
|------|------|
| Flow / architecture / C4-lite | Mermaid `flowchart` (subgraphs = boundaries) |
| Request lifecycle / call order | Mermaid `sequenceDiagram` |
| Schema / tables | Mermaid `erDiagram` or a table |
| State machine | Mermaid `stateDiagram-v2` |
| File tree / module map | ASCII tree |
| Compare options | Table |
| Trend / distribution | Chart (only with real data) |
| Contract check | Swagger `/docs` screenshot or curl transcript |
| Debug reasoning | 7-row chain (`notes/DEBUGGING.md`) |
| Proposed change | diff |

## Anti-overuse

- One visual per concept; at most two per response.
- Diagram labels ≤ 6 words; split anything over ~12 nodes.
- Chat and notebooks: prefer ASCII/tables. Files, GitHub, VS Code: prefer
  Mermaid (native preview).
- No experimental Mermaid features on GitHub; verify the diagram renders.
- Never draw architecture that the code does not implement.

---

# Stage 4 Artifact Formats

- **Sprint Brief** — `templates/sprint-brief.md`.
- **Concept Kit** — `templates/concept-kit.md`.
- **Showcase Pack** — `templates/portfolio-pack.md` (README,
  ARCHITECTURE, DECISIONS, demo, CI, Docker, env, license).
- **Showcase Review** — `templates/showcase-review.md` (6 criteria +
  5 defense questions + gate result).
- Build updates: state the slice done, green-run evidence, next slice.
  No narration of every edit.
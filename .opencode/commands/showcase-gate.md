---
description: Run the Stage 4 project-end (A3/B3) Showcase Pack review and 5-question live defense (V5)
---

You are the **Portfolio Reviewer + Technical Interviewer (Implementor)** (`.opencode/AGENTS.md`, `.opencode/PERSONA.md`). Follow `RULES.md` R18–R19, `CURRICULUM.md` (`# Showcase Pack`), `.opencode/REVIEW.md` (`# Showcase Review`), `.opencode/SCORING.md` (`# Showcase Gate`), `templates/portfolio-pack.md`, and `templates/showcase-review.md`. You never edit system files (`RULES.md` R17).

SHOWCASE GATE WALK (runs at Stage 4 project end `A3` / `B3` only, after the final sprint's `/review-work` code review passes):

1. **Green-Run & Clean-Checkout Prerequisites (`.opencode/WORKFLOW.md` Verification Law):**
   - No showcase pass is possible without a verified green run and working demo. Screenshots alone never count.
   - Verify all prerequisites before grading criteria:
     - [ ] Tests pass green from a clean checkout (`pytest`).
     - [ ] Server boots cleanly; Swagger `/docs` loads.
     - [ ] Documented demo command/URL works locally (including expected `4xx` validation error case).
     - [ ] `Dockerfile` builds and runs reproducibly (when in sprint scope).
     - [ ] CI workflow (tests + lint/type check) is present and green.
     - [ ] `.env.example` documents the config surface; zero secrets exist in git history, code, or logs.

2. **Portfolio Authorship Check (`RULES.md` R18 & `templates/portfolio-pack.md`):**
   - Confirm the complete **Showcase Pack** is present in the project repo:
     `README.md`, `ARCHITECTURE.md` (C4-lite `flowchart` subgraphs + `sequenceDiagram` + `erDiagram`/table), `DECISIONS.md` (5–8 ADR-lite entries: `Context → Decision → Alternative(s) → Consequence`), `docs/demo.md`, CI workflow, `Dockerfile`, `.env.example`, and `LICENSE`.
   - Enforce **R18**: the learner writes all code and the first draft of all portfolio prose in English. You may review structure/accuracy and render Mermaid diagrams from the learner's specification, but you **never** ghostwrite project code or portfolio prose.

3. **Six Showcase Criteria Gate (`PASS` / `NEEDS-WORK` — `RULES.md` R19):**
   - This gate is strictly separate from the 8-bucket code review score. A high code score never substitutes for a showcase pass.
   - Evaluate each criterion using `templates/showcase-review.md`:
     1. **Problem clarity:** A stranger understands the problem, target user, and AI relevance from the first screen of `README.md`.
     2. **Reproducible demo:** Clean checkout → documented install → server boots → demo works locally and in Docker.
     3. **Architecture truth:** Diagrams in `ARCHITECTURE.md` match the actual code and layers (`notes/VISUALIZATION.md` — no aspirational boxes).
     4. **Engineering evidence:** Green tests, vacuous-test check passed, CI badge/workflow, error handling, config hygiene, no secrets.
     5. **Decisions (ADR-lite):** `DECISIONS.md` states honest context, decision, alternatives, and consequences.
     6. **Presentation hygiene:** Clean `README.md`, `LICENSE`, consistent naming, current `/docs` screenshot/transcript in `docs/demo.md`, no broken links.
   - Grade each criterion `PASS` or `NEEDS-WORK`. For any `NEEDS-WORK`, state **one concrete fix**. Any `NEEDS-WORK` blocks the gate until fixed and re-verified.

4. **Live Defense (5 Questions, No Notes — `RULES.md` R19 & `.opencode/REVIEW.md`):**
   - Conduct the live defense. The learner must answer without notes (judged on engineering reasoning, not verbal polish):
     1. *Why this design — what did you reject and why?*
     2. *What breaks first at 10× the data or traffic?*
     3. *What would you change if you rebuilt it?*
     4. *Where is the bottleneck, and how do you know?*
     5. *How did you test it, and what is still untested?*

5. **Gate Result & Portfolio Checkpoint:**
   - Output the completed `templates/showcase-review.md` report (`Gate result: PASS / NEEDS-WORK`, code review score reference, defense `__/5`).
   - Only when all 6 criteria are `PASS`, all 5 defense questions are answered with sound reasoning, and the demo is verified green: update `PROGRESS.md` Stage 4 tracker and `PORTFOLIO.md` showcase status/repo links (`RULES.md` R17), then run `/end-session`.


# Showcase Pack — [Project]

> Mandatory for every Stage 4 project. The learner drafts; the AI reviews
> structure and accuracy. Diagrams are rendered from the learner's
> specification. No ghostwriting.

## Checklist

### README.md

- [ ] Problem: who it is for, what it does, why it matters (first screen).
- [ ] Demo: one command / URL + expected result.
- [ ] Features: only what exists.
- [ ] Quickstart: install, env, run, test — reproducible from a clean
      checkout.
- [ ] API examples: curl or HTTP snippets.
- [ ] Stack + design at a glance.
- [ ] Screenshot/GIF (Swagger `/docs` + one real response).
- [ ] License.

### ARCHITECTURE.md

- [ ] C4-lite context + container (Mermaid `flowchart` subgraphs).
- [ ] One request lifecycle (`sequenceDiagram`).
- [ ] Data model (`erDiagram` or table).
- [ ] Diagrams match the code; no aspirational boxes.
- [ ] Key trade-offs in prose (short).

### DECISIONS.md (ADR-lite, 5–8 entries)

Each entry:

```text
Context → Decision → Alternative(s) → Consequence
```

- [ ] Real decisions only (storage, search backend, validation
      boundary, sync vs async, error strategy).
- [ ] Alternatives are honest, not straw men.

### docs/demo.md

- [ ] curl transcript or GIF.
- [ ] Swagger `/docs` screenshot.
- [ ] Clean-checkout run steps.
- [ ] Error case shown (validation → 4xx).

### Engineering

- [ ] CI workflow: tests + lint/type check, badge.
- [ ] Dockerfile: reproducible local run.
- [ ] `.env.example`: config surface, no secrets.
- [ ] Tests: boundary coverage; vacuous-test check passed.
- [ ] No secrets in git history, code, or logs.

### Presentation

- [ ] Naming consistent.
- [ ] No broken links.
- [ ] Screenshots current.
- [ ] README claims match the demo.

## Defense (5 questions, no notes)

1. Why this design — what did you reject and why?
2. What breaks first at 10× data/traffic?
3. What would you change if you rebuilt it?
4. Where is the bottleneck, and how do you know?
5. How did you test it, and what is still untested?

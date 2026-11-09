# Changelog

## [5.4.1] - 2026-11-09

### Changed

- Generalized the **Adaptive Mechanism Depth & Coverage Contract** globally across
  all lessons and Stage 4 sprints (`CURRICULUM.md`, `ROADMAP.md` Sprints `A1–A3`
  & `B1–B3`, `templates/lesson-template.md`, `templates/concept-kit.md`,
  `templates/code-review-template.md`, `.opencode/TEACHING.md`,
  `.opencode/REVIEW.md`, `.opencode/commands/start-session.md`,
  `.opencode/commands/sprint-slice.md`, and `.opencode/commands/review-work.md`).
- Every distinct mechanism, API, or configuration hook required by any exercise,
  project, or Sprint Brief slice now globally requires its own Why-Chain,
  "when to use vs when NOT to use" decision rule, parameter/constraint/config
  semantics table, runnable worked example, and Coverage Matrix row checked at
  both build time and review time.

## [5.4.0] - 2026-11-09

### Changed

- Extended `CURRICULUM.md` (`## Concept Kit` & `# Coverage Contract`),
  `templates/concept-kit.md`, `.opencode/TEACHING.md`, and
  `.opencode/commands/sprint-slice.md` so Stage 4 Concept Kits enforce the
  Coverage Contract across **both** kit exercises (`E1–H1`) **and** all Sprint
  Brief slice requirements (requiring a Why-Chain, "when to use vs when NOT to
  use" decision rule, parameter/constraint semantics, a runnable worked example
  per distinct mechanism, and a mandatory Section 7 Sprint Slice & Exercise
  Coverage Matrix).
- Expanded `ROADMAP.md` Sprint `A1` topic specification to explicitly require
  Pydantic `Field` constraints & parameter semantics vs custom validators,
  FastAPI `UploadFile`/`File`/`Form` `multipart/form-data` endpoints, and
  registering multiple custom `@app.exception_handler` handlers.

## [5.3.0] - 2026-11-05

### Added

- Six learning-process implementor quick commands across both OpenCode
  (`.opencode/commands/*.md`) and Antigravity (`.agents/skills/*/SKILL.md`) in
  the learner-facing OS: `/start-session`, `/sprint-slice`, `/review-work`,
  `/showcase-gate`, `/dsa-session`, and `/end-session`.

### Changed

- `.opencode/AGENTS.md` indexes the six session commands and adds `.agents/*`,
  `VERSION`, and `CHANGELOG.md` to the implementor's R17 frozen system-file list.
- `verify-os.ps1` verifies the six public implementor commands/skills while
  ensuring private developer rules/skills remain absent from the public OS.

## [5.2.0] - 2026-11-05

### Added

- Antigravity developer quick-command skills (`/dev-start`, `/dev-audit`,
  `/dev-change`, `/dev-profile-sync`, `/dev-release`) in the private developer
  workspace.

### Fixed

- `verify-os.ps1` native `git` stderr handling under `$ErrorActionPreference = "Stop"`
  and verification coverage for the developer quick-command skills.

### Changed

- None to learner-facing behavior.

## [5.1.0] - 2026-11-05

### Added

- Private Antigravity developer workspace and developer-only rule/skill.
- Developer handbook, R1-R19 developer interpretation, behavior contract,
  audit and versioning references, and read-only verifier.

### Changed

- None to learner-facing behavior.

## [5.0.0] - 2026-11-02

### Added

- V5 Stage 4 portfolio model: Showcase Packs, Showcase Reviews,
  `PORTFOLIO.md`, and the R18/R19 showcase gate.

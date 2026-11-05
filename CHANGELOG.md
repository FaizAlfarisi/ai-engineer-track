# Changelog

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

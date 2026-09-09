# Lesson 15 Review — OOP: Classes & Objects

**Date:** 2026-09-09
**Score:** 92/100
**Topics:** classes, instances, `__init__`, `self`, methods vs functions,
instance vs class attributes, `__repr__`/`__str__`, composition (has-a),
delegation, inheritance basics (Enum subclassing, custom exceptions),
when OOP is unnecessary, `enum.Enum`, method annotations.

---

## Strengths

- **Results: all 8 drivers byte-exact** (E1–E4, M1–M2, H1, Challenge),
  verified by running every notebook driver against the real files in a
  temp copy. Challenge side files (`monthly.csv`, `categories.csv`)
  match, and **`mypy main.py` is clean** — the stretch goal.
- **Composition and delegation landed.** `Ledger` holds `Transaction`s;
  `Session` wraps a `Ledger` and forwards calls. The Challenge reuses the
  E1 `Transaction` class across a package without reimplementing it —
  the exact "attach the rule to the data" idea from the lesson.
- **Senior readability choices, unprompted:** `get_date` extracted as a
  named sort key instead of a lambda; `expense/write.py` used
  `csv.DictWriter`; the Challenge `main.py` prints from the CSVs it just
  wrote — one source of truth, no drift between "what we computed" and
  "what we saved".
- **Enum with `is`** (`self.kind is Kind.INCOME`) — the fixed-set
  identity semantics understood, not just copied.
- **H1's drift survives only until a tool reads it.** After the review
  fix, `mypy main_h1.py` reports 0 errors — the lesson's "tools are the
  whole point" message demonstrated on the learner's own file.

## Improvements

- **H1 annotation drift:** `records: list[dict[str, object]]` instead of
  the required exact `list[dict[str, str | float]]`. `object` is the
  "comfortably vague" annotation — every driver still passes, but mypy
  fails on `object`-not-indexable, and the bug report initially listed
  `object` as the goal. Same spec-literalness thread as L14's
  `passing`: read the contract **exactly**, both sides of the signature
  (this time the parameter side slipped — the return was read, the
  parameter wasn't). Fixed at review.
- **Two annotation gaps on first pass:** `display.__repr__` and
  `main_h1.main()` missing `-> None` (both required by the specs).
- **Mypy coverage:** the learner ran `mypy main.py` only; `main_h1.py`
  (and its `summary.py`) were never type-checked by the learner — the
  lie in `summary.py` surfaced only at review. Learner self-flagged this
  ("my bad") at reflection. Lesson carried: run the checker on the
  **whole** entry-point set, not the first file that comes to mind.
- **One external look-up:** the composed-method reuse (delegating
  `add`/`net` through `Session`) sent the learner to Google for the
  approach. Verify-only stays the boundary; "find the pattern" is
  acceptable his first time on a new shape, but the habit watchword
  remains: check logic, don't fetch it.

## Suggestions

- **Read both sides of a signature before coding** — the H1 `object`
  miss came from reading `-> dict[str, float]` and not the parameter.
  A 5-second pass naming each argument's type in plain words.
- **Extend the output-compare habit to tools:** after `mypy`, read the
  *full* file list in the output, not just "Success." If a module was
  checked, it's checked.
- **Multi-layer reading practice:** the learner's own carry-forward —
  get fluent tracing behavior across composed layers (ob objects →
  their methods → the data they hold). DSA #2 and L16's dataclasses are
  natural next practice grounds.
- Keep the AI boundary: "here's my code, check my logic," not "find the
  solution."

## Learning Note

Two ideas demonstrated back-to-back: classes pay off when data and its
rules travel together (a `Transaction` that signs itself), and
annotations are promises — the exact-concrete promise (`str | float`)
survives tools, while the comfortable promise (`object`) survives
drivers but not `mypy`. The learner's strongest artifact was the
Challenge `main.py`: load → objects → compute → write → print-from-what-
you-wrote, a genuinely senior data flow.
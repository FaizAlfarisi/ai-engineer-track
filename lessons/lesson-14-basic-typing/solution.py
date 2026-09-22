# Lesson 14 — Basic Typing (CORE)
# Write all exercise solutions here first, then create the files listed
# in each exercise's File tree, then paste each driver into its notebook
# cell and run it.
# Do not delete or reorder entries below — the notebook cells stay in sync.
# Every function in this lesson is annotated — each parameter and the
# return type.

# E1 — greet.py
# def greet(name: str) -> str: ...
# def score_line(name: str, score: int) -> str: ...

# E2 — stats.py
# def total(values: list[int]) -> int: ...
# def counts(words: list[str]) -> dict[str, int]: ...
# def pair(name: str, score: int) -> tuple[str, int]: ...

# E3 — tips.py
# def tip(total: float, percent: float) -> float: ...
# def print_tips(tips: list[tuple[str, float]]) -> None: ...

# E4 — warn.py
# def score_bonus(score: int) -> int: ...

# E5 — retro.py
# def count_words(text: str) -> int: ...

# M1 — find.py
# def find_by_id(records: list[dict[str, int]], target: int) -> dict[str, int] | None: ...

# M2 — score_tool package
# score_tool/__init__.py (empty)
# score_tool/load.py — load_scores(path: Path) -> dict[str, int]
# score_tool/summarize.py — average(scores) -> float, passing(scores, minimum=60) -> list[str]

# M3 — report.py
# def safe_float(value: str) -> float | None: ...
# def total_scoreable(rows: list[dict[str, str]]) -> float: ...

# H1 — treats package debug drill — bug report
# Four planted bugs: two lying annotations + two runtime defects.
#
# 1. treats/load.py — lying annotation
#    `-> list[dict[str, int]]` claims every record value is an int, but the
#    fixture holds floats (12.5, 4.5, 8.0).
#    Expected: `-> list[dict[str, str | float]]`.
#    Observed: nothing at runtime (annotations are never checked) — the lie
#    only misleads humans and static checkers.
#    Root cause: return type guessed from the shape, not from the data.
#
# 2. treats/monthly.py — lying annotation
#    `def monthly_total(transactions) -> dict[str, int]`: parameter untyped,
#    return claimed ints, but sums are floats (17.0, 8.0).
#    Expected: `(transactions: list[dict[str, str | float]]) -> dict[str, float]`.
#    Root cause: annotated by intuition, never traced what values flow through.
#
# 3. treats/monthly.py — runtime: month slice
#    `txn["date"][5:7]` yields only "09"/"10" — month without year, so labels
#    were wrong and keys collide across years.
#    Expected: "2026-09" / "2026-10" -> printed `2026-09: 17.00`.
#    Fixed: `txn["date"][:7]`.
#
# 4. treats/monthly.py — runtime: overwrite instead of accumulate
#    `out[month] = txn["amount"]` replaced the total, so two September records
#    (12.5 + 4.5) collapsed to 4.5. Expected: summed 17.00.
#    Fixed: `out[month] = out.get(month, 0) + txn["amount"]`.
#
# Extra hardening (not one of the four): load.py checks `path.exists()`
# (LBYL) and catches `json.JSONDecodeError` -> [] — the honest loader shape
# from L9–L11.

# H2 — export.py
# def normalize(rows: list[dict[str, object]]) -> list[dict[str, str | float]]: ...
# def total_qty(rows: list[dict[str, str | float]]) -> float: ...

# CHALLENGE — budget_tool package + main.py
# budget_tool/__init__.py, budget_tool/load.py, budget_tool/compute.py,
# budget_tool/write.py, transactions.json, main.py
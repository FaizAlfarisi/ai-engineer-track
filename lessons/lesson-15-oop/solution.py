# Lesson 15 — OOP: Classes & Objects
# Working space. Draft every solution here FIRST, then create the file
# each exercise lists, then run the Driver cell in exercises.ipynb.
# Keep every method annotated (Lesson 14 habit).

# --- E1: transaction.py ---
# class Transaction with __init__(self, date, category, kind, amount) -> None
# and signed_amount(self) -> float.

# --- E2: account.py ---
# class Account with __init__, deposit(self, amount) -> None, status(self) -> str.

# --- E3: display.py ---
# class Category with __str__(self) -> str and __repr__(self) -> str.

# --- E4: kind.py ---
# class Kind(Enum) and class Transaction using kind: Kind.

# --- M1: ledger.py ---
# class Ledger composing Transaction (from transaction import Transaction).

# --- M2: session.py ---
# class Session composing Ledger (delegation + JSON save).

# --- H1: bug report ---
# summary.py + main_h1.py. After each fix, report:
#   Bug 1 (annotation lie: __init__ records type)
#     expected:   records: list[dict[str, str | float]]
#     observed:   records: list[dict[str, int]]
#   Bug 2 (annotation lie: net_by_month return type)
#     expected:   dict[str, float]
#     observed:   list[str]
#     root cause: ...
#     ...
#   Bug 3 (runtime: totals overwrite)
#     expected:   totals[month] should use dict.get method
#     observed:   totals[month] = 4.5
#     root cause: overwrite totals[month] instead of sum it
#     ...
#   Bug 4 (runtime: missing self)
#     expected:   self as param
#     observed:   error self not defined
#     root cause: summary.py, print_report didn't pass self
#     ...


# --- Challenge: expense package + main.py ---
# expense/load.py, expense/compute.py, expense/write.py, main.py.
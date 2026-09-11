# Lesson 16 — Dataclass
# Working space. Draft every solution here FIRST, then create the file
# each exercise lists, then run the Driver cell in exercises.ipynb.
# Keep every field and method annotated (Lesson 14 habit).

# --- E1: record.py ---
# @dataclass Transaction with annotated fields date (str), category (str),
# kind (str), amount (float) and signed_amount(self) -> float.
# No explicit __init__ / __repr__ / __eq__ — the decorator generates them.

# --- E2: category.py ---
# @dataclass Category with name (str), budget (float = 0.0),
# tags (list[str] = field(default_factory=list)).

# --- E3: kind.py ---
# class Kind(Enum) with INCOME = "income", EXPENSE = "expense".
# @dataclass(frozen=True) Transaction using kind: Kind;
# signed_amount compares with `self.kind is Kind.INCOME`.

# --- M1: ledger.py ---
# @dataclass Ledger(owner: str, transactions=field(default_factory=list))
# with add(self, txn) -> None, net(self) -> float, report(self) -> str —
# composing kind.Transaction.

# --- M2: serialize.py ---
# kind_encoder(obj) and save_json(path: Path, transactions) -> None:
# [asdict(t) for t in transactions] + json.dumps(..., default=kind_encoder).

# --- H1: bug report ---
# budget.py + main_h1.py + budget.json. After each fix report:
#   Bug 1 (import-time ValueError: shared mutable default list)
#     expected:   transactions = field(default_factory=list)
#     observed:   transactions: list[Transaction] = []   # ValueError
#     root cause: ...
#   Bug 2 (annotation lie: amount: str on float data)
#     expected:   amount: float
#     observed:   amount: str
#     root cause: ...
#   Bug 3 (runtime: FrozenInstanceError from mark_spent mutation)
#     expected:   mark_spent returns a new Transaction
#     observed:   self.amount = extra on a frozen record
#     root cause: ...
#   Bug 4 (logic: kind compared to the string "income", never True)
#     expected:   self.kind is Kind.INCOME
#     observed:   self.kind == "income"
#     root cause: ...
#   Final check: python -m mypy main_h1.py  ->  no errors.

# --- Challenge: expense package + main.py (refactor of Lesson 15) ---
# expense/load.py, expense/compute.py, expense/write.py, main.py —
# same interfaces as Lesson 15; the model is now kind.Transaction (frozen)
# loaded with Kind(record["kind"]) and signed by signed_amount().
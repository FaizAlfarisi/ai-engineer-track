# Weekly Project 2 — Expense / Transaction Manager CLI

## Type

[REAL-WORLD]

## Problem

A freelancer wants to know exactly where their money goes. They type a
few short commands each day (`lunch today`, `salary this month`) and the
tool must remember everything, survive restarting, and produce two
reports they can open in a spreadsheet: net by month, and net by
category. Reliability rule: a bad command or a corrupt data file must
never crash with a traceback — always a clear message.

This project continues directly from what you already built: the frozen
`Transaction` dataclass + `Kind` enum from L16, the Expense Manager core
from the L15/L16 Challenges, and the CSV/JSON/typed-package discipline
of L12–L14. This is the **mandatory Stage 2 evidence**.

## Requirements

Data model is the L16 frozen model — no other internal representation:

- `Transaction` dataclass: `date: str`, `category: str`, `kind: Kind`,
  `amount: float`, method `signed_amount(self) -> float` (income
  positive, expense negative).
- `Kind` enum: `INCOME = "income"`, `EXPENSE = "expense"`.
- Persistence: `transactions.json` — a JSON array of records
  (`date`, `category`, `kind`, `amount`) written via `asdict` + the
  enum-aware encoder, exactly like L16's `serialize.py`. Loaded on every
  run; saved after every mutation.

### Commands (exactly four — the main goal)

All run as `python main.py ...` from the project folder.

1. **add** — `python main.py add DATE CATEGORY KIND AMOUNT`
   - `DATE` must parse as `YYYY-MM-DD`; `CATEGORY` non-blank;
     `KIND` is `income` or `expense`; `AMOUNT` a positive number.
   - Appends the transaction, saves the file, prints the confirmation
     (exact format below).
2. **list** — `python main.py list`
   - Prints all transactions sorted by date (stable for ties — the
     order they were added), exact format below.
3. **report monthly** — writes `monthly.csv` (columns `month,net`),
   rows sorted ascending by month, signed net values, two decimals.
   Then prints the CSV rows it wrote (read back from the file).
4. **report categories** — writes `categories.csv` (columns
   `category,net`), rows sorted ascending by category name, signed.
   Then prints the CSV rows it wrote (read back from the file).

## Development environment (folded-in SUPPORTING topic — do this yourself)

- Create a virtualenv for this project and use it for all runs and
  checks: `python -m venv .venv`
- Activate it (Windows: `.venv\Scripts\activate`).
- Add the type checker as the only dependency: `python -m pip install mypy`
- Freeze the environment so it is reproducible:
  `python -m pip freeze > requirements.txt`
- Commit `requirements.txt`; **`.venv` must be gitignored.**
- Run type checks with the venv's checker and the whole-check flag:
  `.venv\Scripts\python -m mypy main.py`
- Rule: **ask before installing anything beyond `mypy`.** This project
  needs no other third-party packages.

## Constraints

- Use only Stage 2 knowledge. No new libraries beyond `mypy` (stdlib
  covers everything: `dataclasses`, `enum`, `json`, `csv`, `pathlib`,
  `sys`, `datetime`).
- The frozen `Transaction` + `Kind` model is the single source of truth.
- No error-string returns from loaders/helpers — raise on corrupt data,
  return a *shape* (empty list) on missing file. Never mix types.
- Edge cases handled, never a raw crash (see Test Matrix).
- Fully annotated; `mypy main.py` clean.
- Prints come from the data that was just written (read the CSV back),
  never from in-memory values — one source of truth.
- Git commit at meaningful milestones; `git log` shows more than one
  commit.
- NO step-by-step plan provided. Design decisions are yours; the AI
  clarifies requirements and reviews code — it never implements.

## Spec output blocks (frozen — byte-exact)

**Seed data fixture** — this exact file must exist for the acceptance
runs and the Test Matrix (name it `transactions.json` in the project
folder):

```json
[
  {"date": "2026-09-01", "category": "salary", "kind": "income", "amount": 5000000.0},
  {"date": "2026-09-02", "category": "food", "kind": "expense", "amount": 15000.0},
  {"date": "2026-09-03", "category": "transport", "kind": "expense", "amount": 10000.0},
  {"date": "2026-09-10", "category": "salary", "kind": "income", "amount": 2500000.0},
  {"date": "2026-09-11", "category": "food", "kind": "expense", "amount": 20000.0},
  {"date": "2026-08-28", "category": "rent", "kind": "expense", "amount": 1000000.0}
]
```

`python main.py list` with the seed fixture installed (one line per
transaction, format rule:
`f"{index}. {date} {category:<10} {kind:<8} {signed_amount:>11.2f}"`):

```text
Transactions (6):
1. 2026-08-28 rent       expense  -1000000.00
2. 2026-09-01 salary     income    5000000.00
3. 2026-09-02 food       expense    -15000.00
4. 2026-09-03 transport  expense    -10000.00
5. 2026-09-10 salary     income    2500000.00
6. 2026-09-11 food       expense    -20000.00
```

`python main.py add 2026-09-12 lunch expense 25000` (seed fixture
installed):

```text
Added: 2026-09-12 lunch expense 25000.00
```

`python main.py report monthly` (seed fixture installed):

```text
Wrote monthly.csv
2026-08,-1000000.00
2026-09,7455000.00
```

…and the file `monthly.csv` must contain exactly:

```text
month,net
2026-08,-1000000.00
2026-09,7455000.00
```

`python main.py report categories` (seed fixture installed):

```text
Wrote categories.csv
category,net
food,-35000.00
rent,-1000000.00
salary,7500000.00
transport,-10000.00
```

…and the file `categories.csv` must contain exactly:

```text
category,net
food,-35000.00
rent,-1000000.00
salary,7500000.00
transport,-10000.00
```

## Test matrix (self-validate before asking for review)

Run against the seed fixture unless stated otherwise. A clean result is
an exit and output identical to the expected column; an "error" case is
the two-line scoped message on **stderr** with **exit code 1** and no
traceback.

Error contract (reconciled with the build's chosen design):
`bad request:` for bad input, `corrupt data:\nfailed to load existing
data | <detail>` for unreadable/shape-invalid data, `unexpected error:`
for anything else (should stay rare). The detail line states the
problem plainly (no embedded severity token — the prefix already says
it). Errors go to **stderr**; happy-path output goes to **stdout**.

| # | Command / setup | Expect |
|---|-----------------|--------|
| T1 | `list` | The `list` block above, byte-exact |
| T2 | `add 2026-09-12 lunch expense 25000` then `list` | `Added:` block above; then `Transactions (7):` with the lunch row as item 7 (`2026-09-12 lunch      expense    -25000.00`), sorted into place |
| T3 | `report monthly` / `report categories` | Both write-print blocks above; CSV files byte-exact |
| T4 | No data file (delete `transactions.json`) | `list` → `Transactions (0):` (no crash); `report monthly` → `Wrote monthly.csv` + only the header row in the file and print |
| T5 | `add 2026-09-12 lunch expense 25000` with no data file | `Added:` block; `transactions.json` is created |
| T6 | (no arguments) | stderr, exit 1: `bad request:\nempty input` |
| T7 | `add 2026-13-40 food expense 10000` | stderr, exit 1: `bad request:\ninvalid date '2026-13-40' (use YYYY-MM-DD)` |
| T8 | `add 2026-09-12 food credit 10000` | stderr, exit 1: `bad request:\nunknown kind 'credit' (use income or expense)` |
| T9 | `add 2026-09-12 food expense abc` | stderr, exit 1: `bad request:\ninvalid amount 'abc' (must be a positive number)` |
| T10 | `add 2026-09-12 food expense -5000` | stderr, exit 1: `bad request:\namount must be greater than 0` |
| T11 | `add 2026-09-12 " " expense 10000` (a whitespace-only category — the shell strips `""` before `sys.argv`, use `" "` instead) | stderr, exit 1: `bad request:\ncategory cannot be empty` |
| T12 | `add` with no arguments | stderr, exit 1: `bad request:\nusage: add DATE CATEGORY KIND AMOUNT` |
| T13 | Overwrite `transactions.json` with the literal text `{bad json` then `list` | stderr, exit 1: `corrupt data:\nfailed to load existing data | Expecting value: ...` (detail = the JSON parser message), no traceback |
| T14 | `add 2026-9-1 food expense 100` | **Must be rejected** (`invalid date '2026-9-1' (use YYYY-MM-DD)`): only the canonical zero-padded form may be stored, so string sorting stays chronological |
| T15 | `bananas` (unknown command) | stderr, exit 1: `bad request:\nunknown command 'bananas'` |
| T16 | `python -m mypy main.py` | `Success: no issues found in 1 source file` |
| T17 | `git status` after setup | `.venv` and `data/*.csv` NOT tracked; `requirements.txt` and `data/transactions.json` ARE tracked |

Contract rule: the wording above IS the spec. If you deliberately change
a message, update this matrix in the same commit — a spec you own beats
a spec you silently drift from.

## Acceptance Criteria

- [ ] All of T1–T15 pass exactly as specified.
- [ ] Data survives restarts: add, run `list` in a separate command
      line, transaction is still there.
- [ ] Reports are byte-exact CSVs the freelancer can open in a
      spreadsheet.
- [ ] Frozen `Transaction` model used end-to-end (no `dict` records in
      the command layer).
- [ ] `mypy main.py` clean; everything annotated.
- [ ] `git log` shows more than one commit.
- [ ] Decisions Log below is filled during the build (Why + Alternative
      columns), and a technical reflection is written.

## Stretch goals (optional, detailed)

Do the main goal first. Each stretch is independent and optional.

- **SG1 — `net` summary:** `python main.py report summary` prints a
  three-line block computed from the loaded transactions:

  ```text
  Summary:
  income:  7500000.00
  expense: -1045000.00
  net:     6455000.00
  ```

  Validation: run with the seed fixture — must be byte-exact (income =
  sum of income amounts with `+`, expense = sum of expense amounts with
  `-`, net = net of all). Decide and document: does `expense:` show a
  negative number (as above, `-1045000.00`) or a positive magnitude?
  Pick one, say why in the Decisions Log, keep it consistent.

- **SG2 — `--seed` sampler:** `python main.py --seed` creates a
  fixed, documented sample dataset when `transactions.json` is missing
  and prints `Seeded: 40 transactions`. The exact 40 records live in
  your decision log (or a `seed.py`), one run reproduces the exact same
  file every time, and `list` after seeding is deterministic. Use it to
  make your own T-cases for reports beyond the official matrix.

- **SG3 — `report weekly`:** writes `weekly.csv` (columns `week,net`),
  grouping by ISO week (`YYYY-Www` — use `datetime.isocalendar()`),
  sorted ascending, signed, two decimals, printed-from-file like the
  other reports. With the seed fixture the expected rows are
  `2026-W35,-1000000.00`, `2026-W36,4975000.00` and
  `2026-W37,2480000.00` (2026-08-28 is week 35; 2026-09-01..03 are
  week 36; 2026-09-10..11 are week 37 — verify with
  `datetime.isocalendar()` yourself in the decision log).

## Deliverables

- Source code in this folder (`main.py` starts blank — learner writes
  everything). A small package split (e.g. `expense/` for
  load/compute/write, like L13–L16) is expected where it genuinely
  helps; not mandatory if a single well-structured `main.py` reads
  better. Decision logged.
- `transactions.json` fixture, `requirements.txt`, `.gitignore`
  (containing `.venv` and cache dirs).
- Short README (how to run, what the reports mean).
- Technical reflection (template style) + the Decisions Log below.

## Decisions Log (filled by learner during build)

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
|          |     |                        |
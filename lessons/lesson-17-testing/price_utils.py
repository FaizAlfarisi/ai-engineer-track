"""Small utility functions for the price/expense CLI theme.

This module is the "code under test" for Lesson 17. A previous team
wrote it; your job this lesson is to write the test suite it deserves.

The functions are deliberately small. The interesting parts are the
contracts:

- `load_amounts` never crashes: a missing file is `[]`, a junk line is
  skipped, numbers are returned as dirty floats.
- `report_from_file` fails loudly: a missing file raises
  `FileNotFoundError` instead of returning anything.
"""

from pathlib import Path


def format_price(amount: float) -> str:
    """Return a plain number with two decimals and thousands separators."""
    return f"{amount:,.2f}"


def is_affordable(balance: float, price: float) -> bool:
    """True when the price can be paid from the balance."""
    return price <= balance


def categorize(amount: float) -> str:
    """Classify an amount: positive income, negative expense, zero stays zero."""
    if amount > 0:
        return "income"
    if amount < 0:
        return "expense"
    return "zero"


def signed(amount: float) -> str:
    """Format an amount with an explicit sign for display."""
    return f"{amount:+.2f}"


def load_amounts(path: Path) -> list[float]:
    """Read one number per line.

    A missing file is a normal empty dataset (`[]`). Blank or unparseable
    lines are skipped, never an error.
    """
    if not path.is_file():
        return []
    amounts: list[float] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        try:
            amounts.append(float(line))
        except ValueError:
            continue
    return amounts


def report_from_file(path: Path) -> str:
    """Build a signed report from `name,amount` lines.

    A missing file raises `FileNotFoundError` — a report needs the file,
    so this fails fast instead of pretending.
    """
    if not path.is_file():
        raise FileNotFoundError(f"report file not found: {path}")
    lines: list[str] = []
    net = 0.0
    for raw in path.read_text(encoding="utf-8").splitlines():
        name, _, amount = raw.partition(",")
        name = name.strip()
        amount = amount.strip()
        if not name or not amount:
            continue
        value = float(amount)
        net += value
        lines.append(f"{name}: {value:+.2f}")
    lines.append(f"net: {net:+.2f}")
    return "\n".join(lines) + "\n"


def print_report(pairs: list[tuple[str, float]]) -> None:
    """Print one signed line per (name, amount) pair."""
    for name, amount in pairs:
        print(f"{name}: {signed(amount)}")
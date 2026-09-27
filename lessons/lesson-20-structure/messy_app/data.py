"""Store inventory for the H1 drill — read, don't fix the data."""

import csv
from pathlib import Path

def get_items() -> list[dict]:
    data_path = Path(__file__).parent / "prices.csv"
    with data_path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [
        {"id": int(r["id"]), "name": r["name"], "price": float(r["price"])}
        for r in rows
    ]

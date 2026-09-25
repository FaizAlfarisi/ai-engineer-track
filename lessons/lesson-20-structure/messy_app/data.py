"""Store inventory for the H1 drill — read, don't fix the data."""

import csv


def get_items() -> list[dict]:
    with open("messy_app/prices.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [
        {"id": int(r["id"]), "name": r["name"], "price": float(r["price"])}
        for r in rows
    ]

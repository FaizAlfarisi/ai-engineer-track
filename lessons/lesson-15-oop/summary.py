import json
from pathlib import Path


class Summary:
    def __init__(self, records: list[dict[str, str | float]]) -> None:
        self.records = records

    def net_by_month(self) -> dict[str, float]:
        totals: dict[str, float] = {}
        for txn in self.records:
            month = str(txn["date"])[:7]
            totals[month] = totals.get(month, 0.0) + float(txn["amount"])
        return totals

    def print_report(self) -> None:
        for month, total in self.net_by_month().items():
            print(f"{month}: {total:.2f}")
import csv
from pathlib import Path

def write_summary(path: Path, totals: dict):
    field_names = ["category", "total"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(field_names)
        for category, total in sorted(totals.items()):
            writer.writerow([category,f"{total:.2f}"])
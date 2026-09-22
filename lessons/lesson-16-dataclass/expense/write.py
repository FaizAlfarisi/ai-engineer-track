import csv
from pathlib import Path

def write_summary(path: Path, totals: dict[str, float], colname: str) -> None:
    fieldnames = [colname, "total"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for key in sorted(totals.keys()):
            v = totals[key]

            writer.writerow({
                colname: key,
                "total": f"{v:.2f}"
            })
        
from pathlib import Path
import csv

def write_summary(path: Path, totals: dict[str, float], colname: str) -> None:
    fieldnames = [colname, "total"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for key in sorted(totals.keys()):
            value = totals[key]
            
            writer.writerow({
                colname: key,
                "total": f"{value:.2f}"
            })
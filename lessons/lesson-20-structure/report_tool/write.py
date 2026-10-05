import csv
from pathlib import Path


def write_summary(totals: dict[str, float], path: str) -> None:
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["team", "total"])
        writer.writeheader()
        for team in sorted(totals):
            writer.writerow({"team": team, "total": f"{totals[team]:.2f}"})

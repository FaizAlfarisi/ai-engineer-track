import csv


def load(path: str) -> list[dict]:
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for r in rows:
        totals[r["team"]] = totals.get(r["team"], 0.0) + float(r["score"])
    return totals

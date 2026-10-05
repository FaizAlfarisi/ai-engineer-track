def summarize(rows: list[dict]) -> dict[str, float]:
    totals: dict[str, float] = {}
    for r in rows:
        totals[r["team"]] = totals.get(r["team"], 0.0) + float(r["score"])
    return totals

from load import load


def totals(rows):
    print(f"read {len(rows)} rows")
    out = {}
    for r in rows:
        out[r["team"]] = out.get(r["team"], 0.0) + float(r["score"])
    print(out)
    return out

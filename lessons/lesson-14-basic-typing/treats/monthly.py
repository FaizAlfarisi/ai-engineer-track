def monthly_total(transactions: list[dict[str, str | float]]) -> dict[str, float]:
    out = {}
    for txn in transactions:
        month = txn["date"][:7]
        out[month] = out.get(month, 0) + txn["amount"]
    return out
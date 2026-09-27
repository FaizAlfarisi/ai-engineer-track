CARTS = {
    "morning": [2.50, 1.80, 3.20],
}


def line_total(items: list[float]) -> float:
    total = 0.0
    for price in items:
        total += price
    return total

def apply_discount(price: float, percentage: int) -> float:
    discount = price * percentage / 100
    return round(price - discount, 2)
    
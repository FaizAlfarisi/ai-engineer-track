from shop.carts import CARTS, line_total


def summary() -> str:
    items = CARTS["morning"]
    return f"cart: {len(items)} items, total {line_total(items):.2f}"

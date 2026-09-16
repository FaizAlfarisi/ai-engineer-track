"""Budget helpers for the Lesson 17 H1 debug drill."""


def total_spend(amounts: list[float]) -> float:
    """Sum of amounts (negative values stay negative and count against it)."""
    return sum(amounts)


def top_spend(items: list[tuple[str, float]]) -> tuple[str, float]:
    """Return the (name, amount) pair with the largest amount."""
    return max(items, key=lambda pair: pair[1])
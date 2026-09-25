from .data import get_items


def report() -> str:
    return f"items: {len(get_items())}"


print(report())

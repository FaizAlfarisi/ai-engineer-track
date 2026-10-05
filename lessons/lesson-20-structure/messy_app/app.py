from messy_app.data import get_items


def report() -> str:
    return f"items: {len(get_items())}"


if __name__ == "__main__":
    print(report())

import csv


def write_csv(items: list[dict], path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "stock"])
        writer.writeheader()
        writer.writerows(items)

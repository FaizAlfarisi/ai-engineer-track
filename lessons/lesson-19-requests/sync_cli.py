import csv
import json
import sys
from pathlib import Path
from typing import Any

import requests
import local_api


Item = dict[str, Any]


def merge(network: list[Item], cached: list[Item]) -> tuple[list[Item], int, int]:
    merged: dict[int, Item] = {item["id"]: item for item in cached}

    network_ids = set()

    for item in network:
        item_id = item["id"]
        network_ids.add(item_id)
        merged[item_id] = item

    kept = sum(1 for item in cached if item["id"] not in network_ids)
    fresh = len(network)

    items = sorted(merged.values(), key=lambda item: item["id"])

    return items, fresh, kept


def load_cache() -> list[Item]:
    path = Path("sync.json")

    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))
    return data.get("items", [])


def save_json(items: list[Item]) -> None:
    Path("sync.json").write_text(
        json.dumps({"items": items}, indent=2),
        encoding="utf-8",
    )


def save_csv(items: list[Item]) -> None:
    fieldnames = ["id", "name", "price", "stock"]

    with Path("sync.csv").open(
        "w",
        newline="",
        encoding="utf-8",
    ) as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in items:
            writer.writerow(
                {
                    "id": item["id"],
                    "name": item["name"],
                    "price": item["price"],
                    "stock": item["stock"],
                }
            )


def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] != "sync":
        print("usage: python sync_cli.py sync", file=sys.stderr)
        raise SystemExit(1)

    api = local_api.LocalAPI()

    try:
        response = requests.get(
            f"{api.base}/items",
            timeout=30,
        )
        response.raise_for_status()
        network = response.json().get("items", [])
    finally:
        api.stop()

    cached = load_cache()
    items, fresh, kept = merge(network, cached)

    save_json(items)
    save_csv(items)

    print(f"Sync: {len(items)} items (fresh {fresh}, cached {kept})")


if __name__ == "__main__":
    main()

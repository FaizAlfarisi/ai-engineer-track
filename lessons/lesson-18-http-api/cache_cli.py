import json
import csv
import sys
from pathlib import Path
import urllib.request
import urllib.error
import local_api
from typing import Any

type Item = dict[str, Any]

def merge(network: list[Item], cached: list[Item]) -> tuple[list[Item], int, int]:
    merge_dict: dict[int, Item] = {}
    
    # handle cached first so the network could override it
    cached_ids = set()
    for item in cached:
        item_id = item["id"]
        cached_ids.add(item_id)
        merge_dict[item_id] = item
        
    # handle network with override
    for item in network:
        item_id = item["id"]
        merge_dict[item_id] = item
        
    fresh_count = len(network)
    network_ids = {item["id"] for item in network}
    kept_count = len(cached_ids - network_ids)
    
    sorted_items = sorted(merge_dict.values(), key=lambda x: x["id"])
    
    return sorted_items, fresh_count, kept_count

def load_json() -> list[Item]:
    path = Path("cache.json")
    if not path.exists() or not path.is_file():
        return []
    
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data.get("items", [])
    except json.JSONDecodeError:
        return []

def save_json(data: list[Item]):
    path = Path("cache.json")
    path.write_text(json.dumps({"items": data}, indent=2), encoding="utf-8")

def save_csv(data: list[Item]):
    path = Path("cache.csv")
    fieldnames = ["id", "name", "price", "stock"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({
                "id": item["id"],
                "name": item["name"],
                "price": item["price"],
                "stock": item["stock"],
            })
            
            
def main() -> None:
    if len(sys.argv) != 2 or sys.argv[1] != "--refresh":
        print("Usage: python cache_cli.py --refresh", file=sys.stderr)
        sys.exit(1)
    
    api = local_api.LocalAPI()
    
    network_data = []
    
    try:
        with urllib.request.urlopen(f"{api.base}/items", timeout=30) as r:
            response_json = json.loads(r.read().decode("utf-8"))
            network_data = response_json.get("items", [])
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e}")
        api.stop()
        return
    finally:
        api.stop()
    
    cached_data = load_json()
    items, fresh, cached = merge(network=network_data, cached=cached_data)
    save_json(items)
    save_csv(items)
        
    print(f"Cache: {len(items)} items (fresh {fresh}, cached {cached})")
    return

if __name__ == "__main__":
    main()
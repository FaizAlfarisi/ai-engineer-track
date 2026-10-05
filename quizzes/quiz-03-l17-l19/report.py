import csv
import requests
from pathlib import Path

def build_search_url(base: str, q: str) -> str:
    return requests.Request("GET", url=base + "/search", params={"q": q}).prepare().url

def merge(network: list[dict], cached: list[dict]) -> tuple[list[dict], int, int]:
    merged_data: dict[int, dict] = {item["id"]: item for item in cached}
    
    network_ids = set()
    for item in network:
        item_id = item["id"]
        merged_data[item_id] = item
        network_ids.add(item_id)
        
    kept = sum(1 for item in cached if item["id"] not in network_ids)
    fresh = len(network)
    
    items = sorted(merged_data.values(), key= lambda item: item["id"])
    
    return items, fresh, kept

def save_csv(items: list[dict], path: Path) -> int:
    field_names = ["id", "name", "price", "stock"]
    count_rows = 0
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        
        for item in items:
            writer.writerow({
                "id": item["id"],
                "name": item["name"],
                "price": item["price"],
                "stock": item["stock"],
            })
            count_rows += 1
            
    return count_rows
    


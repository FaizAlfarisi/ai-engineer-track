import requests
import csv
from pathlib import Path

def search(base: str, q: str, max_items: int = 10) -> dict:
    params = {"q": q, "max": max_items}
    resp = requests.get(f"{base}/search", params=params, timeout=3)
    resp.raise_for_status()
    return resp.json()
    
def save_csv(items: list[dict], path: Path) -> int:
    fieldnames = ["id", "name", "price", "stock"]
    written = 0
    
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in items:
            writer.writerow(item)
            written += 1
            
    return written
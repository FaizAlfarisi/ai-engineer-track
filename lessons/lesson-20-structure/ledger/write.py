import csv
import json
from pathlib import Path

def write_csv(items: list[dict], path: str | Path) -> None:
    path = Path(path)
    
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "price", "stock"], extrasaction="ignore")
        writer.writeheader()
        writer.writerows(items)
def write_json(items: list[dict], path: str | Path) -> None:
    path = Path(path)
 
    path.write_text(
        json.dumps({"items": items}, indent=2),
        encoding="utf-8"
    )

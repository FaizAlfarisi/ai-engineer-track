import json
import csv
from pathlib import Path

def load_transactions(path: Path) -> list[dict[str, str | float]]:
    if not path.exists():
        return []
    
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    
def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
from transaction import Transaction
from pathlib import Path
import json
import csv

def load_transactions(path: Path) -> list[Transaction]:
    if not path.exists():
        return []
    
    try:
        records = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
    
    results = []
    
    for record in records:
        results.append(Transaction(record['date'], record['category'], record['kind'], record['amount']))
        
    return results

def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
import json
import csv
from typing import Any
from pathlib import Path
from models.transactions import Transaction, Kind
from utils.exceptions import ErrorCorruptData
from dataclasses import asdict

def transaction_decoder(dtc: dict[str, Any]) -> Transaction | dict[str, Any]:
    if 'date' in dtc and 'category' in dtc and 'kind' in dtc and 'amount' in dtc:
        return Transaction(
            date=dtc['date'],
            category=dtc['category'],
            kind=Kind(dtc['kind']),
            amount=dtc['amount'],
        )
    
    return dtc

def load_json(path: Path) -> list[Transaction]:
    if not path.exists():
        return []

    try:    
        return json.loads(path.read_text(encoding="utf-8"), object_hook=transaction_decoder)
    except json.JSONDecodeError as err:
        raise ErrorCorruptData(err)
    
def kind_encoder(obj):
    if isinstance(obj, Kind):
        return obj.value
    raise TypeError(f"object of type {type(obj).__name__} is not json serializable")
    
def write_json(path: Path, transactions: list[Transaction]) -> None:
    lines = [asdict(txn) for txn in transactions]
    json_string = json.dumps(lines, indent=2, default=kind_encoder)
    path.write_text(json_string, encoding="utf-8")
    
def write_csv(path: Path, data: dict[str, float], colname: str) -> None:
    field_names = [colname, "net"]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f=f, fieldnames=field_names)
        writer.writeheader()
        
        for key in sorted(data.keys()):
            v = data[key]
            
            writer.writerow({
                colname: key,
                "net": f"{v:.2f}"
            })
        
def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []

    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
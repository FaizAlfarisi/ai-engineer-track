import json
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
    
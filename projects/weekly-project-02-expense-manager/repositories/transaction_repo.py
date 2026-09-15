import json
from typing import Any
from pathlib import Path
from models.transactions import Transaction, Kind
from utils.exceptions import ErrorCorruptData

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
    
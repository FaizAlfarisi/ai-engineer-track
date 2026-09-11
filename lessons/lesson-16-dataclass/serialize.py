import json
from pathlib import Path
from dataclasses import asdict
from kind import Kind, Transaction

def kind_encoder(obj): 
    if isinstance(obj, Kind):
        return obj.value
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")
    
def save_json(path: Path, transactions: list[Transaction]) -> None:
    lines = [asdict(t) for t in transactions]
    json_string = json.dumps(lines, indent=2, default=kind_encoder)
    path.write_text(json_string, encoding="utf-8")
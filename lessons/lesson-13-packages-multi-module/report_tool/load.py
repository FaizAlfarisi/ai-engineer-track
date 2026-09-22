import json
from pathlib import Path

def load_transactions(path: Path):
    if not path.exists():
        raise ValueError("file not found")
    try: 
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError("failed to decode")
    
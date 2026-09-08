import json
from pathlib import Path

def load_transactions(path: Path) -> list[dict[str, str | float]]:
    if not path.exists():
        return []
    
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []
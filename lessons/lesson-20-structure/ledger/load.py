import json
from pathlib import Path

def load(path: str | Path) -> list[dict]:
    path = Path(path)
    
    if not path.exists() or not path.is_file():
        return []
    
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        return data["items"]
    except json.JSONDecodeError:
        return []

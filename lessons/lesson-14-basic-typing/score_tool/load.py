from pathlib import Path
import json

def load_scores(path: Path) -> dict[str, int]:
    if not path.exists():
        return {}
    
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
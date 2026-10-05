import json
import logging
from pathlib import Path

log = logging.getLogger(__name__)

def load_logged(path: str) -> list[dict]:
    file_path = Path(path)
    if not file_path.exists() or not file_path.is_file():
        log.warning("missing file: %s", path)
        return []
    
    try:
        data = json.loads(file_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        log.error("bad json: %s", path, exc_info=True)
        return []
    
    log.info("loaded %d items", len(data.get("items", [])))
    return data.get("items", [])
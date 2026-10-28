import json
import logging
import re
from datetime import datetime
from pathlib import Path
from src.utils.exceptions import CorruptDataError


logger = logging.getLogger(__name__)


def _get_valid_path(path: str | Path) -> Path | None:
    if not isinstance(path, (str, Path)):
        return None
    
    if isinstance(path, str) and not path.strip():
        return None
    
    path = Path(path)
    
    if not path.is_file():
        return None
    
    return path

def _is_valid_line(line: str) -> bool:
    pattern = re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?:INFO|WARN|ERROR) service=\w+ latency=\d+ status=\d+ path=\S+")
    
    m = pattern.fullmatch(line)
    
    if not m:
        return False
    
    CANON = "%Y-%m-%d %H:%M:%S"
    raw_timestamp = m.group("timestamp")
    
    try:
        ts = datetime.strptime(raw_timestamp, CANON)
    except ValueError:
        return False
    
    if ts.strftime(CANON) != raw_timestamp:
        return False
    
    return True

def load_json(file_path: str | Path) -> list[str]:
    path = _get_valid_path(file_path)
    
    if path is None:
        logger.warning("invalid file path: %s", file_path)
        return []
    
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise CorruptDataError(f"failed to load existing data | {exc}")
    
    
def load_log(file_path: str | Path) -> str:
    path = _get_valid_path(file_path)
    
    if path is None:
        logger.warning("invalid file path: %s", file_path)
        return ""
        
    return path.read_text(encoding="utf-8")
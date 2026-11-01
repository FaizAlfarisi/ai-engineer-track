import json
import logging
import re
from datetime import datetime
from pathlib import Path
from src.utils.exceptions import CorruptDataError
from src.log_toolkit.domain.entities import ServiceLog
from typing import Any


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

def is_valid_line(line: str) -> bool:
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

def log_decoder(dtc: dict[str, str]) -> ServiceLog | dict[str, Any]:
    if "date" in dtc and "time" in dtc and "level" in dtc and "service" in dtc and "latency" in dtc and "status" in dtc and "path" in dtc:
        try:
            date = datetime.strptime(dtc["date"], "%Y-%m-%d").date()
        except ValueError:
            raise CorruptDataError(f"invalid date: {dtc["date"]!r}. Expected YYYY-MM-DD date format")
        
        try:
            time = datetime.strptime(dtc["time"], "%H:%M:%S").time()
        except ValueError:
            raise CorruptDataError(f"invalid time: {dtc["time"]!r}. Expected HH:MM:SS time format")
        
        try:
            latency = int(dtc["latency"])
        except ValueError:
            raise CorruptDataError(f"invalid latency: {dtc["latency"]!r}. Expected a positive number")
        if latency < 0:
            raise CorruptDataError(f"invalid latency: {dtc["latency"]!r}. Expected a positive number")
            
        try:
            status = int(dtc["status"])
        except ValueError:
            raise CorruptDataError(f"invalid status: {dtc["status"]!r}. Expected a positive number")
        if status < 0:
            raise CorruptDataError(f"invalid status: {dtc["status"]!r}. Expected a positive number")
        
        level = dtc["level"]
        service = dtc["service"]
        path = dtc["path"]
        
        return ServiceLog(
            date=date,
            time=time,
            latency=latency,
            status=status,
            level=level,
            service=service,
            path=path,
        )
    
    return dtc

def load_json(file_path: str | Path) -> list[ServiceLog]:
    path = _get_valid_path(file_path)
    
    if path is None:
        logger.warning("invalid file path: %s", file_path)
        return []
    
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_hook=log_decoder)
    except json.JSONDecodeError as exc:
        raise CorruptDataError(f"failed to load existing data | {exc}")
    
    
def load_log(file_path: str | Path) -> str:
    path = _get_valid_path(file_path)
    
    if path is None:
        logger.warning("invalid file path: %s", file_path)
        return ""
        
    return path.read_text(encoding="utf-8")

def write_json(file_path: str | Path, data: list[dict[str, Any]]) -> None: 
    path = Path(file_path)
    path.write_text(json.dumps(data, separators=(',', ':')), encoding="utf-8")
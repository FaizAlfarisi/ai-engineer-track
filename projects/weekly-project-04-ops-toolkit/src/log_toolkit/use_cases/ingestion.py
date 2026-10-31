import logging

from pathlib import Path
from datetime import datetime

from src.utils.exceptions import CorruptDataError
from src.log_toolkit.services.storage import load_log, is_valid_line, write_json

logger = logging.getLogger(__name__)

def ingest(log_path: Path, target_path: Path) -> str:
    try: 
        loaded_log = load_log(log_path)
    except CorruptDataError as exc:
        logger.error("failed to load %s data", log_path, exc_info=True)
        raise CorruptDataError(f"failed to load {log_path.stem} data | {exc}")
    
    records = loaded_log.splitlines()
    logger.info("loaded %d record of logs from %s", len(records), log_path)
    
    skipped = 0
    valid_lines = []
    
    for line in records:
        if not is_valid_line(line):
            skipped += 1
            logger.debug("skipped line: %s", line)
            continue
            
        date, time, level, service, latency, status, path = line.split(" ")
        
        data = {
            "date": date,
            "time": time,
            "level": level,
            "service": service.split("=")[1],
            "latency": latency.split("=")[1],
            "status": status.split("=")[1],
            "path": path.split("=")[1],
        }
        
        valid_lines.append(data)
        
    sorted_valid = sorted(valid_lines, key=lambda x: f"{x["date"]} {x["time"]}")
    
    logger.info("total skipped line: %d", skipped)
    logger.info("total valid line: %d", len(sorted_valid))
    
    write_json(target_path, sorted_valid)
    logger.debug("finished writing to %s, data: %s", target_path, sorted_valid)
    
    return f"Ingest: {len(sorted_valid)} valid, {skipped} skipped"
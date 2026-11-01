from pathlib import Path
from datetime import time
from src.log_toolkit.services.storage import load_json

def window(path: Path, start: time, end: time) -> str:
    records = load_json(path)
    
    results: dict[str, int] = {}
    total = 0
    
    for log in records:
        if start <= log.time <= end:
            results[log.service] = results.get(log.service, 0) + 1
            total += 1
    
    lines = []
    
    for service, count in sorted(results.items()):
        lines.append(f"{service}: {count}")
    
    lines.append(f"Window: {total} records")
    
    return "\n".join(lines)
    
    
    



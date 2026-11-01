from pathlib import Path

from src.log_toolkit.services.storage import load_json


def report_slow(path: Path, N: int) -> str:
    records = load_json(path)
    
    sorted_by_latency = sorted(records, key=lambda x: x.latency, reverse=True)
    
    lines = [f"{log.latency} {log.service} {log.path}" for i, log in enumerate(sorted_by_latency) if i < N]
    
    lines.append(f"Slow: {len(lines)} records")
    
    return "\n".join(lines)
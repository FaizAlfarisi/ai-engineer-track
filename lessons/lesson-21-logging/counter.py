from pathlib import Path

def is_valid_level(level: str) -> bool:
    return level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

def count_by_level(path: str) -> dict[str, int]:
    file_path = Path(path)
    
    lines = file_path.read_text(encoding="utf-8")
    result = {}
    
    if not lines:
        return result
    
    for line in lines.splitlines():
        if not line.strip():
            continue
        splitted = line.split()
        level = splitted[0].strip().upper()
        
        if is_valid_level(level):
            result[level] = result.get(level, 0) + 1
        else: 
            result["OTHER"] = result.get("OTHER", 0) + 1
    
    return result

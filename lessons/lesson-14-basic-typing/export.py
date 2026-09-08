def normalize(rows: list[dict[str, object]]) -> list[dict[str, str | float]]:
    if not rows:
        return []
    
    normalized = []
    for row in rows:
        id = str(row.get("id", ""))
        qty = _to_float(row.get("qty", 0.0))    
        tag = str(row.get("tag", "unknown"))
        
        new_row = {
            "id": id,
            "qty": qty,
            "tag": tag
        }
        
        normalized.append(new_row)
        
    return normalized

def _to_float(value: object) -> float:
    try:
        return float(value)
    except ValueError:
        return 0.0


def total_qty(rows: list[dict[str, str | float]]) -> float:
    if not rows:
        return 0.0
    
    total = 0.0
    for row in rows:
        total += row.get("qty", 0.0)
        
    return total

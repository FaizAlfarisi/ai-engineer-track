def safe_float(value: str) -> float | None:
    try:
        return float(value)
    except ValueError:
        return None

def total_scoreable(rows: list[dict[str, str]]) -> float:
    if not rows:
        return 0.0
    
    total = 0.0
        
    for row in rows:
        score = safe_float(row.get("score"))
        
        if score is not None:
            total += score
    
    return total
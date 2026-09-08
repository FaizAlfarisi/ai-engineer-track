def net_by_month(records: list[dict[str, str | float]]) -> dict[str, float]:
    monthly_net: dict[str, float] = {}
    
    for record in records:
        date_str = str(record["date"])
        month = date_str[:7]
        try:
            kind = str(record["kind"])
            raw_amount = record["amount"]
            amount = _route_budget(kind, _safe_float(raw_amount))
        except ValueError:
            continue
        monthly_net[month] = monthly_net.get(month, 0.0) + amount
        
    return monthly_net

def net_by_category(records: list[dict[str, str | float]]) -> dict[str, float]: 
    category_net:dict[str, float] = {}
    
    for record in records:
        category = str(record["category"])
        try:
            kind = str(record["kind"])
            raw_amount = record["amount"]
            amount = _route_budget(kind, _safe_float(raw_amount))
        except ValueError:
            continue
        category_net[category] = category_net.get(category, 0.0) + amount
    
    return category_net

def _route_budget(kind: str, amount: float) -> float:
    match kind:
        case "income":
            return amount
        case "expense":
            return -amount
        case _:
            raise ValueError("invalid kind")
        
def _safe_float(value: str | float) -> float:
    try:
        return float(value)
    except ValueError:
        raise ValueError("invalid amount")
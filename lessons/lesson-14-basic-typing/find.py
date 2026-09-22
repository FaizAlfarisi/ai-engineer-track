def find_by_id(records: list[dict[str,int]], target: int) -> dict[str, int] | None:
    for record in records:
        if record["id"] == target:
            return record
    
    return None
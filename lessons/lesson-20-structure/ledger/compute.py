def merge(network: list[dict], cached: list[dict]) -> tuple[list[dict], int, int]:
    merged_dict: dict[int, dict] = {item["id"]: item for item in cached}
    
    network_ids = set()
    for item in network:
        item_id = item["id"]
        merged_dict[item_id] = item
        network_ids.add(item_id)
    
    fresh = len(network)
    kept = sum(1 for item in cached if item["id"] not in network_ids)
    merged_data = sorted(merged_dict.values(), key=lambda x: x["id"])
    
    return merged_data, fresh, kept

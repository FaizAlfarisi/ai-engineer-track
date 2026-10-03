from src.tracker.services.api import get_items
from src.tracker.services.storage import load_json, write_json, write_csv, merge_data, item_decoder


def sync(cached_json_path, cached_csv_path) -> str:
    raw_network = get_items()
    
    network = [item_decoder(item) for item in raw_network]
    
    cached = load_json(cached_json_path)
    
    merged, fresh, kept = merge_data(network, cached)
    
    write_json(cached_json_path, merged)
    write_csv(cached_csv_path, merged)
    
    return f"Sync: N items (fresh {fresh}, cached {kept})"
from src.tracker.services.api import get_items
from src.tracker.services.storage import load_json, write_json, write_csv, merge_data, item_decoder
from src.tracker.domain.entities import Item

def sync(cached_json_path: str, cached_csv_path: str) -> str:
    raw_network = get_items()
    network: list[Item] = []
    
    for n in raw_network:
        decoded = item_decoder(n)
        
        if isinstance(decoded, Item):
            network.append(decoded)
    
    cached = load_json(cached_json_path)
    
    merged, fresh, kept = merge_data(network, cached)
    
    write_json(cached_json_path, merged)
    write_csv(cached_csv_path, merged)
    
    return f"Sync: {len(merged)} items (fresh {fresh}, cached {kept})"
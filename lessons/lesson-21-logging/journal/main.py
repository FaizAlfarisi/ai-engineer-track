import sys
import logging
import json
import csv
from pathlib import Path

def setup_verbosity(mode: str = "normal") -> logging.Logger:
    log = logging.getLogger("journal")
    log.setLevel(logging.DEBUG)
    log.propagate = False
    
    if log.handlers:
        log.handlers.clear()
    
    # Include levelname so 'DEBUG' appears in the log file text
    formatter = logging.Formatter("%(levelname)s %(filename)s %(name)s %(message)s")
    
    if mode == "verbose":
        level = logging.DEBUG
    elif mode == "quiet":
        level = logging.CRITICAL
    else:
        level = logging.INFO
    
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setLevel(level)
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    
    # Place journal.log beside the module
    file_path = Path(__file__).with_name("journal.log")
    file_handler = logging.FileHandler(file_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    return log

def load_json(path: str | Path) -> list[dict]:
    logger = logging.getLogger("journal")
    
    if not isinstance(path, (str, Path)) or not path:
        return []
    
    path = Path(path)
    if not path.is_file():
        logger.warning("file not found: %s", path)
        return []
    
    try: 
        content = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(content, list):
            logger.info("loaded %d items from %s", len(content), path)
            return content
        if isinstance(content, dict) and "items" in content:
            items = content["items"]
            logger.info("loaded %d items from %s", len(items), path)
            return items
    except json.JSONDecodeError:
        logger.error("broken json in %s", path, exc_info=True)
        return []
    
    return []

def write_csv(path: str | Path, data: list[dict]) -> None:
    path = Path(path)
    fieldnames = ["id", "name", "price", "stock"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        for row in data:
            writer.writerow({k: row.get(k, "") for k in fieldnames})
    
def write_json(path: str | Path, data: list[dict]) -> None:
    path = Path(path)
    path.write_text(json.dumps({"items": data}, indent=2), encoding="utf-8")

def merge(network: list[dict], cached: list[dict]) -> tuple[list[dict], int, int]:
    merged: dict[int, dict] = {d["id"]: d for d in cached}
    
    network_ids = set()
    for item in network:
        item_id = item["id"]
        merged[item_id] = item
        network_ids.add(item_id)
        
    fresh = len(network)
    kept = sum(1 for data in cached if data["id"] not in network_ids)
    merge_result = sorted(merged.values(), key=lambda x: x["id"])
    
    return merge_result, fresh, kept

def is_valid(row):
    return isinstance(row, dict) and "id" in row and "price" in row and "stock" in row

def main(argv: list[str]):
    if len(argv) < 3 or argv[1] != "sync":
        sys.stderr.write("usage: python -m journal.main sync <dir> [quiet|verbose]\n")
        sys.exit(1)
    
    mode = "normal"
    if len(argv) == 4:
        mode = argv[3]
        if mode not in ["quiet", "verbose", "normal"]:
            sys.stderr.write("usage: python -m journal.main sync <dir> [quiet|verbose]\n")
            sys.exit(1)
    elif len(argv) > 4:
        sys.stderr.write("usage: python -m journal.main sync <dir> [quiet|verbose]\n")
        sys.exit(1)

    data_dir = Path(argv[2])
    feed = data_dir / "feed.json"
    cache = data_dir / "cache.json"
    
    network_raw = load_json(feed)
    cached_raw = load_json(cache)
    
    logger = setup_verbosity(mode)
    logger.debug("starting sync from %s", data_dir)

    skipped = 0
    valid_network = []
    for item in network_raw:
        if not is_valid(item):
            logger.warning("invalid network row: %s", item)
            skipped += 1
        else:
            valid_network.append(item)
            
    valid_cached = []
    for item in cached_raw:
        if not is_valid(item):
            logger.warning("invalid cache row: %s", item)
            skipped += 1
        else:
            valid_cached.append(item)
    
    merged_data, fresh, kept = merge(valid_network, valid_cached)

    write_json("journal.json", merged_data)
    write_csv("journal.csv", merged_data)
    
    print(f"Ledger: {len(merged_data)} items (fresh {fresh}, cached {kept}, skipped {skipped})")

if __name__ == "__main__":
    main(sys.argv)
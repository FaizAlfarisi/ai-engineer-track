import sys
from pathlib import Path
from ledger.load import load
from ledger.compute import merge
from ledger.write import write_csv, write_json

def main(argv: list[str]) -> None:
    if len(argv) != 3 or argv[1].strip() != "sync":
        print("usage: python -m ledger.main sync <dir>", file=sys.stderr)
        sys.exit(1)

    data_dir = Path(argv[2].strip())
    
    feed = data_dir / "feed.json"
    cache = data_dir / "cache.json"
    
    network = load(feed)
    cached = load(cache)
    
    items, fresh, kept = merge(network, cached)
    
    write_csv(items, Path("ledger.csv"))
    write_json(items, Path("ledger.json"))
    
    print(f"Ledger: {len(items)} items (fresh {fresh}, cached {kept})")

if __name__ == "__main__":
    main(sys.argv)

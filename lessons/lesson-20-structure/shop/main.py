import csv
import sys
from pathlib import Path
from shop.report import summary

def load_basket(path: str) -> list[float]:
    if not isinstance(path, str) or not path:
        raise ValueError(f"bad basket path: {path!r}")
    
    with Path(path).open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [float(row["price"]) for row in reader]
        

def main(argv: list[str]) -> None:
    if len(argv) > 2:
        print("usage: python -m shop.main [basket.csv]", file=sys.stderr)
        sys.exit(1)
    elif len(argv) == 2:
        prices = load_basket(argv[1])
        print(f"cart: {len(prices)} items, total {sum(prices):.2f}")
    else:
        print(summary())

if __name__ == "__main__":
    main(sys.argv)

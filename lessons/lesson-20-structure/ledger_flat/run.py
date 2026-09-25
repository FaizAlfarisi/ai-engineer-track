import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from load import load
from compute import merge
from write import write_csv

network = load(sys.argv[1])
cached = load(sys.argv[2])
items = merge(network, cached)
write_csv(items, "ledger.csv")
print(f"Ledger: {len(items)} items")

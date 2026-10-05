import sys

from report import totals
from load import load

rows = load(sys.argv[1])
result = totals(rows)
print(f"Summary ({len(result)} teams, {len(rows)} rows)")

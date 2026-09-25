from load import load
from compute import summarize
from write import write_summary

rows = load("grades.csv")
totals = summarize(rows)
write_summary(totals, "summary.csv")
print(f"Summary ({len(totals)} teams, {len(rows)} rows)")

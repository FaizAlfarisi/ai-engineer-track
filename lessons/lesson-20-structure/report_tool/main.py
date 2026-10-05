import sys
from pathlib import Path
from report_tool.load import load
from report_tool.compute import summarize
from report_tool.write import write_summary

def main():
    args = sys.argv
    if len(args) != 2:
        print("usage: python -m report_tool.main <grades.csv>", file=sys.stderr)
        sys.exit(1)
    
    path = args[1]
    rows = load(path)
    totals = summarize(rows)
    
    out_path = Path(path).with_name("summary.csv")
    write_summary(totals, out_path)
    print(f"Summary ({len(totals)} teams, {len(rows)} rows)")

if __name__ == "__main__":
    main()

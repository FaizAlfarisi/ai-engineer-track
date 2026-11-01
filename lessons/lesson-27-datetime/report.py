import sys
import csv
from pathlib import Path
from datetime import date

from aging import build_aging
from tenure import parse_date, tenure_days

TODAY = date(2026, 3, 1)

def main(argv) -> None:
    if len(argv) != 3:
        sys.stderr.write("usage: report.py <signups.csv> <tenure.txt>\n")
        sys.exit(1)

    signups_path = Path(argv[1])
    tenure_path = Path(argv[2])

    if not signups_path.exists() or not signups_path.is_file():
        sys.stderr.write("bad log: not found\n")
        sys.exit(1)

    lines = []
    months = {}
    
    with signups_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for i, raw in enumerate(reader):
            try:
                name, text = raw
            except ValueError:
                lines.append(f"skip {i}: invalid line: bad shape")
                continue
            
            try:
                day = parse_date(text)
            except ValueError as e:
                lines.append(f"skip {i}: {e}")
                continue
            
            tenure = tenure_days(day, TODAY)
            
            if tenure < 0:
                lines.append(f"skip {i}: invalid tenure: future signup")
                continue
            
            if tenure < 30:
                bucket = "new"
            elif tenure <= 364:
                bucket = "active"
            else:
                bucket = "veteran"
            
            lines.append(f"line {i}: {name} {bucket} {tenure}")
            month = day.isoformat()[:7]
            months[month] = months.get(month, 0) + 1

    
    monthly = [f"month {month}: {count}" for month, count in months.items()]
    text = build_aging(monthly, lines)

    tenure_path.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main(sys.argv)

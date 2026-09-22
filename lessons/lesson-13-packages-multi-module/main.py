from report_tool.load import load_transactions
from report_tool.compute import summarize
from report_tool.write import write_summary
from pathlib import Path
import csv

def main():
    records = load_transactions(Path("transactions.json"))

    summary = summarize(records)
    
    saved = Path("summary.csv")
    write_summary(saved, summary)
    
    with saved.open(newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))
    

if __name__ == "__main__":
    main()
# Lesson 13 — Packages & Multi-Module Structure
# Write all exercise solutions here first, then create the files listed
# in each exercise's File tree, then paste each driver into its notebook
# cell and run it.
# Do not delete or reorder entries below — the notebook cells stay in sync.

# E1 — greet.py
def greet(name):
    return f"Hello, {name}!"

# E2 — words.py + report.py
# textstats/words.py
def count_words(text):
    return len(text.split())

# report.py
from words import count_words

def word_count(text):
    return count_words(text)

# E3 — textstats/__init__.py + textstats/words.py
# textstats/__init__.py empty

# textstats/words.py
def count_words(text):
    return len(text.split())

# M1 — textstats/longest.py
from .words import count_words

def summarize(text):
    word_count = count_words(text)
    longest = max(text.split(), key=len)

    return f"{word_count} words; longest: {longest}"
    

# H1 — greeter package debug drill (write the bug report at the end)
# greeter/__init__.py
from .greet import greet

# greeter/greet.py
# print("greeting module loaded")

def greet(name):
    return f"Hello, {name}!"

# main_greet.py i changed it to main_greet because challenge also use main.py
from greeter import greet

def run():
    print(greet("ada"))

if __name__ == "__main__":
    run()

# greeter/greet.py must not print out at the module root
# main.py using relative import, which is cause the module not found, so it is should be importing the package name
# there is two approach to solve bug 2, raising bug 3 by the empty __init__.py file which is suppose to be importing the module in that package
# or by simply importing greeter.greet in main.py
# since there should be 3 bug, i will take the import on __init__.py approach.

# CHALLENGE — report_tool package + main.py
# report_tool/load.py
import json
from pathlib import Path

def load_transactions(path: Path):
    if not path.exists():
        raise ValueError("file not found")
    try: 
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError("failed to decode")
    
# report_tool/compute.py
def summarize(records):
    result = {}
    for r in records:
        result[r['category']] = result.get(r['category'], 0) + r['amount']

    return result.items()

# report_tool/write.py
import csv
from pathlib import Path

def write_summary(path: Path, totals: dict):
    field_names = ["category", "total"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(field_names)
        for category, total in sorted(totals.items()):
            writer.writerow([category,f"{total:.2f}"])
        
# main.py
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
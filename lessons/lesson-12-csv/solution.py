# E1 — your solution here
import csv

with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(f"{line['name']}: {line['score']}")


# E2 — your solution here
from pathlib import Path

fruit_path = Path("fruits.csv")

with fruit_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "quantity", "price"])
    writer.writerows([("apple", 5, 1500), ("banana", 2, 1200), ("watermelon", "4", "2500")])

with fruit_path.open(newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    count = sum(1 for _ in reader)
    print(count)
    
# E3 — your solution here
def load_scores(path: Path):
    if not path.exists():
        return []
    
    valid = []
    
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader, start=1):
            try:
                row['score'] = int(row['score'])
                valid.append(row)
            except ValueError:
                print(f"skipped row: non-numeric score '{row['score']}' (row {i})")
    
    return valid

print(load_scores(Path("students.csv")))

# Challenge — your solution here

def read_csv(path: Path):
    if not path.exists():
        raise ValueError("no grades file found")
    
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        rows = [row for row in reader]
        return rows

def grades_stat_builder(rows):
    stats = {}
    stat_summaries = []
    
    for row in rows:
        name = row['name']
        
        if name not in stats:
            stats[name] = {
                "total_score": 0,
                "count": 0,
            }
        
        stats[name]['total_score'] += row['score']
        stats[name]['count'] += 1
        
    for name in sorted(stats):
        if stats[name]['count'] > 0:
            average = stats[name]['total_score']/stats[name]['count']
            status = 'pass' if average >= 60 else 'fail'
            stat_summaries.append({"name": name, "average": f"{average:.1f}", "status": status})
        
    return stat_summaries

def write_csv(path: Path, data):
    field_names = list(data[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)

def main():
    FILE_PATH = Path("grades.csv")
    
    rows = read_csv(FILE_PATH)
    parsed_rows = []
    
    for i, row in enumerate(rows, start=1):
        try:
            row['score'] = int(row['score'])
            parsed_rows.append(row)
        except ValueError:
            print(f"skipped row: non-numeric score '{row['score']}' (row {i})")
            continue
    
    stat_summaries = grades_stat_builder(parsed_rows)
    
    save_path = Path('summary.csv')
    write_csv(save_path,stat_summaries)
    
    results = read_csv(save_path)
    print(f"Summary ({len(results)} students):")
    for i, r in enumerate(results, start=1):
        print(f"{i}. {r['name']}: {r['average']} [{r['status']}]")

if __name__ == '__main__':
    main()
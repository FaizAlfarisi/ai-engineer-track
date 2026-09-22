# Lesson 12 — CSV (Tier: SUPPORTING)

Stage 2, fifth topic. You can read and write text files (L9), navigate
the filesystem with pathlib (L10), and serialize structured data as JSON
(L11). CSV is the other half of the serialization story — simpler than
JSON, but the format the world already uses for spreadsheets, databases,
and data exports.

---

## Objective

By the end of this lesson you can:

- Read a CSV file with `csv.reader` and `csv.DictReader`.
- Write a CSV file with `csv.writer` and `csv.DictWriter`.
- Explain why `newline=''` is required when opening CSV files.
- Convert CSV string values to Python types (e.g., `int`, `float`).
- Combine CSV with pathlib and exception handling from previous lessons.
- Decide when to use CSV vs JSON.

---

## Why This Matters

Spreadsheets, databases, and data exports almost always speak CSV. A
sensor logs temperature readings to a CSV. A bank exports transactions
as CSV. A machine-learning dataset is a CSV. Your programs will read and
write CSV files constantly — not because CSV is the best format, but
because the world already uses it.

A data pipeline that reads a CSV, transforms it, and writes a new CSV
is one of the most common patterns in applied programming. The "read →
transform → write" shape you build here is the same shape as a real
data-for-AI pipeline.

---

## Mental Model

CSV is a **table saved as text**. Each line is a row. Each comma is a
column boundary. The first row is usually the header (column names).

```text
name,subject,score
Alice,math,92
Bob,science,78
```

Think of it as a list of lists — or, better, a list of dicts when you
use `DictReader`. Every value is a string. There are no numbers, no
booleans, no null. The file is just text with commas.

---

## Core Concept

### 1. `csv.reader` — rows as lists

```python
import csv

with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # ["Alice", "math", "92"]
```

Each `row` is a **list of strings**. No type conversion happens —
`"92"` is a string, not a number. The header row is just another list:
`["name", "subject", "score"]`.

### 2. `csv.writer` — write rows

```python
import csv

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])              # header
    writer.writerow(["Alice", 92])                  # one row
    writer.writerows([["Bob", 78], ["Carol", 88]])  # multiple rows
```

`writerow` writes one row. `writerows` writes many. The writer converts
numbers to strings automatically when writing — but the reader does NOT
convert strings back to numbers when reading.

### 3. `csv.DictReader` — rows as dicts

```python
import csv

with open("students.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["score"])  # "Alice" "92"
```

`DictReader` uses the **first row as headers**. Each row becomes a
dict with column names as keys. Accessing a missing key raises
`KeyError` — use `.get("key", default)` for optional fields (L6).

### 4. `csv.DictWriter` — write dicts

```python
import csv

with open("output.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["name", "score"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "Alice", "score": 92})
    writer.writerows([{"name": "Bob", "score": 78}])
```

`fieldnames` is **required** — it tells the writer which keys to use
and in what order. Call `writeheader()` first to write the column names.

---

## Practical Examples

### Example 1: Read and filter

```python
import csv

with open("scores.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    passing = [row for row in reader if int(row["score"]) >= 60]

for student in passing:
    print(f"{student['name']}: {student['score']}")
```

Note: `int(row["score"])` converts the string `"92"` to the number
`92`. Without this, `"92" >= 60` does lexicographic comparison, which
gives wrong results.

### Example 2: Write with type conversion

```python
import csv

data = [("Alice", 92), ("Bob", 78), ("Carol", 88)]

with open("report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "score"])
    for name, score in data:
        writer.writerow([name, score])  # int → string automatically
```

The writer handles the int-to-string conversion for you. The reader
does NOT handle the reverse — you must do that yourself.

---

## Engineering Notes

1. **`newline=''` is required.** Without it, Windows writes double
   line breaks (`\r\n\n`). This is the most common CSV bug. Always
   use it.

2. **`encoding="utf-8"` always.** Same rule as L9/L10/L11. Never
   skip it.

3. **All values are strings.** CSV has no types. `score` is `"92"`,
   not `92`. You must convert yourself: `int(row["score"])`,
   `float(row["price"])`. Wrap conversions in `try/except ValueError`
   (L8).

4. **Pathlib + CSV.** You can use `Path.open()` (L10) instead of raw
   `open()`. The `newline=''` still applies:
   ```python
   from pathlib import Path
   with Path("data.csv").open("w", newline="", encoding="utf-8") as f:
       writer = csv.writer(f)
       ...
   ```
   But `Path.write_text` does NOT support `newline=''`. Do not use it
   for CSV.

5. **CSV vs JSON — when to use which:**

   | CSV | JSON |
   |-----|------|
   | Flat tables (rows + columns) | Nested data (objects inside objects) |
   | Spreadsheet-compatible | Program-native |
   | No type info (everything is string) | Type-aware (numbers, booleans, null) |
   | Compact for simple data | Verbose but richer |

   Use CSV when the data is flat and the consumer is a spreadsheet or
   another program that expects CSV. Use JSON when you need structure,
   types, or nesting.

---

## Common Pitfalls

1. **Forgetting `newline=''`.** Double line breaks on Windows. Always
   use `newline=""` in `open()`.

2. **Not converting types.** `row["score"]` is `"92"` (string).
   Comparing `"92" >= 60` does lexicographic comparison, not numeric.
   Convert first.

3. **Quoting confusion.** If a field contains a comma (e.g.,
   `"Smith, John"`), the CSV writer quotes it automatically. You do
   not need to handle this manually.

4. **`DictReader` without a header row.** If the CSV has no header,
   `DictReader` uses the first data row as keys — silent data loss.
   Pass `fieldnames=` explicitly.

5. **`DictWriter` without `fieldnames`.** It is required, not optional.
   You will get a `TypeError`.

6. **Using `Path.write_text` for CSV.** It does not support
   `newline=''`. Use `Path.open()` or raw `open()` instead.

---

## Connection to Previous Knowledge

- **File Handling (L9):** `open()` context manager, streaming row by
  row. CSV uses the same `with` block — just with `newline=""` added.
- **Pathlib (L10):** `Path.open()` gives you the same file handle.
  But `Path.write_text` does not support `newline=''`, so CSV writing
  uses `Path.open()` or raw `open()` instead.
- **JSON (L11):** both serialize data. CSV is simpler (flat, strings
  only). JSON is richer (nested, typed). Decide by data shape.
- **Exception Handling (L8):** `csv.Error` for malformed input. Type
  conversion errors caught with `try/except ValueError` (L8 rule).
  Clean re-raise with `from None` for loader errors (Quiz 01 D2).
- **Collections (L6):** CSV rows are lists; DictReader rows are dicts.
  The `dict.get()` pattern from L6 applies for optional fields.
- **Functions (L5):** loaders return data, never print, never
  error-strings (L9 rule).
- **Modules (L7):** `import csv`.

---

## Quick Recall

Answer from memory before starting Practice:

1. What does `newline=""` do when opening a CSV file, and why is it
   required?
2. What is the difference between `csv.reader` and `csv.DictReader`?
3. Why must you convert `row["score"]` to `int` before comparing it
   with a number?
4. When should you use CSV instead of JSON?
5. Why can't you use `Path.write_text` to write CSV files?

---

## Practice

Volume follows the SUPPORTING pipeline (CURRICULUM.md). Every exercise
states rule, output format, and constraints explicitly. Write solutions
in `solution.py` first, then paste into notebook cells.

### Easy

**E1 — Read and print** `[REAL-WORLD]`

Read `students.csv` (provided: `name,subject,score` with 5 rows).
Print each student's name and score, one per line.

Output:
```text
Alice: 92
Bob: 78
Carol: 88
Dan: 45
Eve: 95
```

Constraints:
- Use `csv.DictReader`.
- Use `newline=""` and `encoding="utf-8"`.
- Do not hardcode the data — read from the file.

---

**E2 — Write a CSV** `[REAL-WORLD]`

Write a CSV file `fruits.csv` with header `name,quantity,price` and
three rows of your choice.

Rules:
- Use `csv.writer` and `writerow`/`writerows`.
- Header row must be written first.
- Output file must have exactly 4 lines (header + 3 data rows).

Constraints:
- Use `newline=""` and `encoding="utf-8"`.
- Use pathlib for the file path.

---

### Medium (combine with previous concepts)

**E3 — Safe CSV loader** `[REAL-WORLD]`

Write a function `load_scores(path)` that:
1. Reads a CSV file with `DictReader`.
2. Converts `score` to `int` for each row.
3. If the file does not exist, returns an empty list.
4. If a row has a non-numeric score, skips that row (prints a
   warning).
5. Returns a list of dicts:
   `[{"name": "Alice", "subject": "math", "score": 92}, ...]`.

Output (for a CSV with one bad row):
```text
skipped row: non-numeric score 'abc' (row 3)
```

Constraints:
- Use `newline=""` and `encoding="utf-8"`.
- Wrap `int()` in `try/except ValueError`.
- Follow the L9/L11 loader contract: return data, never error strings.
- Do not print the loaded data — return it.

---

### Challenge / Micro Build

**CSV Grade Book** `[REAL-WORLD]`

Given a CSV file `grades.csv` with columns `name,subject,score`, write
a program that:

1. Reads the CSV with `csv.DictReader`.
2. Converts `score` to `int` (skips rows with bad scores, prints a
   warning per skipped row).
3. Computes the **average score per student** (across all subjects).
4. Writes a summary CSV `summary.csv` with columns
   `name,average,status` where:
   - `average` is a float with 1 decimal place (e.g., `85.0`).
   - `status` is `"pass"` if average >= 60, `"fail"` otherwise.
5. Prints the summary to stdout in this exact format:

```text
Summary (3 students):
1. Alice: 88.3 [pass]
2. Bob: 72.0 [pass]
3. Carol: 55.0 [fail]
```

Rules:
- Use `csv.DictReader` for reading, `csv.DictWriter` for writing.
- Handle missing file -> print "no grades file found" and exit.
- Handle corrupt rows -> skip and warn, never crash.
- Output format is a contract — byte-exact.

Constraints:
- Use `newline=""` and `encoding="utf-8"`.
- Use pathlib for file paths.
- No classes. Functions only.
- Follow the L9/L11 loader contract.

Deliverable: `solution.py` (starts blank).

---

Scoring: Easy 10 x 2 + Medium 20 + Challenge 100 = 140 points
possible. Points are diagnostic, not a target.

Completion evidence (SUPPORTING -> Level 3): independent
implementation, read/write CSV with DictReader/DictWriter, type
conversion with error handling, pathlib integration, decides when CSV
vs JSON is appropriate.

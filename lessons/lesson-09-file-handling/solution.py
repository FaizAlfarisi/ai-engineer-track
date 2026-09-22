# Lesson 9 — File Handling · solution workspace
# ==============================================================
# Blank on purpose: write your implementations below, then paste
# finished code into the matching exercises.ipynb cell and run it.
#
# House rules for every exercise:
#   - every open() sits inside a with block
#   - explicit encoding="utf-8" on every open
#   - loader/saver functions return data and never print
#     (exception: merge_and_report prints through its out parameter)
#   - risky opens live inside try/except catching the SPECIFIC error
#
# Sections below mirror the notebook — keep them in order.


# --- E1 — Round trip ------------------------------------------
# save_greeting(path) -> None        two write calls, two lines
# load_text(path) -> str             one .read()
def save_greeting(path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("hello\n")
        f.write("file handling\n")
    
def load_text(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"file {path} not found"
    
save_greeting("greetings.txt")
print(load_text("greetings.txt"), end="")

# --- E2 — Append proves memory --------------------------------
# append_line(path, line) -> None    append mode
def append_line(path, line):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    
with open("events.log", "w", encoding="utf-8"):
    pass

append_line("events.log", "boot")
append_line("events.log", "ready")
append_line("events.log", "shutdown")

print(load_text("events.log"), end="")

# --- E3 — One line at a time ----------------------------------
# report_temperatures(path) -> (count, total)   iterate the handle
def report_temperatures(path):
    count_lines = 0
    total = 0
    
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                count_lines += 1
                total += float(line)
        return count_lines, total
    except FileNotFoundError:
        return count_lines, total

with open("temperatures.txt", "w", encoding="utf-8") as f:
    f.write("21.5\n20.1\n22.8\n")
    
c, t = report_temperatures("temperatures.txt")
print(f"lines: {c}")
print(f"total: {t:.1f}")
            

# --- E4 — The file wasn't there -------------------------------
# load_greeting(path) -> str         specific except, default fallback
def load_greeting(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "hello, newcomer"
    
print(load_greeting("user-name.txt"))

with open("user-name.txt", "w", encoding="utf-8") as f:
    f.write("hello, Ada")
    
print(load_greeting("user-name.txt"))

# --- E5 — Report writer ---------------------------------------
# write_report(stock, path) -> None  join lines, ONE write
def write_report(stock: dict, path):
    with open(path, "w", encoding="utf-8") as f:
        report = [f"{item}: {qty}\n" for item, qty in stock.items()]
        f.write("".join(report))
            
stock = {"apples": 12, "bananas": 0, "cherries": 7}

write_report(stock, "report.txt")
print(load_text("report.txt"), end="")

# --- M1 — Transactions file -> summary ------------------------
# summarize_file(path) -> dict       {"total": float, "valid": int, "invalid": int}
def summarize_file(path):
    s = {
        "total": 0,
        "valid": 0,
        "invalid": 0
    }
    
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    name, amount = (part.strip() for part in line.split(","))
                    if not name:
                        raise ValueError("invalid name")
                    amount = float(amount)
                except ValueError:
                    s["invalid"] += 1
                else:
                    s["valid"] += 1
                    s["total"] += amount
                    
    except FileNotFoundError:
        return f"file {path} not found"
        
    return s

with open("transactions.txt", "w", encoding="utf-8") as f:
    f.write("coffee,-3.50\nsalary,+2500.00\nrent:bad\n\n-12\nsnacks,+4.20\n")

s = summarize_file("transactions.txt")
print(f"total: {s['total']:.2f}")
print(f"valid: {s['valid']}")
print(f"invalid: {s['invalid']}")

"""
but i have a question. 
the try block have a lot of code
which is contradictive with my understanding that the try block should be as least as possible
but i cant find another way to solve this exercise
"""

# --- M2 — Filter and copy pipeline ----------------------------
# copy_errors(src, dst) -> int       ONE with, two handles
def copy_errors(src, dst):
    copied = 0
    try:
        with open(src, encoding="utf-8") as x, open(dst, "w", encoding="utf-8") as y:
            for line in x:
                if line.split(" ", 1)[0] == "ERROR":
                    y.write(line)
                    copied += 1
    except FileNotFoundError as err:
        return f"file not found: {err}"
    return copied

with open("sensor.log", "w", encoding="utf-8") as f:
    f.write("INFO boot ok\nERROR disk full\nINFO user login\nERROR timeout\nDEBUG noise\n")
    
n = copy_errors("sensor.log", "errors.log")
print(f"copied: {n}")
print(load_text("errors.log"), end="")

# --- M3 — Typed config loader ---------------------------------
# SPEC lives at module level in the notebook cell:
#   SPEC = {"retries": int, "rate": float, "name": str}
# load_settings(path) -> dict        strip values, ignore unknown keys,
#                                    raise ValueError(f"bad setting: {key}")
SPEC = {
    "retries": int, 
    "rate": float,
    "name": str
}

def load_settings(path):
    result = {}
    
    with open(path, encoding="utf-8") as f:
        for line in f:
            key, value = line.strip().split("=")
            if key in SPEC:
                try:
                    result[key] = SPEC[key](value)
                except ValueError:
                    raise ValueError(f"bad setting: {key}")
    
    return result

with open("app.cfg", "w", encoding="utf-8") as f:
    f.write("retries=3\nrate=0.5\nname=expense-cli\n")

try:
    print(load_settings("app.cfg"))
except ValueError as err:
    print(err)

with open("bad.cfg", "w", encoding="utf-8") as f:
    f.write("retries=three\nrate=0.5\n")

try:
    print(load_settings("bad.cfg"))
except ValueError as err:
    print(err)

# --- H1 — Debug: five bugs ------------------------------------
# Fix analyze(source_path, error_path) IN the notebook cell.
# Keep a written list here of each bug: expected vs observed, root cause.
# Bug 1: write error 'not writable' - open file written in bare - open file without 'with' block and not using write mode
# Bug 2: undefined 'errors' - append 'errors' - no errors declared
# Bug 3: unprocessed line - "processed 0" comes from consumed = source.read() exhausting the cursor
# Bug 4: error message in uppercase - script added .upper() while append errors - delete .upper()
# Bug 5: printed out with extra enter - fields not stripped - need strip for fields
def analyze(source_path, error_path):
    errors = []
    processed = 0
    with open(source_path, encoding="utf-8") as source:
        for line in source:
            processed += 1
            fields = line.strip().split(" ", 1)
            if fields[0] == "ERROR":
                errors.append(fields[1])
                
    with open(error_path, "w", encoding="utf-8") as out:
        out.write("=== errors ===\n")
        for msg in errors:
            out.write(msg + "\n")
            
    return processed


# --- driver (do not change) ---
with open("sensor2.log", "w", encoding="utf-8") as f:
    f.write("INFO boot\nERROR disk full\nINFO scan\nERROR timeout\nINFO done\n")

count = analyze("sensor2.log", "errors2.txt")
print(f"processed {count} entries")
with open("errors2.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")

# --- H2 — Interview drill: tail -------------------------------
# tail(path, n) -> list[str]         two passes: count, then collect
def tail(path, n):
    with open(path, encoding="utf-8") as f:
        total = sum(1 for _ in f)
    
    cutoff = total - n
    result = []
    
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            if i >= cutoff:
                result.append(line.strip())
    
    return result
    
def make_fixture(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + ("\n" if lines else ""))

make_fixture("app.log", ["boot", "scan", "alert", "fix", "done"])
print(tail("app.log", 2))
print(tail("app.log", 10))
make_fixture("empty.log", [])
print(tail("empty.log", 3))

# --- Challenge — Expense Persistence CLI ----------------------
# parse_entry(line) -> (str, float)          Lesson 8 contract, retyped fresh
# load_expenses(path) -> list[(str, float)]  missing file -> []
# save_expenses(path, expenses) -> None      canonical ":.2f" rewrite
# merge_and_report(path, new_lines, out=print) -> None
#                                            all try/except lives here
def parse_entry(line: str):
    if "," not in line:
        raise ValueError("missing comma")
    
    description, amount = (part.strip() for part in line.split(","))
    
    if not description:
        raise ValueError("empty description")
    
    try:
        amount = float(amount)
    except ValueError:
        raise ValueError("bad amount")
    
    return description, amount

def load_expenses(path):
    with open(path, encoding="utf-8") as f:
        return [parse_entry(line) for line in f]

def save_expenses(path, expenses):
    formatted = []
    for expense in expenses:
        description, amount = expense
        formatted.append(f"{description},{amount:.2f}\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(formatted)
            
        
def merge_and_report(path, new_lines, out=print):
    result = {
        "loaded": 0,
        "rejected": 0,
        "accepted": 0,
        "saved": 0,
        "total": 0,
    }
    try:
        existed_lines = load_expenses(path)
    except FileNotFoundError:
        expenses = []
    else:
        expenses = [x for x in existed_lines]
    
    for line in new_lines:
        try: 
            description, amount = parse_entry(line)
        except ValueError:
            result["rejected"] += 1
        else:
            result["accepted"] += 1
            expenses.append((description,amount))
    
    save_expenses(path, expenses)
    result["loaded"] = len(existed_lines)
    result["saved"] = len(expenses)
    result["total"] = sum(expense[1] for expense in expenses)

    out(f"=== loaded: {result["loaded"]} ===")
    out(f"accepted: {result["accepted"]}")
    out(f"rejected: {result["rejected"]}")
    out(f"=== saved: {result["saved"]} ===")
    out(f"total: {result["total"]}")
    return


with open("expenses.txt", "w", encoding="utf-8") as f:
    f.write("coffee,-3.50\nsalary,+2500.00\n")

new_entries = ["bus,-2.75", "", "snack,abc", "tea, 1.20"]
merge_and_report("expenses.txt", new_entries)

print("--- file now ---")
print(open("expenses.txt", encoding="utf-8").read(), end="")
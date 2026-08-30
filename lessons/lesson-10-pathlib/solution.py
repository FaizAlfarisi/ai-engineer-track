# Lesson 10 — Pathlib · solution workspace
# ==============================================================
# Blank on purpose: write your implementations below, then paste
# finished code into the matching exercises.ipynb cell and run it.
#
# House rules for every exercise:
#   - import: from pathlib import Path
#   - every Path read/write passes encoding="utf-8"
#   - loader functions return data and never print
#     (exception: challenge write_report returns the report string)
#   - a missing path is guarded with .exists() (LBYL) or caught (EAFP)
#
# Sections below mirror the notebook — keep them in order.


# --- E1 — Inspect a path --------------------------------------
# describe(path) -> (name, stem, suffix, parent_stem)
from pathlib import Path

def describe(path: Path):
    return path.name, path.stem, path.suffix, path.parent.name

p = Path("reports/2026/monthly/sales.csv")
name, stem, suffix, parent_stem = describe(p)
print(name)
print(stem)
print(suffix)
print(parent_stem)

# --- E2 — Join with / -----------------------------------------
# data_file(base, year, name) -> Path
def data_file(base, year, name):
    year = str(year)
    return Path(base) / year / name

p = data_file("data", 2026, "expenses.txt")
print(p)
print(p.parent)
print(p.name)

# --- E3 — Does it exist? --------------------------------------
# status(path) -> "exists" | "missing"
def status(path: Path):
    return "exists" if path.exists() else "missing"

Path("present.txt").write_text("x", encoding="utf-8")
print(status(Path("present.txt")))
print(status(Path("absent.txt")))

# --- E4 — List only .txt files --------------------------------
# list_txt(folder) -> list[str]          sorted, names only
def list_txt(folder: Path):
    names = []
    for file in folder.iterdir():
        if file.suffix == ".txt":
            names.append(file.name)
    return names
    # i have a question
    # as i tested with multiple file name variation
    # the result is always sorted even without using sorted(names)
    # so it is unnecessary to add sorted() for the result right?
        
folder = Path("docs")
folder.mkdir(exist_ok=True)
for name in ["c.txt", "b.csv", "a.txt", "d.log"]:
    (folder / name).write_text("hi", encoding="utf-8")

print(list_txt(folder))

# --- E5 — Whole-file round trip -------------------------------
# save_text(path, content) -> True       write_text
# load_text(path) -> str                 read_text
def save_text(path: Path, content):
    path.write_text(content, encoding="utf-8")
    return True

def load_text(path: Path):
    return path.read_text(encoding="utf-8")
    
    
p = Path("story.txt")
print(save_text(p, "line one\nline two\n"))
print(repr(load_text(p)))
print(save_text(p, "replacement\n"))
print(repr(load_text(p)))
print(repr(load_text(p)))

# --- M1 — read_text summary -----------------------------------
# summarize(path) -> dict {"total": int, "valid": int}
def summarize(path: Path):
    summary = {
        "total": 0,
        "valid": 0,
    }
    lines = path.read_text(encoding="utf-8")
    for line in lines.splitlines():
        if "," not in line:
            continue
        try:
            name, value = line.split(",")
            value = int(value)
        except:
            continue
        else:
            summary["total"] += value
            summary["valid"] += 1
    return summary
    
    
Path("scores.txt").write_text("ana,10\nbob,20\nbad\ncid,5\n", encoding="utf-8")

s = summarize(Path("scores.txt"))
print(f"total: {s['total']}")
print(f"valid: {s['valid']}")

# --- M2 — Organize by extension -------------------------------
# organize(folder) -> list[str]          sorted "ext: count" lines
#                                         creates subfolders, moves files
def organize(folder: Path):
    result = {}
    
    for file in folder.iterdir():
        if file.is_dir():
            continue
        
        ext = file.suffix[1:] 
        subfolder = folder / ext
        subfolder.mkdir(exist_ok=True)
        
        target = subfolder / file.name
        if target.exists():
            continue
        
        file.rename(target)
        result[ext] = result.get(ext, 0) + 1
        
    return sorted(f"{key}: {value}" for key, value in result.items())

    
folder = Path("inbox")
folder.mkdir(exist_ok=True)
for f in ["a.csv", "b.txt", "c.csv"]:
    (folder / f).write_text("x", encoding="utf-8")

for line in organize(folder):
    print(line)

print(sorted(p.name for p in folder.iterdir() if p.is_dir()))

# --- M3 — Typed loader on Path --------------------------------
# SPEC lives at module level in the notebook cell:
#   SPEC = {"retries": int, "rate": float, "name": str}
# load_settings(path) -> dict            starts EMPTY, strips values,
#                                        raises ValueError(f"bad setting: {key}")
def load_settings(path: Path):
    result = {}
    
    lines = path.read_text(encoding="utf-8")
    for line in lines.split():
        key, value = line.strip().split("=", 1)
        if key in SPEC:
            try:
                result[key] = SPEC[key](value)
            except ValueError:
                raise ValueError(f"bad setting: {key}") 
    return result


SPEC = {"retries": int, "rate": float, "name": str}
Path("app.cfg").write_text("retries=3\nrate=0.5\nname=cli\n", encoding="utf-8")
print(load_settings(Path("app.cfg")))

Path("bad.cfg").write_text("retries=three\nrate=0.5\n", encoding="utf-8")
try:
    print(load_settings(Path("bad.cfg")))
except ValueError as err:
    print(err)

# --- H1 — Debug: three bugs -----------------------------------
# Fix report_folder(folder) IN the notebook cell.
# Keep a written list here of each bug: expected vs observed, root cause.
#   Bug 1 (suffix filter case):
#     expected: ['app.py','util.py']   observed: []
#     root cause: ".PY" never matches real ".py" suffixes.
#   Bug 2 (uppercased names):
#     expected: app.py   observed: APP.PY
#     root cause: ".upper()" is a string method applied to the base name.
#   Bug 3 (folder counted as a file):
#     expected: no data.py   observed: data.py listed
#     root cause: iterdir() yields folders; missing an is_dir() guard.
from pathlib import Path

def report_folder(folder):
    result = []
    for child in folder.iterdir():
        if child.suffix == ".py" and not child.is_dir(): # change .PY to .py, add not is_dir
            result.append(child.name) # remove upper()
    return result


# --- driver (do not change) ---
folder = Path("proj")
folder.mkdir(exist_ok=True)
for name in ["app.py", "util.py", "readme.txt"]:
    (folder / name).write_text("x", encoding="utf-8")
(folder / "data.py").mkdir()

print(report_folder(folder))
print(report_folder(folder) == ["app.py", "util.py"])



# --- H2 — Interview drill: count by extension -----------------
# count_ext(folder) -> dict              extension (with dot) -> count
def count_ext(path: Path):
    result = {}
    
    if not path.exists():
        return result
    
    for item in path.iterdir():
        if not item.is_file():
            continue
        
        ext = item.suffix
        result[ext] = result.get(ext, 0) + 1
        
    return result

folder = Path("mix")
folder.mkdir(exist_ok=True)
for f in ["a.csv", "b.txt", "c.csv", "d.py", "e.csv", "notes.txt"]:
    (folder / f).write_text("x", encoding="utf-8")
(folder / "sub").mkdir(exist_ok=True)

print(count_ext(folder))
print("empty:", count_ext(Path("emptydir")))

# --- Challenge — Folder Reporter ------------------------------
# count_by_ext(folder) -> dict           extension -> count, files only
# largest(folder) -> str | None          name of largest file by size
# write_report(folder, out_path) -> str  builds the report, writes it with
#                                        Path.write_text, returns the text.
#                                        The report ends with a trailing "\n".
def count_by_ext(folder: Path):
    result = {}
    if not folder.exists():
        return result
    
    for item in folder.iterdir():
        if not item.is_file():
            continue
        
        ext = item.suffix
        result[ext] = result.get(ext, 0) + 1
        
    return result

def get_size(file_path: Path):
    return file_path.stat().st_size

def largest(folder: Path):
    if not folder.exists():
        return None
    
    files = [item for item in folder.iterdir() if item.is_file()]
    
    largest_file = max(files, key=get_size)
    
    return largest_file.name

def write_report(folder: Path, out_path: Path):
    ext_counts = count_by_ext(folder)
    largest_file_name = largest(folder)
    
    report_lines = ["Extension summary:"]
    
    for key, value in sorted(ext_counts.items()):
        report_lines.append(f"{key}: {value}")
    
    report_lines.append(f"Largest file: {largest_file_name}")
    
    report_string = "\n".join(report_lines) + "\n"
    out_path.write_text(report_string, encoding="utf-8")
    return report_string


folder = Path("assets")
folder.mkdir(exist_ok=True)
sizes = {"aa.csv": 100, "bb.txt": 300, "cc.csv": 200, "dd.log": 50}
for name, size in sizes.items():
    (folder / name).write_bytes(b"x" * size)

body = write_report(folder, Path("assets_report.txt"))
print(body, end="")
print("--- file ---")
print(Path("assets_report.txt").read_text(encoding="utf-8"), end="")
print("empty:", largest(Path("empty_assets")))
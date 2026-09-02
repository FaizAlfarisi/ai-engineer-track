# Lesson 11 — JSON · solution workspace
# ==============================================================
# Blank on purpose: write your implementations below, then paste
# finished code into the matching exercises.ipynb cell and run it.
#
# House rules for every exercise:
#   - import: from pathlib import Path, and import json
#   - every Path read/write passes encoding="utf-8"
#   - loaders return data or a documented default — never an error
#     string, never print
#   - a missing/broken file is guarded with .exists() (LBYL) or caught,
#     e.g. json.JSONDecodeError (EAFP)
#
# Sections below mirror the notebook — keep them in order.


# --- E1 — Round trip with dumps / loads -----------------------
# dumps_then_loads(data) -> (text, back)
#   text with json.dumps(data), then back with json.loads(text)
from pathlib import Path
import json
# (write your dumps_then_loads function here)
def dumps_then_loads(data):
    text = json.dumps(data)
    back = json.loads(text)
    
    return text, back

data = {"name": "alice", "retries": 3, "ok": True, "val": None}
text, back = dumps_then_loads(data)
print(text)
print(back == data)

# --- E2 — Save and load through a file ------------------------
# save_json(path, data) -> True      write_text + dumps (default options)
# load_json(path) -> data            read_text + loads
def save_json(path: Path, data):
    path.write_text(json.dumps(data), encoding="utf-8")
    return True

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

rows = [{"name": "x", "amount": 10.0}, {"name": "y", "amount": 20.5}]
save_json(Path("rows.json"), rows)
back = load_json(Path("rows.json"))
print(back == rows)
print(type(back).__name__)


# --- E3 — Iterate a loaded list -------------------------------
# summarize_rows(data) -> (total, names)
#   total via sum(...); names via a list comprehension (n > 1)
# (write your summarize_rows function here)

def summarize_rows(data):
    total = sum(d["n"] for d in data)
    names = [d["name"] for d in data if d["n"] > 1]
    return total, names

data = json.loads('[{"name": "a", "n": 1}, {"name": "b", "n": 2}, {"name": "c", "n": 3}]')
total, names = summarize_rows(data)
print(total)
print(names)


# --- E4 — indent and compact output ---------------------------
# show_both_forms(cfg) -> None    prints indent=2 form, then compact form
# (write your show_both_forms function here)

def show_both_forms(cfg):
    print(json.dumps(cfg, indent=2))
    print(json.dumps(cfg, separators=(",", ":")))

cfg = {"host": "localhost", "ports": [80, 443]}
show_both_forms(cfg)

# --- E5 — JSON type mapping -----------------------------------
# json_types(data) -> list[str]    type name per key in order, list comp
# (write your json_types function here)

def json_types(data):
    return [type(data[k]).__name__ for k in data]

text = '{"a": 1, "b": 2.5, "c": "x", "d": true, "e": false, "f": null, "g": [1, 2]}'
data = json.loads(text)
print(json_types(data))


# --- M1 — Safe loader with a default --------------------------
# load_settings(path) -> dict
#   missing file            -> {}
#   present but broken JSON -> {}   (catch json.JSONDecodeError)
#   valid JSON              -> the loaded dict
def load_settings(path: Path):
    if not path.exists():
        return {}
    
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}

Path("good.json").write_text('{"retries": 3}', encoding="utf-8")
Path("broken.json").write_text("{oops", encoding="utf-8")
print(load_settings(Path("missing.json")))
print(load_settings(Path("broken.json")))
print(load_settings(Path("good.json")))

# --- M2 — Pretty round trip -----------------------------------
# save_pretty(path, data) -> True     write_text with dumps(indent=2)
# load(path) -> data                  read_text + loads

def save_pretty(path: Path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return True

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


nested = {"user": {"name": "alice", "tags": ["a", "b"]}}
save_pretty(Path("n.json"), nested)
back = load(Path("n.json"))
print(back == nested)
print(Path("n.json").read_text(encoding="utf-8"))


# --- M3 — Typed loader with a clean re-raise, and a match route
# SPEC = {"retries": int, "rate": float, "name": str}
# load_typed(path) -> dict
#   skip blank lines and unknown keys
#   on conversion failure: raise ValueError(f"bad setting: {key}") from None
# describe(record) -> str   using match (mapping patterns)

SPEC = {
    "retries": int,
    "rate": float,
    "name": str
}

def load_typed(path: Path):
    result = {}
    
    lines = path.read_text(encoding="utf-8")
    for raw in lines.splitlines():
        line = raw.strip()
        if not line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key not in SPEC:
            continue
        try:
            result[key] = SPEC[key](value)
        except ValueError:
            raise ValueError(f"bad setting: {key}") from None
    return result

def describe(record):
    match record:
        case {"kind": "income", "amount": amt}:
            return f"+{amt}"
        case {"kind": "expense", "amount": amt}:
            return f"-{amt}"
        case _:
            return "?"
    return


cfg = Path("app.cfg")
cfg.write_text("retries=3\nrate=12.5\nname=alice\n", encoding="utf-8")
print(load_typed(cfg))
bad = Path("bad.cfg")
bad.write_text("retries=oops\n", encoding="utf-8")
try:
    load_typed(bad)
except ValueError as e:
    print("ValueError:", e)
records = [{"kind": "income", "amount": 5}, {"kind": "expense", "amount": 3}, {"kind": "junk", "amount": 1}]
print([describe(r) for r in records])


# --- H1 — Debug: bugs in a JSON folder tool -------------------
# Fix collect_json(folder) IN the notebook cell.
# Keep a written list here of each bug: expected vs observed, root cause.
#   Bug 1 (suffix filter case):
#     expected: catch the json file observed: catch no data
#     root cause: suffix '.JSON' must be '.json'
#   Bug 2 (folder read as a file):
#     expected: iter through folder dir then skip the child that is not a file   observed: Permission denied: 'conf\\config.json'
#     root cause: no check if the child is a file
#   Bug 3 (wrong result shape):
#     expected: merge read text to a single dict   observed: return list of dict from read text
#     root cause: result declared as a list 
#   Bug 4:
#     expected: handle the dict result   observed: append result list
#     root cause: changing data type must be changing how the handling data behaviour
from pathlib import Path
import json

# def collect_json(folder):
#     result = []
#     for child in folder.iterdir():
#         if child.suffix == ".JSON":
#             result.append(json.loads(child.read_text(encoding="utf-8")))
#     return result

def collect_json(folder):
    result = {}
    for child in folder.iterdir():
        if not child.is_file():
            continue
        if child.suffix == ".json":
            text = json.loads(child.read_text(encoding="utf-8"))
            for key, value in text.items():
                result[key] = value
    return result

# --- driver (do not change) ---
folder = Path("conf")
folder.mkdir(exist_ok=True)
(folder / "app.json").write_text('{"retries": 3}', encoding="utf-8")
(folder / "db.json").write_text('{"host": "x"}', encoding="utf-8")
(folder / "config.json").mkdir()
expected = {"retries": 3, "host": "x"}
print(collect_json(folder))
print(collect_json(folder) == expected)


# --- H2 — Interview drill: count by key with edge cases -------
# count_by(items, key) -> dict
#   missing key counts as "missing"   (use it.get(key, "missing"))
#   items whose value is None are skipped
#   preserve first-seen insertion order

def count_by(items, key):
    result = {}
    
    for item in items:
        value = item.get(key, "missing")
        
        if value is None:
            continue
        
        result[value] = result.get(value, 0) + 1
        
    return result

records = [
    {"kind": "income", "tag": "a"},
    {"kind": "expense", "tag": "b"},
    {"kind": "income", "tag": "a"},
    {"kind": "expense", "tag": None},
    {"amount": 5},
]
print(count_by(records, "tag"))
print(count_by(records, "kind"))

# --- Challenge — Expense JSON seed ----------------------------
# load(path) -> list        missing/broken/not-a-list -> []
# categorize(record) -> float   match: income -> +amt, expense -> -amt, else 0
# summarize(spends) -> dict     category -> signed total (start each at 0.0)
# save(path, spends) -> True    write_text + dumps(indent=2)

def load(path: Path):
	if not path.exists():
		return []
	
	try:
		text = json.loads(path.read_text(encoding="utf-8"))
	except json.JSONDecodeError:
		return []
	
	if type(text).__name__ != "list":
		return []

	return text

def categorize(record):
	match record:
		case {"kind": "income", "amount":amt}:
			return amt
		case {"kind": "expense", "amount":amt}:
			return -amt
		case _:
			return 0.0

def summarize(spends):
	result = {}
	for spend in spends:
		category = spend['category']
		result[category] = result.get(category, 0.0) + categorize(spend)
	return result

def save(path: Path, spends):
	path.write_text(json.dumps(spends, indent=2), encoding="utf-8")
	return True

p = Path("expenses.json")
print("missing:", load(Path("nope.json")))
p.write_text(json.dumps([
    {"category": "food", "amount": 12.5, "kind": "expense"},
    {"category": "travel", "amount": 40.0, "kind": "expense"},
    {"category": "salary", "amount": 2000.0, "kind": "income"},
], indent=2), encoding="utf-8")
spends = load(p)
print("summarize:", summarize(spends))
save(Path("saved.json"), spends)
print("roundtrip:", load(Path("saved.json")) == spends)
print("saved line1:", repr(Path("saved.json").read_text(encoding="utf-8").splitlines()[1]))
bad = Path("broken.json")
bad.write_text("{oops", encoding="utf-8")
print("broken:", load(bad))

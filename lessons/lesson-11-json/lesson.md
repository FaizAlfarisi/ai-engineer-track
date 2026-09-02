# Lesson 11 — JSON (Tier: CORE)

Stage 2, fourth topic. You can already read and write text files. JSON
turns that text into real data that your program can use. The Expense
Manager you are building toward will save its data as JSON.

---

## Objective

By the end of this lesson you can:

- Convert a dict or list to a JSON string with `json.dumps()`.
- Convert a JSON string back to a dict or list with `json.loads()`.
- Save a Python value to a file and load it back, using pathlib.
- Write readable JSON with `indent` and compact JSON with `separators`.
- Handle a broken JSON file without crashing (`JSONDecodeError`).
- Route on the shape of a loaded record with `match`.

---

## Why This Matters

Text files (Lesson 9) store lines of text. A line like
`"alice,42"` means nothing until your code decides how to split it. JSON
fixes that: it is a standard format that holds numbers, strings, lists,
and nested objects, so the data keeps its type and its shape.

Almost every real program that talks to another program uses JSON — a
web API returns JSON, a config file is JSON, the Expense Manager will
store its data as JSON. Learning JSON means learning the interchange
format the whole industry uses.

---

## Mental Model

A Python dict and a JSON object have the same shape: a set of keys and
values.

```text
Python:    {"name": "alice", "retries": 3}
JSON:      {"name": "alice", "retries": 3}
```

JSON is a **string** that looks like Python data. `json.dumps()` turns a
Python value into that string. `json.loads()` turns the string back into
a Python value.

You usually store that string in a file with pathlib, then load it back
when the program runs again. Save with `write_text` (Lesson 10), load
with `read_text` (Lesson 10).

---

## Core Concept

### Convert a value to a JSON string

```python
import json

data = {"name": "alice", "retries": 3}
text = json.dumps(data)
print(text)   # {"name": "alice", "retries": 3}
```

`json.dumps()` returns a string. By default it adds a space after the
colon and after each comma.

### Convert a JSON string back to a value

```python
text = '{"name": "alice", "retries": 3}'
data = json.loads(text)
print(data["name"])   # alice
```

JSON numbers become Python `int`/`float`, JSON strings become `str`,
JSON arrays become `list`, JSON objects become `dict`, `true`/`false`
become `True`/`False`, and `null` becomes `None`.

Example: JSON `[1, 2.5, "x"]` loads as the Python list `[1, 2.5, 'x']`.

### Save and load through a file (pathlib)

```python
from pathlib import Path
import json

path = Path("data.json")
path.write_text(json.dumps(data), encoding="utf-8")

loaded = json.loads(path.read_text(encoding="utf-8"))
```

Use `encoding="utf-8"` on every read and write, as in Lessons 9 and 10.

### Readable and compact output

`json.dumps(value, indent=2)` puts each key on its own line. Use it when
a human may read the file.

`json.dumps(value, separators=(",", ":"))` removes the extra spaces. Use
it when size matters. It produces `{"a":1,"b":2}` instead of
`{"a": 1, "b": 2}`.

### Handle a broken file

A file that is not valid JSON raises `json.JSONDecodeError`. That is a
subclass of `ValueError` (Lesson 8). Catch it where you load, and decide
what to do — raise a clean message, or return a default.

```python
try:
    data = json.loads(path.read_text(encoding="utf-8"))
except json.JSONDecodeError:
    data = {}   # default when the file is broken
```

### Route on the shape of a record with `match`

JSON data often has records of different kinds. You can use `match`
(Lesson 3) with mapping and sequence patterns to pick a branch by shape:

```python
def route(record):
    match record:
        case {"kind": "income", "amount": amt}:
            return amt
        case {"kind": "expense", "amount": amt}:
            return -amt
        case _:
            return 0
```

---

## Practical Examples

**1. Save a list of dicts and load it back:**

```python
rows = [{"name": "x", "amount": 10.0}, {"name": "y", "amount": 20.5}]
path = Path("rows.json")
path.write_text(json.dumps(rows), encoding="utf-8")
back = json.loads(path.read_text(encoding="utf-8"))
print(back == rows)   # True
```

**2. Pretty-print a config for a human:**

```python
cfg = {"host": "localhost", "ports": [80, 443]}
print(json.dumps(cfg, indent=2))
```

**3. Guard a missing or broken file:**

```python
def load_settings(path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
```

**4. Route a record by its `kind`:**

```python
records = [{"kind": "income", "amount": 5},
           {"kind": "expense", "amount": 3}]
total = sum(route(r) for r in records)
print(total)   # 2
```

---

## Engineering Notes

- **Use pathlib, not `open()`.** `Path.read_text` and `Path.write_text`
  (Lesson 10) are the shortest way to save and load JSON.
- **`import json` at the top**, not inside a function (Lesson 7).
- **Keep loaders clean.** A JSON loader returns data or a documented
  default — never an error string (Lesson 9, still true here).
- **Catch at the boundary.** A broken file is caught where you load, near
  the call, not scattered through the logic (Lesson 8).
- **Canonicalize at save.** Re-write stored data in one consistent form so
  re-runs are stable (Lesson 9 idea, applied to JSON).
- **`json.dumps` cannot serialize everything.** A `set` or a custom object
  is not JSON. Convert to lists/dicts first if you need them.

---

## Applied AI Perspective

AI pipelines are loaded with JSON: the config that sets model
parameters, the dataset of prompt/response records, the API payloads
sent and received. A training script reads a JSON config at startup,
loads a JSON dataset, and writes results back as JSON. When an API
returns malformed JSON, the pipeline must not crash — it catches
`JSONDecodeError` at the boundary and falls back (Lesson 8). The
"save records → load records → summarize" pattern you build here is the
same shape as a real data-for-AI pipeline.

---

## Common Pitfalls

1. **JSON uses double quotes.** `'{"a": 1}'` is valid; `"{'a': 1}"` is
   not. `json.loads` rejects single quotes around keys.
2. **Forgetting `encoding="utf-8"`.** A JSON file written with it must be
   read with it (Lessons 9–10).
3. **Loading a broken file without a guard.** It raises
   `JSONDecodeError`; catch it at the boundary or guard the file first.
4. **Returning an error string from a loader.** Return data or a default
   (Lesson 9 rule; Quiz 01 B1).
5. **`indent` vs `separators`.** `indent=2` for humans, compact
   `separators=(",", ":")` for size. Do not mix them casually.
6. **Case sensitivity in `match`.** `{"kind": "income"}` matches only an
   exact `"income"`. Watch spelling and case.
7. **`get` for optional keys.** A loaded dict may miss a key; use
   `.get("key", default)` to avoid a `KeyError` (Lesson 6).

---

## Connection to Previous Knowledge

- **Pathlib (L10):** JSON lives in a file. You save with `Path.write_text`
  and load with `Path.read_text`, both with `encoding="utf-8"`.
- **File Handling (L9):** whole-file read/write is exactly the JSON round
  trip; clean-loader and canonicalize-at-save rules carry over.
- **Exception Handling (L8):** a broken JSON file raises
  `json.JSONDecodeError`, a `ValueError` subclass. Guard with `.exists()`
  (LBYL) or catch it (EAFP) — the L8 decision rule applies. Clean
  re-raise with `from None` appears in M3 (Quiz 01 D2).
- **Collections (L6):** JSON maps one-to-one with dicts and lists — the
  type table (L1) returns. Summaries land in dicts.
- **Functions (L5):** loaders return data, never print, never error-strings.
- **Loops (L4):** you iterate a loaded JSON list with `for`.
- **Modules (L7):** `import json`.
- **Boolean logic / `match` (L3):** mapping and sequence patterns pick a
  branch by the shape of a record.
- **Spec-literalness:** output is byte-exact — including the exact spaces
  JSON adds around colons and commas.

---

## Quick Recall

Answer from memory before starting Practice:

1. What do `json.dumps()` and `json.loads()` do, and which way does each go?
2. How do JSON `true`, `false`, and `null` map to Python values?
3. What is the default spacing of `json.dumps`, and how do `indent=2` and
   `separators=(",", ":")` change it?
4. What exception does `json.loads` raise on broken JSON, and what is it a
   subclass of?
5. Why save JSON with pathlib instead of raw `open()`?
6. How do you pick a branch by the shape of a loaded record?

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`; write solutions
in `solution.py` first, then paste into notebook cells. Every cell is
self-contained — it builds its own fixtures.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1–E5 | Easy ×5 | [REAL-WORLD] | round-trip dumps/loads · save/load via pathlib · iterate a loaded list · indent & compact · type mapping |
| M1–M3 | Medium ×3 | [REAL-WORLD] | safe loader with default · pretty round trip · typed loader that re-raises cleanly (`from None`) + `match` route |
| H1 | Hard | [REAL-WORLD] | debug drill: bugs in a JSON folder tool |
| H2 | Hard | [INTERVIEW] | merge JSON records / report by key — edge cases |
| Challenge | Micro Build | [REAL-WORLD] | Expense JSON seed — load, validate, summarize, save |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, save/load a JSON value through pathlib, existence and
`JSONDecodeError` guards, a `match` route by record shape, and a worked
JSON tool that survives re-runs.

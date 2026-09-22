# Lesson 10 — Pathlib (Tier: CORE)

Stage 2, third topic. In Lesson 9 you worked with files by gluing
strings together. Pathlib makes a path a real object, not a string.

---

## Objective

By the end of this lesson you can:

- Build a `Path` object and read its parts (`.name`, `.stem`, `.suffix`, `.parent`).
- Join paths with `/` and list directory contents with `.iterdir()`.
- Read a whole file with `.read_text()` and write one with `.write_text()`.
- Check whether a path exists before you touch it (`.exists()`).
- Decide when to use `Path` methods and when to fall back to a file handle.

---

## Why This Matters

On your machine, paths can be tricky. A folder name may contain a space.
A Windows path uses `\`; the web and most other systems use `/`.
Writing `"data/" + name + ".txt"` breaks when a part has a space, and it
forces you to remember which separator your OS uses.

Pathlib removes all of that. You build a path as a `Path` object, join
parts with `/`, and let Python handle the separator for your OS. This is
the tool real projects use — the Expense Manager you are building toward
will live in a folder and read and write files in it.

---

## Mental Model

A string path is text that happens to name a file. A `Path` is an object
that knows how to talk to the file system.

```text
"data/report.txt"          # a plain string — no literacy about files
Path("data/report.txt")    # an object with .name, .parent, .exists()...
```

You make a `Path`, then ask it questions (`.exists()`, `.name`) and give
it commands (`.read_text()`, `.write_text()`). The `/` operator joins
two `Path` objects into one new path.

---

## Core Concept

### Build a path

```python
from pathlib import Path

p = Path("data") / "report" / "final.txt"
# p.name   == "final.txt"
# p.stem   == "final"
# p.suffix == ".txt"
# p.parent == path to the data/report folder
```

`/` joins parts and inserts the correct separator for your OS. No more
`"data" + "/" + "report"`.

### Inspect a path before using it

```python
if p.exists():
    print(p.name, "is there")
else:
    print(p.name, "is missing")
```

`Path.iterdir()` lists the entries in a folder. Combine it with a check
on `.suffix` or `.name` to filter:

```python
sub = Path("data")
for child in sub.iterdir():
    if child.suffix == ".txt":
        print(child.name)
```

### Read and write a whole file

For whole files, these short forms replace the longer `open()` dance:

```python
text = Path("note.txt").read_text()       # one string, whole file
Path("note.txt").write_text("hello\n")    # write a whole file at once
```

Both use text mode and default to your OS encoding unless you pass
`encoding="utf-8"` explicitly — keep passing it, as in Lesson 9.

Example: `Path("n.txt").write_text("a\nb\n")`, then `read_text()`
returns `"a\nb\n"` — the exact two lines you wrote.

### When you still need a handle (retrieve Lesson 9)

Whole-file is easy. For line-by-line work, `Path.open()` gives you the
same handle you learned in Lesson 9:

```python
with Path("big.log").open(encoding="utf-8") as f:
    for line in f:
        ...
```

`Path.open()` is the `open()` you know, accessed through the path
object. `with` still closes it for you.

---

## Practical Examples

**1. Build and join:**

```python
base = Path("data")
report = base / "2026" / "sales.csv"
print(report.suffix)     # .csv
print(report.name)       # sales.csv
```

**2. List only Python files:**

```python
for f in Path("src").iterdir():
    if f.suffix == ".py":
        print(f.name)
```

**3. Read a whole config in one line:**

```python
text = Path("app.cfg").read_text(encoding="utf-8")
print(text)
```

**4. Guard before you act:**

```python
source = Path("diary.txt")
if source.exists():
    Path("backup.txt").write_text(source.read_text(encoding="utf-8"))
else:
    print("diary.txt missing — nothing to back up")
```

---

## Engineering Notes

- **`Path` is the standard.** `os.path` (Lesson 7) still works, but
  `pathlib` is what new code prefers. Use it for new work.
- **Join with `/`, never by string.** `/` handles separators and spaces
  for you.
- **`read_text`/`write_text` are whole-file.** They read or write at
  once. For big files or per-line output, use `Path.open()` and a loop.
- **Check existence when it matters.** `.exists()` is cheap. Guard a
  read or rename with it when the file may not be there.
- **`write_text` has no `open` mode argument.** It always (re)writes the
  whole file — like `"w"`. It truncates. Do not expect append semantics.
- **Encoding on both sides.** Pass `encoding="utf-8"` to `read_text`,
  `write_text`, and `Path.open()` — same habit as Lesson 9.
- **Keep loaders clean.** A loader returns data (or a default), never an
  error-string — same rule we set in Lesson 9.

---

## Applied AI Perspective

AI pipelines are full of paths: where the dataset lives, where checkpoints
are saved, which files are logs. Pathlib makes those "which folder /
which extension / is it there" questions obvious and OS-safe. A training
script often starts by building a `Path` from a config value, checking it
exists, and iterating the files it must load — every one of those is a
Pathlib line you are learning today.

---

## Common Pitfalls

1. **Gluing paths with strings.** `"data/" + name` breaks with spaces
   and the wrong separator. Use `/`.
2. **Forgetting `.exists()`.** Reading or renaming a path that is not
   there raises `FileNotFoundError`. Check first when the file may be
   absent.
3. **Expecting `write_text` to append.** It rewrites the whole file (like
   `"w"`). It erases old content.
4. **Testing a path that is a folder as if it were a file.** A folder is
   also a path. Use `.is_file()` when you specifically need a file.
5. **No encoding argument.** Omitting it uses your OS default, which
   differs between machines. Pass `encoding="utf-8"`.
6. **Filtering `iterdir` with string tricks.** Compare `.suffix` or
   `.name` directly instead of slicing the string.
7. **String path methods on `Path`.** A `Path` is not a string; use
   `str(p)` if you truly need text, not `.lower()` on the object.

---

## Connection to Previous Knowledge

- **File Handling (L9):** this lesson is a direct follow-up. `Path.open()`
  is the `open()` you mastered; `read_text`/`write_text` are short forms of
  the two-handle read/write you built. All of L9's modes (`r`/`w`/`a`),
  `with`, and `encoding="utf-8"` habits carry over unchanged.
- **Exception Handling (L8):** a missing path is still a
  `FileNotFoundError`. Guard with `.exists()` (LBYL) or catch it (EAFP) —
  the decision rule from L8 applies.
- **Collections (L6):** summaries of what you found land in dicts; a
  per-extension count is your old counting-in-dict pattern.
- **Functions (L5):** loaders and savers stay pure — they take a path,
  return data, never print.
- **Loops & accumulators (L4):** `for child in folder.iterdir()` is your
  loop pattern with a new source of items.
- **Modules (L7):** `from pathlib import Path` — the import form you
  already know.
- **Spec-literalness:** output is byte-exact — including file contents.

---

## Quick Recall

Answer from memory before starting Practice:

1. What does `Path("data") / "report" / "final.txt"` produce, and why is
   `/` better than `"data/" + "report/" + ...`?
2. `.name`, `.stem`, `.suffix` for `Path("a/b/c.json")` — what is each?
3. Name one operation that returns `True`/`False`, and one that lists the
   entries in a folder.
4. `read_text()` vs `Path.open()` — when do you use each?
5. What does `write_text` do to a file that already exists?
6. A missing file still raises `FileNotFoundError`. Give one way to
   avoid it (LBYL) and one way to handle it (EAFP).

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`; write solutions
in `solution.py` first, then paste into notebook cells. Every cell is
self-contained — it builds its own fixture folders and files.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1–E5 | Easy ×5 | [REAL-WORLD] | build & inspect · join with `/` · `.exists()` · list `.txt` in a folder · whole-file read/write |
| M1–M3 | Medium ×3 | [REAL-WORLD] | read_text summary · organize by extension (mkdir) · typed loader rewired to `Path` |
| H1 | Hard | [REAL-WORLD] | debug drill: three bugs in a pathlib tool |
| H2 | Hard | [INTERVIEW] | count files by extension — edge cases |
| Challenge | Micro Build | [REAL-WORLD] | Folder Reporter — list, filter, summarize to a file |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, correct choice between `Path` whole-file methods and a
handle, existence guards, and a worked Pathlib folder tool that survives
re-runs.

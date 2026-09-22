# Lesson 9 — File Handling (Tier: CORE)

Stage 2, second topic. Scripts become programs the moment they remember
things. This lesson is where your data survives the process.

---

## Objective

By the end of this lesson you can:

- Open, read, write, and append to text files using `with` — every time.
- Choose between `read()`, iteration, and `readlines()` and justify the choice.
- Explain what the file cursor is and predict where it points after each operation.
- Handle missing and unreadable files gracefully (`FileNotFoundError`).
- Write files that another run of your own program can read back correctly.

---

## Why This Matters

Every variable dies when the process ends. Files are the first persistence
tool you own — config, logs, datasets, saved state all arrive as files.
The Expense Manager you're building toward must reload its data on every
launch; after this lesson, that requirement is within reach.

Files also fail differently than variables: the thing you asked for may
not exist, may be locked, or may contain surprises. That is why this
lesson sits directly after Exception Handling — every exercise here is
also an unannounced retrieval for try/except.

---

## Mental Model

A file is a **named sequence of bytes on disk**. Opening it in text mode
gives you a **handle**: a cursor with permissions.

```text
handle = permission slip + cursor
"r"    → read from cursor          (cursor starts at position 0)
"w"    → truncate file to ZERO, then write   ← destructive!
"a"    → append; cursor parked at end
```

Reading pulls bytes from the cursor forward and decodes them into `str`
using an encoding. Writing encodes `str` back to bytes. When the cursor
hits the end, reads return nothing — silently. Most "my loop never ran"
mysteries are a cursor that was already consumed.

`with` gives the handle a guaranteed retirement: whatever happens inside
the block — success, exception, early `return` — the file gets closed.
It is your Lesson 8 `finally`, automated.

---

## Core Concept

### The three modes you need

| Mode | Cursor | Existing content | Typical use |
|------|--------|------------------|-------------|
| `"r"` | start | untouched (must exist) | reading |
| `"w"` | start | **erased** | fresh writes, rewrites |
| `"a"` | end | untouched | logs, appends |

### Reading strategies

```python
with open(path, encoding="utf-8") as f:
    whole = f.read()          # one string — fine for small config-ish files

with open(path, encoding="utf-8") as f:
    for line in f:            # DEFAULT for line work: lazy, memory-friendly
        ...

with open(path, encoding="utf-8") as f:
    lines = f.readlines()     # list of ALL lines — only when you truly need them all
```

Iterating the handle yields lines **including their trailing `\n`** —
`.strip()` before comparing or printing cleanly.

### Writing strategies

`f.write(s)` writes exactly what you give — no implicit newline. Build
multi-line output yourself (`"\n".join(lines)` + final `"\n"`), or call
`write` per line. `f.writelines(seq)` exists but does NOT add newlines;
join-then-write is clearer and does exactly what it says.

### The with statement

```python
with open(path, "w", encoding="utf-8") as f:
    f.write("data")
# f closed HERE — even if write() raised
```

Two handles at once share one `with`:

```python
with open(src, encoding="utf-8") as fin, open(dst, "w", encoding="utf-8") as fout:
    ...
```

### Encoding: say it out loud

Text mode needs an agreement about how bytes become characters. Always
pass `encoding="utf-8"` explicitly — the silent OS default differs
between machines (and Windows history is exactly why). Three words,
whole class of bugs gone.

### Missing files are normal

```python
try:
    with open(path, encoding="utf-8") as f:
        return f.read()
except FileNotFoundError:
    return ""            # or a default, or create-and-continue
```

First-run behavior is a design decision, not an accident.

---

## Practical Examples

**1. Round trip** — write, then read back:

```python
with open("note.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

with open("note.txt", encoding="utf-8") as f:
    print(f.read(), end="")      # hello
```

**2. Append proves persistence:**

```python
for event in ["boot", "ready"]:
    with open("events.log", "a", encoding="utf-8") as f:
        f.write(event + "\n")
```

**3. Line-by-line summary** — loops + accumulators meet files:

```python
count = 0
total = 0.0
with open("temps.txt", encoding="utf-8") as f:
    for line in f:
        count += 1
        total += float(line)     # float tolerates the trailing newline
```

**4. Missing → default** — the first-run pattern:

```python
try:
    with open(path, encoding="utf-8") as f:
        return f.read()
except FileNotFoundError:
    return DEFAULT
```

---

## Engineering Notes

- **`with` is not optional style.** Unclosed handles lock resources and,
  on some platforms, lose buffered data. If you ever write bare
  `open()`, be ready to say why in review.
- **Iterate, don't hoard.** `for line in f` streams; `readlines()` loads
  everything. For a 2 GB log the difference is your RAM.
- **`readlines()` vs `read().split("\n")`:** similar results, different
  details (trailing newline handling). Know which artifact you're holding.
- **Newline translation:** text mode converts `\n` to the OS newline on
  write and back on read. Don't fight it; strip what you read.
- **Never name a variable `open`, `file`, `input`, or `type`** — you did
  this once with `min`/`max`; builtins don't forgive twice.
- Pathlib arrives next lesson and replaces string path-gluing entirely.
  Until then, keep paths short and literal.

---

## Applied AI Perspective

AI engineering is file engineering: training manifests, dataset splits,
prompt templates, inference logs, exported metrics. Pipelines that
stream corpora line-by-line process more data than fits in memory, and
every robust loader you'll ever write has the same skeleton you build
today: open with `with`, decode explicitly, expect the missing file,
summarize what survived.

---

## Common Pitfalls

1. **Opening for `'w'` on existing data** — instant, silent erasure. If
   the file must survive until you've read it, read first.
2. **Reading after consuming** — a second `read()` returns `''`; a loop
   after `read()` never runs. One cursor, one direction.
3. **Comparing unstripped lines** — `"ERROR disk full\n" != "ERROR disk
   full"`. Strip at the boundary.
4. **Forgetting the trailing newline** — `write("a"); write("b")` gives
   you `ab`. Join with `\n` and terminate the last line deliberately.
5. **Bare `open()` without `with`** — works until it doesn't (buffered
   loss, locked files).
6. **Wrong-mode writes** — writing through a handle opened for reading
   raises `io.UnsupportedOperation`; read the traceback's first line.
7. **Assuming encoding** — the machine across the desk may disagree with
   yours. Explicit `encoding="utf-8"` always.

---

## Connection to Previous Knowledge

- **Exception Handling (L8):** every exercise wraps risky opens in
  try/except — catching *specific* types, raising at boundaries, first-run
  defaults. No labels needed; you know this now.
- **Collections (L6):** summaries of file contents land in dicts; counts
  and totals accumulate like M1 taught you.
- **Loops & accumulators (L4):** `processed += 1` inside `for line in f`
  is the accumulator pattern wearing a new hat.
- **Functions (L5):** loaders and savers stay pure — they take a path,
  return data, never print. Printing belongs to the caller.
- **Modules & validation (L7/L8-M3):** the config loader reuses your
  spec-driven typed conversion, including the exact error-message contract
  and the blueprint-stays-read-only lesson.
- **Spec-literalness:** file contents are output too — byte-exact,
  canonicalized amounts included.

---

## Quick Recall

Answer from memory before starting Practice:

1. You opened a file with `"w"`, wrote one line, closed it, reopened with `"w"`, wrote another line. What's in the file — both lines or one? Why?
2. After `f.read()` succeeds, what does a second `f.read()` return, and what does `for line in f` do?
3. Iterating a handle gives you lines ending in `\n`. Name two places that newline bites you if you forget to strip.
4. What does `with` guarantee, and which Lesson 8 block does it automate?
5. Your program should work on first launch, when no data file exists yet. Give the exception you catch and one sane fallback.
6. Why write `open(path, encoding="utf-8")` instead of trusting the default?

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`; write solutions
in `solution.py` first, then paste into notebook cells. Every cell is
self-contained — it builds its own fixture files.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1–E5 | Easy ×5 | [REAL-WORLD] | round trip · append · iterate+accumulate · missing-file default · report writer |
| M1–M3 | Medium ×3 | [REAL-WORLD] | transactions file → summary · filter-and-copy pipeline · typed config loader |
| H1 | Hard | [REAL-WORLD] | debug drill: five bugs in a log analyzer |
| H2 | Hard | [INTERVIEW] | `tail(path, n)` under edge cases |
| Challenge | Micro Build | [REAL-WORLD] | Expense Persistence CLI — L8's validator grows a memory |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, file round-trips that survive re-runs, demonstrated
debugging (H1), and correct decisions about modes, strategies, and
first-run behavior.

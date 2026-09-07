# Lesson 13 — Packages & Multi-Module Structure (Tier: CORE)

Stage 2, sixth topic. In Lesson 7 you imported modules — `random`,
`sys`, `os`, and your own scripts. That was one file importing another.
This lesson is the next step: **splitting a program into several files
that work together, and organizing those files into a package.** Every
real Python project you will ever read — including AI projects — is
built this way.

---

## Objective

By the end of this lesson you can:

- Explain that a module is a file, and its import name is the file name
  without `.py`.
- Create a package (a folder with `__init__.py`) and import from it with
  dotted names like `import report_tool.load`.
- Split one program across multiple files, with each file importing the
  functions it needs from the others.
- Use a relative import (`from . import sibling`) inside a package, and
  know why the main file must use absolute imports.
- Know what `import` does when it runs a module's code, and why a module
  must not have side effects at the top level.
- Fix the classic multi-module bugs: side effects on import, wrong dotted
  paths, and relative imports in a script.

---

## Why This Matters

A program that lives in one file can grow until no human can hold it in
their head. Engineering solves that by **separating concerns**: the
loading code, the calculation code, and the output code become three
files with clear jobs.

- You already do this with *functions* (Lesson 5). Multi-module structure
  is the same idea one level up: files instead of functions.
- Readability and maintainability (RULES R8) are the goal. A colleague
  opens your project and can find the loader, the logic, and the entry
  point in seconds.
- The Expense Manager stage project, and every AI pipeline afterwards
  (data loading, model training, inference), are organized as packages.

---

## Mental Model

```text
module  = one file          greet.py            → import greet
package = a folder that     textstats/          → import textstats
          contains modules     __init__.py      → runs when imported
                              words.py          → textstats.words
                              longest.py        → textstats.longest
```

- A **module** is a file. Its name is the file name minus `.py`.
- A **package** is a folder that Python treats as one importable thing.
  The folder needs an `__init__.py` file (even an empty one) so Python
  knows it is a package.
- **Dotted names** walk this tree: `import textstats.words` means "go
  into the `textstats` folder and load `words.py`".

---

## Core Concept

### A module is a file

Create `greet.py`:

```python
def greet(name):
    return f"Hello, {name}!"
```

From another file, or from the notebook, it is already importable:

```python
from greet import greet
print(greet("ada"))          # Hello, ada!
```

The filename *is* the module name. No `greet.py` in the import — just
`greet`.

### How `import` finds your file

When you write `import something`, Python searches, in order:

1. Built-in modules (they live in the interpreter itself).
2. Directories in `sys.path` — which starts with the directory of the
   script, then `PYTHONPATH`, then the installation defaults.
3. When it finds a matching `.py` file, it loads it. If it cannot find
   one, you get `ModuleNotFoundError`.

This is why a file in the same folder as your notebook or script just
works: that folder is on the search path.

### What `import` does when it runs a module

Importing a module **executes its code once**, top to bottom. After the
first import, Python remembers the module (in `sys.modules`), so a
second `import` does **not** re-run it.

```python
# timer.py
print("timer module started")          # runs only on the FIRST import
def now():
    return "checked"
```

```python
import timer    # prints "timer module started"
import timer    # nothing this time
```

Rule that follows: **a module must not print, write files, or start
anything at the top level.** Importing should only define names. Work
happens inside functions, called when someone calls them.

### A package is a folder with `__init__.py`

```text
textstats/
    __init__.py
    words.py
```

- `words.py` defines functions (a normal module).
- `__init__.py` runs when the package is imported. It is often empty,
  or it holds a tiny bit of package-level setup (like `__version__`).
- `import textstats` runs `__init__.py`. `import textstats.words` runs
  `__init__.py` **and** loads `words.py`.

### Absolute and relative imports

Inside a package, a module can import its sibling in two ways.

Absolute (full path from the top):

```python
from textstats.words import count_words
```

Relative (from the current package — one dot means "this package"):

```python
from .words import count_words
```

The relative form only works **inside a package**, where a parent
package exists. The **main file** — the one you run — has no parent
package, so it must always use absolute imports. That is also why
running a file inside a package directly (`python mypkg/sub.py`) can
fail with `ImportError: attempted relative import` — the file is being
run as a script, outside its package.

### `from package import ...` and `import *`

`from textstats import words` works if `words` is a module in the
package. `import *` copies every public name from the target — but it
hides where names came from and can silently shadow other names (the
star-import shadowing you fixed in H1, Lesson 7). It is almost always
better to import exactly the names you need.

---

## Practical Examples

**1. Two files, one shared function:**

```python
# report.py
from words import count_words        # absolute import, same folder

def word_report(text):
    return f"words: {count_words(text)}"
```

**2. Package import by dotted name:**

```python
import textstats.words               # folder → file
print(textstats.words.count_words("a b c"))
```

**3. Relative import between siblings:**

```python
# textstats/longest.py
from .words import count_words       # this package's words module

def longest_word(text):
    return max(text.split(), key=len)
```

**4. `if __name__ == "__main__"` in a module (review from L7):**

```python
# main.py
from report_tool.load import load_transactions

def main():
    print(len(load_transactions("data.json")))

if __name__ == "__main__":
    main()
```

The guard lets `main.py` be imported (for example, to reuse `main()` in
a test) without running the pipeline by accident. Running `python
main.py` sets `__name__` to `"__main__"`, so `main()` runs.

---

## Engineering Notes

- **Import at the top of the file.** Do not scatter `import` mid-code.
  A reader should see every dependency in the first lines.
- **No work at import time.** Importing a module must only define names.
  Printing, reading files, or calling functions at the top level is a
  bug — it triggers on import, once, invisibly.
- **Keep `__init__.py` minimal.** An empty file is fine. Put package
  identity there (`__version__`), not logic.
- **Main file uses absolute imports.** The main file has no package, so
  relative imports fail there. Inside submodules, prefer relative
  imports for siblings so the package stays movable.
- **Watch for circular imports.** Two modules importing each other break.
  When a cycle appears, move the shared piece into its own module — the
  dependency should flow one way.
- **`__pycache__` is normal.** Python caches compiled modules there. Do
  not touch it; keep it out of git.
- **A loader returns data — never a side effect and never an error
  string** (the L9 rule carries into every multi-module project).

---

## Common Pitfalls

1. **Side effects at module top level** — a `print()` or file write
   triggers invisibly at import. Wrap work in functions.
2. **Relative import in the main file** — `from . import x` fails with
   `ImportError` because the main file has no parent package. Use
   absolute imports there.
3. **Wrong dotted path** — `import textstats.words` needs `words` to be
   a file or package in `textstats/`. A typo gives `ModuleNotFoundError`.
4. **Forgetting `__init__.py`** — without it, the folder is not a
   regular package (Python 3 can fall back to namespace packages, but
   the explicit `__init__.py` is the standard, clear form).
5. **`import *` shadowing** — unknown names appear from nowhere (L7
   star-import shadowing, now at package scale). Import exactly what you
   need.
6. **Circular imports** — `a` imports `b`, `b` imports `a`. Break the
   cycle by extracting the shared code into a third module.
7. **`__name__` confusion** — a file run as a script gets `__name__ ==
   "__main__"`; a file imported gets its module name. The guard exists
   for precisely this reason (L7 review).

---

## Connection to Previous Knowledge

- **Modules & imports (L7):** import forms, the `__main__` guard, and
  star-import shadowing return here — now across multiple files and a
  package.
- **Functions (L5):** multi-module structure is function decomposition
  one level up. A loader, a calculator, a writer — each a module.
- **Exception handling (L8):** `ModuleNotFoundError` and `ImportError`
  are exceptions. You catch and diagnose them by tracing where the
  import is looking.
- **Pathlib (L10), JSON (L11), CSV (L12), File handling (L9):** the
  Challenge merges the whole persistence stack into one package.
- **Collections (L6):** dict grouping and sets reappear unannounced in
  the Challenge's summarize step and in exercises.
- **Spec-literalness:** every exercise pins exact `Driver:` and
  `Output:` blocks. Byte-exact, always.

---

## Quick Recall

Answer from memory before starting Practice:

1. What is a module, and what name do you use to import it?
2. What makes a folder a package? What does `import` run when the
   package is imported?
3. What does `import` do the first time it loads a module, and why is
   top-level `print()` there a bug?
4. What is the difference between a relative import (`from . import x`)
   and an absolute import? Where does each one work?
5. After the first `import timer`, why does a second `import timer`
   print nothing?
6. Where does Python look when it searches for a module? What exception
   does it raise if nothing matches?

---

## Practice

Volume follows the CORE pipeline. Work top to bottom; difficulty climbs
after the Easy set. Full specs live in `exercises.ipynb`.

For every exercise you create the files yourself — `solution.py` holds
your working code, then you create the files listed in each **File
tree:**, then run the **Driver:** in the notebook. If a cell shows no
output when you run it, check that the file names and locations match
the File tree byte-for-byte.

| ID | Difficulty | Type | Focus |
|----|-----------|------|-------|
| E1 | Easy | [REAL-WORLD] | module = file · import `greet` from the same folder |
| E2 | Easy | [REAL-WORLD] | two files, one imports the other · functions across modules |
| E3 | Medium | [REAL-WORLD] | a package: `textstats/__init__.py` + submodule · dotted import |
| M1 | Medium | [REAL-WORLD] | relative import between siblings inside the package |
| H1 | Hard | [REAL-WORLD] | debug drill: 3 planted bugs in a `greeter` package |
| Challenge | Micro Build | [REAL-WORLD] | package restructure of a JSON→CSV report tool + `main.py` |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target.

Completion evidence for this topic (CORE → Level 4): independent
implementation, a working multi-module program, a package with
`__init__.py` imported by dotted name, a relative import that works
inside the package, the H1 bugs fixed with the DEBUGGING protocol, and
the Challenge package transferred into a new context.
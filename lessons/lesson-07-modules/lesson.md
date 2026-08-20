# Lesson 7 — Modules

## Learning Objective

By the end of this lesson you can organize code into **modules** (`.py` files),
import them three ways without tripping over namespaces, use the standard
library (`random`, `sys`, `os`) to make your programs nondeterministic,
argument-aware, and filesystem-aware, and know why `if __name__ == "__main__"`
is the load-bearing guard on every professional Python file.

---

## Motivation

Every exercise so far has been one file. Real programs are dozens of files —
and every AI pipeline is `import` statements at the top (pandas, numpy,
torch are all modules). Modules are how Python stops being a calculator and
becomes a system: you get someone else's tested code with one line, you keep
your own code organized, and your program can talk to the OS and the command
line.

---

## Mental Model

- **Module** — a `.py` file. `import math` finds `math.py` on `sys.path`,
  runs it once, and gives you a **namespace** you reach through the dot.
- **Namespace** — the module's own name box. `math.sqrt` means "the `sqrt`
  name inside the `math` box". `from math import sqrt` copies just that name
  into *your* box.
- **`sys.path`** — the address book Python searches when you `import`. It
  holds: the script's folder, `PYTHONPATH`, and `site-packages`. Your local
  file must be reachable from one of those.
- **`__name__`** — every module knows how it was run: `"__main__"` when run
  directly, its own name when imported. The guard exploits that difference.
- **`random`** — a module with a hidden state machine; `seed()` resets it so
  runs become reproducible.
- **`sys`** — your program's conversation with the interpreter (`argv`,
  `version`, `path`).
- **`os`** — your program's conversation with the operating system (files,
  folders, paths).

---

## Visualization

### What `import` actually does

```
import math
  ┌──────────────────────┐
  │  1. find math.py     │  sys.path search
  │  2. run it ONCE      │  cached in sys.modules
  │  3. bind name math   │  → math.sqrt, math.pi
  └──────────────────────┘

from math import sqrt
  ┌──────────────────────┐
  │  run math once       │
  │  copy ONLY sqrt      │  → sqrt (bare)
  │  into your box       │
  └──────────────────────┘

import math as m
  ┌──────────────────────┐
  │  bind under alias m  │  → m.sqrt, m.pi
  └──────────────────────┘
```

### The `__name__` switch

```
run directly:    __name__ == "__main__"   → guard code RUNS
imported:        __name__ == "mymod"      → guard code SILENT
```

---

## Theory

### Three import forms

```python
import math                      # module namespace: math.sqrt
from math import sqrt            # bare name: sqrt
import math as m                 # alias: m.sqrt
```

`import` runs the module file **once**; every later import reuses the cached
result (`sys.modules`). You don't reload on every line.

### `if __name__ == "__main__"`

```python
def main():
    print("only when run directly")

if __name__ == "__main__":
    main()
```

Run directly → `__name__` is `"__main__"` → `main()` runs. Imported → runs the
definitions, skips `main()`. This lets a file be both a library and a script.

### `random` — deterministic-looking randomness

```python
import random
random.seed(42)          # fix the sequence — same seed, same "random"
random.randint(1, 6)     # int in [1, 6]
random.choice(seq)       # one element of seq
random.sample(seq, k)    # k distinct elements, no repeats
random.shuffle(seq)      # reorder seq in place
random.choices(seq, k=n) # n picks, repeats allowed
```

Without `seed()`, every run differs. With it, results are reproducible — the
whole point of seeded AI experiments.

### `sys` — interpreter facts

```python
import sys
sys.argv          # ["program.py", "arg1", "arg2"] — command-line arguments
sys.version_info  # (3, 12, 4, ...) version parts
sys.path          # the module search path (a list)
sys.exit()        # end the program (0 = ok, nonzero = error)
```

`sys.argv[0]` is the script name; the real arguments start at `[1]`.

### `os` — filesystem facts

```python
import os
os.getcwd()                    # current directory as a string
os.path.join("data", "raw")    # platform-safe path joining (Windows vs \nix)
os.path.basename(p)            # last component of a path
os.path.exists(p)              # does this path exist?
```

Use `os.path.join` instead of string concatenation with `/` — it inserts the
right separator for the current OS.

### Comprehension recycling

Sets, dicts, and lists all have comprehensions (Lesson 6) — modules just give
you new data to feed them, e.g. `{word for word in line.split()}`.

---

## Best Practice

- **Import at the top of the file**, in the order: standard library, third
  party, your own modules — one blank line between groups.
- **Prefer `import module` (or `as` alias) over `from module import *`.**
  Star imports dump unknown names into your namespace and silently shadow
  your variables.
- **Use `from module import name` only when you use that name constantly**
  and the module name adds noise (`from math import sqrt`).
- **Always guard your `main()` with `if __name__ == "__main__":`** so the
  file is both importable and runnable.
- **Seed `random` before any nondeterministic logic that must be
  reproducible** — tests and experiments both require it.
- **Build paths with `os.path.join`**, never by gluing strings with `/`.
- **Keep modules small and single-purpose** — one job per file, named for
  that job (`read_students.py`, not `stuff.py`).

---

## Common Mistakes

1. **Star imports** (`from random import *`) — unknown names enter your
   namespace; a variable you define can silently override a library function.
2. **`from`-import then using the module name** — `from math import sqrt`
   does NOT create `math`; calling `math.pi` later raises `NameError`.
3. **Missing `__main__` guard** — importing the module runs `main()`
   (prints, prompts, crashes) at import time instead of being a library.
4. **No `seed()`** when you need reproducible "random" output — every run
   differs and tests can't assert anything.
5. **`sys.argv` indexing off by one** — `argv[0]` is the script name; args
   start at `[1]`. Forgetting this makes the first real argument vanish.
6. **Path glue with `/` or `\`** — breaks on the other OS; `os.path.join`
   handles the separator.
7. **Importing inside functions/loops** — works but runs (and re-runs) on
   every call; imports belong at the top.
8. **Module not found** — your file isn't on `sys.path`; run from its folder
   or add the folder.

---

## Applied AI Perspective

- **Every AI stack is modules.** `import numpy as np`, `import pandas as pd`,
  `import torch` — you already know the syntax that loads an entire framework.
- **Seed everything.** `random.seed(0)` before data shuffling or weight init
  is what makes an experiment rerunnable; `numpy.random.seed` and torch seeds
  extend the same idea.
- **`sys.argv` is how CLIs work** — every model-training entrypoint parses
  arguments (epochs, batch size, data path) the same way you'll parse them
  next.
- **`os.path.join` and `os.path.exists`** are the scaffolding of dataset
  loading: locating `train.csv`, checking the model dir exists, building
  artifact paths across machines.
- **One module per concern** mirrors production ML repos: `data.py`
  (loading), `model.py` (architecture), `train.py` (entrypoint) — import the
  pieces, never paste them.

---

## Mini Summary

- A module is a `.py` file; `import` finds it on `sys.path`, runs it once
  (cached in `sys.modules`), and hands you a namespace via the dot.
- `import m` / `from m import x` / `import m as a` — namespace, single name,
  alias. Avoid `from m import *`.
- `if __name__ == "__main__": main()` makes a file both a script and a
  library; without it, importing triggers side effects.
- `random.seed(n)` fixes the pseudo-random sequence; `choice`, `sample`,
  `shuffle`, `choices` cover pick/distinct/order/pick-with-replacement.
- `sys.argv` is the command line (`[0]` = script, args from `[1]`);
  `sys.version_info`, `sys.path` read the interpreter.
- `os.getcwd`, `os.path.join`, `os.path.basename`, `os.path.exists` bridge to
  the filesystem portably.
- Import at top, guard your `main`, seed for reproducibility, build paths
  with `os.path.join`.

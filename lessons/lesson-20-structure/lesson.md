# Lesson 20 — Project Structure (Tier: CORE)

Stage 3, fourth topic. Lessons 17–19 gave you tested, networked code that
lives in flat lesson folders. This lesson asks the next question: **where
does everything live when the project grows up?**

---

## Objective

After this lesson you will be able to:

- Predict `sys.path[0]` for every launch form — and explain *why* it differs.
- Choose absolute vs relative imports from the launch context, not habit.
- Convert a flat script pile into a package with a `-m` entry point.
- Write the supporting files correctly: minimal `requirements.txt`, honest
  `.gitignore`, runnable README.
- Diagnose structural bugs (path hacks, import-time side effects,
  cwd-fragile data access) by traceback, not guessing.

---

## Why This Matters

Flat works until it doesn't — roughly at five files. Then the symptoms
start: `ModuleNotFoundError` that vanishes when you `cd` elsewhere, a
`sys.path.insert` hack copied into every entry point, tests that pass only
from one folder, a `requirements.txt` with 278 packages (your WP2 scar), a
99 MB `.venv` committed inside a lesson folder (your L19 scar).

Every codebase you will join already made these decisions. This lesson
teaches you to read a layout, judge it, and fix it — the exact skill WP3
(the half-stage integration) will demand next.

---

## Mental Model

A Python project has no fixed shape. What it has is a **launch context**:
three facts that decide what every import means.

```text
cwd          = where you stand when you press enter
sys.path[0]  = where Python looks FIRST (set by HOW you launched)
entry point  = the file that runs first (script? -m? pytest?)
```

Same files, different launch, different program:

```text
python shop/main.py     → path[0] = shop/      (the file's own folder)
python -m shop.main     → path[0] = cwd        (where you stand)
pytest                  → path[0] = rootdir-ish (where config/conftest anchors it)
```

**If an import works under one launch and breaks under another, the bug is
in the launch context or the import style — never "Python being weird".**

---

## Core Concept

### 1. Layouts — flat vs `src/`, and when flat is negligent

```text
flat (lessons, scripts):      scaled (projects):
main.py                       src/shop/__init__.py
clients.py                        shop/carts.py
tests/test_x.py                   shop/main.py
                              tests/test_shop.py
                              requirements.txt / README.md
```

Flat is fine when one folder holds one concern and every launch starts
there (every lesson so far). It turns negligent when: a second entry
point appears, tests must run from anywhere, or someone else must run
your code. `src/` adds one more virtue: your package can never be
imported *by accident* from a stray cwd — imports must be deliberate.

### 2. The three launches — what lands on `sys.path`

| Launch (from the project root) | `sys.path[0]` | Meaning |
|---|---|---|
| `python shop/main.py` | `.../shop` | the script's own folder; the project root is NOT there |
| `python -m shop.main` | `...` (your cwd) | you anchor the root explicitly |
| `pytest tests/` | rootdir insertion | conftest collection anchors it (L17: fixtures live there for a reason) |

Consequence you will use all lesson: a file *inside* a package can be run
as a script (`python shop/main.py`) **only** if its imports resolve from
its own folder downwards. The moment it says `from shop.x import ...`,
script-launch dies with `ModuleNotFoundError` — and `-m` is the fix, not
a `sys.path` hack.

### 3. Absolute in entries, relative only inside

```python
# shop/main.py (an entry — absolute, anchored at the project root)
from shop.report import summary

# shop/report.py (inside the package — EITHER works, absolute preferred)
from shop.carts import line_total      # clear under every launch
from .carts import line_total          # legal ONLY when imported, never script-run
```

A leading dot means "my package" — and a file run as a script *has* no
package (`__package__` is `None`), hence the classic
`ImportError: attempted relative import with no known parent package`.
That error is never fixed with `sys.path.insert`. It is fixed by
choosing the launch (`-m`) or the import style (absolute) to match.

### 4. Entry points — a ladder, not a jump

1. `if __name__ == "__main__":` guard (Stage 1 — script *or* import).
2. `python -m pkg.main` (this lesson — root-anchored, the project norm).
3. Console scripts (`pip install` the project, get a command — concept
   only; publishing is project-dependent, not this lesson).

Each rung removes one assumption about cwd. Climb when the assumption
breaks, not before.

### 5. Supporting files — small, honest, hand-written

`requirements.txt` lists what **you directly import** — nothing else:

```text
requests
pytest
```

Not `pip freeze` from a laptop (your WP2 file: 278 lines, tensorflow to
torch, plus a BOM). Freeze *reproduces* an environment; requirements
*declares* one. Different jobs.

`.gitignore` excludes what is **generated or private**:

```text
.venv/
__pycache__/
.pytest_cache/
*.csv
```

Envs, caches, and data files never belong in version control (your L19
`.venv` and every `__pycache__` we delete at review time).

`README.md` answers three questions and nothing else: what is this, how
do I run it (exact commands), how do I test it.

### 6. Tests live in `tests/`, fixtures in `conftest.py`

```text
tests/
  conftest.py        (shared fixtures — L17 pattern)
  test_shop.py       (test_count / test_total / test_empty)
```

No `sys.path` hacks in tests — if `pytest tests/` cannot import your
package, the *layout* is wrong, and the test just told you. That is the
test doing its second job: pinning the structure, not just the logic.

### 7. Data files are located, never assumed

```python
# cwd-fragile (works only where you happen to stand):
open("messy_app/prices.csv")

# located (works under every launch):
Path(__file__).with_name("prices.csv")
```

A module knows where *it* lives (`__file__`); it knows nothing about
where *you* stand. Anchor data to the module, never to the cwd.

**Deliberately NOT taught:** publishing to PyPI, build backends,
`pyproject.toml` packaging tables, Docker images. You now know they
exist and which problem each solves — that is the correct depth until a
real project needs them.

---

## Practical Examples

Read these — the exercises reuse the same moves.

**1. Proving `sys.path[0]` (the E1 instrument):**

```python
# launchlab/src/shop/main.py
import sys
print(sys.path[0])
```

```text
$ python launchlab/src/shop/main.py     → .../launchlab/src/shop
$ cd launchlab/src && python -m shop.main   → .../launchlab/src
```

Same file, different first-lookup-folder. Predictions before runs, always.

**2. Flat → package (the M1 move):**

```python
# BEFORE (flat_shop/run.py — works only from flat_shop/):
from report import summary

# AFTER (shop/main.py — works from the project root):
from shop.report import summary

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

**3. Minimal requirements (the E3 triage):**

```text
# GLOBAL_FROZEN.txt: 8 lines (requests, pytest, tensorflow, torch, ...)
# requirements.txt: 2 lines — what YOU import, nothing else
requests
pytest
```

---

## Engineering Notes

- **Use `-m` as the default entry form** for anything inside a
  package. Script-launch is for leaves (one-offs, instruments), not branches.
- **`__init__.py` stays empty** (or docstring-only) unless you are
  deliberately designing a public API (L13 re-export lesson, reused
  knowingly or not at all). Import-time side effects — prints, network,
  computation — are a bug, full stop.
- **No `sys.path` manipulation in project code.** If you type
  `sys.path.insert`, stop: the launch or the layout is wrong. Fix that.
- **Positional argv, still no `--flags`** (Tool Sync unchanged): entries
  take `argv[1]` with a usage line on stderr + exit 1.
- **Provided in this lesson** (read-only references): `launchlab/`,
  `importlab/`, `vend/`, `flat_shop/`, `messy_app/` (buggy), plus
  `report_tool_flat/` and `ledger_flat/` as restructure patients.

---

## Common Pitfalls

1. **`sys.path.insert` "fix".** Masks a launch/layout mismatch; rots into
   every entry. The traceback goes away, the disease stays.
2. **Noisy `__init__.py`.** A print (or worse) at import time fires on
   every import, every test, every `-m` run.
3. **Leading-dot import in a script-run file.** `ImportError: no known
   parent package` — fix the launch or the import, never the path.
4. **Cwd-anchored data paths.** `open("pkg/data.csv")` passes from the
   project root and nowhere else. Anchor with `Path(__file__)`.
5. **Global-freeze `requirements.txt`.** Declares your laptop, not your
   project. Hand-write what you import.
6. **Committed envs/caches.** If `.gitignore` doesn't exclude it, review
   will make you remove it.

---

## Connection to Previous Knowledge

- **Lesson 13 — Modules/packages**: `__init__` runs at import, dots need
  a parent, `sys.modules` caches — now applied to whole trees.
- **Lesson 17 — pytest**: `conftest.py` placement + `tmp_path` are
  structural decisions; suites pin layouts (M3/H-suites do exactly this).
- **Lesson 9/12 — Files/CSV**: `newline=""`, `encoding="utf-8"`,
  DictWriter — reused in every restructure patient.
- **Lessons 18/19 — Merge semantics**: `report_tool` totals and `ledger`
  network-wins reappear as the *behavior* that must survive restructuring
  (structure changes, contracts don't).
- **WP2 scars**: global freeze + committed scratch → E3 + `.gitignore`
  drills. Your history is the curriculum.

---

## Quick Recall

Answer out loud, before looking back:

1. Same file `shop/main.py`: `python shop/main.py` vs `python -m
   shop.main` from the root. What is `sys.path[0]` in each — and which
   import style (`import shop.x` vs `from .x import`) survives each?
2. A submodule says `from .data import get`. It runs under `-m` but dies
   as `python pkg/sub.py`. Which error, and what are the two honest fixes?
3. `import pkg` prints a banner. Which file holds the bug, and what is
   the file's correct content?
4. `open("pkg/data.csv")` passes from the root, fails from `/tmp`. What
   is the one-line anchor that works everywhere?
5. Your `requirements.txt` has 40 lines but you import 3 packages. What
   produced it, and what should the file contain instead?
6. `if not isinstance(path, str) or not path:` — which two inputs raise
   in `load_basket`, and which input would slip through if the `or` were
   an `and`?

---

## Practice

Provided (read-only unless the spec says fix it): `launchlab/`,
`importlab/`, `vend/GLOBAL_FROZEN.txt`, `flat_shop/`, `messy_app/`
(buggy — YOU fix it), `test_messy.py` + `test_restructure.py` (do NOT
modify), `report_tool_flat/`, `ledger_flat/`, `solution.py` (blank).
You create every other file, flat in the lesson folder unless the spec
says otherwise.

| ID | Tier | Type | What you build |
|----|------|------|----------------|
| E1 | Easy | [REAL-WORLD] | `paths.py` — predict `sys.path[0]` tails for two launches |
| E2 | Easy | [REAL-WORLD] | `imports.py` — predict the 6-cell import/launch truth table |
| E3 | Easy | [REAL-WORLD] | `vend/requirements.txt` + `vend/.gitignore` — triage a global freeze |
| M1 | Medium | [REAL-WORLD] | `shop/` package from `flat_shop/` — absolute imports, `-m` entry |
| M2 | Medium | [REAL-WORLD] | `shop/main.py` argv + `load_basket` guard — foreign-cwd proof |
| M3 | Medium | [REAL-WORLD] | `tests/` + `conftest.py` — exactly 3 pinned tests, all green |
| H1 | **Hard** | [DEBUG] | `messy_app/` (provided, 4 planted bugs) — find + fix each |
| H2 | **Hard** | [REAL-WORLD] | `report_tool/` + README — restructure the flat patient |
| Challenge | — | [REAL-WORLD] | `ledger/` project — package + `ledger/tests/` + supporting files |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target to farm.

Rules of the pack:

- Learner files stay where the spec puts them — `shop/`, `tests/`,
  `report_tool/`, `ledger/` are real subdirectories this lesson.
- A file you create must pass every check the notebook drive cell runs.
- H1: the bug report table is a blank write-in — fill the slots
  (Expected / Observed / Root cause / Fix) as you work, never after.
- Challenge: one positional form (`sync <dir>`); anything else exits 1
  with usage on stderr. No `--flags` in this lesson.

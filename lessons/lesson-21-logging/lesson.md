# Lesson 21 — Logging (Tier: CORE)

Stage 3, fifth topic. Lessons 17–20 gave you tested, networked,
well-housed code — still narrated by `print()`. This lesson replaces
diagnostic printing with the stdlib's answer: **leveled, routed,
formatted logging.**

---

## Objective

After this lesson you will be able to:

- Choose a severity (`DEBUG` → `CRITICAL`) per call site, numerically.
- Configure once (`basicConfig`, incl. `force=True`) and route to
  stream + file with different levels.
- Format records exactly (`%(levelname)s %(name)s %(message)s`).
- Log tracebacks with `exc_info` instead of printing errors.
- Keep data on stdout and diagnosis on stderr — always separated.
- Test logging with `caplog` and handler probes.

---

## Why This Matters

Your WP2 scoped prefixes (`bad request:` on stderr) and every L20 usage
line were hand-rolled logging. They work — and they don't compose: no
levels, no routing, no silence switch. The moment someone runs your CLI
inside a pipeline, a stray diagnostic `print()` on stdout corrupts the
data for the next program.

Real services don't print. They log at a level, route by deployment, and
stay silent until asked. This lesson is the last skill WP3 needs.

---

## Mental Model

Three roles, one flow:

```text
log.debug("loaded %s", name)     →  a RECORD with a severity (the call site decides HOW BAD)
    ↓
Logger "shop" (level DEBUG)      →  the first gate: below my level? dropped. (the logger decides IF)
    ↓
Handler ×2                       →  the second gate + destination:
  StreamHandler(stderr, WARNING)    only WARNING and worse, to the terminal
  FileHandler(shop.log, DEBUG)      everything, to the file
    ↓
Formatter                        →  the text shape: "WARNING shop bad row 'x'"
```

Two rules that prevent 90% of logging bugs:

1. **Two gates in series.** Logger level AND handler level must both pass.
   Setting one to DEBUG while the other sits at WARNING still silences.
2. **Print is data, log is diagnosis.** If a human needs it to debug, it
   goes to the log. If a program needs it to compute, it goes to stdout.

---

## Core Concept

### 1. Levels are numbers — order them numerically

```python
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50
```

A record is visible when `record.level >= gate.level`, applied at BOTH
gates. `visible("ERROR", "INFO")` is `40 >= 20` → True. There is no
vibes-based severity — it is arithmetic.

### 2. `basicConfig` — one call, and it only works once

```python
import logging

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s %(name)s %(message)s",
)
```

This configures the **root** logger's stream handler. Call it twice and
the second call is silently ignored — the classic "why did my format not
change" trap. Reconfiguration needs `force=True` (Python 3.8+), which
tears down existing handlers first:

```python
def setup_logging(verbose=False):
    logging.basicConfig(
        force=True,
        level=logging.DEBUG if verbose else logging.WARNING,
        format="%(levelname)s %(name)s %(message)s",
    )
```

### 3. Handlers — one logger, many destinations

```python
handler = logging.FileHandler("shop.log", mode="w", encoding="utf-8")
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
logging.getLogger().addHandler(handler)
```

Stream (stderr, terse, WARNING+) for the operator; file (verbose, DEBUG+)
for forensics. Same records, different gates, different fates.

### 4. Formatters — exact strings, always

```python
"%(levelname)s %(name)s %(message)s"
# → "WARNING noisy_shop bad row 'mystery'"
```

`%(name)s` is the logger's dotted name (`getLogger(__name__)` gives you
the module path for free). Format strings are contracts — byte-exact,
like every output in this OS.

### 5. `exc_info` — the traceback belongs to the log

```python
try:
    float(row["price"])
except ValueError:
    log.warning("bad row %r", row.get("name"), exc_info=True)
```

The traceback is formatted *into the record* — no `print()`, no
traceback on stdout, no lost context. `exc_info=True` outside an `except`
block logs a lying `NoneType: None` — placement is the whole skill.

### 6. Laziness — don't pay for silenced logs

```python
log.debug(f"loaded {expensive()}")        # BUG: f-string runs BEFORE the level check
log.debug("loaded %s", expensive())       # STILL EAGER: the argument evaluates first
if log.isEnabledFor(logging.DEBUG):       # the guard that actually defers the work
    log.debug("loaded %s", expensive())
```

`%-args` defer *formatting*, never *evaluation*. Only `isEnabledFor`
defers the call itself.

### 7. Hierarchy — children, parents, and the duplication trap

```python
logging.getLogger("shop")        # child — records propagate upward by default
logging.getLogger()              # root — handlers here see everything below
```

`getLogger("a.b").parent is getLogger("a")` — the tree is real, with one
sharp edge: **the link forms at creation time against existing loggers.**
Create the child first and its parent stays the root forever (a placeholder
holds the name, not the link) — so create parents before children, and
verify links with `is`, never with hope. The second trap: a handler on
the child AND a handler on the root emits every record twice. One handler
per record path — either handle at the leaf with `propagate = False`, or
handle once at the root.

**Deliberately NOT taught:** dictConfig/YAML configuration, rotation
handler internals, structured/JSON logging libraries. You know they exist
and which problem each solves — correct depth until a project needs them.

---

## Practical Examples

Read these — the exercises reuse the same moves.

**1. The standard setup (dual routing, one call site each):**

```python
import logging
from pathlib import Path

log = logging.getLogger("tracked")

logging.basicConfig(
    force=True, level=logging.INFO, format="%(levelname)s %(name)s %(message)s"
)
logging.getLogger("tracked").setLevel(logging.DEBUG)
handler = logging.FileHandler(Path(__file__).with_name("tracked.log"),
                              mode="w", encoding="utf-8")
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter("%(levelname)s %(name)s %(message)s"))
logging.getLogger().addHandler(handler)

log.info("loaded %d rows", 4)     # stderr: yes · file: yes
log.debug("team red 180.50")      # stderr: no (INFO gate) · file: yes
```

**2. The loader that never crashes, never prints:**

```python
def load_logged(path):
    if not Path(path).exists():
        log.warning("missing file: %s", path)
        return []
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        log.error("bad json: %s", path, exc_info=True)
        return []
    log.info("loaded %d items", len(data.get("items", [])))
    return data.get("items", [])
```

**3. Testing logs with caplog (pytest's seam):**

```python
def test_warns_on_corrupt(tmp_path, caplog):
    with caplog.at_level(logging.DEBUG, logger="safe_load"):
        assert load_logged(str(tmp_path / "bad.json")) == []
    assert any(r.levelno == logging.ERROR and r.exc_info
               for r in caplog.records)
```

---

## Engineering Notes

- **Never log secrets.** Passwords, tokens, full payloads with PII stay
  out of every handler — files get read by more people than terminals.
- **`%-args` always, f-strings never** in log calls (formatting is
  deferred); `isEnabledFor` when the argument itself is expensive.
- **Module loggers via `getLogger(__name__)`**, configured once at the
  entry. Libraries configure nothing — applications configure once.
- **`mode="w"` on run-scoped log files** unless you explicitly want
  history; appended reruns are how "the log said WHAT?" mysteries start.
- **Provided in this lesson** (deterministic, offline): `noisy_shop/`
  (5-bug patient), `plain_run/`, `sample.log`, `broken.json`/`good.json`,
  suites `test_logging.py` + `test_tracked.py` (do NOT modify).

---

## Common Pitfalls

1. **Second `basicConfig` silently ignored.** Reconfig needs `force=True`.
2. **Two handlers, one record path.** Child + root handlers duplicate
   every line — count your stderr lines.
3. **Eager f-strings / eager args.** The call evaluates before the gate;
   `isEnabledFor` is the only real deferral.
4. **Misplaced `exc_info`.** On the success branch it logs a lying
   `NoneType: None`; missing on the except branch it drops the traceback.
5. **Cwd-relative log paths.** `FileHandler("x.log")` lands wherever you
   stand — anchor with `Path(__file__)`, same as data files (L20).
6. **Root-level gate starving named loggers.** `basicConfig(level=INFO)`
   + named logger at NOTSET ⇒ DEBUG dies at the logger gate. Set both
   gates deliberately.

---

## Connection to Previous Knowledge

- **Lesson 8 — Exceptions**: `exc_info` is `raise`-site context
  preserved; handlers are ordered specific-before-general, same as
  `except` clauses.
- **Lesson 20 — Streams**: stdout=data, stderr=diagnosis — logging is
  that rule with levels and routing; `Path(__file__)` anchoring reused
  for log files.
- **Lesson 17 — pytest**: `caplog` + `tmp_path` are the test seams;
  M3 writes real `caplog` tests (no vacuous assertions — L17's scar).
- **Lessons 9/11/12 — Persistence**: loaders return data-shaped
  defaults, never error strings; CSV/JSON discipline unchanged.
- **WP2**: scoped stderr prefixes were proto-logging; this lesson is
  their graduation.

---

## Quick Recall

Answer out loud, before looking back:

1. `record.level = ERROR`, logger gate INFO, handler gate DEBUG. Visible?
   Now swap: logger gate DEBUG, handler gate ERROR. Which gate decides —
   and why must you set both deliberately?
2. `basicConfig` called in two modules. Which call wins, and which
   keyword re-arms reconfiguration?
3. `log.debug(f"loaded {expensive()}")` with DEBUG disabled. How many
   times does `expensive()` run — and what single guard makes it zero?
4. A WARNING appears twice on stderr, zero times in the file. Sketch the
   handler layout that produces exactly this.
5. `except ValueError: log.warning("bad row")` — what forensic evidence
   is missing, and which keyword restores it?
6. `if not isinstance(row, dict) or "id" not in row:` — which two inputs
   skip, which input crashes under `and`, and why does the current form
   never crash?

---

## Practice

Provided (read-only unless the spec says fix it): `noisy_shop/`
(buggy — YOU fix it), `plain_run/`, `sample.log`, `broken.json` /
`good.json`, `test_logging.py` + `test_tracked.py` (do NOT modify),
`solution.py` (blank). Installs: none — stdlib only.
You create every other file, flat in the lesson folder unless the spec
says otherwise.

| ID | Tier | Type | What you build |
|----|------|------|----------------|
| E1 | Easy | [REAL-WORLD] | `filters.py` — level ordering, numerically |
| E2 | Easy | [REAL-WORLD] | `counter.py` — count log levels in `sample.log` |
| E3 | Easy | [REAL-WORLD] | `names.py` — logger parent-chain predicates |
| M1 | Medium | [REAL-WORLD] | `dual.py` — one logger, stream + file, two gates |
| M2 | Medium | [REAL-WORLD] | `safe_load.py` — logged loader, data-shaped defaults |
| M3 | Medium | [REAL-WORLD] | `tests/` — exactly 3 `caplog` tests, all green |
| H1 | **Hard** | [DEBUG] | `noisy_shop/` (provided, 5 planted bugs) — find + fix each |
| H2 | **Hard** | [REAL-WORLD] | `tracked/` + README — print-to-log migration |
| Challenge | — | [REAL-WORLD] | `journal/` project — run journal with verbosity modes |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target to farm.

Rules of the pack:

- Learner files stay where the spec puts them — `tests/`, `tracked/`,
  `journal/` are real subdirectories this lesson.
- A file you create must pass every check the notebook drive cell runs.
- H1: the bug report table is a blank write-in — fill the slots
  (Expected / Observed / Root cause / Fix) as you work, never after.
  One hint total lives in the H1 spec (your standing request).
- Challenge: positional forms only (`sync <dir> [quiet|verbose]`);
  anything else exits 1 with usage on stderr. No `--flags` in this lesson.

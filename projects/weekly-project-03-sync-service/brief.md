# Weekly Project 3 — Feed Sync & Report Service

## Type

[REAL-WORLD]

## Problem

A small shop tracks inventory in a supplier feed, but the network is not
to be trusted and the trouble tickets need forensics. They want one CLI
that syncs the feed into a local cache (offline-only rows survive),
reports stock value and low-stock rows from the files it just wrote, and
journals every run at a verbosity the operator chooses. Reliability rule
from WP2 still holds — and grows: bad argv, corrupt cache, and dead
network must each produce a scoped message on **stderr** with **exit 1**,
never a traceback; stdout carries only data.

This project integrates Stage 3 so far: the `requests` client + typed
errors (L18/L19), the `pytest` suite with fixtures (L17), package
structure with a `-m`-runnable layout (L20), and leveled logging with
verbosity modes (L21). This is the **half-stage integration evidence**.

## Requirements

### The stub API (PROVIDED infrastructure — read it, do NOT modify it)

- `stub_api.py` in this folder: the same deterministic JSON server as the
  lessons (`GET /items`, `GET /items/{id}`, `GET /search`, `POST /echo`,
  `POST /count`, `GET /slow`), serving 4 items (id, name, price, stock).
- Your code starts its own `stub_api.StubAPI()` (same shape as
  `local_api.LocalAPI`) for every network call — no internet, fully
  offline and deterministic.
- `SYNC_API_BASE` env var, when set, overrides the base URL (used by the
  network-error test; documented 12-factor-lite configuration).

### Data model

- Item: `{"id": int, "name": str, "price": float, "stock": int}`.
- `sync.json` — `{"items": [...]}` merged cache, sorted by id.
- `sync.csv` — header `id,name,price,stock`, same rows, same order.

### Commands (exactly three — the main goal)

All run as `python main.py ...` from the project folder (same form as
WP2; a `-m` package entry is acceptable instead if used consistently and
the matrix commands are adapted + documented in the log).

1. **sync** — `python main.py sync [quiet|verbose]` (default `normal`):
   - Starts its own stub, fetches `/items` (`timeout=`,
     `raise_for_status()`, typed wrap).
   - Reads `sync.json` from the current directory if present (the cached
     set); merges with **network-wins** semantics (every network id wins;
     cached-only items kept; sorted by id).
   - Writes `sync.json` + `sync.csv`; prints exactly
     `Sync: N items (fresh F, cached K)` (`fresh = len(network)`).
   - Logging: `normal` → INFO+ on stderr; `quiet` → stderr silent
     (CRITICAL); `verbose` → DEBUG+ on stderr; `service.log` beside
     `main.py` (`mode="w"`, always DEBUG).
2. **report value** — reads `sync.csv` back (never the in-memory copy)
   and prints one line per item plus the total (exact format below).
3. **report low N** — reads `sync.csv` back; prints items with
   `stock < N` plus a `Low:` count line (exact format below). `N` must be
   a non-negative integer.

## Development environment (do this yourself, L20 discipline)

- `python -m venv .venv`, activate it, use it for everything.
- `python -m pip install requests pytest mypy` — ask before anything else.
- Hand-write `requirements.txt` (what YOU directly import — `requests`,
  `pytest`, `mypy` — never a global freeze).
- `.gitignore` covers `.venv/`, `__pycache__/`, `.pytest_cache/`,
  `*.log`, and your local data files (`sync.json`, `sync.csv`,
  `service.log`); `requirements.txt` IS tracked.
- `.venv\Scripts\python -m mypy main.py` clean; everything annotated.

## Constraints

- Use only Stage 3 knowledge so far (plus AWARENESS-level lookups).
  `argparse`/`--flags` stay out — positional argv only.
- Layered shape expected where it genuinely helps (a `service/` or
  equivalent split: fetch/merge/persist/log — like L13–L16 and WP2);
  not mandatory if a single well-structured `main.py` reads better.
  Decision logged either way.
- No error-string returns — typed errors with `status`-or-`None`
  discipline from L18/L19; loaders return shapes (`[]`) on missing file.
- Prints come from the data just written (read the CSV back), never from
  in-memory values — one source of truth (WP2 rule, still law).
- Log records carry levels; no `print()` diagnostics; no secrets in logs.
- Git commit at meaningful milestones; `git log` shows more than one
  commit.
- NO step-by-step plan provided. Design decisions are yours; the AI
  clarifies requirements and reviews code — it never implements.

## Spec output blocks (frozen — byte-exact)

**Seed cache fixture** — this exact file must exist for the acceptance
runs (name it `sync.json` in the project folder):

```json
{"items": [{"id": 3, "name": "muffin", "price": 0.99, "stock": 99}, {"id": 5, "name": "donut", "price": 1.0, "stock": 3}]}
```

(The stale muffin proves network-wins; the donut proves cached-only
survival.)

`python main.py sync` with the seed fixture installed:

```text
Sync: 5 items (fresh 4, cached 1)
```

`python main.py report value` (after the seeded sync — one line per item,
format rule `f"{name}: {stock} x {price:.2f} = {stock * price:.2f}"`,
id order, then the total):

```text
coffee: 40 x 2.50 = 100.00
tea: 25 x 1.80 = 45.00
muffin: 0 x 3.20 = 0.00
latte: 12 x 4.10 = 49.20
donut: 3 x 1.00 = 3.00
Total: 197.20
```

…and `sync.csv` must contain exactly:

```text
id,name,price,stock
1,coffee,2.5,40
2,tea,1.8,25
3,muffin,3.2,0
4,latte,4.1,12
5,donut,1.0,3
```

`python main.py report low 10` (after the seeded sync):

```text
muffin: 0 left
donut: 3 left
Low: 2 items
```

## Test matrix (self-validate before asking for review)

Run against the seed fixture unless stated otherwise. Happy path =
stdout block byte-exact, exit 0. Error case = scoped message on
**stderr**, **exit 1**, no traceback, no files written.

Error contract: `bad request:` for bad argv, `network error:` for
`requests` failures (with the detail on the next line),
`corrupt data:` for unreadable/shape-invalid cache. Detail lines state
the problem plainly.

| # | Command / setup | Expect |
|---|-----------------|--------|
| T1 | `sync` (seed installed) | `Sync: 5 items (fresh 4, cached 1)`; `sync.json`/`sync.csv` byte-exact |
| T2 | `sync` (no cache file) | `Sync: 4 items (fresh 4, cached 0)` |
| T3 | `report value` (after T1) | The 5-line + `Total: 197.20` block above, byte-exact |
| T4 | `report low 10` (after T1) | The 2-line + `Low: 2 items` block above, byte-exact |
| T5 | `report low abc` | stderr, exit 1: `bad request:` + non-negative-integer detail |
| T6 | `report low -5` | stderr, exit 1: `bad request:` + non-negative-integer detail |
| T7 | `report value` (no cache files at all) | stderr, exit 1: `corrupt data:`-family message (missing input, no crash) |
| T8 | (no arguments) | stderr, exit 1: usage line |
| T9 | `bananas` (unknown command) | stderr, exit 1: `bad request:` + unknown-command detail |
| T10 | Overwrite `sync.json` with `{bad json`, then `report value` | stderr, exit 1: `corrupt data:` + parser detail, no traceback |
| T11 | `SYNC_API_BASE=http://127.0.0.1:1 python main.py sync` | stderr, exit 1: `network error:` + detail, no traceback |
| T12 | `sync quiet` (seed installed) | stdout pin exactly; stderr EMPTY |
| T13 | `sync verbose` (seed installed) | stdout pin exactly; stderr contains `DEBUG` |
| T14 | `python -m pytest tests -q` | your suite, all green (≥5 tests incl. ≥1 `caplog` test and ≥1 `tmp_path` test) |
| T15 | `python -m mypy main.py` | clean |
| T16 | `git status` after setup | `.venv`, `*.log`, `sync.json`, `sync.csv` NOT tracked; `requirements.txt` IS tracked |
| T17 | Delete cache, run `sync`, run `report value` in a separate command line | data survives restarts; report reads the files |

Contract rule (WP2 rule, still law): the wording above IS the spec. If
you deliberately change a message, update this matrix in the same commit.

## Acceptance Criteria

- [ ] All of T1–T17 pass exactly as specified (run in a temp copy for
      the file-mutating rows).
- [ ] Reports are byte-exact outputs computed from files just read back.
- [ ] `requests` + typed errors + timeouts end-to-end (no `urllib`
      fallback, no bare `except`).
- [ ] Logging: three verbosity modes behave; `service.log` carries DEBUG;
      no diagnostic prints.
- [ ] `mypy main.py` clean; everything annotated.
- [ ] `git log` shows more than one commit.
- [ ] Decisions Log below is filled during the build (Why + Alternative
      columns), and a technical reflection is written.

## Stretch goals (optional, detailed)

Do the main goal first. Each stretch is independent and optional.

- **SG1 — `report summary`:** one block from the files just read:
  ```text
  Summary (5 items):
  total value: 197.20
  low stock: 2
  ```
  (`low stock` counts `stock < 10`, consistent with `report low`.)
  Validation: seeded sync → byte-exact.
- **SG2 — `report restock N`:** for each item, `need = max(0, N -
  stock)`; print `f"{name}: need {need}"` when positive else
  `f"{name}: ok ({stock})"`, id order. `report restock 20` on the seed:
  ```text
  coffee: ok (40)
  tea: ok (25)
  muffin: need 20
  latte: need 8
  donut: need 17
  ```
- **SG3 — `report.json` export:** `report value` additionally writes
  `report.json` (`{"items": [...], "total": 197.20}`); acceptance: file
  parses, `total` field byte-exact on the seed.

## Deliverables

- Source code in this folder (`main.py` starts blank — learner writes
  everything). A layered split is expected where it genuinely helps;
  not mandatory if a single well-structured `main.py` reads better.
  Decision logged.
- `stub_api.py` stays EXACTLY as provided (verify with `git diff` —
  it must show no changes).
- `tests/` suite (conftest + fixtures encouraged), `requirements.txt`,
  `.gitignore`, short README (how to run, what the reports mean, the
  `SYNC_API_BASE` override).
- Technical reflection (template style) + the Decisions Log below.

## Decisions Log (filled by learner during build)

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
|          |     |                        |

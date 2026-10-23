# Weekly Project 4 — Ops Log Toolkit (merged Stage-3 Capstone)

## Type

[REAL-WORLD]

## Problem

The on-call team has service logs nobody can query: raw lines pile up
all day, and answering "what happened between 09:14:04 and 09:14:09?"
means eyeballing the file. They want one CLI that ingests the raw log
into a normalized store, answers time-window and slow-endpoint
questions from that store, and pulls the current incident snapshot from
the ops feed — offline and deterministic, with the same reliability
discipline WP3 drilled: bad argv, corrupt store, and dead network each
produce a scoped message on **stderr** with **exit 1**, never a
traceback; stdout carries only data.

This is the **Stage-3 capstone, merged with WP4** (Rule 12): it carries
WP3's laws forward (requests + typed errors (L18/L19), pytest (L17),
package discipline (L20), leveled logging (L21)) and integrates the
second half of the stage where they genuinely fit — generators as the
streaming pipeline (L24), context managers for safe file IO (L25),
regex as the parser (L26), datetime validation and windowing (L27).
Asyncio is AWARENESS: it is **not** required (SG3 only if you want it).
Decorators/iterators may appear if your design reaches for them — never
forced.

## Requirements

### The raw log

- `logs/app.log` (PROVIDED fixture — tracked, never modified).
- A line is **valid** iff the whole line, anchored at both ends, is:
  `YYYY-MM-DD` + space + `HH:MM:SS` + space + one of
  `INFO|WARN|ERROR` + space + `service=<word>` + space +
  `latency=<non-negative int>` + space + `status=<int>` + space +
  `path=<no spaces>` — in exactly that order, single spaces.
- Any non-blank line that fails the grammar is **skipped and counted**
  (loud skips, L27 discipline). Blank lines are ignored silently
  (neither valid nor skipped). Whether you additionally parse the
  timestamps as validation is your decision — logged either way.

### Data model

- `clean.json` — a JSON **list** of records, sorted chronologically
  (date, then time). Each record has exactly these keys, this order:
  `date` (str), `time` (str), `level` (str), `service` (str),
  `latency` (int), `status` (int), `path` (str).
- `state.json` — the incident snapshot fetched by `fetch` (byte-exact
  content pinned below).
- Writing rule: compact `json.dumps(..., separators=(",", ":"))`,
  **no trailing newline** — the pinned files below are byte-exact.

### Commands (run as `python main.py ...` from the project folder)

1. **`ingest [quiet|normal|verbose]`** (default `normal`) — parse
   `logs/app.log`, skip-and-count malformed lines, sort
   chronologically, write `clean.json`, print
   `Ingest: <V> valid, <S> skipped`. Missing `logs/app.log` is not an
   error: ingests nothing (see matrix).
2. **`window START END`** — read `clean.json` back, keep records whose
   time-of-day is between START and END **inclusive** (both bounds are
   strict `HH:MM:SS`), print one line per present service in
   alphabetical order (`<service>: <count>`), then
   `Window: <N> records`. No mode argument.
3. **`fetch [quiet|normal|verbose]`** (default `normal`) — GET
   `{base}/incident` with `requests` (`timeout=`,
   `raise_for_status()`), starting your own `stub_feed.StubAPI()` for
   the base URL unless `FEED_API_BASE` is set (env overrides — same
   law as WP3's `SYNC_API_BASE`). Validate the response is a dict with
   an `incident` key (else `corrupt data:` + detail, exit 1). Write
   `state.json`, print `Incident: <incident> (severity <severity>)`.
4. **`report slow N`** — read `clean.json` back; print the top `N`
   records by `latency` descending as `<latency> <service> <path>`,
   ties won by the earlier record, then `Slow: <k> records` (k = lines
   printed; `N` larger than the store prints the whole store). `N` is
   a strict non-negative integer (digits only). No mode argument.
   Reads `clean.json` only — never re-reads `logs/app.log`
   (one source of truth, WP2 law).

### Logging (the tool's own logs)

- `ingest` and `fetch` accept the trailing mode; `window`/`report` do
  not (readers stay silent on stderr).
- `normal` → INFO+ on stderr · `quiet` → stderr silent · `verbose` →
  DEBUG+ on stderr · every run of a mode command writes `ops.log`
  beside `main.py` (`mode="w"`, always DEBUG, leveled records).
- No `print()` diagnostics ever — stdout is data only. No secrets.

### Error contract (two lines on stderr, then exit 1)

- Prefix line, then detail line. Prefixes: `bad request:` for bad
  argv/validation · `network error:` for `requests` failures (detail =
  the failure's first line) · `corrupt data:` for unreadable/invalid
  `clean.json` (detail = `failed to load clean data | <cause>`).
- The two-line message is written **directly** to stderr — never
  routed through the logger. Logging lives only inside the mode
  commands (`ingest`/`fetch`): in `normal`/`verbose`, the command's
  own INFO/DEBUG lines may appear on stderr **before** the error
  message; in `quiet`, log lines are suppressed but the two-line error
  message still prints. `window`/`report` and argv errors never log.
- Usage (no arguments at all): one usage line on stderr, exit 1,
  wording is yours.
- Error case = stderr + exit 1 + **no traceback + no files written**.
- If you deliberately change a pinned message, update the matrix in
  the same commit (WP3 contract rule, still law).

## Development environment (do this yourself, L20 discipline)

- `python -m venv .venv`, activate it, use it for everything.
- `python -m pip install requests pytest mypy` — ask before anything
  else.
- Hand-write `requirements.txt` (what YOU directly import — never a
  global freeze).
- `.gitignore` covers `.venv/`, `__pycache__/`, `.pytest_cache/`,
  `ops.log`, `clean.json`, `state.json`, `summary.json`;
  `requirements.txt`, `logs/app.log`, `stub_feed.py` ARE tracked.
- `mypy` clean on `main.py` and every module you write; everything
  annotated.

## Constraints

- Use only Stage 3 topics and earlier (plus AWARENESS-level lookups).
  `argparse`/`--flags` stay out — positional argv only. Asyncio only
  via SG3, never required.
- Layered split expected where it genuinely helps (ingest/parse,
  query/report, fetch, logging — or whatever YOUR design argues);
  a single well-structured `main.py` is acceptable — decision logged
  either way.
- No error-string returns — typed errors with `status`-or-`None`
  discipline (L18/L19); missing store file → graceful empty shape
  (`[]`), corrupt store → typed error reaching `main` → two-line
  stderr, exit 1.
- Log records carry levels; no `print()` diagnostics; no secrets.
- Git commit at meaningful milestones; `git log` shows more than one
  commit.
- `stub_feed.py` stays EXACTLY as provided (verify with `git diff` —
  it must show no changes).
- NO step-by-step plan provided. Design decisions are yours; the AI
  clarifies requirements and reviews code — it never implements.
- R16: no `solution.py` anywhere — everything ships in `main.py` /
  your modules, written by you.

## Spec output blocks (frozen — byte-exact)

**Provided fixture** — `logs/app.log` ships with this project (14
lines: 13 valid, 1 deliberately malformed, deliberately out of
chronological order).

`python main.py ingest` in the project folder:

```text
Ingest: 13 valid, 1 skipped
```

…and `clean.json` must contain exactly this line (no trailing
newline):

```text
[{"date":"2026-10-19","time":"09:14:02","level":"INFO","service":"api","latency":142,"status":200,"path":"/health"},{"date":"2026-10-19","time":"09:14:03","level":"INFO","service":"api","latency":118,"status":200,"path":"/health"},{"date":"2026-10-19","time":"09:14:04","level":"ERROR","service":"api","latency":940,"status":503,"path":"/report"},{"date":"2026-10-19","time":"09:14:05","level":"WARN","service":"worker","latency":890,"status":200,"path":"/jobs"},{"date":"2026-10-19","time":"09:14:06","level":"INFO","service":"db","latency":88,"status":200,"path":"/query"},{"date":"2026-10-19","time":"09:14:07","level":"INFO","service":"worker","latency":430,"status":200,"path":"/jobs"},{"date":"2026-10-19","time":"09:14:08","level":"WARN","service":"db","latency":660,"status":200,"path":"/query"},{"date":"2026-10-19","time":"09:14:09","level":"ERROR","service":"db","latency":1500,"status":500,"path":"/query"},{"date":"2026-10-19","time":"09:14:11","level":"INFO","service":"worker","latency":512,"status":200,"path":"/jobs"},{"date":"2026-10-19","time":"09:14:12","level":"INFO","service":"db","latency":95,"status":200,"path":"/query"},{"date":"2026-10-19","time":"09:14:13","level":"INFO","service":"worker","latency":377,"status":200,"path":"/jobs"},{"date":"2026-10-19","time":"09:14:14","level":"INFO","service":"api","latency":201,"status":200,"path":"/health"},{"date":"2026-10-19","time":"09:14:15","level":"WARN","service":"api","latency":760,"status":429,"path":"/report"}]
```

(The out-of-order file proves the sort; line 6 proves the skip;
keys prove the normalization.)

`python main.py window 09:14:04 09:14:09` (after T1):

```text
api: 1
db: 3
worker: 2
Window: 6 records
```

`python main.py report slow 3` (after T1):

```text
1500 db /query
940 api /report
890 worker /jobs
Slow: 3 records
```

`python main.py report slow 99` (after T1 — N bigger than the store):

```text
1500 db /query
940 api /report
890 worker /jobs
760 api /report
660 db /query
512 worker /jobs
430 worker /jobs
377 worker /jobs
201 api /health
142 api /health
118 api /health
95 db /query
88 db /query
Slow: 13 records
```

`python main.py fetch` (fresh folder):

```text
Incident: db-latency-degraded (severity 2)
```

…and `state.json` must contain exactly (no trailing newline):

```text
{"incident":"db-latency-degraded","severity":2,"updated":"2026-10-19T09:30:00"}
```

## Test matrix (self-validate before asking for review)

Run from the project folder. Happy path = stdout block byte-exact,
exit 0. Error case = two-line scoped message on **stderr**, **exit 1**,
no traceback, no files written. Rows that mutate files: run in a temp
copy.

| # | Command / setup | Expect |
|---|-----------------|--------|
| T1 | `ingest` (fixture present) | `Ingest: 13 valid, 1 skipped`; `clean.json` byte-exact (the long line above) |
| T2 | `ingest` with `logs/app.log` removed | `Ingest: 0 valid, 0 skipped`, exit 0; `clean.json` contains `[]` |
| T3 | `window 09:14:04 09:14:09` (after T1) | the 4-line block above, byte-exact |
| T4 | `window 09:15:00 09:16:00` (after T1) | stdout `Window: 0 records`, exit 0 |
| T5 | `window 9am 10am` | stderr, exit 1: `bad request:` + `times must be HH:MM:SS` |
| T6 | `window 09:14:09 09:14:04` (reversed) | stderr, exit 1: `bad request:` + `start must not be after end` |
| T7 | `report slow 3` (after T1) | the 4-line block above, byte-exact |
| T7b | `report slow 99` (after T1) | the 14-line block above, byte-exact |
| T7c | `report slow 0` (after T1) | stdout `Slow: 0 records`, exit 0 |
| T8 | `window 09:14:04 9:14:09` (one-digit hour) | stderr, exit 1: `bad request:` + `times must be HH:MM:SS` |
| T9 | `report slow abc` | stderr, exit 1: `bad request:` + `N must be a non-negative integer` |
| T10 | `report slow -5` | stderr, exit 1: `bad request:` + `N must be a non-negative integer` |
| T11 | `report slow` (missing N) | stderr, exit 1: `bad request:` + detail naming what `report` accepts |
| T12 | overwrite `clean.json` with `{bad json`, then `window 09:14:04 09:14:09` | stderr, exit 1: `corrupt data:` + `failed to load clean data \| Expecting property name enclosed in double quotes: line 1 column 2 (char 1)`, no traceback |
| T12b | overwrite `clean.json` with `[{"foo": 1}]`, then `report slow 3` | stderr, exit 1: `corrupt data:` + `failed to load clean data \| bad record: {'foo': 1}`, no traceback |
| T12c | overwrite `clean.json` with `{"foo": 1}`, then `window 09:14:04 09:14:09` | stderr, exit 1: `corrupt data:` + `failed to load clean data \| bad shape: expected a list`, no traceback |
| T13 | `fetch` (fresh folder) | `Incident: db-latency-degraded (severity 2)`; `state.json` byte-exact |
| T14 | `FEED_API_BASE=http://127.0.0.1:1 python main.py fetch` | stderr, exit 1: contains `network error:` + a detail line naming the connection failure (INFO/DEBUG log lines may precede it — see error contract), no traceback, `state.json` NOT written |
| T15 | (no arguments) | one usage line on stderr (your wording), exit 1 |
| T15b | `bananas` | stderr, exit 1: `bad request:` + `unknown command 'bananas'` |
| T16 | `window 09:14:04 09:14:09` with no `clean.json` at all | stdout `Window: 0 records`, exit 0 (graceful empty, WP2 precedent) |
| T16b | `report slow 3` with no `clean.json` at all | stdout `Slow: 0 records`, exit 0 |
| T17 | `python -m pytest tests -q` | your suite, all green (≥5 tests incl. ≥1 `caplog` test and ≥1 `tmp_path` test) |
| T18 | `mypy` on `main.py` + every module you write | clean |
| T19 | `git status` / `git diff stub_feed.py` | `.venv/`, `ops.log`, `clean.json`, `state.json`, `summary.json` NOT tracked; `requirements.txt`, `logs/app.log`, `stub_feed.py` tracked; stub diff EMPTY |
| T20 | `ingest quiet` → then `ingest verbose` | quiet: stdout pin exact, stderr EMPTY; verbose: stdout pin exact, stderr contains `DEBUG`; `ops.log` exists both times |
| T21 | delete `clean.json`, run `ingest` in one command line, `window 09:14:04 09:14:09` in a separate command line | T3 block again — files survive across runs |

Exact detail lines for the corrupt-data rows (verbatim — the matrix's
`\|` is only table escaping):

```text
failed to load clean data | Expecting property name enclosed in double quotes: line 1 column 2 (char 1)
failed to load clean data | bad record: {'foo': 1}
failed to load clean data | bad shape: expected a list
```

## Acceptance Criteria

- [ ] All of T1–T21 pass exactly as specified (temp copy for the
      file-mutating rows).
- [ ] Reports (`window`, `report`) read `clean.json` back from disk —
      one source of truth, never re-reading `logs/app.log`.
- [ ] `requests` + `timeout=` + `raise_for_status()` + typed errors
      end-to-end (no `urllib` fallback, no bare `except`).
- [ ] Logging: quiet/normal/verbose behave as specified; `ops.log`
      carries DEBUG; no diagnostic prints anywhere.
- [ ] `mypy` clean on everything you wrote; annotations throughout.
- [ ] `git log` shows more than one commit.
- [ ] `stub_feed.py` unchanged (`git diff` empty).
- [ ] Decisions Log filled during the build (Why + Alternative
      columns), README written, technical reflection written.

## Stretch goals (optional)

Do the main goal first. Each stretch is independent and optional.

- **SG1 — `report errors`:** statuses ≥ 400 from `clean.json`, one
  line per distinct status ascending, then `Errors: <n> records`.
  Validation: after T1 → byte-exact:

```text
429: 1
500: 1
503: 1
Errors: 3 records
```

  (Graceful empty → `Errors: 0 records`, exit 0.)
- **SG2 — `report export`:** writes `summary.json` (compact, no
  trailing newline) with `records`, `max_latency`, `worst_status`
  (highest status code in the store, `0` if empty) and prints
  `Export: <n> records`. Validation: after T1 → stdout
  `Export: 13 records` and `summary.json` byte-exact:

```text
{"records":13,"max_latency":1500,"worst_status":503}
```
- **SG3 — async `fetch`:** rework the fetch path as a genuine async
  task with stdlib-only `asyncio` (no new dependencies). The full
  matrix — especially T13/T14 — must stay green, and the decision is
  logged. Only if you actually want it: the tier never requires it.

## Deliverables

- Source in this folder (`main.py` starts blank — you write
  everything). Layered split decision logged.
- `tests/` suite (conftest + fixtures encouraged), `requirements.txt`,
  `.gitignore`, short README (setup, how to run each command, what
  each output means, the `FEED_API_BASE` override).
- Technical reflection (template style) + the Decisions Log below.

## Decisions Log (filled by learner during build)

| Decision | Why | Alternative Considered |
|----------|-----|------------------------|
|          |     |                        |


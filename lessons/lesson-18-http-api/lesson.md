# Lesson 18 — HTTP & API Concepts (Tier: CORE)

Stage 3, second topic. Lesson 17 made your tests the source of truth.
This lesson makes the **network** the thing you read and write — the
layer under every API, every AI SDK, every web service.

---

## Objective

After this lesson you will be able to:

- Read a URL as a spec: scheme, host, path, query.
- Make a GET request and interpret status, headers, and body correctly.
- Send a POST with a JSON body and prove that POST is **not idempotent**.
- Turn an HTTP error into a structured, typed Python error — never a crash.
- Debug a broken HTTP client by traceback, not by guessing.

---

## Why This Matters

So far your data lived in files on your machine. Real engineering data
lives on **other machines** — you fetch it, you send it, you handle the
fact that nothing is guaranteed.

Every tool you will use as an Applied AI Engineer sits on HTTP:
OpenAI, Anthropic, Hugging Face, your company's internal services, the
tool-calls your agent makes. When you understand the request/response
contract, an "SDK" stops being magic — it becomes a thin wrapper around
what you can already do.

---

## Mental Model

HTTP is a **conversation with a verdict**.

```text
Client:  REQUEST        Server:
         method + URL    ──►   looks it up
         headers + body         does work (or not)
         ─────────────────►     replies:
                                status  = the verdict   (200 "ok", 404 "not here")
                                headers = the meta      (content type, length, …)
                                body    = the evidence  (usually JSON)
```

Two rules that solve most confusion:

1. **Status is the contract; body is the details.** Decide success or
   failure from the status number, never from the body.
2. **A URL is a spec, not a sentence.** Scheme tells the protocol, netloc
   tells the machine, path tells the resource, query tells the filters.

---

## Core Concept

### 1. URL anatomy — `urllib.parse.urlsplit`

A URL is built from four parts you must learn to separate:

```python
from urllib.parse import urlsplit

parts = urlsplit("https://api.example.com/v1/items?q=coffee&max=5")
parts.scheme   # "https"
parts.netloc   # "api.example.com"
parts.path     # "/v1/items"      <- which resource, on the server
parts.query    # "q=coffee&max=5" <- which filter/options
```

The **path** answers "which thing", the **query** answers "which view of
it". Putting filters into the path (`/items/coffee`) works for some APIs
but is the wrong tool for optional, ordered criteria. Routing is the
server's business; the client just builds the spec.

### 2. Methods — the verb is the intent

| Method | Intent | Safe? | Idempotent? |
|--------|--------|-------|-------------|
| GET    | read something | yes | yes |
| POST   | create / trigger an action | no | **no** |
| (PUT/DELETE later) | replace / remove | no | yes |

- **Safe**: asking the same question twice changes nothing.
- **Idempotent**: doing the same operation twice gives the same result.

GET is both. POST is neither. A POST that "adds one to a counter" will
add 1, then 2, then 3 — same request, different result. That is exactly
why naive retries of a POST can double-create things.

### 3. Status codes — the verdict

| Range | Meaning | First digits |
|-------|---------|--------------|
| 2xx | ok | 200 success, 201 created |
| 3xx | redirect | 301/302 moved |
| 4xx | **you** asked wrong | 400 bad request, 404 not found, 405 method not allowed |
| 5xx | **server** failed | 500 internal error |

In Python, a 2xx response comes back normally; any other status raises:

```python
import urllib.error, urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:8000/items") as r:
        print(r.status)          # 200
except urllib.error.HTTPError as e:
    print(e.code)                # 404 — the verdict still exists
```

`HTTPError` is a subclass of `URLError`, which is a subclass of
`OSError`. The hierarchy mirrors reality: an HTTP 404 is a *response*
(you reached the machine, it said no) — different from *no response at
all* (machine unreachable / too slow).

**Put the more specific handler first.** `except HTTPError` before
`except URLError`, or `HTTPError` is swallowed by its parent.

### 4. Headers — the meta data

```python
with urllib.request.urlopen(url) as r:
    print(r.headers.get("Content-Type"))    # "application/json; charset=utf-8"
    print(r.headers.get("Content-Length"))
```

`Content-Type` tells you *how to read the body*. You already learned the
Jes reading rule with files: not every body is text, and even text has
an encoding.

### 5. JSON as the wire format

The body always arrives as **bytes** — you decode, then parse:

```python
import json, urllib.request

with urllib.request.urlopen(url) as r:
    raw = r.read()                                     # bytes
    text = raw.decode("utf-8")                        # str
    data = json.loads(text)                           # dict/list — Lesson 11
```

Sending JSON is the same idea in reverse:

```python
import json, urllib.request

payload = {"name": "cookie"}
req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),         # bytes, not str
    headers={"Content-Type": "application/json"},     # the server must know
    method="POST",
)
with urllib.request.urlopen(req) as r:
    print(r.status)                                   # 201
```

### 6. Query strings — `urllib.parse.urlencode`

Never type `q=coffee latte` by hand. Spaces and special characters must
be **encoded**:

```python
from urllib.parse import urlencode

urlsafe = urlencode({"q": "coffee latte", "max": 5})
print(urlsafe)   # "q=coffee+latte&max=5"  (spaces become + or %20)
```

The server parses that back into `q="coffee latte"`. Skipping the encode
is a classic bug: the request either breaks or the server reads a
truncated value.

### 7. Structured errors — the three failure classes

| Failure | Exception to catch | What it means |
|---------|--------------------|---------------|
| Server answered "no" | `urllib.error.HTTPError` | `.code` = status, body readable |
| Machine unreachable | `urllib.error.URLError` | `.reason` = underlying error |
| Took too long | `TimeoutError` | **Python 3.12: a *read* timeout raises `TimeoutError` directly — it is NOT wrapped in `URLError`.** |

The third row is the trap. A server that accepts the connection but is
slow to answer times out *while reading*, and `except urllib.error.URLError`
will NOT catch it. Catch `TimeoutError` (or the common parent `OSError`)
too.

You already know how to give these a shape: turn them into one typed
error of your own (Lesson 8 + Lesson 14), so the rest of your code sees
`status`/`category`/`detail` — not raw exception soup.

---

## Practical Examples

Read these — the exercises reuse the same moves.

**1. A straight GET, not forgetting the context manager:**

```python
import urllib.request

with urllib.request.urlopen("http://127.0.0.1:8000/items", timeout=3) as r:
    print(r.status, r.headers.get("Content-Type"), r.read()[:40])
```

**2. A 404 the way it really appears:**

```python
import urllib.error, json, urllib.request

try:
    with urllib.request.urlopen("http://127.0.0.1:8000/items/999", timeout=3) as r:
        print(r.status)
except urllib.error.HTTPError as e:
    detail = json.loads(e.read().decode("utf-8"))   # the 404 body is readable
    print(e.code, detail)                           # 404 {'error': 'item not found'}
```

**3. A query built by the book:**

```python
from urllib.parse import urlencode
import json, urllib.request

query = urlencode({"q": "coffee"})
with urllib.request.urlopen(f"http://127.0.0.1:8000/search?{query}", timeout=3) as r:
    print(json.loads(r.read().decode("utf-8"))["count"])
```

**4. A POST with a JSON body, wanting a 201:**

```python
import json, urllib.request

req = urllib.request.Request(
    "http://127.0.0.1:8000/echo",
    data=json.dumps({"note": "hi"}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=3) as r:
    print(r.status, r.read().decode("utf-8"))
```

---

## Engineering Notes

- **Always use `with`** on the response and **always pass `timeout=`**.
  A network call with no timeout can hang your whole program forever.
- **Decode once, read once.** A second `r.read()` returns empty bytes.
- **Status decides; body explains.** Never report success because the
  body "looked right".
- **Secrets live in headers, never in URLs.** A URL ends up in logs,
  history, and error messages. An API key in the header is also not a
  toy — but at minimum it is not broadcast. Never `print()` a key.
- **Retries are a design decision, not a reflex.** Retrying a failed GET
  is nearly free; retrying a failed POST can duplicate the action.
- **Provided in this lesson** (so exercises stay deterministic and
  offline): `local_api.py` — a small JSON server on `127.0.0.1` with a
  free port. Its internals mirror what you will write yourself in H2.
  Everything in it is simple by design: read it, run it, learn from it.
- **Deliberately NOT taught yet:** the `requests` library. Real projects
  use it (it wraps all of this). You will get it in Lesson 19 — after
  you have seen the wire with your own stdlib hands.
- **`BaseHTTPRequestHandler` writes back** with `send_response(status)`,
  `send_header(name, value)`, `end_headers()`, then
  `self.wfile.write(body_bytes)`. Statelessness: do not store per-client
  state on the handler class — keep data in a module-level structure.

---

## Common Pitfalls

1. **Reading the body twice.** Second read is empty. Read once, decode,
   parse, keep the parsed object.
2. **Catching `URLError` before `HTTPError`** (or only `URLError`) — the
   status error is swallowed and `.code` stops existing.
3. **Forgetting `TimeoutError`.** In Python 3.12 a read timeout is a
   `TimeoutError`, not a `URLError`.
4. **`== 200` when the API returns 201.** Accept `2xx`, not one number,
   unless you truly need exactly 200.
5. **Manually formatting query strings.** Use `urlencode`; hand-joined
   `?q=coffee latte` breaks on spaces and special characters.
6. **`json.dumps(...)` without `.encode("utf-8")`** — the body must be
   bytes. And never omit `Content-Type: application/json`.
7. **Passwords/key material in the query string** — it leaks into logs.

---

## Connection to Previous Knowledge

- **Lesson 8 — Exceptions**: `HTTPError`/`URLError`/`TimeoutError` is a
  real hierarchy; you already know how to turn hierarchies into your own
  typed errors.
- **Lesson 3 — `match`**: status ranges are a perfect match target —
  `case 200: ... case 404: ...`.
- **Lesson 9–11 — Files & JSON**: the body pipe is
  `bytes → decode → json.loads`; writing a cached API response to disk
  reuses all of it.
- **Lesson 12 — CSV**: exporting fetch results to CSV for a report.
- **Lesson 13–15 — Modules, typing, classes**: your client becomes a
  module with an annotated API (`fetch_json(base, path) -> dict`);
  the server handler is a class you will subclass in H2.
- **Lesson 16 — Dataclass**: a natural description of a *fixed response
  shape* (e.g. one weather reading).
- **Lesson 17 — pytest**: tests now spin the real local server in a
  fixture (`tmp_path` + `LocalAPI`) — integration tests, byte-exact.

---

## Quick Recall

Answer out loud, before looking back:

1. `urlsplit("https://shop.local/a/b?x=1").path` — what is it, and what
   is `.query`?
2. GET `/items` twice changes nothing. POST `/count` twice changes the
   result. Which property (safe / idempotent) is which, and why does it
   matter for retries?
3. A server is reachable and answers "resource unknown". What status ?
   Which exception do you write `except` — and why must it come before
   `URLError`?
4. In Python 3.12, a request that connects but never answers in time —
   which exception actually fires, and what is the common parent of it
   and `URLError`?
5. Your program must decide "is this a 404 or a 500?" — do you read the
   body or the status? Back your answer with the mental model.
6. `json.dumps(payload)` alone is not a valid request body. What is
   missing, and why?

---

## Practice

Read `local_api.py` first — it is your reference server for every
exercise. Provided: `local_api.py` (the server), `solution.py` (blank).
You will create the client/test files listed below.

| ID | Tier | Type | What you build |
|----|------|------|----------------|
| E1 | Easy | [REAL-WORLD] | `url_parts.py` — split URLs into scheme/netloc/path/query |
| E2 | Easy | [REAL-WORLD] | `client_basics.py` — GET status + status-family mapping |
| E3 | Easy | [REAL-WORLD] | `client_basics.py` — decode + `json.loads` a JSON body |
| E4 | Easy | [REAL-WORLD] | `client_basics.py` — read response headers / Content-Type |
| E5 | Easy | [REAL-WORLD] | `client_basics.py` — timeout that becomes `TimeoutError` |
| M1 | Medium | [REAL-WORLD] | `api_client.py` — one typed `fetch_json` with structured errors |
| M2 | Medium | [REAL-WORLD] | `post_client.py` — POST JSON; prove POST is not idempotent |
| M3 | Medium | [REAL-WORLD] | `search_client.py` — query strings with `urlencode` |
| H1 | **Hard** | [DEBUG] | `weather_client.py` (provided, 4 planted bugs) — find + fix each |
| H2 | **Hard** | [REAL-WORLD] | `store_server.py` + `store_client.py` — a tiny REST stub you design |
| Challenge | — | [REAL-WORLD] | `cache_cli.py` — fetch → persist (JSON/CSV) → dedupe → report |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target to farm.

Rules of the pack:

- Every file stays **flat in the lesson folder** — no `tests/` package.
- A file you create must pass every check the notebook drive cell runs.
- H1: the bug report table is a blank write-in — fill the slots
  (Expected / Observed / Root cause / Fix) as you work, never after.
- H2: `BaseHTTPRequestHandler` must stay **stateless**; validation
  decides 201 vs 400; id is decided by the server.
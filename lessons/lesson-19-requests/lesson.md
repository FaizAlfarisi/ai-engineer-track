# Lesson 19 — Requests (Tier: CORE)

Stage 3, third topic. Lesson 18 made you speak HTTP with the stdlib —
`urlopen`, status codes, `urlencode`, one-shot reads. This lesson gives you
the tool real projects actually use: **`requests`, the industry-standard
way to talk HTTP in Python.**

---

## Objective

After this lesson you will be able to:

- Install a third-party package with `pip` and import it.
- Build a GET URL with `params=` so encoding is never hand-made.
- Read a `Response` (`status_code`, `headers`, `text`, `json()`) correctly.
- Send a POST with `json=` and prove that POST is **not idempotent**.
- Turn every `requests` failure into one typed Python error — never a crash.
- Reuse one `Session` so headers and settings are set once, not per call.

---

## Why This Matters

`urllib` taught you the wire. Nobody ships `urllib` by choice: every call
needs a context manager, a manual encode, a manual decode, and a
three-branch exception ladder.

Real code — OpenAI clients, data pipelines, the sync CLI you will build in
the Challenge — looks like this instead:

```python
resp = requests.get(url, params={"q": "coffee latte"}, timeout=3)
resp.raise_for_status()
data = resp.json()
```

Three lines, same contract you already know: status decides, body
explains. When you meet an SDK later, you will recognize it as a thin
wrapper around exactly these moves.

---

## Mental Model

`urllib` is assembling the envelope by hand. **`requests` is the post
office counter**: you state the intent, it handles the envelope.

```text
urllib:    you encode → you open → you read once → you decode → you parse
requests:  you ask    → Response object holds everything, read it many times
```

Two rules carry over unchanged from Lesson 18:

1. **Status is the contract; body is the details.** With one twist:
   `requests` does **not** raise on 404/500 by itself — you ask for it
   with `raise_for_status()`.
2. **Never build a query string by hand.** `params={...}` encodes spaces
   and special characters for you, same job `urlencode` did.

---

## Core Concept

### 1. Installing third-party code — `pip install requests`

The stdlib ends where the ecosystem begins. `requests` lives on PyPI:

```python
# in your terminal, once per environment:
# pip install requests
import requests
print(requests.__version__)
```

Same environment discipline as Lesson 14 (`pip install mypy`):
install into your project `.venv`, never into global Python.

### 2. GET with `params=` — encoding done for you

```python
import requests

resp = requests.get(
    "http://127.0.0.1:8000/search",
    params={"q": "coffee latte", "max": 5},
    timeout=3,
)
print(resp.url)   # ".../search?q=coffee+latte&max=5" — space encoded, by the library
```

Want to see the URL *before* sending? Prepare it without sending:

```python
req = requests.Request("GET", "http://127.0.0.1:8000/search",
                       params={"q": "coffee latte"}).prepare()
print(req.url)    # ".../search?q=coffee+latte"
```

**The params dict IS the query spec.** No `+`, no `%20` typed by you.

### 3. The Response object — read it many times

```python
resp = requests.get("http://127.0.0.1:8000/items", timeout=3)
resp.status_code          # 200 — the verdict, always present, never raises by itself
resp.headers.get("Content-Type")   # "application/json; charset=utf-8"
resp.text                 # str — decoded body (read again, still there)
resp.content              # bytes — the raw body
resp.json()               # dict/list — parsed body (Lesson 11, one call)
```

The `urllib` trap is gone: there is no single-read cursor. `resp.text`,
`resp.content`, and `resp.json()` can each be called repeatedly.

### 4. POST with `json=` — one keyword, two jobs done

```python
resp = requests.post(
    "http://127.0.0.1:8000/echo",
    json={"note": "hi"},     # encodes to bytes AND sets Content-Type: application/json
    timeout=3,
)
print(resp.status_code)   # 201
print(resp.json())        # {"received": {"note": "hi"}}
```

`json=` replaces both `json.dumps(...).encode("utf-8")` and the manual
header from Lesson 18. (`data=` sends form bytes without the JSON header —
a different contract, not what a JSON API wants.)

POST stays **not idempotent**: three identical POSTs to `/count` answer
`{"n": 1}`, `{"n": 2}`, `{"n": 3}`. Same request, different result —
retries can duplicate the action.

### 5. `timeout=` + `raise_for_status()` — status decides again

```python
resp = requests.get("http://127.0.0.1:8000/items/999", timeout=3)
print(resp.status_code)   # 404 — no exception yet!
resp.raise_for_status()   # NOW it raises requests.HTTPError carrying .response
```

- **Always pass `timeout=`.** A network call with no timeout can hang
  your whole program forever (same rule as L18).
- **Call `raise_for_status()` when a non-2xx must stop you.** Then decide
  with `match` on the status (Lesson 3), exactly as before.

### 6. Structured errors — one family, one parent

| Failure | Exception | What it means |
|---------|-----------|---------------|
| Server answered "no" | `requests.HTTPError` (after `raise_for_status()`) | `.response.status_code` = the verdict |
| Machine unreachable / refused | `requests.ConnectionError` | nothing answered at all |
| Took too long | `requests.Timeout` | connect **or** read was too slow |
| Anything above | `requests.RequestException` | the common parent — catch-all for "HTTP failed" |

```python
import requests

class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status

def fetch_json(base: str, path: str) -> dict:
    try:
        resp = requests.get(base + path, timeout=3)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        raise ApiError(f"http {exc.response.status_code}",
                       status=exc.response.status_code) from exc
    except requests.ConnectionError as exc:
        raise ApiError(f"network error: {exc}") from exc
    except requests.Timeout as exc:
        raise ApiError(f"timeout: {exc}") from exc
```

**Order matters the same way it did in L18:** the specific handlers
(`HTTPError`) come before the general ones. One `except
requests.RequestException` first would swallow every row of the table
into a single branch and the status would be lost.

### 7. `Session` — set once, reuse everywhere

```python
sess = requests.Session()
sess.headers.update({"Authorization": "Bearer SECRET"})
resp = sess.get("http://127.0.0.1:8000/items", timeout=3)  # header sent automatically
sess.close()
```

A `Session` carries headers, cookies, and settings across calls — the
API key is attached once, not pasted into every function. (Connection
pooling rides along for free; you do not need its internals.)

---

## Practical Examples

Read these — the exercises reuse the same moves.

**1. Inspect the URL before sending:**

```python
import requests

req = requests.Request("GET", "http://127.0.0.1:8000/search",
                       params={"q": "coffee latte", "max": 5}).prepare()
print(req.url)   # http://127.0.0.1:8000/search?q=coffee+latte&max=5
```

**2. A 404 the requests way (no exception until asked):**

```python
import requests

resp = requests.get("http://127.0.0.1:8000/items/999", timeout=3)
print(resp.status_code)   # 404
try:
    resp.raise_for_status()
except requests.HTTPError as e:
    print(e.response.status_code, resp.json())   # 404 {'error': 'item not found'}
```

**3. A search plus a CSV export (Lessons 11 + 12, reused):**

```python
import csv, requests
from pathlib import Path

resp = requests.get("http://127.0.0.1:8000/search",
                    params={"q": "latte"}, timeout=3)
resp.raise_for_status()
items = resp.json()["items"]
with Path("hits.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["id", "name", "price", "stock"])
    w.writeheader()
    w.writerows(items)
```

**4. A POST that counts (idempotence disproved):**

```python
import requests

for _ in range(3):
    r = requests.post("http://127.0.0.1:8000/count", json={}, timeout=3)
    print(r.json())   # {"n": 1} then {"n": 2} then {"n": 3}
```

---

## Engineering Notes

- **Always pass `timeout=`, always decide with the status.**
  `raise_for_status()` + `match` on `status_code` is the standard spine.
- **`.json()` trusts the server.** Call it only after a 2xx (or inside
  `try`), because an error page is HTML, not JSON.
- **Secrets live in headers, never in URLs — and never `print()` them.**
  A `Session` with `headers.update(...)` keeps the key in one place.
- **Retries are still a design decision.** GET ≈ free to retry; POST can
  duplicate. `requests` will not retry for you — that honesty is a feature.
- **Provided in this lesson** (deterministic, offline): `local_api.py` —
  the same JSON server as L18. Its routes are unchanged; only your client
  library changes.
- **Deliberately NOT taught:** `requests` retry adapters, custom auth
  handlers, async HTTP (`httpx`/`aiohttp`) — project-dependent, not this
  lesson.

---

## Common Pitfalls

1. **Expecting `get()` to raise on 404.** It won't — check
   `status_code` or call `raise_for_status()`.
2. **`except RequestException` first.** The parent swallows `HTTPError`
   and the status is lost. Specific before general.
3. **Hand-building `?q=coffee latte`.** Use `params=`; raw spaces break
   or silently truncate the query.
4. **`data=json.dumps(payload)` without the header.** The server sees
   bytes with no content type — use `json=`.
5. **`.json()` on an error page.** A 500 body is usually HTML;
   `resp.json()` then raises a *second* error that hides the first.
6. **No `timeout=`.** One slow server freezes your program.
7. **`== 200` when the API returns 201.** Accept 2xx (or
   `raise_for_status`), unless you truly need exactly 200.

---

## Connection to Previous Knowledge

- **Lesson 18 — HTTP wire**: same conversation, same verdict/body split;
  `params=` replaces `urlencode`, `json=` replaces dumps+encode+header.
- **Lesson 8 — Exceptions**: the `RequestException` family is a second
  real hierarchy; your typed-error wrap (`ApiError`) is the same pattern.
- **Lesson 3 — `match`**: status ranges are still a match target.
- **Lesson 9–12 — Files/JSON/CSV**: cache the fetched items with
  `write_text`/`DictWriter`; accumulate with `.get(k, 0.0)` where totals
  apply.
- **Lesson 13–15 — Modules, typing, classes**: the client is a module
  with an annotated API; the `Session` variant is one small class.
- **Lesson 17 — pytest**: the H-drills run as suites with a live-server
  fixture — same integration-test shape as L18.

---

## Quick Recall

Answer out loud, before looking back:

1. `requests.get(url)` against a missing resource returns 404 in
   `status_code` — but nothing raised. Which single call turns it into an
   exception, and what does the exception carry?
2. `params={"q": "coffee latte"}` produces what substring in the final
   URL — and why must you never type that substring by hand?
3. `except requests.RequestException` sits above `except
   requests.HTTPError`. What breaks, and which L18 ordering rule is the
   same idea?
4. Three identical POSTs to `/count` answer n = 1, 2, 3. Which property
   (safe / idempotent) does this disprove — and what does it mean for
   retries?
5. `resp.json()` raises on a 500 page. Is the bug in your code or the
   server's — and where should the guard live?
6. Your CLI validates its command word. `if not isinstance(cmd, str)
   and not cmd:` — which inputs slip through, and which single-word fix
   closes it?

---

## Practice

Read `local_api.py` first — same reference server as L18, unchanged.
Provided: `local_api.py` (server), `weather_client.py` (buggy, H1),
`test_weather.py` + `test_sess.py` (suites, do not modify),
`solution.py` (blank). Install once: `pip install requests`.
You create every other file, flat in the lesson folder.

| ID | Tier | Type | What you build |
|----|------|------|----------------|
| E1 | Easy | [REAL-WORLD] | `url_parts.py` — build query URLs with `params=` via a prepared request |
| E2 | Easy | [REAL-WORLD] | `client_basics.py` — GET status + status-family mapping |
| E3 | Easy | [REAL-WORLD] | `client_basics.py` — parsed JSON body via `.json()` |
| E4 | Easy | [REAL-WORLD] | `client_basics.py` — response headers / Content-Type |
| E5 | Easy | [REAL-WORLD] | `client_basics.py` — timeout that becomes `requests.Timeout` |
| M1 | Medium | [REAL-WORLD] | `api_client.py` — one typed `fetch_json` with structured errors + path guard |
| M2 | Medium | [REAL-WORLD] | `post_client.py` — POST JSON; prove POST is not idempotent |
| M3 | Medium | [REAL-WORLD] | `search_client.py` — `params=` search + CSV export |
| H1 | **Hard** | [DEBUG] | `weather_client.py` (provided, 4 planted bugs) — find + fix each |
| H2 | **Hard** | [REAL-WORLD] | `sess_client.py` — a `Session`-based client with headers-once |
| Challenge | — | [REAL-WORLD] | `sync_cli.py` — fetch → persist (JSON/CSV) → merge → report (positional argv) |

Scoring: Easy 10 · Medium 20 · Hard 35 · Challenge 100. Points are
diagnostic, not a target to farm.

Rules of the pack:

- Every file stays **flat in the lesson folder** — no `tests/` package.
- A file you create must pass every check the notebook drive cell runs.
- H1: the bug report table is a blank write-in — fill the slots
  (Expected / Observed / Root cause / Fix) as you work, never after.
- Challenge: one positional command word (`sync`); unknown/missing args
  exit 1 with usage on stderr. No `--flags` in this lesson.

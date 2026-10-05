"""Provided stub API for Weekly Project 3 — read-only infrastructure.

Do NOT modify this file (verify with `git diff` — it must show no
changes). It is the same deterministic JSON server as the lessons,
renamed for the project.

Routes
------
GET  /items                -> all items, sorted by id
GET  /items/{id}           -> one item, or 404
GET  /search?q=..&max=..   -> case-insensitive substring search, capped
GET  /echo                 -> 405 (echo is POST-only)
GET  /count                -> 405 (count is POST-only)
GET  /slow                 -> sleeps ~0.5s then answers (timeout drills)
GET  /weather?city=..      -> known cities, or 404
POST /echo   (JSON body)   -> 201, echoes {"received": <body>}
POST /count  (any body)    -> 200, {"n": N}; N increments per POST

Usage
-----
    api = stub_api.StubAPI()
    api.base            # e.g. "http://127.0.0.1:51234"
    ... make requests against api.base ...
    api.stop()

Set SYNC_API_BASE to override the base URL (used by the network-error
test row). The counter is per StubAPI instance.
"""

import json
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

ITEMS = [
    {"id": 1, "name": "coffee", "price": 2.50, "stock": 40},
    {"id": 2, "name": "tea", "price": 1.80, "stock": 25},
    {"id": 3, "name": "muffin", "price": 3.20, "stock": 0},
    {"id": 4, "name": "latte", "price": 4.10, "stock": 12},
]

WEATHER = {
    "london": {"city": "london", "temp_c": 15.0, "condition": "cloudy"},
    "tokyo": {"city": "tokyo", "temp_c": 24.5, "condition": "sunny"},
    "denver": {"city": "denver", "temp_c": 9.0, "condition": "rain"},
    "new york": {"city": "new york", "temp_c": 18.2, "condition": "foggy"},
}


class _StubAPIHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass

    def _reply(self, payload, status=200):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json(self):
        try:
            length = int(self.headers.get("Content-Length", "0") or "0")
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if length else b""
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return None

    def _item_id(self):
        tail = self.path.rsplit("/", 1)[1]
        try:
            return int(tail)
        except ValueError:
            return None

    def _safe(self, func):
        try:
            func()
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError, TimeoutError):
            pass

    def do_GET(self):
        self._safe(self._do_get)

    def _do_get(self):
        if self.path == "/items":
            self._reply({"count": len(ITEMS), "items": ITEMS})
        elif self.path.startswith("/items/"):
            item_id = self._item_id()
            if item_id is None:
                self._reply({"error": "item id must be an integer"}, 404)
                return
            for item in ITEMS:
                if item["id"] == item_id:
                    self._reply(item)
                    return
            self._reply({"error": "item not found"}, 404)
        elif self.path.startswith("/search"):
            qs = parse_qs(urlparse(self.path).query)
            q = (qs.get("q") or [""])[0]
            if not q:
                self._reply({"error": "missing q", "count": 0, "items": []}, 400)
                return
            try:
                max_items = int((qs.get("max") or ["10"])[0])
            except ValueError:
                max_items = 10
            hits = [it for it in ITEMS if q.lower() in it["name"].lower()]
            self._reply(
                {"query": q, "count": len(hits[:max_items]), "items": hits[:max_items]}
            )
        elif self.path.startswith("/weather"):
            qs = parse_qs(urlparse(self.path).query)
            city = (qs.get("city") or [""])[0]
            report = WEATHER.get(city.lower())
            if not report:
                self._reply({"error": "unknown city"}, 404)
                return
            self._reply(report)
        elif self.path == "/echo":
            self._reply({"error": "echo is POST-only"}, 405)
        elif self.path == "/count":
            self._reply({"error": "count is POST-only"}, 405)
        elif self.path == "/slow":
            time.sleep(0.5)
            self._reply({"slow": True})
        else:
            self._reply({"error": "not found"}, 404)

    def do_POST(self):
        self._safe(self._do_post)

    def _do_post(self):
        if self.path == "/echo":
            data = self._read_json()
            if data is None:
                self._reply({"error": "body must be valid JSON"}, 400)
                return
            self._reply({"received": data}, 201)
        elif self.path == "/count":
            self.server.count["n"] += 1
            self._reply({"n": self.server.count["n"]})
        else:
            self._reply({"error": "not found"}, 404)


class StubAPI:
    """Start a deterministic JSON API on 127.0.0.1 with a free port."""

    def __init__(self):
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), _StubAPIHandler)
        self._server.count = {"n": 0}
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    @property
    def port(self):
        return self._server.server_address[1]

    @property
    def base(self):
        return f"http://127.0.0.1:{self.port}"

    def reset_count(self):
        self._server.count["n"] = 0

    def stop(self):
        self._server.shutdown()
        self._server.server_close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.stop()

"""Spec-faithful alternative for H2 — reference for comparison only.

Follows the exercise contract exactly: `store_server.start(port=0)` returns a
`ThreadingHTTPServer` bound to 127.0.0.1. Your `StoreAPI` version and this
one share the same client interface (`store_client.py`), so either server
can back the same tests. This file is a reference model, not a replacement.
"""

import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

INVENTORY: list[dict] = []
_next_id = {"n": 1}


class StoreHandler(BaseHTTPRequestHandler):
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

    def do_GET(self):
        if self.path == "/items":
            self._reply({"count": len(INVENTORY), "items": INVENTORY})
        elif self.path.startswith("/items/"):
            try:
                item_id = int(self.path.rsplit("/", 1)[1])
            except ValueError:
                self._reply({"error": "item id must be an integer"}, 404)
                return
            for item in INVENTORY:
                if item["id"] == item_id:
                    self._reply(item)
                    return
            self._reply({"error": "item not found"}, 404)
        else:
            self._reply({"error": "not found"}, 404)

    def do_POST(self):
        if self.path != "/items":
            self._reply({"error": "not found"}, 404)
            return
        data = self._read_json()
        if data is None or not isinstance(data, dict):
            self._reply({"error": "body must be a JSON object"}, 400)
            return
        name = data.get("name")
        price = data.get("price")
        if not isinstance(name, str) or not name.strip():
            self._reply({"error": "name must be a non-empty string"}, 400)
            return
        if not isinstance(price, (int, float)) or isinstance(price, bool) or not price > 0:
            self._reply({"error": "price must be a positive number"}, 400)
            return
        item = {"id": _next_id["n"], "name": name.strip(), "price": float(price)}
        _next_id["n"] += 1
        INVENTORY.append(item)
        self._reply(item, status=201)


def start(port: int = 0):
    return ThreadingHTTPServer(("127.0.0.1", port), StoreHandler)
"""Provided stub feed for Weekly Project 4 — read-only infrastructure.

Do NOT modify this file (verify with `git diff` — it must show no
changes). It is the same deterministic server shape as WP3's
`stub_api`, slimmed for the ops toolkit.

Routes
------
GET  /incident   -> current incident snapshot (deterministic)
GET  /health     -> node health snapshot (deterministic)
anything else    -> 404

Usage
-----
    feed = stub_feed.StubAPI()
    feed.base            # e.g. "http://127.0.0.1:51234"
    ... make requests against feed.base ...
    feed.stop()

Set FEED_API_BASE to override the base URL (used by the network-error
test row).
"""

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

INCIDENT = {
    "incident": "db-latency-degraded",
    "severity": 2,
    "updated": "2026-10-19T09:30:00",
}

HEALTH = {"status": "ok", "nodes": 3}


class _StubFeedHandler(BaseHTTPRequestHandler):
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

    def _safe(self, func):
        try:
            func()
        except (ConnectionAbortedError, ConnectionResetError, BrokenPipeError, TimeoutError):
            pass

    def do_GET(self):
        self._safe(self._do_get)

    def _do_get(self):
        if self.path == "/incident":
            self._reply(INCIDENT)
        elif self.path == "/health":
            self._reply(HEALTH)
        else:
            self._reply({"error": "not found"}, 404)


class StubAPI:
    """Start a deterministic JSON feed on 127.0.0.1 with a free port."""

    def __init__(self):
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), _StubFeedHandler)
        self._thread = threading.Thread(target=self._server.serve_forever, daemon=True)
        self._thread.start()

    @property
    def port(self):
        return self._server.server_address[1]

    @property
    def base(self):
        return f"http://127.0.0.1:{self.port}"

    def stop(self):
        self._server.shutdown()
        self._server.server_close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.stop()

import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ITEMS = []
NEXT_ID = 1

class _StoreAPIHandler(BaseHTTPRequestHandler):
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
        try:
            tail = self.path.rsplit("/", 1)[1]
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
        global ITEMS
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
            
        else:
            self._reply({"error": "not found"}, 404)
    
    def do_POST(self):
        self._safe(self._do_post)
        
    def _do_post(self):
        global ITEMS, NEXT_ID
        
        if self.path == "/items":
            data = self._read_json()
            if not isinstance(data, dict):
                self._reply({"error": "invalid json body"}, 400)
                return

            name = data.get("name")
            price = data.get("price")
            
            if not isinstance(name, str) or not name.strip():
                self._reply({"error": "name must be a non-empty string"}, 400)
                return
            if not isinstance(price, (int, float)) or price <= 0:
                self._reply({"error": "price must be a number > 0"}, 400)
                return
            
            new_item = {"id": NEXT_ID, "name": name, "price": float(price)}
            ITEMS.append(new_item)
            NEXT_ID += 1
            
            self._reply(new_item, 201)
            
        else:
            self._reply({"error": "not found"}, 404)
            
class StoreAPI:
    def __init__(self):
        global ITEMS, NEXT_ID
        ITEMS.clear()
        NEXT_ID = 1
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), _StoreAPIHandler)
        self._thread = threading.Thread(
            target=self._server.serve_forever, daemon=True
        )
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
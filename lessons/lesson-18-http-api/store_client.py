import json
import urllib.request
import urllib.error

class StoreError(Exception):
    def __init__(self, status: int | None, detail: str):
        self.status = status
        self.detail = detail
        super().__init__(f"Status: {status} - Detail: {detail}")
        
def list_items(base: str) -> list[dict]:
    url = f"{base}/items"
    try:
        with urllib.request.urlopen(url) as r:
            data = json.loads(r.read().decode("utf-8"))
            return data["items"]
    except urllib.error.HTTPError as exc:
        raise StoreError(status=exc.code, detail=exc.read().decode("utf-8"))
    
def get_item(base: str, item_id: int) -> dict:
    url = f"{base}/items/{item_id}"
    try:
        with urllib.request.urlopen(url) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise StoreError(status=exc.code, detail=exc.read().decode("utf-8"))
    
def create_item(base: str, name: str, price: float) -> dict:
    url = f"{base}/items"
    payload = {"name": name, "price": price}
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
           raise StoreError(status=exc.code, detail=exc.read().decode("utf-8"))
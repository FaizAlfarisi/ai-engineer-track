import json
import urllib.request
import urllib.error
from urllib.parse import urlencode

def search(base: str, term: str, max_items: int = 10, timeout: float = 3.0) -> dict:
    query = urlencode({"q": term, "max": max_items})
    
    try: 
        with urllib.request.urlopen(f"{base}/search?{query}", timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        try:
            error_body = json.loads(exc.read().decode("utf-8"))
        except Exception:
            error_body = {}
        return error_body
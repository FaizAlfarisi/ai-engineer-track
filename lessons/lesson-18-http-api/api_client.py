import json
import urllib.request
import urllib.error


class APIError(Exception):
    def __init__(self, category: str, status: int | None, detail: str | None):
        super().__init__(f"{category} {status} {detail}")
        self.category = category
        self.status = status
        self.detail = detail
        
def fetch_json(base: str, path: str, timeout: float = 3.0) -> dict:
    try:
        with urllib.request.urlopen(f"{base}{path}", timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
        
    except urllib.error.HTTPError as exc:
        detail = None
        
        try:
            error_body = json.loads(exc.read().decode("utf-8"))
            detail = error_body.get("error")
        except json.JSONDecodeError:
            pass
        
        raise APIError("status", status=exc.code, detail=detail)
    
    except TimeoutError as exc:
        raise APIError("timeout", status=None, detail=str(exc))
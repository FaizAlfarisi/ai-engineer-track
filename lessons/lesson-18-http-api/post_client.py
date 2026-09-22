import json
import urllib.request
import urllib.error

def post_json(base: str, path: str, payload: dict | None = None, timeout: float = 3.0) -> tuple[int, dict]:
    data = None
    headers = {}
    
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    
    req = urllib.request.Request(
        url=f"{base}{path}",
        data=data,
        headers=headers,
        method="POST",
    )
    
    try:
        with urllib.request.urlopen(req) as r:
            body = json.loads(r.read().decode("utf-8"))
            return r.status, body
    except urllib.error.HTTPError as exc:
        try:
            error_body = json.loads(exc.read().decode("utf-8"))
        except Exception:
            error_body = {}
        return exc.code, error_body    
        
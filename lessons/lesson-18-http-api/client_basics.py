import json
import urllib.error
import urllib.request


def get_status(base: str, path: str) -> int:
    try:
        with urllib.request.urlopen(f"{base}{path}", timeout=5) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code

def status_family(code: int) -> str:
    code_str = str(code)
    
    match code_str[0]:
        case "2":
            return "2xx"
        case "3":
            return "3xx"
        case "4":
            return "4xx"
        case "5":
            return "5xx"
        case _:
            return "?"
        
def get_json(base: str, path: str) -> dict:
    try:
        with urllib.request.urlopen(f"{base}{path}", timeout=5) as r:
            raw = r.read()
            text = raw.decode("utf-8")
            return json.loads(text)
    except urllib.error.HTTPError:
        return {}
    
def get_headers(base: str, path: str) -> dict:
    try:
        with urllib.request.urlopen(f"{base}{path}", timeout=5) as r:
            return {
                "content-type": r.headers.get("Content-Type"),
                "content-length": r.headers.get("Content-Length"),
                "body_bytes": len(r.read()),
            }
    except urllib.error.HTTPError:
        return {}
    
def probe_timeout(base: str, path: str = "/slow", timeout: float = 0.05) -> str:
    try:
        with urllib.request.urlopen(f"{base}{path}", timeout=timeout) as r:
            pass
    except TimeoutError as exc:
        return f"TimeoutError {exc}"
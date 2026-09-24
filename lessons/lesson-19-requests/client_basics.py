import requests


def get_status(base: str, path: str) -> int:
    resp = requests.get(f"{base}{path}", timeout=3)
    return resp.status_code

def status_family(code: int) -> str:
    first_code = str(code)[0]
    
    match first_code:
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
        resp = requests.get(f"{base}{path}", timeout=3)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException:
        return {}
    
def get_headers(base: str, path: str) -> dict:
    try:
        resp = requests.get(f"{base}{path}", timeout=3)
        return {
            "content-type": resp.headers.get("Content-Type"),
            "content-length": resp.headers.get("Content-Length"),
            "body_bytes": len(resp.content),
        }
    except requests.RequestException:
        return {}
    
def probe_timeout(base: str, path: str = "/slow", timeout: float = 0.05) -> str:
    try:
        resp = requests.get(f"{base}{path}", timeout=timeout)
        resp.raise_for_status()
        return "no-timeout"
    except requests.Timeout as exc:
        return f"{type(exc).__name__}"
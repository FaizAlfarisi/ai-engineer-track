import requests

class ApiError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status
        
def fetch_json(base: str, path: str) -> dict:
    if not isinstance(path, str) or not path.startswith("/"):
        raise ApiError(message=f"bad path: {path!r}")
    
    try:
        resp = requests.get(f"{base}{path}", timeout=3)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        code = exc.response.status_code
        raise ApiError(message=f"http {code}", status=code) from exc
    except requests.ConnectionError as exc:
        raise ApiError(message=f"network error: {exc}") from exc
    except requests.Timeout as exc:
        raise ApiError(message=f"timeout: {exc}") from exc
        
    
    
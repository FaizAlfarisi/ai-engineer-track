import requests

class ShopError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.message = message
        self.status = status
        
def make_session(api_key: str) -> requests.Session:
    sess = requests.Session()
    sess.headers.update({"Authorization": f"Bearer {api_key}"})
    return sess

def fetch_with(session: requests.Session, base: str, path: str) -> dict:
    try: 
        resp = session.get(f"{base}{path}", timeout=3)
        resp.raise_for_status()
        return resp.json()
    except requests.HTTPError as exc:
        code = exc.response.status_code
        raise ShopError(message=f"http {code}", status=code) from exc
    except requests.ConnectionError as exc:
        raise ShopError(message=f"network error: {exc}") from exc
    except requests.Timeout as exc:
        raise ShopError(message=f"timeout: {exc}") from exc
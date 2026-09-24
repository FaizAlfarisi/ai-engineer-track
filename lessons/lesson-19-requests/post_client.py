import requests

def post_json(base: str, path: str, payload: dict) -> tuple[int, dict]:
    resp = requests.post(f"{base}{path}", json=payload, timeout=3)
    resp.raise_for_status()
    return resp.status_code, resp.json()
        
    
import requests

def build_url(base: str, path: str, params: dict) -> str:
    return requests.Request("GET", f"{base}{path}", params=params).prepare().url

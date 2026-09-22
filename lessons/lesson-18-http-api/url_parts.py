from urllib.parse import urlsplit

def split_url(url: str) -> tuple[str, str, str, str]:
    parts = urlsplit(url)
    
    return parts.scheme, parts.netloc, parts.path, parts.query
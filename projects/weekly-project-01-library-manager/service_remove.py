from custom_error import ErrorBadRequest
from helper import load_json, write_json

def remove_book(raw, path):
    title = raw[2].lower().strip()
    
    data_found = None

    data = load_json(path)

    for book in data:
        if book["title"].lower() == title:
            data_found = book
            break
    
    if data_found is None:
        raise ErrorBadRequest(f"remove data failed: title '{title}' not found")
    else:
        data.remove(data_found)
        return write_json(path, data)
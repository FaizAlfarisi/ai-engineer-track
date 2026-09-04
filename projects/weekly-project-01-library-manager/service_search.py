from helper import load_json, list_builder
from custom_error import ErrorBadRequest

def search_book(raw, path):
    search_text = raw[0].lower().strip()

    data = load_json(path)

    data_found = [book for book in data if book["title"].lower() == search_text or book["author"].lower() == search_text]

    if not data_found:
        raise ErrorBadRequest(f"no books found")
    else:
        result = list_builder(data_found)
        return print("\n".join(result))
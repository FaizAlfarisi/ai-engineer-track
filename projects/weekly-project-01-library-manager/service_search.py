from custom_error import ErrorBadRequest
from helper import load_json, list_builder

def search_book(raw, path):
    search_text = raw[2].lower().strip()
    if not search_text:
        raise ErrorBadRequest(f"empty input: search can't be empty")

    data = load_json(path)

    data_found = [book for book in data if search_text in book["search_index"]]

    if not data_found:
        return print("no books found")
    else:
        result = list_builder(data_found)
        return print("\n".join(result))
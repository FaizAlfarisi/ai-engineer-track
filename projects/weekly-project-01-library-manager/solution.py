import sys
import json
from pathlib import Path

class ErrorBadRequest(Exception):
    """ Custom exception for handling invalid user input """
    pass

def map_action(action, data):
    match action:
        case "add":
            add(data)
        case "remove":
            remove(data)
        case "search":
            search(data)
        case "list":
            show_list(data)
        case _:
            raise ErrorBadRequest("action invalid")

# === ADD helper ===
class ErrorCorruptData(Exception):
    """ Custom exception for handling JSONDecodeError """
    pass     

def parse_year(text_year):
    try:
        year = int(text_year)
    except ValueError:
        raise ErrorBadRequest("invalid year: format is not supported")
    
    # assuming only accept book released after industry revolution
    if year < 1800 or year > 2026: 
        raise ErrorBadRequest("invalid year: year out of range") from None
    
    return year

def get_title(data):
    return data["title"].lower()
# === ADD helper ===

def add(raw):
    if len(raw) < 3 or len(raw) > 4:
        raise ErrorBadRequest(f"invalid add args: usage 'python soluton.py add <title> <author> <year> <genre(optional)>'\nenclose more than one word in quotation marks")
    
    # parsed = parse_data(raw)
    title, author, year = [r.strip() for r in raw[:3]]
    
    if not title or not author:
        raise ErrorBadRequest(f"empty input: title or author can't be empty")
    
    # default romance since it is the most popular book genre
    genre = raw[3] if len(raw) > 3 else "Romance" 
    
    data = load_json(FILE_PATH)
    existing_title = {d["title"] for d in data}
    
    if title in existing_title:
        raise ErrorBadRequest(f"duplicate title: title '{title}' already exist")
    
    new_data = {}
    new_data["title"] = title
    new_data["author"] = author
    new_data["year"] = parse_year(year)
    new_data["genre"] = genre
    new_data["search_index"] = f"{author} | {title}"
    
    data.append(new_data)
    
    return write_json(FILE_PATH, sorted(data, key=get_title))

def remove(raw):
    title = raw[0].lower().strip()
    
    data_found = None

    data = load_json(FILE_PATH)

    for book in data:
        if book["title"].lower() == title:
            data_found = book
            break
    
    if data_found is None:
        raise ErrorBadRequest(f"remove data failed: title '{title}' not found")
    else:
        data.remove(data_found)
        return write_json(FILE_PATH, data)

def search(data):
    return

def show_list(data):
    return

def load_json(path: Path):
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise ErrorCorruptData(err) from None

def write_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return

def main():
    args = sys.argv
    
    if len(args) < 2:
        print(f"bad request: need action")
        sys.exit(1)
    
    action = args[1]
    data = args[2:]
    
    try:
        map_action(action, data)
    except ErrorBadRequest as err:
        print(f"bad request:\n{err}")
    except ErrorCorruptData as err:
        print(f"corrupt data:\nfailed to load existing data | {err}")
        sys.exit(1)
    except:
        print(f"Unexpected error:\n{err}")
        sys.exit(1)
        
if __name__ == "__main__":
    FILE_PATH = Path("library_data.json")

    main()

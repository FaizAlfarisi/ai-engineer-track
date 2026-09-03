import sys
import json
from pathlib import Path

'''
my analysis
request -> validate argv -> map action -> (each action):  parse data -> load data -> action
- add data: search by title -> reject if exist -> append existing data -> re-write file
- remove data: search by title -> remove if exist -> re-write file
- search data: search by title and author -> combine both -> show data
- list data: return formatted data
'''

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
            raise ValueError("action invalid")

# === ADD helper ===
class ErrorCorruptData(Exception):
    """ Custom exception for handling JSONDecodeError """
    pass            

def parse_year(text_year):
    try:
        year = int(text_year)
    except ValueError:
        raise ValueError("invalid year: format is not supported")
    
    # assuming only accept book released after industry revolution
    if year < 1800 or year > 2026: 
        raise ValueError("invalid year: year out of range") from None
    
    return year

def get_title(data):
    return data["title"].lower()
# === ADD helper ===

def add(raw):
    # parsed = parse_data(raw)
    title, author, year = raw[:3]
    # default romance since it is the most popular book genre
    genre = raw[3] if len(raw) > 3 else "Romance" 
    
    data = load_json(FILE_PATH)
    existing_title = {d["title"] for d in data}
    
    if title in existing_title:
        raise ValueError(f"duplicate title: title '{title}' already exist")
    
    new_data = {}
    new_data["title"] = title
    new_data["author"] = author
    new_data["year"] = parse_year(year)
    new_data["genre"] = genre
    new_data["search_index"] = f"{author} | {title}"
    
    data.append(new_data)
    
    return write_json(FILE_PATH, sorted(data, key=get_title))

def remove(data):
    return

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
    
    if len(args) < 5:
        print("bad request: input format invalid")
        print("usage: python soluton.py <action> <title> <author> <year> <genre(optional)>")
        print("usage: enclose more than one word in quotation marks")
        sys.exit(1)
        
    action = args[1]
    data = args[2:]
    
    try:
        map_action(action, data)
    except ValueError as err:
        print(f"bad request: {err}")
        sys.exit(1)
    except ErrorCorruptData as err:
        print(f"corrupt data: failed to load existing data | {err}")
        sys.exit(1)
        
if __name__ == "__main__":
    FILE_PATH = Path("library_data.json")

    main()

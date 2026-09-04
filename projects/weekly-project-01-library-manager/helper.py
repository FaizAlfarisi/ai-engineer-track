import json
from pathlib import Path
from custom_error import ErrorBadRequest, ErrorCorruptData

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

def list_builder(data):
    result = [f"Books ({len(data)}):"]
    for i, book in enumerate(data, start=1):
        result.append(f"{i}. {book["title"]} — {book["author"]} ({book["year"]}) [{book["genre"]}]")
    return result

def count_by_genre(data):
    genre_count = {}
    
    for book in data:
        key = book["genre"]
        genre_count[key] = genre_count.get(key, 0) + 1
    
    result = [f"Genres ({len(genre_count)}):"]
    for i, (genre, count) in enumerate(sorted(genre_count.items()), start=1):
        result.append(f"{i}. {genre}: {count}")
        
    return result

def load_json(path: Path):
    if not path.exists() or not path.is_file():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise ErrorCorruptData(err) from None

def write_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
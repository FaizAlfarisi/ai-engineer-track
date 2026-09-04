from solution import ErrorBadRequest
from helper import load_json, parse_year, write_json, get_title

def add_book(raw, path):
    if len(raw) < 3 or len(raw) > 4:
        raise ErrorBadRequest(f"invalid add args: usage 'python soluton.py add <title> <author> <year> <genre(optional)>'\nenclose more than one word in quotation marks")
    
    # parsed = parse_data(raw)
    title, author, year = [r.strip() for r in raw[:3]]
    
    if not title or not author:
        raise ErrorBadRequest(f"empty input: title or author can't be empty")
    
    # default romance since it is the most popular book genre
    genre = raw[3] if len(raw) > 3 else "Romance" 
    
    data = load_json(path)
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
    
    return write_json(path, sorted(data, key=get_title))
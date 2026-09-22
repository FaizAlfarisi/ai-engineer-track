from custom_error import ErrorBadRequest
from helper import load_json, parse_year, write_json, get_title

def add_book(raw, path):
    request_data = raw[2:]
    if len(request_data) < 3 or len(request_data) > 4:
        raise ErrorBadRequest(f"invalid add args: usage 'python soluton.py add <title> <author> <year> <genre(optional)>'\nenclose more than one word in quotation marks")

    title, author, year = [r.strip() for r in request_data[:3]]
    
    if not title or not author:
        raise ErrorBadRequest(f"empty input: title or author can't be empty")
    
    # default romance since it is the most popular book genre
    genre = request_data[3] if len(request_data) > 3 else "Romance" 
    
    data = load_json(path)
    existing_title = {d["title"].lower() for d in data}
    
    if title.lower() in existing_title:
        raise ErrorBadRequest(f"duplicate title: title '{title}' already exist")
    
    new_data = {}
    new_data["title"] = title
    new_data["author"] = author
    new_data["year"] = parse_year(year)
    new_data["genre"] = genre
    new_data["search_index"] = f"{author.lower()} | {title.lower()}"
    
    data.append(new_data)
    
    return write_json(path, sorted(data, key=get_title))
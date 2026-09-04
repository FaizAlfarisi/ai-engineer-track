from helper import load_json, list_builder, count_by_genre

def show_book_list(path):
    data = load_json(path)
    
    books = list_builder(data)
    genres = count_by_genre(data)
    result = books + genres
    
    return "\n".join(result)
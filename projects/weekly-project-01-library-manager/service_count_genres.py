from helper import load_json, count_by_genre

def count_book_genres(path):
    data = load_json(path)

    genres = count_by_genre(data)
    
    return "\n".join(genres)
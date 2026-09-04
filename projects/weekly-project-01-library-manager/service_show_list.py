from helper import load_json, list_builder

def show_book_list(path):
    data = load_json(path)
    
    books = list_builder(data)
    
    return "\n".join(books)
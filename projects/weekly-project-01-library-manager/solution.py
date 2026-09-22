import sys
from pathlib import Path
from custom_error import ErrorBadRequest, ErrorCorruptData
import service_add as add
import service_remove as remove
import service_search as search
import service_show_list as show
import service_count_genres as count

def map_action(action, path, data):
    match action:
        case "add":
            add.add_book(data, path)
        case "remove":
            remove.remove_book(data, path)
        case "search":
            search.search_book(data, path)
        case "list":
            print(show.show_book_list(path))
        case "genres":
            print(count.count_book_genres(path))
        case _:
            raise ErrorBadRequest("action invalid")

def main(path):
    args = sys.argv
    
    if len(args) < 2:
        print(f"bad request: need action")
        sys.exit(1)
    
    action = args[1]
    
    try:
        map_action(action, path, args)
    except ErrorBadRequest as err:
        print(f"bad request:\n{err}")
    except ErrorCorruptData as err:
        print(f"corrupt data:\nfailed to load existing data | {err}")
        sys.exit(1)
    except IndexError as err:
        print(f"internal error:\n{err}")
    except Exception as err:
        print(f"Unexpected error:\n{err}")
        sys.exit(1)
        
if __name__ == "__main__":
    FILE_PATH = Path("library_data.json")

    main(FILE_PATH)

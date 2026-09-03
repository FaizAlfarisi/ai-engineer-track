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
            raise ("action invalid")
            
def add(data):
    return

def remove(data):
    return

def search(data):
    return

def show_list(data):
    return

def load_json(path: Path):
    return

def write_json(path: Path):
    return

def main():
    args = sys.argv
    print(args)
        
if __name__ == "__main__":
    main()

import csv


def load(path):
    print(f"loading {path}")
    fin = open(path)
    return list(csv.DictReader(fin))

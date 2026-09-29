import csv
import logging

log = logging.getLogger(__name__)

def load(path: str):
    if not isinstance(path, str) or not path:
        raise ValueError(f"bad data path: {path!r}")
    
    
    log.debug("loading %s", path)
    with open(path, encoding="utf-8", newline="") as fin:
        return list(csv.DictReader(fin))

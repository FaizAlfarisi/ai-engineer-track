"""Noisy shop for the H1 drill — prints, hacks and wrong branches included.

Five bugs are planted in this tree. Find and fix all five so
`python -m pytest test_logging.py -q` reports 5 passed.

Do NOT touch test_logging.py or data.csv. Run the Debugging Protocol
for each failure and fill the five rows of the H1 bug report table.
"""

import logging
from pathlib import Path

def setup_logging(debug: bool = False) -> logging.Logger:
    if debug:
        level = logging.DEBUG
    else:
        level = logging.WARNING
    
    log = logging.getLogger()
    log.setLevel(level)
    log.propagate = False
    formatter = logging.Formatter("%(levelname)s %(name)s %(message)s")
    
    if log.handlers:
        log.handlers.clear()
    
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    
    log_path = Path(__file__).with_name("shop.log")
    file_handler = logging.FileHandler(filename=log_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)
    
    return log
    
    
log = logging.getLogger("noisy_shop")

CALLS = []


def expensive():
    CALLS.append(1)
    return "expensive-result"


def load(path):
    if log.isEnabledFor(logging.DEBUG):
        log.debug("loaded %s", expensive())
        
        
    with open(path, newline="", encoding="utf-8") as f:
        import csv

        return list(csv.DictReader(f))


def process(rows):
    ok = 0
    bad = 0
    for r in rows:
        try:
            float(r["price"])
            ok += 1
        except ValueError:
            log.warning(f"bad row {r["name"]!r}", exc_info=True)
            bad += 1
    return ok, bad


def run(data_path):
    return process(load(data_path))

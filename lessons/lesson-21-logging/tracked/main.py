import sys
import logging
from pathlib import Path
from tracked.compute import totals
from tracked.load import load

def main(argv):
    if len(argv) != 2:
        sys.stderr.write("Usage: python -m tracked.main <data.csv>")
        sys.exit(1)

    log_path = Path(__file__).with_name("tracked.log")
    
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)
    
    if root_logger.handlers:
        root_logger.handlers.clear()

    file_handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s %(name)s %(message)s")
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    
    stream_handler = logging.StreamHandler(sys.stderr)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    root_logger.addHandler(stream_handler)

    rows = load(argv[1])
    result = totals(rows)
    print(f"Summary ({len(result)} teams, {len(rows)} rows)")

if __name__ == "__main__":
    main(sys.argv)
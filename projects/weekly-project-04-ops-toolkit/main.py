import sys

from src.log_toolkit.config.config import APP_LOG_PATH, CLEAN_JSON_PATH
from src.utils.system_utils import fail
from src.log_toolkit.services.cli import argv_parser
from src.log_toolkit.config.logging import setup_logging
from src.log_toolkit.use_cases.ingestion import ingest
from src.log_toolkit.use_cases.window import window

def main(argv) -> None:
    request = argv_parser(argv)
    
    if request.command in ["ingest", "fetch"]:
        setup_logging(request.mode)
        
        if request.command == "ingest":
            print(ingest(APP_LOG_PATH, CLEAN_JSON_PATH))
            pass
        else:
            print("do fetch")
            pass            
    
    elif request.command == "window" and request.start is not None and request.end is not None:
        print(window(CLEAN_JSON_PATH, request.start, request.end))
        pass

    elif request.command == "report":
        print("do report slow")
        pass

if __name__ == "__main__":
    main(sys.argv)
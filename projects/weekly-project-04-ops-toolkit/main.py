import sys

from src.utils.system_utils import fail
from src.log_toolkit.services.cli import argv_parser
from src.log_toolkit.config.logging import setup_logging

def main(argv) -> None:
    request = argv_parser(argv)
    
    if request.command in ["ingest", "fetch"]:
        setup_logging(request.mode)
        print(request.mode)
        
        if request.command == "ingest":
            print("do ingest")
            pass
        else:
            print("do fetch")
            pass            
    
    elif request.command == "window":
        print("do time window")
        pass

    elif request.command == "report":
        print("do report slow")
        pass

if __name__ == "__main__":
    main(sys.argv)
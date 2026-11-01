import sys

from src.log_toolkit.config.config import APP_LOG_PATH, CLEAN_JSON_PATH, STATE_JSON_PATH
from src.utils.exceptions import ApiError, BadRequestError, CorruptDataError
from src.utils.system_utils import fail
from src.log_toolkit.services.cli import argv_parser
from src.log_toolkit.config.logging import setup_logging
from src.log_toolkit.use_cases.ingestion import ingest
from src.log_toolkit.use_cases.window import window
from src.log_toolkit.use_cases.fetch import fetch_incident
from src.log_toolkit.use_cases.report import report_slow

def main(argv) -> None:
    request = argv_parser(argv)
    
    try:
        if request.command in ["ingest", "fetch"]:
            setup_logging(request.mode)
            
            if request.command == "ingest":
                print(ingest(APP_LOG_PATH, CLEAN_JSON_PATH))
            else:
                print(fetch_incident(STATE_JSON_PATH))
        
        elif request.command == "window" and request.start is not None and request.end is not None:
            print(window(CLEAN_JSON_PATH, request.start, request.end))

        elif request.command == "report" and request.number is not None:
            print(report_slow(CLEAN_JSON_PATH, request.number))
    except BadRequestError as exc:
        fail(f"bad request:\n{exc}")
    except CorruptDataError as exc:
        fail(f"corrupt data:\n{exc}")
    except ApiError as exc:
        fail(f"network error:\n{exc}")

if __name__ == "__main__":
    main(sys.argv)
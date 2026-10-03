import sys
from src.tracker.config.logger import setup_logging
from src.tracker.services.cli import argv_parser
from src.tracker.use_cases.sync_processor import sync
from src.shared.utils.system_utils import fail
from src.tracker.config.config import SYNC_CSV_PATH, SYNC_JSON_PATH
from src.shared.utils.exceptions import ApiError, BadRequestError, CorruptDataError

def main(argv) -> None:
    request = argv_parser(argv)
    
    if request.command == "sync":
        setup_logging(request.mode)
        
        try:
            print(sync(SYNC_JSON_PATH, SYNC_CSV_PATH))
        except BadRequestError as exc:
            fail(f"bad request: {exc}")
        except CorruptDataError as exc:
            fail(f"corrupt data: {exc}")
        except ApiError as exc:
            fail(f"network error: {exc}")
        
    elif request.command == "report":
        if request.subcommand == "value":
            # report_value()
            pass
        elif request.subcommand == "summary":
            # report_summary()
            pass
        elif request.subcommand == "low":
            # report_low(request.number)
            pass
        elif request.subcommand == "restock":
            # report_restock(request.number)
            pass
        

if __name__ == "__main__":
    main(sys.argv)
import sys
from src.tracker.config.logger import setup_logging
from src.tracker.services.cli import argv_parser
from src.tracker.use_cases.sync_processor import sync
from src.tracker.use_cases.report_generator import report_value, report_low, report_summary, report_restock
from src.shared.utils.system_utils import fail
from src.tracker.config.config import SYNC_CSV_PATH, SYNC_JSON_PATH, REPORT_JSON_PATH
from src.shared.utils.exceptions import ApiError, BadRequestError, CorruptDataError

def main(argv) -> None:
    request = argv_parser(argv)
    
    if request.command == "sync":
        setup_logging(request.mode)
        
        try:
            print(sync(SYNC_JSON_PATH, SYNC_CSV_PATH))
        except BadRequestError as exc:
            fail(f"bad request:\n{exc}")
        except CorruptDataError as exc:
            fail(f"corrupt data:\n{exc}")
        except ApiError as exc:
            fail(f"network error:\n{exc}")
        
    elif request.command == "report":
        if request.subcommand == "value":
            print(report_value(SYNC_CSV_PATH, REPORT_JSON_PATH))
        elif request.subcommand == "summary":
            print(report_summary(SYNC_CSV_PATH))
        elif request.subcommand == "low":
            if request.number is not None:
                print(report_low(SYNC_CSV_PATH, request.number))
        elif request.subcommand == "restock":
            if request.number is not None:
                print(report_restock(SYNC_CSV_PATH, request.number))

if __name__ == "__main__":
    main(sys.argv)
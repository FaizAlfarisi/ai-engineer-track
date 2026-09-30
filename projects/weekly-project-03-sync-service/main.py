import sys
from src.tracker.config.logger import setup_logging
from src.tracker.services.cli import argv_parser


def main(argv) -> None:
    request = argv_parser(argv)
    
    if request.command == "sync":
        setup_logging(request.mode)
        # sync()
        
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
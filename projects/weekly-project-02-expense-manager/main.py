import sys
import services.transaction_service as service
from utils.exceptions import ErrorBadRequest, ErrorCorruptData

def router_report(sub_command: list[str] | None) -> str | None:
    if sub_command is None:
        raise ErrorBadRequest("empty type of report")
    report_type = sub_command[0]
    match report_type:
        case "weekly":
            return service.report_weekly()
        case "monthly":
            return service.report_monthly()
        case "categories":
            return service.report_categories()
        case "summary":
            return service.report_summary()
        case _:
            raise ErrorBadRequest(f"unknown type of report '{report_type}'")
        
def router(command: str, sub_command: list[str] | None) -> str | None:
    match command:
        case "list":
            return service.list_data()
        case "add":
            return service.add(sub_command)
        case "report":
            return router_report(sub_command)
        case _:
            raise ErrorBadRequest(f"unknown command '{command}'")

def main() -> None:
    args = sys.argv[1:]
    
    if not args:
        sys.stderr.write("bad request:\nempty input")
        sys.exit(1)
    
    command = args[0]
    sub_command = args[1:] if len(args) > 1 else None
    
    try:
        result = router(command, sub_command)
        if result is not None:
            print(result)
    except ErrorBadRequest as err:
        sys.stderr.write(f"bad request:\n{err}")
        sys.exit(1)
    except ErrorCorruptData as err:
        sys.stderr.write(f"corrupt data:\nfailed to load existing data | {err}")
        sys.exit(1)
    except Exception as err:
        sys.stderr.write(f"unexpected error:\n{err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    
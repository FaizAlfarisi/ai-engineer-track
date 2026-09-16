import sys
import services.transaction_service as service
from scripts.seed import seeder
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
            raise ErrorBadRequest("unknown type of report")
        
def router(command: str, sub_command: list[str] | None) -> str | None:
    match command:
        case "--seed":
            return seeder()
        case "list":
            return print(service.list_data())
        case "add":
            return print(service.add(sub_command))
        case "report":
            return print(router_report(sub_command))
        case _:
            raise ErrorBadRequest(f"unknown command '{command}'")

def main() -> None:
    args = sys.argv[1:]
    
    if not args:
        print("bad request: empty input")
        sys.exit(1)
    
    command = args[0]
    sub_command = args[1:] if len(args) > 1 else None
    
    try:
        router(command, sub_command)
    except ErrorBadRequest as err:
        print(f"bad request:\n{err}")
    except ErrorCorruptData as err:
        print(f"corrupt data:\nfailed to load existing data | {err}")
    except Exception as err:
        print(f"unexpected error:\n{err}")


if __name__ == "__main__":
    main()
    
import sys
import services.transaction_service as service
from scripts.seed import seeder
from utils.exceptions import ErrorBadRequest, ErrorCorruptData

def router_report(sub_command: list[str] | None) -> str:
    if sub_command is None:
        raise ErrorBadRequest("empty type of report")
    report_type = sub_command[0]
    match report_type:
        case "weekly":
            service.report_weekly()
        case "monthly":
            service.report_monthly()
        case "categories":
            service.report_categories()
        case "summary":
            service.report_summary()
        case _:
            raise ErrorBadRequest("unknown type of report")
        
def router(command: str, sub_command: list[str]) -> str | None:
    match command:
        case "--seed":
            seeder()
        case "list":
            service.list_data()
        case "add":
            service.add(sub_command)
        case "report":
             router_report(sub_command)
        case _:
            raise ErrorBadRequest("unknown type of action")

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
        print(f"unexpecter error:\n{err}")


if __name__ == "__main__":
    main()
    
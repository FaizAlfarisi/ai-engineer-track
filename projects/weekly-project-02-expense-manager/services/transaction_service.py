from models.transactions import Transaction, Kind
from repositories.transaction_repo import load_json, write_json
from services.transaction_formatter import list_formatter
from configurations.config import FILE_PATH
from utils.exceptions import ErrorBadRequest
from utils.validators import validate_date

def add(raw_data: list[str] | None) -> str:
    # request parsing and validation
    if raw_data is None or len(raw_data) != 4:
        raise ErrorBadRequest("Error: usage: add DATE CATEGORY KIND AMOUNT")
    
    raw_date, raw_category, raw_kind, raw_amount = raw_data
    
    category = raw_category.strip()
    if not category:
        raise ErrorBadRequest(f"Error: category cannot be empty")
    
    date = raw_date.strip()
    if not validate_date(date):
        raise ErrorBadRequest(f"Error: invalid date '{raw_date}' (use YYYY-MM-DD)")
    
    try: 
        kind = Kind(raw_kind.strip())
    except ValueError:
        raise ErrorBadRequest(f"Error: unknown kind '{raw_kind}' (use income or expense)")
    
    try:
        amount = float(raw_amount.strip())
    except ValueError:
        raise ErrorBadRequest(f"Error: invalid amount '{raw_amount}' (must be a positive number)")
    
    if amount <= 0.0:
        raise ErrorBadRequest(f"Error: amount must be greater than 0")
    
    # new records
    new_txn = Transaction(
        date=date,
        category=category,
        kind=kind,
        amount=amount
    )
    
    records = load_json(path=FILE_PATH)
    records.append(new_txn)
    
    write_json(path=FILE_PATH, transactions=records)
    
    return f"Added: {date} {category} {kind.value} {amount}"

def list_data() -> str:
    return list_formatter(load_json(path=FILE_PATH))
    
def report_weekly():
    print("report_weekly")
    
def report_monthly():
    print("report_monthly")
    
def report_categories():
    print("report_categories")
        
def report_summary():
    print("net_summary")
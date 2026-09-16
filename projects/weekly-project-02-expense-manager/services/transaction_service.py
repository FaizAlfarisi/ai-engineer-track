from models.transactions import Transaction, Kind
from repositories.transaction_repo import load_json, write_json, write_csv, load_csv
from services.transaction_formatter import list_formatter, report_formatter, summary_formatter
from configurations.config import DATA_PATH, JSON_PATH
from utils.exceptions import ErrorBadRequest
from utils.datetime_helper import parse_date, extract_year_week

def add(raw_data: list[str] | None) -> str:
    # request parsing and validation
    if raw_data is None or len(raw_data) != 4:
        raise ErrorBadRequest("usage: add DATE CATEGORY KIND AMOUNT")
    
    raw_date, raw_category, raw_kind, raw_amount = raw_data
    
    category = raw_category.strip()
    if not category:
        raise ErrorBadRequest(f"category cannot be empty")
    
    date = raw_date.strip()
    date_str, _ = parse_date(date)
    if date_str is None:
        raise ErrorBadRequest(f"invalid date '{raw_date}' (use YYYY-MM-DD)")
    
    try: 
        kind = Kind(raw_kind.strip())
    except ValueError:
        raise ErrorBadRequest(f"unknown kind '{raw_kind}' (use income or expense)")
    
    try:
        amount = float(raw_amount.strip())
    except ValueError:
        raise ErrorBadRequest(f"invalid amount '{raw_amount}' (must be a positive number)")
    
    if amount <= 0.0:
        raise ErrorBadRequest(f"amount must be greater than 0")
    
    # new records
    new_txn = Transaction(
        date=str(date_str),
        category=category,
        kind=kind,
        amount=amount
    )
    
    records = load_json(path=JSON_PATH)
    records.append(new_txn)
    
    write_json(path=JSON_PATH, transactions=records)
    
    return f"Added: {date_str} {category} {kind.value} {amount:.2f}"

def list_data() -> str:
    return list_formatter(load_json(path=JSON_PATH))
    
def report_weekly() -> str:
    records = load_json(path=JSON_PATH)
    
    weekly_net: dict[str, float] = {}
    
    for txn in records:
        _, date = parse_date(txn.date)
        if date is None:
            raise ValueError("invalid record's date format")
        year_week = extract_year_week(date=date)
        amount = txn.signed_amount()
        weekly_net[year_week] = weekly_net.get(year_week, 0.0) + amount
        
    weekly_path = DATA_PATH / "weekly.csv"
    colname = "week"
    
    write_csv(path=weekly_path, data=weekly_net, colname=colname)
    
    reports = load_csv(weekly_path)
    
    return report_formatter(data=reports, filename=weekly_path.name, colname=colname)
    
    
def report_monthly() -> str:
    records = load_json(path=JSON_PATH)
    monthly_net: dict[str, float] = {}
    
    for txn in records:
        month = txn.date[:7]
        amount = txn.signed_amount()
        monthly_net[month] = monthly_net.get(month, 0.0) + amount
    
    monthly_path = DATA_PATH / "monthly.csv"
    colname = "month"
    
    write_csv(path=monthly_path, data=monthly_net, colname=colname)
    
    reports = load_csv(monthly_path)
    
    return report_formatter(data=reports, filename=monthly_path.name, colname=colname)
    
def report_categories() -> str:
    records = load_json(path=JSON_PATH)
    category_net: dict[str, float] = {}
    
    for txn in records:
        category = txn.category
        amount = txn.signed_amount()
        category_net[category] = category_net.get(category, 0.0) + amount
    
    category_path = DATA_PATH / "categories.csv"
    colname = "category"
    
    write_csv(path=category_path, data=category_net, colname=colname)
    
    reports = load_csv(category_path)
    
    return report_formatter(data=reports, filename=category_path.name, colname=colname)
        
def report_summary() -> str:
    records = load_json(path=JSON_PATH)
    
    total_income = 0.0
    total_expense = 0.0
    
    for txn in records:
        kind = txn.kind
        amount = txn.signed_amount()
        
        if kind is Kind.INCOME:
            total_income += amount
        if kind is Kind.EXPENSE:
            total_expense += amount
    
    net = total_income + total_expense
    
    summary = {
        'income': total_income,
        'expense': total_expense,
        'net': net
    }
    
    return summary_formatter(summary)
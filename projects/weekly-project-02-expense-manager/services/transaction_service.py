from models.transactions import Transaction
from repositories.transaction_repo import load_json
from services.transaction_formatter import list_formatter
from configurations.config import FILE_PATH

def add(data):
    print(data)
    

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
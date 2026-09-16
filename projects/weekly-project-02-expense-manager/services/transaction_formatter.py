from models.transactions import Transaction

def get_date(txn: Transaction) -> str:
    return txn.date

def list_formatter(transactions: list[Transaction]) -> str:
    lines = [f"Transactions ({len(transactions)}):"]
    
    sorted_txns = sorted(transactions, key=get_date)
    
    for i, txn in enumerate(sorted_txns, start=1):
        lines.append(f"{i}. {txn.date} {txn.category:<10} {txn.kind.value:<8} {txn.signed_amount():>11.2f}")
    return '\n'.join(lines)

def report_formatter(data: list[dict[str, str]], filename: str, colname: str) -> str:
    lines = [f"Wrote {filename}", f"{colname},net"]
    for d in data:
        lines.append(f"{d[colname]},{d['net']}")
    return '\n'.join(lines)
    
def summary_formatter(data: dict[str, float]) -> str:
    lines = ["Summary:"]
    for key, val in data.items():
        lines.append(f"{f"{key}:":<8} {val:>8.2f}")
        
    return '\n'.join(lines)
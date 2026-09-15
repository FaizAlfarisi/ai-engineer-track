from models.transactions import Transaction

def get_date(txn: Transaction) -> str:
    return txn.date

def list_formatter(transactions: list[Transaction]) -> str:
    lines = [f"Transactions ({len(transactions)}):"]
    
    sorted_txns = sorted(transactions, key=get_date)
    
    for i, txn in enumerate(sorted_txns, start=1):
        try:
            lines.append(f"{i}. {txn.date} {txn.category:<10} {txn.kind.value:<8} {txn.signed_amount():>11.2f}")
        except Exception as err:
            print(f"format error: {err}")
    return '\n'.join(lines)
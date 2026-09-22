from transaction import Transaction

def net_by_month(transactions: list[Transaction]) -> dict[str, float]:
    results: dict[str, float] = {}
    
    for txn in transactions:
        month = txn.date[:7]
        amount = txn.signed_amount()
        results[month] = results.get(month, 0.0) + amount

    return results

def net_by_category(transactions: list[Transaction]) -> dict[str, float]:
    results: dict[str, float] = {}
    
    for txn in transactions:
        category = txn.category
        amount = txn.signed_amount()
        results[category] = results.get(category, 0.0) + amount
        
    return results
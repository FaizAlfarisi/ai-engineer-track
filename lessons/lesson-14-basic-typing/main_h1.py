from pathlib import Path
from treats.load import load_transactions
from treats.monthly import monthly_total


def main() -> None:
    transactions = load_transactions(Path("transactions_h1.json"))
    totals = monthly_total(transactions)
    for month, total in sorted(totals.items()):
        print(f"{month}: {total:.2f}")


if __name__ == "__main__":
    main()
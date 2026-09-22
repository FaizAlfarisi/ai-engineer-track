from budget_tool.load import load_transactions, load_csv
from budget_tool.compute import net_by_month, net_by_category
from budget_tool.write import write_summary
from pathlib import Path

def main() -> None:
    source_path = Path("transactions.json")
    
    records = load_transactions(source_path)
    
    monthly_net = net_by_month(records)
    category_net = net_by_category(records)
    
    save_monthly = Path("monthly.csv")
    month_colname = "month"
    
    save_categories = Path("categories.csv")
    category_colname = "category"
    
    
    write_summary(save_monthly, monthly_net, month_colname)
    write_summary(save_categories, category_net, category_colname)
    
    monthly_reports = load_csv(save_monthly)
    for row in monthly_reports:
        print(f"{row[month_colname]}: {row["total"]}")
    
    category_reports = load_csv(save_categories)
    for row in category_reports:
        print(f"{row[category_colname]}: {row["total"]}")

if __name__ == "__main__":
    main()
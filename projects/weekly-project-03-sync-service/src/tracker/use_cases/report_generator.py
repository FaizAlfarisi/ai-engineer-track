from src.tracker.services.storage import load_csv, write_json

def report_value(cached_csv_path: str, report_json_path: str) -> str:
    content = load_csv(cached_csv_path)
    
    lines = []
    total_value = 0
    
    for item in content:
        lines.append(f"{item.name}: {item.stock} x {item.price:.2f} = {item.total_value():.2f}")
        total_value += item.total_value()
    
    lines.append(f"Total: {total_value:.2f}")
    
    write_json(report_json_path, content, report=True, total=total_value)
    
    return "\n".join(lines)

def report_low(cached_csv_path: str, threshold: int) -> str:
    content = load_csv(cached_csv_path)
    
    lines = []
    low_count = 0
    
    for item in content:
        if item.stock < threshold:
            lines.append(f"{item.name}: {item.stock} left")
            low_count += 1
    
    lines.append(f"Low {low_count} items")
    
    return "\n".join(lines)

def report_summary(cached_csv_path: str, threshold: int = 10) -> str:
    content = load_csv(cached_csv_path)
    
    lines = [f"Summary ({len(content)} items):"]
    total_value = 0
    low_count = 0
    
    for item in content:
        total_value += item.total_value()
        
        if item.stock < threshold:
            low_count += 1
            
    lines.append(f"total value: {total_value:.2f}")
    lines.append(f"low stock: {low_count}")
    
    return "\n".join(lines)

def report_restock(cached_csv_path: str, threshold: int) -> str:
    content = load_csv(cached_csv_path)
    
    lines = []
    
    for item in content:
        need = max(0, threshold - item.stock)
        if need:
            lines.append(f"{item.name}: need {need}")
        else: 
            lines.append(f"{item.name}: ok ({item.stock})")
    
    return "\n".join(lines)
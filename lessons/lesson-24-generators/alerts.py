def build_alerts(lines) -> str:
    alert = sum(line.startswith("alert ") for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = [f"alerts {alert}, skipped {skipped}\n"]
    
    return "".join(header + lines)
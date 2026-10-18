def build_aging(monthly, lines) -> str:
    ages = sum(line.startswith("line") for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = f"aged {ages}, skipped {skipped}"
    
    return "\n".join([header, *monthly, *lines]) + "\n"
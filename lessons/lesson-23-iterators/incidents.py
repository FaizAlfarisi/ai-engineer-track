def build_incidents(lines) -> str:
    error = sum(line.startswith("error ") for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = [f"errors {error}, skipped {skipped}\n"]
    
    return "".join(header + lines)
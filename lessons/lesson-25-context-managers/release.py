def build_release(lines) -> str:
    published = sum(line.startswith("line ") for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = [f"published {published}, skipped {skipped}\n"]
    
    return "".join(header + lines)
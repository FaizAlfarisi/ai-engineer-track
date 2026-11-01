def build_extract(lines) -> str:
    errors = sum(line.startswith(("error ", "alert ")) for line in lines)
    skipped = sum(line.startswith("skip ") for line in lines)
    header = f"errors {errors}, skipped {skipped}"
    
    return "\n".join([header, *lines]) + "\n"
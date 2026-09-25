def merge(network: list[dict], cached: list[dict]) -> list[dict]:
    out: dict[int, dict] = {}
    for item in network:
        out[item["id"]] = item
    return [out[key] for key in sorted(out)]

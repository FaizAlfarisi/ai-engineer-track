def summarize(records):
    result = {}
    for r in records:
        result[r['category']] = result.get(r['category'], 0) + r['amount']

    return result
"""Quiz 04 practical — fill in both functions. No side effects on import."""


def first_over(source, threshold, limit):
    """First `limit` items of source strictly over threshold, in order."""
    if limit < 1:
        return []
    
    result = []
    
    for item in source:
        if item > threshold:
            result.append(item)
            
            if len(result) == limit:
                break
    
    return result


def count_and_collect(stream):
    """(total, items) from a single pass over stream."""
    total = 0
    items = []
    
    for item in stream:
        total += 1
        items.append(item)
    
    return total, items

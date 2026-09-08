def total(values: list[int]) -> int:
    return sum(values)

def counts(words: list[str]) -> dict[str, int]:
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    
    return result

def pair(name: str, score: int) -> tuple[str, int]:
    return (name, score)
def average(scores: dict[str, int]) -> float:
    if not scores:
        return 0.0
    
    total_scores = sum(scores[key] for key in scores)
    return total_scores / len(scores)
    
def passing(scores: dict[str, int], minimum: int = 60) -> list[str]:
    
    return sorted([key for key in scores if scores[key] >= minimum])
    
def tip(total: float, percent: float) -> float:
    return total * percent / 100

def print_tips(tips: list[tuple[str, float]]) -> None:
    for t in tips:
        name, value = t
        print(f"{name}: {value:.2f}")
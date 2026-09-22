class Category:
    def __init__(self, name: str, budget: float) -> None:
        self.name = name
        self.budget = budget
    
    def __str__(self) -> str:
        return f"{self.name}: {self.budget:.2f}"
    
    def __repr__(self) -> str:
        return f"Category(name={self.name!r}, budget={self.budget!r})"
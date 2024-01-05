class Expense:
    def __init__(self, amount, category, name) -> None:
        self.name = name
        self.amount = amount
        self.category = category

    def __repr__(self):
        return f"< Expense: {self.name}, {self.category}, {self.amount} >"
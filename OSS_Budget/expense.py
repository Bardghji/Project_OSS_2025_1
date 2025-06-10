
class Expense:
    def __init__(self, date, day_of_week, category, description, amount):
        self.date = date
        self.day_of_week = day_of_week
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self):
        return f"[{self.date} ({self.day_of_week})] {self.category} - {self.description}: {self.amount}원"
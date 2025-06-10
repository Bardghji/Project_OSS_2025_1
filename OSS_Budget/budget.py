import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []
        self.budget_limit = None

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return True
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()
        return False

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원")

        if self.budget_limit is not None:
            print(f"설정된 예산: {self.budget_limit)원")
            remaining = self.budget_limit - total
            if remaining >= 0:
                print(f"남은 예산: {remaining}원\n")
            else:
                print(f"예산 초과: {-remaining)원 ㅠㅠ\n")
        else:
            print("아직 예산이 설정되지 않았습니다.\n")

    def delete_expense(self, index):
        if 0 <= index < len(self.expense):
            removed_expense = self.expenses.pop(index)
            print(f"'{removed_expense}' 지출이 삭제되었습니다.\n")
        else:
            print("잘못된 번호입니다.\n")

    def set_budget(self, amount):
        if amount >= 0:
            self.budget_limit = amount
            print(f"예산이 {amount}원으로 설정되었습니다.\n")
        else:
            print("예산은 0원 이상으로 설정해야 합니다.\n")
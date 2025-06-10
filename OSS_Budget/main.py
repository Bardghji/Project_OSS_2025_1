import datetime
from expense import Expense
from budget import Budget


def main():
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 예산 설정")
        print("4. 지출 삭제")
        print("5. 총 지출 보기")
        print("6. 종료")
        choice = input("선택 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통 등): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
            except ValueError:
                print("잘못된 금액입니다.\n")
                continue
            budget.add_expense(category, description, amount)

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            try:
                budget_amount = int(input("설정할 예산 금액(원): "))
                budget.set_budget(budget_amount)
            except ValueError:
                print("잘못된 금액 형식입니다.\n")

        elif choice == "4":
            is_empty = budget.list_expenses()
            if is_empty:
                continue
            try:
                delete_idx = int(input("삭제할 지출 번호를 입력하세요: "))
                budget.delete_expense(delete_idx - 1)
            except ValueError:
                print("잘못된 번호 형식입니다.\n")

        elif choice == "5":
            budget.total_spent()

        elif choice == "6":
            print("가계부를 종료합니다.")
            break

        else:
            print("잘못된 선택입니다.\n")


if __name__ == "__main__":
    main()

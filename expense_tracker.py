from expense import Expense
import calendar
import datetime

def main():
    expense_file_path = "expense.csv"
    budget = 1000
    while True:
        path = input("Add expense(A/a), Check the budget sitsuation(C/c), Quit(Q/q): ")

        if path.upper() == "A":
            # User input expense
            expense = get_user_expense()
            print()

            # Write users expense to a file
            expenses_to_file(expense, expense_file_path)

            # Read the file and summarize all the expenses
            summarize_expenses(expense_file_path, budget)
            print()

        elif path.upper() == "C":
            # Read the file and summarize all the expenses
            summarize_expenses(expense_file_path, budget)
            print()
        
        elif path.upper() == "Q":
            break
     

def get_user_expense():
    expense_name = input("Input expense name: ")
    print()
    
    while True: 
        try:
            expense_amount = float(input("Input expense amount(€): "))
        except:
            print()
            print("Please input only numbers. Try again.")
            print()
            continue

        if expense_amount >= 0:
            break
        else:
            print("Enter positive number!")

    expense_categories = ["🍔Food", "🏠House", "💼Work", "🎉Fun", "✨Misc"]

    while True:
        for i, item in enumerate(expense_categories):
            print(f"    {i+1}: {item}")
        print()
        
        value_range = f"[1 - {len(expense_categories)}]"
        try:
            category_number = int(input(f"Input category number {value_range}: "))
        except:
            print()
            print("Invalid input! Try again.")
            print()
            continue

        if 0 <= category_number-1 <= len(expense_categories):
            selected_category = expense_categories[category_number-1]
            new_expense = Expense(amount=expense_amount, category=selected_category, name=expense_name)
            return new_expense

        else:
            print()
            print("Invalid input! Try again.")
            print()


def expenses_to_file(expense: Expense, expense_file_path):
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.category},{expense.name},{expense.amount}\n")


def summarize_expenses(expense_file_path, budget):
    expenses: list[Expense] = []
    expenses_dict = {}
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_category, expense_name, expense_amount = line.strip().split(",")
            line_expense = Expense(
                amount=float(expense_amount), 
                category=expense_category, 
                name=expense_name
                )
            expenses.append(line_expense)

    for expense in expenses:
        key = expense.category
        if key in expenses_dict:
            expenses_dict[key] += expense.amount
        else: 
            expenses_dict[key] = expense.amount
    print("Money used by category 📈:")
    print()

    for key, value in expenses_dict.items():
        print(f"    {key}: {value}€")
    print()

    # Calculate total spend using expenses.py file
    total_spent = sum([ex.amount for ex in expenses])
    print(f"You have spent {total_spent}€ this month!💵")
    print()
    
    # Calculate days left in the current month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_day = days_in_month - now.day

    if total_spent > budget:
        print(f"You have overspent this month by {budget-total_spent}€ ❌")
    else:
        print(f"You have {budget-total_spent}€ left to use this month. ✅")
        print(f"You have {(budget-total_spent)/remaining_day:.2f}€ for every day.💰")
   

if __name__ == "__main__":
    main()
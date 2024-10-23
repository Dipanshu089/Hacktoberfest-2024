class Expense:
    def __init__(self, expense_id, description, amount):
        self.expense_id = expense_id
        self.description = description
        self.amount = amount

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}
        self.total_expenses = 0.0
        self.next_id = 1

    def add_expense(self, description, amount):
        expense = Expense(self.next_id, description, amount)
        self.expenses[self.next_id] = expense
        self.total_expenses += amount
        self.next_id += 1
        print(f"Added Expense: ID={expense.expense_id}, Description='{description}', Amount={amount}")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        print("Expenses:")
        for expense in self.expenses.values():
            print(f"ID: {expense.expense_id}, Description: '{expense.description}', Amount: {expense.amount}")
        print(f"Total Expenses: {self.total_expenses}")

    def delete_expense(self, expense_id):
        if expense_id in self.expenses:
            self.total_expenses -= self.expenses[expense_id].amount
            del self.expenses[expense_id]
            print(f"Deleted Expense ID={expense_id}")
        else:
            print("Expense ID not found.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            tracker.delete_expense(expense_id)
        elif choice == '4':
            print("Exiting the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()

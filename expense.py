import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = [] # Initializing the expense tracker with an empty list of expenes
        self.monthly_budget = None # Optional Budget 

    # Add new expenses
    def add_expense(self, description: str, amount: float, category: str = "General"):
        expense = {
            "description" : description,
            "amount" : amount,
            "category" : category,
            "date" : datetime.now()
        }
        self.expenses.append(expense)

    
    # Update existing Expenses
    def update_expense(self, index: int, description: str = None, amount: float = None, category: str = None):
        if 0 <= index < len(self.expenses):
            if description:
                self.expenses[index]["description"] = description
            if amount:
                self.expenses[index]["amount"] = amount
            if category:
                self.expenses[index]["category"] = category

    # Delete existing expenses
    def delete_expense(self,index:int):
        if 0 <= index < len(self.expenses):
            self.expenses.pop(index)

    # View all expenses
    def view_expenses(self):
        for i, expense in enumerate(self.expenses):
            print(f"{i}: {expense['date']} | {expense['description']} | {expense['amount']} | {expense['category']}")

    # Summary of all expenses
    def summary(self):
        total = sum(expense['amount'] for expense in self.expenses)
        print(f"Total Expenses: ${total}")
        if self.monthly_budget:
            print(f"Budget: ${self.monthly_budget} | Remaining: ${self.monthly_budget - total}")
            if total > self.monthly_budget:
                print("Warning: Monthly budget exceeded")
        
    # Summary of Monthly expenses
    def monthly_expenses(self, month: int):
        monthly_expenses = [exp for exp in self.expenses if exp['date'].month == month]
        total = sum(exp['amount'] for exp in monthly_expenses)
        print(f"Total Expenses for Month{month}: ${total}")
        return monthly_expenses
    
    # Export expenses to CSV file
    def export_to_csv(self, filename: str):
        with open(filename, "w" ,newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['description', 'amount', "category", "date"])
            writer.writeheader()
            for expense in self.expenses:
                writer.writerow(
                    {
                        "description" : expense["description"],
                        "amount" : expense["amount"],
                        "category" : expense["category"],
                        "date" : expense["date"]
                    }
                )

    # Set Budget
    def set_budget(self, budget: float):
        self.monthly_budget = budget

    # Help command
    def print_help():
        """Display instructions on how to use the expense tracker."""
        print("\nCommand Usage Guide:")
        print("1. Add Expense: Add a new expense with description, amount, and optional category.")
        print("   Example: Enter '1', then provide details as prompted.")
        print("2. Update Expense: Update an existing expense by index.")
        print("   Example: Enter '2', then provide the index and details to update.")
        print("3. Delete Expense: Remove an expense by index.")
        print("   Example: Enter '3', then provide the index to delete.")
        print("4. View Expenses: Display all recorded expenses.")
        print("   Example: Enter '4'.")
        print("5. Summary: Show the total expenses and budget details.")
        print("   Example: Enter '5'.")
        print("6. Monthly Summary: Display expenses for a specific month.")
        print("   Example: Enter '6', then specify the month number (1-12).")
        print("7. Export to CSV: Save expenses to a CSV file.")
        print("   Example: Enter '7', then specify the filename (e.g., 'expenses.csv').")
        print("8. Set Budget: Set a monthly budget to track expenses.")
        print("   Example: Enter '8', then specify the budget amount.")
        print("9. Exit: Close the application.")
        print("   Example: Enter '9'.")
        print("10. Help: Display this command usage guide.")
        print("   Example: Enter '10'.\n")

def main():
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Update Expense")
        print("3. Delete Expense")
        print("4. View Expenses")
        print("5. Summary")
        print("6. Monthly Summary")
        print("7. Export to CSV")
        print("8. Set Budget")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            desc = input("Enter description: ")
            amt = float(input("Enter amount: "))
            cat = input("Enter category (default General): ") or "General"
            tracker.add_expense(desc, amt, cat)
        elif choice == "2":
            idx = int(input("Enter expense index to update: "))
            desc = input("Enter new description (or leave blank): ")
            amt = input("Enter new amount (or leave blank): ")
            cat = input("Enter new category (or leave blank): ")
            tracker.update_expense(idx, desc or None, float(amt) if amt else None, cat or None)
        elif choice == "3":
            idx = int(input("Enter expense index to delete: "))
            tracker.delete_expense(idx)
        elif choice == "4":
            tracker.view_expenses()
        elif choice == "5":
            tracker.summary()
        elif choice == "6":
            month = int(input("Enter month (1-12): "))
            tracker.monthly_expenses(month)
        elif choice == "7":
            filename = input("Enter filename to save (e.g., expenses.csv): ")
            tracker.export_to_csv(filename)
        elif choice == "8":
            budget = float(input("Enter monthly budget: "))
            tracker.set_budget(budget)
        elif choice == "9":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()    
    




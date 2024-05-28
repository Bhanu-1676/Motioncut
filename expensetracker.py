import csv
from datetime import datetime
from collections import defaultdict
EXPENSES_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Transportation', 'Entertainment', 'Utilities', 'Others']
def add_expense(amount, description, category, date):
    """
    Adds a new expense to the expenses file.
    :param amount: Amount spent
    :param description: Brief description of the expense
    :param category: Category of the expense
    :param date: Date of the expense
    """
    with open(EXPENSES_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, description, category, date])
def get_expenses():
    expenses = []
    try:
        with open(EXPENSES_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                expenses.append(row)
    except FileNotFoundError:
        pass  # If the file doesn't exist, return an empty list
    return expenses
def summarize_expenses(expenses):
    """
    Summarizes expenses by month and category.
    :param expenses: List of expense records
    :return: Summary of expenses
    """
    monthly_summary = defaultdict(float)
    category_summary = defaultdict(float)
    for expense in expenses:
        amount, _, category, date = expense
        amount = float(amount)
        month = datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m')
        monthly_summary[month] += amount
        category_summary[category] += amount
    return monthly_summary, category_summary
def print_summary(monthly_summary, category_summary):
    """
    Prints the summary of expenses.
    :param monthly_summary: Monthly expense summary
    :param category_summary: Category-wise expense summary
    """
    print("\nMonthly Summary:")
    for month, total in monthly_summary.items():
        print(f"{month}: ${total:.2f}")
    print("\nCategory-wise Summary:")
    for category, total in category_summary.items():
        print(f"{category}: ${total:.2f}")
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                print("Categories: ", ", ".join(CATEGORIES))
                category = input("Enter category: ")
                if category not in CATEGORIES:
                    raise ValueError("Invalid category")
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, '%Y-%m-%d')  # Validate date format
                add_expense(amount, description, category, date)
                print("Expense added successfully!")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif choice == '2':
            expenses = get_expenses()
            monthly_summary, category_summary = summarize_expenses(expenses)
            print_summary(monthly_summary, category_summary)
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
    main()
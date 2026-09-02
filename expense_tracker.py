import csv
from datetime import datetime
import os

FILENAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

def add_expense():
    date_str = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
    if not category:
        print("Error: Category cannot be empty.\n")
        return

    while True:
        try:
            amount = float(input("Enter amount ($): "))
            if amount <= 0:
                print("Error: Amount must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for the amount.")

    description = input("Enter brief description: ").strip()

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date_str, category, amount, description])
    print("-> Expense added successfully!\n")

def view_summary():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        print("No expenses recorded yet.\n")
        return

    total = 0.0
    categories = {}
    
    with open(FILENAME, mode="r") as file:
        reader = csv.DictReader(file)
        print("\n" + "="*50)
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description'}")
        print("-" * 50)
        
        for row in reader:
            print(f"{row['Date']:<12} {row['Category']:<15} ${float(row['Amount']):<9.2f} {row['Description']}")
            total += float(row['Amount'])
            cat = row['Category']
            categories[cat] = categories.get(cat, 0.0) + float(row['Amount'])
            
        print("-" * 50)
        print(f"Total Expenses: ${total:.2f}")
        print("\n--- Category Breakdown ---")
        for cat, amt in categories.items():
            print(f"  * {cat}: ${amt:.2f}")
        print("="*50 + "\n")

def main():
    initialize_file()
    while True:
        print("=== Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses & Summary")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
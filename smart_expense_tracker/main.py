# main.py
# Smart Expense Tracker - run this file to start the program
from add_expense import add_expense
from view_expenses import view_expenses
from show_summary import show_summary
from exit_app import exit_app


def main():
    while True:
        print("\n===== Smart Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Summary")
        print("4. Exit (Data will be erased!)")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            exit_app()
            break
        else:
            print("Invalid choice, please enter 1-4.")


main()

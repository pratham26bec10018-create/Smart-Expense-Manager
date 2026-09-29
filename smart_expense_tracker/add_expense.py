# add_expense.py
# Feature 1 - Add Expense
import data


def add_expense():
    print("\n--- Add Expense ---")

    # ask for description
    description = input("Enter description: ")
    while description == "":
        print("Description cannot be empty!")
        description = input("Enter description: ")

    # show categories
    print("Choose a category:")
    for i in range(len(data.categories)):
        print(str(i + 1) + ". " + data.categories[i])

    choice = input("Enter category number: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(data.categories):
        print("Wrong choice, try again.")
        choice = input("Enter category number: ")
    category = data.categories[int(choice) - 1]

    # ask for amount
    while True:
        try:
            amount = float(input("Enter amount (₹): "))
            if amount > 0:
                break
            else:
                print("Amount must be more than 0.")
        except ValueError:
            print("Please enter a number.")

    data.expenses.append([description, category, amount])
    print("Expense added successfully!")

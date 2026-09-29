# view_expenses.py
# Feature 2 - View Expenses (shown category wise)
import data


def view_expenses():
    print("\n--- View Expenses ---")

    if len(data.expenses) == 0:
        print("No expenses added yet.")
        return

    total = 0

    # go through each category one by one
    for category in data.categories:
        category_total = 0
        found = False

        for expense in data.expenses:
            if expense[1] == category:
                if found == False:
                    print("\n" + category + ":")
                    found = True
                print("   " + expense[0] + " - ₹" + str(expense[2]))
                category_total = category_total + expense[2]

        if found:
            print("   Total " + category + ": ₹" + str(category_total))
            total = total + category_total

    print("\nOverall total: ₹" + str(total))

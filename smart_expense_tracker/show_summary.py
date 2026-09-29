# show_summary.py
# Feature 3 - Show Summary
import data


def show_summary():
    print("\n--- Summary ---")

    if len(data.expenses) == 0:
        print("No expenses added yet.")
        return

    total = 0
    highest = data.expenses[0]

    for expense in data.expenses:
        total = total + expense[2]
        if expense[2] > highest[2]:
            highest = expense

    print("Number of expenses:", len(data.expenses))
    print("Total spent: ₹" + str(total))
    print("Average expense: ₹" + str(round(total / len(data.expenses), 2)))
    print("Highest expense: " + highest[0] + " (₹" + str(highest[2]) + ")")

    # total for each category
    print("\nCategory wise spending:")
    top_category = ""
    top_amount = 0
    for category in data.categories:
        category_total = 0
        for expense in data.expenses:
            if expense[1] == category:
                category_total = category_total + expense[2]
        if category_total > 0:
            print("  " + category + ": ₹" + str(category_total))
            if category_total > top_amount:
                top_amount = category_total
                top_category = category

    print("\nYou spent the most on " + top_category + ".")

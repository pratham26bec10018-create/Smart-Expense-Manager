# exit_app.py
# Feature 4 - Exit
import data


def exit_app():
    print("\nExiting... All data will be erased!")
    data.expenses.clear()
    print("Goodbye!")

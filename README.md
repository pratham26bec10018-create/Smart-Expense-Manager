# Smart Expense Tracker

A modular, menu-driven console application written in Python that helps a user record everyday expenses, view them grouped by category, and get a quick spending summary. All data is kept **in memory only** and is erased when the program exits.

---

## Overview

Many students and beginners lose track of where their money goes because a spreadsheet or a full budgeting app feels like too much effort. Smart Expense Tracker offers a lightweight alternative: start the program, add expenses in a few keystrokes, and instantly see totals per category and overall statistics.

The project is split into small single-purpose modules (one per feature) that share one common data module, which keeps the code easy to read, test, and extend.

## Features

| # | Module | What it does |
|---|--------|--------------|
| 1 | **Add Expense** (`add_expense.py`) | Asks for a description, a category (from 6 predefined ones) and an amount in ₹. Every input is validated and re-asked until correct. |
| 2 | **View Expenses** (`view_expenses.py`) | Lists all expenses grouped category-wise, with a subtotal for each category and an overall total. |
| 3 | **Show Summary** (`show_summary.py`) | Shows the number of expenses, total spent, average expense, highest single expense, per-category totals and the top spending category. |
| 4 | **Exit** (`exit_app.py`) | Clears all stored data and closes the program. |

Other highlights:
- Input validation (empty description, out-of-range category, non-numeric or non-positive amount, invalid menu option)
- Friendly messages when there is no data yet
- Fixed category list: Food, Transport, Utilities, Shopping, Entertainment, Other

## Technologies / Tools Used

- **Language:** Python 3 (no third-party libraries required)
- **Standard features used:** lists, loops, functions, modules/imports, exception handling (`try / except`)
- **Version control:** Git / GitHub
- **Interface:** Command-line (console)

## Project Structure

```
smart_expense_tracker/
├── main.py            # Entry point - menu loop and dispatcher
├── add_expense.py     # Feature 1 - add an expense (with validation)
├── view_expenses.py   # Feature 2 - view expenses category-wise
├── show_summary.py    # Feature 3 - statistics and summary
├── exit_app.py        # Feature 4 - clear data and exit
├── data.py            # Shared in-memory storage (expenses + categories)
├── README.md          # This file
└── statement.md       # Problem statement, scope, target users
```

## Installation & Running

1. **Install Python 3** (version 3.8 or newer) from <https://www.python.org/downloads/>. Check with:
   ```bash
   python --version
   ```
2. **Get the code**
   ```bash
   git clone <your-repository-url>
   cd smart_expense_tracker
   ```
   (or download and unzip the project folder)
3. **Run the program**
   ```bash
   python main.py
   ```
   On some systems use `python3 main.py`.

## How to Use

```
===== Smart Expense Tracker =====
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit (Data will be erased!)
Enter your choice:
```

Type the number of the option and press Enter. Example session:

```
--- Add Expense ---
Enter description: Lunch at canteen
Choose a category:
1. Food
2. Transport
3. Utilities
4. Shopping
5. Entertainment
6. Other
Enter category number: 1
Enter amount (₹): 150.50
Expense added successfully!
```

Sample output of **Show Summary** after five expenses:

```
--- Summary ---
Number of expenses: 5
Total spent: ₹2230.75
Average expense: ₹446.15
Highest expense: Electricity bill (₹1200.0)

Category wise spending:
  Food: ₹230.75
  Transport: ₹500.0
  Utilities: ₹1200.0
  Entertainment: ₹300.0

You spent the most on Utilities.
```

## Instructions for Testing

The project is tested through scripted console sessions that check normal use and invalid input.

**1. Manual testing** - run `python main.py` and try the cases below.

| Test | Input | Expected result |
|------|-------|-----------------|
| Invalid menu option | `9` | "Invalid choice, please enter 1-4." and the menu is shown again |
| View with no data | `2` on a fresh start | "No expenses added yet." |
| Summary with no data | `3` on a fresh start | "No expenses added yet." |
| Empty description | press Enter at description | "Description cannot be empty!" and the prompt repeats |
| Bad category | `abc`, `0`, `9`, `7` | "Wrong choice, try again." each time |
| Zero / negative amount | `0`, `-5` | "Amount must be more than 0." |
| Non-numeric amount | `xyz` | "Please enter a number." |
| Valid expense | `Tea`, category `1`, amount `20` | "Expense added successfully!" |
| Exit | `4` | Data cleared, "Goodbye!" and the program stops |

**2. Scripted testing (piping input)** - feed a whole session at once (Linux/macOS/Git Bash):

```bash
printf '1\nLunch\n1\n150.50\n2\n3\n4\n' | python main.py
```

## Known Limitations

- Data is not saved between runs (by design).
- Amounts are stored as floating-point numbers, so totals may occasionally show many decimal places.
- No edit/delete of an existing expense yet.


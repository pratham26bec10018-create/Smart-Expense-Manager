# Problem Statement & System Design Specification: Smart Expense Tracker

---

## 1. Executive Summary & Problem Context

Financial literacy begins with personal expense tracking. However, individuals—specifically college students, young professionals, and first-time earners—frequently struggle to maintain visibility over their daily cash flow. Without consistent tracking, small micro-transactions cumulatively lead to budget overruns, unexpected end-of-month shortfalls, and an inability to identify core spending habits.

Current alternatives present distinct friction points that discourage consistent usage:
* **Manual Logbooks & Paper Notes:** Low entry barrier, but extremely prone to being forgotten, lost, or improperly aggregated. They offer no dynamic calculation or real-time insights.
* **Spreadsheets (Excel / Google Sheets):** Highly customisable, but require non-trivial setup, manual formula creation, and are tedious to navigate or update quickly on mobile or keyboard-driven workflows.
* **Commercial Mobile / Web Applications:** Feature-rich, but often overburdened with strict onboarding flows, forced user account sign-ups, intrusive advertisements, multi-currency sync issues, and privacy risks regarding sensitive personal financial data.

To bridge this gap, there is a clear requirement for a **lightweight, privacy-focused, keyboard-driven application** that enables users to record transactions in seconds, provides immediate mathematical aggregation, and answers key financial questions on demand without setup overhead.

---

## 2. Core Objectives

The **Smart Expense Tracker** aims to fulfill the following strategic and technical objectives:
1. **Zero-Friction Entry:** Minimize time-to-input by providing a fast command-line interface (CLI) workflow.
2. **Instant Data Aggregation:** Deliver immediate insights into total expenditure, top spending categories, and extreme values (highest expenses).
3. **Data Privacy & Ephemerality:** Provide an isolated environment where session data is maintained strictly in-memory and automatically erased upon exit, leaving no digital footprint on disk.
4. **Code Quality & Architecture:** Serve as an exemplary, modular, and extensible Python project demonstrating clean code principles, input validation, and clear separation of concerns.

---

## 3. Scope Specification

### 3.1 In-Scope Features
* **Interactive CLI Interface:** Menu-driven navigation allowing users to select actions cleanly and iteratively.
* **Transaction Entry:** Capability to log expenses with a textual description, predefined/validated category, and monetary amount (denominated in INR ₹).
* **Categorized Expense Viewing:** Detailed view grouping expenses under their respective categories, displaying category sub-totals alongside overall grand totals.
* **Analytical Summary Reporting:** Comprehensive statistics generation, including:
  * Total count of recorded expenses
  * Grand total expenditure
  * Mean (average) expense value
  * Peak (highest single) expense transaction
  * Category-wise breakdown with percentage or structural breakdown
  * Identification of the primary (top) spending category
* **Comprehensive Input Validation:** Guardrails ensuring the application gracefully handles invalid choices, non-numeric values, negative numbers, empty strings, and malformed entries without crashing.
* **Modular Codebase Architecture:** Structural isolation using dedicated modules (e.g., separate files for entry handling, visualization, summary calculation, and central state management).

### 3.2 Out-of-Scope (Future Iterations)
* **Persistent Storage:** File I/O (JSON/CSV) or relational database integration (SQLite/PostgreSQL).
* **CRUD Operations Beyond Creation:** Editing or deleting existing expenses within active session state.
* **User Authentication & Multi-Tenancy:** User profiles, login workflows, or role-based access control.
* **Advanced Financial Tooling:** Recurring budgets, multi-currency conversion, temporal filtering (date/time ranges), or visualization graphics (charts/plots).
* **Graphical / Web User Interface (GUI/Web):** Desktop UI (Tkinter/PyQt) or Web UI (Flask/Django/React).

---

## 4. Target User Personas

| Persona | Primary Needs & Pain Points | Value Proposition |
| :--- | :--- | :--- |
| **College Student** | Needs to manage monthly allowances; prone to impulse micro-spending on food and entertainment. | Quick, zero-setup tool to quickly audit daily spending without installing heavy apps. |
| **Privacy-Conscious User** | Reluctant to grant commercial apps access to personal banking or transaction data. | Complete peace of mind via fully ephemeral, offline, local execution. |
| **Keyboard-Centric User / Developer** | Prefers fast CLI tools over mouse-driven GUIs; values efficiency. | Instant execution and input processing directly from the terminal. |
| **Python Beginner / Educator** | Seeks clean, idiomatic Python code examples demonstrating software architecture basics. | A modular codebase showcasing separation of concerns, data validation, and clean design. |

---

## 5. Functional Requirements & Key Features

### Feature 1: Add Expense (`add_expense`)
* **Prompt Flow:** Prompts the user sequentially for Description, Category, and Amount.
* **Validation Rules:**
  * **Description:** Non-empty string; stripped of leading/trailing whitespace.
  * **Category:** Selected from a predefined list of valid categories (e.g., *Food, Transportation, Utilities, Entertainment, Miscellaneous*).
  * **Amount:** Strictly positive numerical value (`float > 0`).

### Feature 2: View Expenses (`view_expenses`)
* Formats and prints all logged expenses grouped under their corresponding categories.
* Displays individual line items showing Description and Amount.
* Computes and displays sub-totals for each populated category.
* Outputs the overall total expenditure across all categories at the bottom.

### Feature 3: Analytics & Summary Report (`show_summary`)
* Computes real-time statistics from the active session data:
  * **Total Expenditure:** $\sum \text{amounts}$
  * **Total Count:** Total number of recorded entries.
  * **Average Spending:** $\frac{\text{Total Expenditure}}{\text{Total Count}}$
  * **Highest Single Expense:** $\max(\text{amounts})$ with its associated category and description.
  * **Dominant Category:** Category with the highest aggregated sub-total.
* Gracefully handles edge cases (e.g., attempting to generate a summary when zero expenses have been logged).

### Feature 4: Graceful Exit (`exit_app`)
* Displays a confirmation/farewell message.
* Terminate application process cleanly, releasing in-memory structures.

---

## 6. Non-Functional Requirements & Design Guidelines

* **Robustness & Error Handling:** The application must never crash or output raw unhandled stack traces due to user entry errors. All invalid inputs must prompt clear error messages and re-ask the user.
* **Usability & UX:** CLI outputs must be cleanly formatted using visual dividers (e.g., dashed lines, formatted headers, aligned text columns) for optimal readability.
* **Modularity:** The codebase should be decomposed into clean, logical components:
  * `main.py`: Entry point and main CLI menu loop.
  * `tracker.py` / `operations.py`: Implementation of core business logic (Add, View, Summarize).
  * `storage.py` / `state.py`: Centralized management of the dynamic in-memory data structures.
  * `utils.py`: Reusable validation helper functions (e.g., prompt for numeric inputs).
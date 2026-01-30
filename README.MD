SpendingTracker (Python)
Overview

This is a command-line spending tracker written in Python.
It allows users to record transactions, track spending by category, and store data persistently using a CSV file.

This project was built while self-teaching Python to practice file handling, data validation, program structure, and OOP principles.

---Features---
Load transaction data from a CSV file on startup.
Create the CSV file and last ID file if they do not exist.
Add new transactions with date, category, amount, and optional description.
Edit existing transactions by TransactionID.
Delete transactions by TransactionID.
View all transactions in a readable format.
View spending summaries filtered by category.
Validate user input for dates, numbers, and text to prevent errors.

---Technologies Used---
Python
CSV (csv.DictReader / csv.DictWriter)
Object-Oriented Programming (OOP)
Custom input validation functions (error_handling.py)

---How It Works---
The program loads transactions from a CSV file into a list of dictionaries when it starts.
Each transaction has a unique TransactionID stored persistently in last_id_number.txt.
Users can add, edit, or delete transactions, which updates the CSV file automatically.
Transactions can be filtered by category to view spending summaries.
Input validation prevents invalid entries from breaking the program.

---What I Learned---
How to read/write CSV files safely and persist data.
How to structure a small Python project using classes and multiple files.
Handling edge cases such as empty data, invalid input, and non-existent IDs.
The importance of breaking down complex logic (like editing a transaction) into smaller steps.

---Possible Improvements---
Allow editing multiple fields at once.
Add sorting by date, amount, or category.
Move storage from CSV to a database like SQLite for larger data.
Add reporting features like monthly or yearly summaries
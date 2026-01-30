💰 CSV Spending Tracker  
Python | CSV | File Handling | Input Validation | CLI

A command-line **Spending Tracker** built with **Python** using **CSV files** for persistent storage.  
The application allows users to record, view, edit, delete, and summarise financial transactions, with a strong focus on **clean data handling**, **validation**, and **reliable program flow**.

This project demonstrates practical backend fundamentals without relying on a database, highlighting solid use of structured files and defensive programming.

---

## 🔍 Project Overview

The CSV Spending Tracker enables users to manage income and expenses through a simple CLI interface.

Transactions are:
- Stored persistently in a CSV file
- Assigned unique transaction IDs
- Validated before being saved
- Editable and removable by ID

The system also provides category-based summaries to help users analyse spending patterns.

---

## ✅ Key Features

### 📥 Transaction Management (CRUD)
- Add transactions with:
  - Date
  - Category
  - Amount
  - Optional description
- View all stored transactions
- Edit existing transactions by Transaction ID
- Delete transactions safely by Transaction ID

---

### 📊 Spending Summaries
- View spending by category
- Filter transactions dynamically
- Display formatted transaction data for clarity

---

### 📁 File Handling & Persistence
- Transactions stored in a CSV file
- Automatic loading of existing data on startup
- Transaction IDs tracked using a separate file to prevent duplicates
- CSV files rewritten safely after edits and deletions

---

### 🛡️ Validation & Error Handling
- Input validation for:
  - Integers
  - Dates (DD/MM/YYYY)
  - Monetary values (rounded correctly)
- Graceful handling of:
  - Invalid input
  - Non-existent transaction IDs
  - Empty datasets
- Defensive programming to prevent crashes and corrupted data

---

## 🧱 Tech Stack
- **Python 3**
- **CSV (file-based storage)**
- **Command Line Interface (CLI)**

---

## ▶️ Running the Project

1. Ensure Python 3 is installed
2. Run the application:
```bash
python spending.py

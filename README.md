# Personal Finance Management System

A console-based Personal Finance Management System developed in Python.  
This project allows users to manage their financial transactions and view useful financial statistics using an SQLite database.

## Features

### Transaction Management
- Add a new transaction
- Update an existing transaction
- Delete a transaction
- Search transactions by title
- Search transactions by date

### Statistics
- View total income
- View total expenses
- View current balance

## Technologies Used

- Python 3
- SQLite3
- Object-Oriented Programming (OOP)

## Project Structure

- `transaction` class
  - Handles all transaction-related operations.
- `statistics` class
  - Calculates and displays financial statistics.
- Main menu
  - Provides access to the Transaction Management and Statistics menus.

## Database

The application uses an SQLite database (`management.db`) to store all transactions.

Each transaction contains:

- Title
- Amount
- Type (Income / Expense)
- Date
- Description

## Skills Practiced

- Object-Oriented Programming
- SQLite Database
- CRUD Operations
- Functions
- Exception Handling
- Loops
- Input Validation
- Menu-Driven Programs

## How to Run

1. Make sure Python 3 is installed.
2. Clone or download this repository.
3. Run the main Python file:

```bash
python main.py
```

## Future Improvements

- Monthly and yearly financial reports
- Category-based transactions
- Data visualization with charts
- Export reports to CSV or Excel
- Graphical User Interface (GUI)

## Author

Developed by Mahya Parsa.

# Pocket Money Tracker

Pocket Money Tracker is a simple desktop application that helps keep track of personal income and expenses. I made this project to practice building desktop applications with Python and to create an easy way to monitor spending without using spreadsheets.

The application keeps a running balance, stores transaction history, and automatically saves data so it is available the next time the program is opened.

## What It Can Do

* Add income and update the balance instantly.
* Record expenses with a category and description.
* View transaction history in a table.
* Automatically save all data locally.
* Prevent invalid entries such as non-numeric amounts.

## Running the Application

If you are using the executable version, simply run:

```text
main.exe
```

No additional installation is required.

## Files

* `main.py` – Contains the application logic and user interface.
* `data.json` – Stores the balance and transaction history.
* `README.md` – Project documentation.

## How It Works

When the application starts, it loads any previously saved data from `data.json`. If no data file exists, a new one is created automatically.

Adding income increases the current balance, while recording an expense decreases it and stores the transaction details. Every change is saved immediately so that information is not lost when the application closes.

The transaction table displays all recorded expenses, making it easier to review spending habits.

## Built With

* Python
* Tkinter
* JSON

## Future Improvements

Some features I would like to add in the future include:

* Filtering transactions by date.
* Charts to visualize spending habits.
* Editing and deleting transactions.
* Exporting transaction history to a file.


import os
import datetime
import json
import tkinter as tk
from tkinter import messagebox, ttk

saved_data = {
    "balance": 0,
    "expenses": []
}

def load_data(data):
  file_path = "data.json"
  if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=4)
    return data
  else:
    with open(file_path, 'r') as file:
      return json.load(file)

def add_income(data, amount):
  data['balance'] += amount
  save_data(data)
  return data

def add_expences(data, amount, category, description):
  data['balance'] -= amount
  new_expenses = {
    "amount" : amount,
    "category" : category,
    "description" : description,
    "time" : str(datetime.datetime.now())
  }
  data["expenses"].append(new_expenses)
  save_data(data)
  return data


current_data = load_data(saved_data)


def save_data(data):
  with open("data.json", 'w') as file:
    json.dump(data, file, indent=4)

def handle_income():
  amount_str = income_entry.get()
  try:
    amount = float(amount_str)
    global current_data
    current_data = add_income(current_data, amount)
    label_amount.config(text=f"${current_data['balance']}")
    income_entry.delete(0, tk.END)
  except ValueError:
    messagebox.showerror("Error", "Please enter a valid number")


def handle_expense():
  global current_data
  try:
    amount = float(exp_amount_entry.get())
    category = category_entry.get()
    description = desc_entry.get()

    if amount > current_data['balance']:
      messagebox.showwarning("Warning", "Not enough balance!")
      return


    current_data = add_expences(current_data, amount, category, description)
    exp_amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    desc_entry.delete(0, tk.END)
    label_amount.config(text=f"${current_data['balance']}")
    update_table()

  except ValueError:
    messagebox.showerror("Error", "Please enter a valid amount")

def update_table():
  for i in tree.get_children():
    tree.delete(i)
  for item in reversed(current_data['expenses']):
    tree.insert("", tk.END, values=(item['time'][:16], item["category"], f"${item['amount']}"))


root = tk.Tk()
root.title("Pocket Money Tracker")
root.geometry("600x650")
balance_frame = tk.Frame(root, bg="#2e7d32")
label_title = tk.Label(balance_frame, text="Current Balance", font=("Arial", 12), fg="white", bg='#2e7d32')
label_title.pack(pady=5)
balance_frame.pack(fill="x", padx=15, pady=15)


label_amount = tk.Label(balance_frame, text=f"${current_data['balance']}", font=("Arial", 24, "bold"), fg="white", bg="#2e7d32")
label_amount.pack(pady=10)

ops_frame = tk.LabelFrame(root, text=" Operations ", padx=10, pady=10)
ops_frame.pack(fill="x", padx=15, pady=5)
lbl_income = tk.Label(ops_frame, text="Add Income ($): ")
lbl_income.grid(row=0, column=0, padx=5, pady=5)
income_entry = tk.Entry(ops_frame)
income_entry.grid(row=0, column=1, padx=5, pady=5)

btn_add = tk.Button(ops_frame, text="Add +", bg="#4caf50", fg="white", command=handle_income)
btn_add.grid(row=0, column=2, padx=5, pady=5)

tk.Label(ops_frame, text="Spend ($): ").grid(row=1, column=0)
exp_amount_entry = tk.Entry(ops_frame)
exp_amount_entry.grid(row=1, column=1)

tk.Label(ops_frame, text="Category:").grid(row=2, column=0)
category_entry = tk.Entry(ops_frame)
category_entry.grid(row=2, column=1)

tk.Label(ops_frame, text="Desc:").grid(row=3, column=0)
desc_entry = tk.Entry(ops_frame)
desc_entry.grid(row=3, column=1)

btn_spend = tk.Button(ops_frame, text="Spend -", bg="#f44336", fg='white', command=handle_expense)
btn_spend.grid(row=4, column=1, pady=10)

history_frame = tk.LabelFrame(root, text=' Expense History ', padx=10, pady=10)
history_frame.pack(fill="both", expand=True, padx=15, pady=15)
columns = ("Date", "Category", "Amount")
tree = ttk.Treeview(history_frame, columns=columns, show='headings')

tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")

tree.pack(fill='both', expand=True)

update_table()

root.mainloop()



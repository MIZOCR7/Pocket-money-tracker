import os
import datetime
import json


saved_data = {
    "balance": 0,
    "expenses": []
}

def load_data(data):
  file_path = "data.json"
  if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
      json.dump(data, file, indent=4)
  else:
    with open(file_path, 'r') as file:
      return json.load(file)

def add_income(data, amount):
  data['balance'] += amount
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
  return data


current_data = load_data(saved_data)

current_data = add_income(current_data, 500)

current_data = add_expences(current_data, 30, "Food", "I was starving")

print(current_data)

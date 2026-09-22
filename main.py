import json
from datetime import datetime


#load existing expenses
try :
   with open("expenses.json", "r") as file :
    expenses = json.load(file)
except FileNotFoundError :
    expenses = []

def addExpense () :
    # Collect user input and create expense obj
   title = input("Enter title: ")
   try:
     amount = float(input("Enter amount: "))
   except ValueError:
     print("Invalid amount! Setting amount to 0.0")
     amount = 0.0
   catt = input("Enter category: ")
 
   expense = {
    "Title": title,
    "Amount": amount,
    "Category": catt,
    "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
   }

   expenses.append(expense)

with open("expenses.json", "w") as file :
      json.dump(expenses, file, indent=4)


for e in expenses:
    print(f"  • [{e['Date']}] {e['Title']} - ${e['Amount']} ({e['Category']})")

    








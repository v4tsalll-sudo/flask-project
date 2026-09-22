from flask import Flask, render_template, request, redirect
import json
import os
from datetime import datetime


app = Flask(__name__)

def load_expenses():
     if os.path.exists("expenses.json"):
        with open("expenses.json", "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
     return []

def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


@app.route("/")
def home():
    all_expenses = load_expenses()
    items = len(all_expenses)
    total_spent = 0
    for e in all_expenses:
        total_spent += float(e.get("Amount", 0))
    return render_template("index.html", expenses=all_expenses, total=total_spent, items=items)
           

@app.route("/add", methods=["POST"])
def add_expense():
    title = request.form.get("title")
    amount = float(request.form.get("amount", 0))
    category = request.form.get("category")
    date_now = datetime.now().strftime("%Y-%m-%d • %H:%M:%S")

    new_expense = {
        "Title": title,
        "Amount": amount,
        "Category": category,
        "Date": date_now
    }

    expenses = load_expenses()
    expenses.append(new_expense)
    save_expenses(expenses)
    return redirect("/")

@app.route("/delete/<int:index>", methods=["POST"])
def delete_expenses(index):
    expenses = load_expenses()

    if 0 <= index < len(expenses) :
        expenses.pop(index)
        save_expenses(expenses)
    return redirect("/")


@app.route("/edit/<int:index>", methods=["POST"])
def edit_expense(index):
    expenses = load_expenses()

    if 0 <= index <len(expenses):
        expenses[index]["Title"] = request.form.get("title")
        expenses[index]["Amount"] = float(request.form.get("amount", 0))
        expenses[index]["Category"] = request.form.get("category"),
        expenses[index]["Date"] = datetime.now().strftime("%Y-%m-%d • %H:%M:%S")

        save_expenses(expenses)
    
    return redirect("/")   

if __name__ == "__main__":
    app.run(debug=True)

# Day 29 - Practice - Expense Tracker
# Author: shakshi-codes-63
import os
from datetime import datetime
import json

print("--- Day 29 Practice Start ---")

FILE_NAME = "my_expenses.json"

# Load old data
def load_expenses():
    try:
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return data
    except json.JSONDecodeError:
        print("File corrupt hai, naya shuru karte hain")
        return []
    except Exception as e:
        print(f"Load Error: {e}")
        return []

# Save data
def save_expenses(expenses):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(expenses, f, indent=4)
    except Exception as e:
        print(f"Save Error: {e}")

# Add Expense
def add_expense(expenses):
    try:
        item = input("Kya kharida? (ex: Chai, Book): ").strip()
        if not item:
            print("Item khali nahi")
            return
        
        amount = float(input("Kitna kharcha hua? Rs: "))
        if amount <= 0:
            print("Amount 0 se zyada hona chahiye")
            return

        record = {
            "date": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "item": item,
            "amount": amount
        }
        expenses.append(record)
        save_expenses(expenses)
        print(f"Added: {item} - Rs {amount}")

    except ValueError:
        print("Error: Amount me number daalo!")
    except Exception as e:
        print(f"Error: {e}")

# Show All
def show_expenses(expenses):
    if not expenses:
        print("Abhi koi kharcha nahi hai!")
        return
    
    total = 0
    print(f"\n--- Total {len(expenses)} Kharch ---")
    for i, ex in enumerate(expenses, 1):
        print(f"{i}. {ex['date']} | {ex['item']} - Rs {ex['amount']}")
        total += ex['amount']
    
    print(f"\nTOTAL KHARCHA: Rs {total:.2f}")

# Delete Last
def delete_last(expenses):
    if not expenses:
        print("Delete karne ko kuch nahi hai")
        return
    last = expenses.pop()
    save_expenses(expenses)
    print(f"Deleted: {last['item']} - Rs {last['amount']}")

# Main Loop
expenses = load_expenses()

while True:
    print("\n--- EXPENSE TRACKER ---")
    print("1. Add Kharcha")
    print("2. Show All Kharcha")
    print("3. Delete Last Entry")
    print("4. Exit")

    ch = input("Choice (1-4): ")

    if ch == "1":
        add_expense(expenses)
    elif ch == "2":
        show_expenses(expenses)
    elif ch == "3":
        delete_last(expenses)
    elif ch == "4":
        print("Tracker Band! Day 29 Complete")
        break
    else:
        print("1-4 me se chuno")

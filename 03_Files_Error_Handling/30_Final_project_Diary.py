# Day 30 - Final Project - Personal Diary with Lock (File & Error Complete)
# Author: shakshi-codes-63
import os
import json
from datetime import datetime
from getpass import getpass

print("--- Day 30 - Final Project ---")

FILE_NAME = "secret_diary.json"
PASSWORD_FILE = "diary_lock.txt"

# --- Lock System (Error Handling Practice) ---
def set_password():
    try:
        if not os.path.exists(PASSWORD_FILE):
            print("Pehli baar diary khol rahi ho, password set karo!")
            pwd = getpass("Naya Password set karo: ")
            if len(pwd) < 4:
                print("Password kam se kam 4 letters ka rakho!")
                return False
            with open(PASSWORD_FILE, "w") as f:
                f.write(pwd)
            print("Password set ho gaya!")
            return True
        return True
    except Exception as e:
        print(f"Password Error: {e}")
        return False

def check_password():
    try:
        if not os.path.exists(PASSWORD_FILE):
            return True
        with open(PASSWORD_FILE, "r") as f:
            correct_pwd = f.read()
        # input() use kar rahe hain phone compatibility ke liye
        entered = input("Diary ka password daalo: ").strip()
        if entered == correct_pwd:
            print("Lock khula!")
            return True
        else:
            print("Galat Password!")
            return False
    except Exception as e:
        print(f"Lock Error: {e}")
        return False

# --- Diary Functions ---
def load_diary():
    try:
        if not os.path.exists(FILE_NAME):
            return []
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Diary file kharab hai, nayi ban rahi hai")
        return []
    except Exception as e:
        print(f"Load Error: {e}")
        return []

def save_diary(data):
    try:
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Save Error: {e}")

def add_entry(diary):
    try:
        print("\n--- Nayi Entry ---")
        title = input("Title: ").strip()
        content = input("Aaj kya hua? likho: ").strip()
        
        if not title or not content:
            print("Title aur Content khali nahi ho sakta!")
            return

        entry = {
            "id": len(diary) + 1,
            "date": datetime.now().strftime("%d-%m-%Y %I:%M %p"),
            "title": title,
            "content": content
        }
        diary.append(entry)
        save_diary(diary)
        print("Entry save ho gayi!")

    except Exception as e:
        print(f"Entry Error: {e}")

def view_entries(diary):
    if not diary:
        print("Diary khali hai, pehle likho!")
        return
    
    print(f"\n--- Total {len(diary)} Entries ---")
    for e in diary:
        print(f"\nID: {e['id']} | {e['date']}")
        print(f"Title: {e['title']}")
        print(f"Note: {e['content']}")
        print("-" * 30)

def search_entry(diary):
    try:
        keyword = input("Kya search karna hai? (Title/Date): ").lower()
        found = False
        for e in diary:
            if keyword in e['title'].lower() or keyword in e['date'].lower() or keyword in e['content'].lower():
                print(f"\nFound - ID: {e['id']} | {e['date']} | {e['title']}")
                print(f"{e['content']}")
                found = True
        if not found:
            print("Kuch nahi mila us naam se")
    except Exception as e:
        print(f"Search Error: {e}")

# --- Main Program ---
if not set_password():
    exit()

if not check_password():
    print("Access Denied!")
    exit()

diary_data = load_diary()

while True:
    print("\n--- MY SECRET DIARY ---")
    print("1. Nayi Entry Likho")
    print("2. Saari Entries Dekho")
    print("3. Search Karo")
    print("4. Exit")

    choice = input("Choice (1-4): ").strip()

    if choice == "1":
        add_entry(diary_data)
    elif choice == "2":
        view_entries(diary_data)
    elif choice == "3":
        search_entry(diary_data)
    elif choice == "4":
        print("\nDiary Band! --- Day 21 to 30 COMPLETE ---")
        print("Kal se Day 31 - OOPs Start hoga!")
        break
    else:
        print("Sahi number chuno 1-4")

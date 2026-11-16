# Day 27 - Practice - Student Report Manager
# Author: shakshi-codes-63
import os
import datetime

print("--- Day 27 Practice Start ---")

FILE_NAME = "student_records.txt"

# Function 1: Record Add Karna
def add_record():
    try:
        name = input("Student ka naam: ")
        if not name.strip():
            print("Naam khali nahi ho sakta!")
            return
            
        marks = int(input("Marks (0-100): "))
        if marks < 0 or marks > 100:
            print("Marks 0 se 100 ke beech hone chahiye!")
            return

        today = datetime.date.today()
        data = f"{today} | Name: {name} | Marks: {marks}\n"

        with open(FILE_NAME, "a") as f:
            f.write(data)
        print("Record save ho gaya!")

    except ValueError:
        print("Error: Marks me sirf number daalo!")
    except Exception as e:
        print(f"Kuch galat hua: {e}")

# Function 2: Saare Records Dekhna
def show_records():
    try:
        if not os.path.exists(FILE_NAME):
            print("Abhi koi record nahi hai!")
            return

        with open(FILE_NAME, "r") as f:
            content = f.read()
            if not content:
                print("File khali hai!")
            else:
                print("\n--- Saare Records ---")
                print(content)

    except Exception as e:
        print(f"Read Error: {e}")

# Function 3: Search Karna
def search_record():
    try:
        search_name = input("Kiska record dhundna hai? ")
        found = False
        with open(FILE_NAME, "r") as f:
            for line in f:
                if search_name.lower() in line.lower():
                    print(f"Found: {line.strip()}")
                    found = True
        if not found:
            print(f"{search_name} ka record nahi mila")
    except FileNotFoundError:
        print("File hi nahi hai, pehle record add karo!")

# Main Menu - Loop
while True:
    print("\n--- MENU ---")
    print("1. Add Record")
    print("2. Show All Records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Apna choice (1-4): ")

    if choice == "1":
        add_record()
    elif choice == "2":
        show_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        print("Bye Bye! Day 27 Complete")
        break
    else:
        print("Galat choice! 1-4 me se chuno")

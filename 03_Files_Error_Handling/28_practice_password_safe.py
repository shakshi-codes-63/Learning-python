# Day 28 - Practice - Mini Password Safe
# Author: shakshi-codes-63
import os
import random
import string
from datetime import datetime

print("--- Day 28 Practice Start ---")

FILE_NAME = "my_passwords.txt"

# Function 1: Strong Password Generate Karna (Module Practice)
def generate_password(length=12):
    try:
        # string module ka use
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password
    except Exception as e:
        print(f"Password generate error: {e}")
        return None

# Function 2: Password Save Karna (File Write + Error)
def save_password():
    try:
        website = input("Website/App ka naam: ").strip()
        username = input("Username/Email: ").strip()
        
        if not website or not username:
            print("Website aur Username khali nahi ho sakta!")
            return

        choice = input("1. Khud password likhna hai? 2. Generate karu? (1/2): ")
        
        if choice == "1":
            pwd = input("Password likho: ")
        elif choice == "2":
            length = int(input("Kitne letters ka password chahiye? (ex: 12): "))
            pwd = generate_password(length)
            print(f"Generated Password: {pwd}")
        else:
            print("Galat choice")
            return

        # File me save
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        data = f"{date} | Website: {website} | User: {username} | Pass: {pwd}\n"

        with open(FILE_NAME, "a") as f:
            f.write(data)
        
        print("Password safe me save ho gaya!")

    except ValueError:
        print("Error: Length me number hi daalo!")
    except Exception as e:
        print(f"Error: {e}")

# Function 3: Saare Password Dekhna
def view_passwords():
    try:
        if not os.path.exists(FILE_NAME):
            print("Abhi koi password save nahi hai!")
            return
        
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            if not lines:
                print("File khali hai")
                return
            
            print(f"\n--- Total {len(lines)} Passwords ---")
            for line in lines:
                print(line.strip())

    except FileNotFoundError:
        print("File nahi mili!")
    except Exception as e:
        print(f"Error: {e}")

# Main Menu
while True:
    print("\n--- PASSWORD SAFE MENU ---")
    print("1. Save New Password")
    print("2. View All Passwords")
    print("3. Generate Only (Without Saving)")
    print("4. Exit")

    opt = input("Choice (1-4): ")

    if opt == "1":
        save_password()
    elif opt == "2":
        view_passwords()
    elif opt == "3":
        try:
            l = int(input("Length: "))
            print(f"Password: {generate_password(l)}")
        except:
            print("Number daalo")
    elif opt == "4":
        print("Safe Closed! Day 28 Complete")
        break
    else:
        print("1-4 me se chuno")

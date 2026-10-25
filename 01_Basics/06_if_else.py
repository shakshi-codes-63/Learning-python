# Day 06 - If-Else Condition
# Author: Shakshi 
# Topic: Logic Start

print("--- Day 06: If-Else Condition ---")

# Example 1: Simple If-Else
age = 18
if age >= 18:
    print("1. You can vote - Vote de sakte ho")
else:
    print("1. You cannot vote")

# Example 2: Elif Ladder - Shamli to Noida Ticket System

print("\n2. Ticket Price System:")
distance = 120  # Shamli se Noida ~120km

if distance < 50:
    print("Ticket: 50 Rs - Local")
elif distance < 100:
    print("Ticket: 100 Rs - Baghpat tak")
elif distance <= 150:
    print("Ticket: 150 Rs - Shamli to Noida")
else:
    print("Ticket: 200+ Rs - Long Route")

# Example 3: Nested If-Else
print("\n3. Nested Condition - Login Check:")
username = "shakshi"
password = "1234"

if username == "shakshi":
    if password == "1234":
        print("Login Successful - Shamli wali ID khul gayi!")
    else:
        print("Wrong Password")
else:
    print("User Not Found")

# Example 4: Practice Task for GitHub
# User se input leke check karo - Even/Odd
print("\n4. Practice Task:")
num = 10
if num % 2 == 0:
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")

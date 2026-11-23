# Day 35 - OOPs Practice - Bank Account
# Author: shakshi-codes-63
print("--- Day 35 - OOPs Practice 1: Bank Account ---")

class BankAccount:
    def __init__(self, name, account_no, balance=0):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        print(f"Account ban gaya! Welcome {self.name} ji")

    def show_balance(self):
        print(f"{self.name} ka Balance: Rs. {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Rs. {amount} Jama hue! New Balance: Rs. {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Paise kam hain! Balance: Rs. {self.balance} hi hai.")
        else:
            self.balance = self.balance - amount
            print(f"Rs. {amount} Nikale! Bacha hua Balance: Rs. {self.balance}")

    def show_details(self):
        print(f"--- Account Details ---")
        print(f"Name: {self.name}")
        print(f"Account No: {self.account_no}")
        print(f"Balance: Rs. {self.balance}")

# Object 1 - Tumhara Account
print("\n--- Shakshi ka Account ---")
acc1 = BankAccount("Shakshi", "1234567890", 1000)
acc1.show_balance()
acc1.deposit(500)
acc1.withdraw(200)
acc1.withdraw(5000)  # Ye fail hoga, paise kam hain
acc1.show_details()

# Object 2
print("\n--- Priya ka Account ---")
acc2 = BankAccount("Priya", "0987654321", 500)
acc2.deposit(1000)
acc2.show_balance()

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
# Ek Student class banao jisme marks add ho aur average nikle
class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_marks(self, mark):
        self.marks.append(mark)
        print(f"{self.name} ko {mark} marks mile!")

    def show_average(self):
        avg = sum(self.marks) / len(self.marks)
        print(f"{self.name} ka Average: {avg}")

s = Student("Shakshi")
s.add_marks(90)
s.add_marks(85)
s.add_marks(95)
s.show_average()

print("\n--- Day 35 Complete ---")

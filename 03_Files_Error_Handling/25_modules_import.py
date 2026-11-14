# Day 25 - Modules & Import
# Author: shakshi-codes-63

# --- PART 1: Humara khud ka function (Jaise mymodule hota hai) ---
def greet(name):
    return f"Hello {name}, from Shamli!"

def add(a, b):
    return a + b

# --- PART 2: Modules ka use ---

# 1. Custom functions ko use karna
print(greet("Shakshi"))
print(f"Add: {add(10, 20)}")

# 2. Built-in Modules
import math
import random
import datetime

print(f"\nmath.sqrt(16) = {math.sqrt(16)}")
print(f"Random number 1-100: {random.randint(1, 100)}")
print(f"Today's Date: {datetime.date.today()}")

# 3. Alias ka use
import math as m
print(f"With alias m.pow(2,3) = {m.pow(2,3)}")

print("\n--- Day 25 Complete ---")

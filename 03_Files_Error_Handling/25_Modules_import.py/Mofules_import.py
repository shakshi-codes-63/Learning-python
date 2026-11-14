# Day 25 - Modules & Import
# Author: Shakshi - Shamli

# METHOD 1: Poora module import karna
import mymodule
print(mymodule.greet("Shakshi"))
print(mymodule.add(10, 20))

# METHOD 2: Specific function import karna
from mymodule import add, PI
print(f"Direct add: {add(5, 5)}")
print(f"PI value: {PI}")

# METHOD 3: Alias (Nickname) dena
import mymodule as mm
print(mm.is_even(10))

# METHOD 4: Built-in Modules ka use
import math
import random
import datetime

# math module
print(f"\nMath sqrt(16): {math.sqrt(16)}")
print(f"Math pow(2,3): {math.pow(2, 3)}")

# random module
print(f"Random number (1-100): {random.randint(1, 100)}")
print(f"Random choice: {random.choice(['Shamli', 'Delhi', 'Agra'])}")

# datetime module
today = datetime.date.today()
print(f"Today's Date: {today}")
now = datetime.datetime.now()
print(f"Current Time: {now.strftime('%H:%M:%S')}")

# METHOD 5: from module import * (Not recommended but interview me poochte hain)
from mymodule import *
print(f"\n* import se greet: {greet('Coder')}")

# Bonus: Module ka naam check karna
print(f"\nModule name: {__name__}")
if __name__ == "__main__":
    print("Ye main file hai, direct run ho rahi hai")

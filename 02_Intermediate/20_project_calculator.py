# Day 20 - Project 1 - Smart Calculator
# Phase 1 Complete Project

# Functions (Day 11-15 ka use)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Zero se divide nahi kar sakte!"
    return a / b

# Dictionary se operations map kiye (Day 18 ka use)
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# String Methods se history clean karenge (Day 19 ka use)
history = []  # List ka use (Day 16)

print("=== Shakshi's Smart Calculator ===")
print("Operations: + , - , * , /")
print("Exit karne ke liye 'q' likho\n")

# Loop ka use (Day 07-10)
while True:
    user_input = input("Calculation likho (jaise 5 + 5) ya 'q': ").strip().lower()
    
    if user_input == 'q':
        print("Calculator band ho raha hai...")
        break
    
    # String Methods ka use
    parts = user_input.split()
    
    if len(parts) != 3:
        print("Format galat hai! Aise likho: 10 + 5")
        continue
    
    num1_str, op, num2_str = parts
    
    # Check number hai ya nahi
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except:
        print("Number sahi likho!")
        continue
    
    if op in operations:
        # Function call Dictionary se
        result = operations[op](num1, num2)
        final_result = f"{num1} {op} {num2} = {result}"
        print(final_result)
        
        # History me save karna
        history.append(final_result)
    else:
        print("Operation samjha nahi! + - * / me se use karo")
    
    print("-" * 30)

# Final History Show
print("\n=== Tumhari Calculation History ===")
for item in history:
    print(item.title()) # String method ka use

print(f"\nTotal calculations: {len(history)}")
print("Phase 1 Complete! Congratulations Shakshi! 🎉")

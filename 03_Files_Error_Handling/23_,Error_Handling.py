# Day 23 - Error Handling (try-except)
# Author: Shakshi - Shamli

# 1. Basic try-except - Program crash hone se bachata hai
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result is: {result}")
except ZeroDivisionError:
    print("Error: Zero se divide nahi kar sakte")
except ValueError:
    print("Error: Please number hi dalo, text nahi")

# 2. Multiple Errors ko ek saath handle karna
try:
    a = int(input("\nFirst number: "))
    b = int(input("Second number: "))
    print(f"Division: {a/b}")
except (ZeroDivisionError, ValueError) as e:
    print(f"Error hua: {e}")

# 3. try-except-else-finally - Complete structure
try:
    file = open("notes.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("\nFile nahi mili, pehle Day 22 ka code chalao")
else:
    print("\nFile successfully padh li:")
    print(data[:100]) # pehle 100 characters
finally:
    print("\nYe block hamesha chalega, error ho ya na ho")
    try:
        file.close()
    except:
        pass

# 4. Real-life example - User input validation
while True:
    try:
        age = int(input("\nEnter your age: "))
        if age < 0:
            raise ValueError("Age negative nahi ho sakti")
        break
    except ValueError as e:
        print(f"Invalid input: {e}, dobara try karo")

print(f"Your age is {age} - Saved!")

# 5. Custom Error with raise
def check_password(password):
    if len(password) < 6:
        raise ValueError("Password 6 character se kam hai")
    return True

try:
    check_password("123")
except ValueError as e:
    print(f"\nPassword Error: {e}")

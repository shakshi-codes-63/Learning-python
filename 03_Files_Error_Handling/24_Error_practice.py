# Day 24 - Error Handling Practice
# Author: Shakshi - Shamli
# 5 Practice Questions - Real World Examples

# Practice 1: Safe Calculator (ZeroDivision + ValueError)
print("--- Practice 1: Safe Calculator ---")
def safe_divide():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ZeroDivisionError:
        print("Error: Second number 0 nahi ho sakta")
    except ValueError:
        print("Error: Sirf number daalo")
    else:
        print(f"Answer: {result}")
    finally:
        print("Calculator closed\n")

safe_divide()

# Practice 2: File Handling with Error Handling (Day 22 + Day 23 Combo)
print("--- Practice 2: Safe File Read ---")
def read_file_safely(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"File Content: {content[:100]}")
    except FileNotFoundError:
        print(f"Error: {filename} naam ki file exist nahi karti")
    except PermissionError:
        print(f"Error: {filename} ko read karne ki permission nahi hai")

read_file_safely("notes.txt")
read_file_safely("not_exist.txt")

# Practice 3: Age Validator with Custom Raise
print("\n--- Practice 3: Age Validator ---")
def validate_age(age_str):
    try:
        age = int(age_str)
        if age < 0:
            raise ValueError("Age negative nahi ho sakti")
        if age > 120:
            raise ValueError("Age 120 se zyada valid nahi hai")
        print(f"Valid Age: {age}")
    except ValueError as e:
        print(f"Invalid Age -> {e}")

validate_age("25")
validate_age("-5")
validate_age("abc")

# Practice 4: List Index Error Handling
print("\n--- Practice 4: Safe List Access ---")
fruits = ["apple", "mango", "banana"]
try:
    index = int(input("Enter index (0-2): "))
    print(f"Fruit: {fruits[index]}")
except IndexError:
    print("Error: Itna bada index list me nahi hai")
except ValueError:
    print("Error: Number daalo")

# Practice 5: Dictionary Key Error Handling
print("\n--- Practice 5: Safe Dictionary Access ---")
user_data = {"name": "Shakshi", "city": "Shamli"}

try:
    key = input("Kaunsi info chahiye? (name/city/age): ")
    print(f"{key}: {user_data[key]}")
except KeyError:
    print(f"Error: '{key}' naam ka data available nahi hai")
    print(f"Available keys: {list(user_data.keys())}")

print("\n--- Day 24 Practice Complete ---")

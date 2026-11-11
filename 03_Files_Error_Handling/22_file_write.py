# Day 22 - File Handling (Write Mode)
# Author: Shakshi - Shamli

# 1. Basic Write Mode - w (Creates new file or overwrites existing)
with open("notes.txt", "w") as file:
    file.write("Day 22 - File Handling (Write)\n")
    file.write("Learning Python File Handling\n")

print("File created with w mode")

# 2. Append Mode - a (Adds data without deleting old data)
with open("notes.txt", "a") as file:
    file.write("\n--- Appended Line ---\n")
    file.write("This line is added using append mode")

print("Data appended successfully")

# 3. writelines() - Writing multiple lines from a list
my_lines = [
    "\n1. Python is easy\n",
    "2. File handling is important\n",
    "3. Day 22 completed\n"
]

with open("notes.txt", "a") as file:
    file.writelines(my_lines)

print("Multiple lines added")

# 4. Exclusive Mode - x (Creates file, error if already exists)
try:
    with open("my_journey.txt", "x") as file:
        file.write("My Python Learning Journey - Day 22\n")
    print("my_journey.txt created with x mode")
except FileExistsError:
    print("File already exists, x mode failed")

# 5. Final Check - Reading what we wrote
with open("notes.txt", "r") as file:
    content = file.read()
    print("\n--- File Content ---")
    print(content)

# Day 26 - Practice (File Handling + Error Handling)
# Author: shakshi-codes-63

print("--- Day 26 Practice Start ---")

# Practice 1: Diary App - Write with Error Handling
print("\n1. Diary Entry Saver")
try:
    entry = input("Aaj ki diary entry likho: ")
    with open("my_diary.txt", "a") as f:
        f.write(entry + "\n")
    print("Entry save ho gayi!")
except Exception as e:
    print(f"Error aaya: {e}")

# Practice 2: Safe File Reader
print("\n2. Diary Reader")
try:
    with open("my_diary.txt", "r") as f:
        lines = f.readlines()
        print(f"Total entries: {len(lines)}")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")
except FileNotFoundError:
    print("Abhi koi diary entry nahi hai. Pehle likho!")

# Practice 3: Marks Calculator with try-except
print("\n3. Marks Percentage Calculator")
try:
    marks = input("Apne marks comma me daalo (ex: 80,90,75): ")
    marks_list = [int(m.strip()) for m in marks.split(",")]
    total = sum(marks_list)
    percent = total / len(marks_list)
    print(f"Total: {total}, Percentage: {percent:.2f}%")
except ValueError:
    print("Error: Sirf number daalo comma se alag karke")
except ZeroDivisionError:
    print("Error: Koi marks nahi daale")

# Practice 4: Word Counter from File
print("\n4. Word Counter")
try:
    with open("my_diary.txt", "r") as f:
        content = f.read()
        words = len(content.split())
        print(f"Diary me total {words} words hain")
except FileNotFoundError:
    print("File nahi mili")

print("\n--- Day 26 Complete ---")

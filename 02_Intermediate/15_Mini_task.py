# Day 15 - Mini Task : Student Report Card System
# Isme Day 11, 12, 13, 14 sab cover hai

# Day 11 - Function Intro
def welcome():
    print("=== V.V. College Report System ===")
    print("Namaste Shakshi!\n")

# Day 12 - Function Arguments
def add_marks(name, marks_list):
    print(f"Student: {name}")
    return marks_list

# Day 13 - Return Keyword
def calculate_result(marks):
    total = sum(marks)
    avg = total / len(marks)
    
    if avg >= 33:
        status = "PASS"
    else:
        status = "FAIL"
    
    return total, avg, status

# Day 14 + 15 - Function Practice + Mini Task
def show_report(name, total, avg, status):
    print("\n--- Report Card ---")
    print(f"Name: {name}")
    print(f"Total Marks: {total}")
    print(f"Average: {avg:.2f}")
    print(f"Result: {status}")
    
    if status == "PASS":
        print("Bahut badhiya! Bharat BoudhIKS ke liye ready ho.")
    else:
        print("Mehnat karo, ho jayega.")

# Main Program Start
welcome()

# Tumhare marks
my_marks = add_marks("Shakshi", [78, 82, 65, 88, 90])

total_marks, average, result = calculate_result(my_marks)

show_report("Shakshi", total_marks, average, result)

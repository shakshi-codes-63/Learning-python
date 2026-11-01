# Day 12 - Function Arguments

# 1. Positional Arguments - Position ke hisaab se
def student_info(name, course):
    print(f"Name: {name}, Course: {course}")

student_info("Shakshi", "BCA")
# student_info("BCA", "Shakshi") -> Ulta ho jayega

print("---")

# 2. Default Arguments - Pehle se value set
def greet(name="Friend"):
    print(f"Hello {name}")

greet()  # Kuch nahi bhejoge to Friend lega
greet("Anjali")

print("---")

# 3. Keyword Arguments - Naam se bhejo, order ka tension khatam
def make_coffee(sugar, milk):
    print(f"Coffee with {sugar} sugar and {milk} milk")

make_coffee(milk="low", sugar="high") # Order change kar diya, phir bhi sahi

print("---")

# 4. Real Task - Infosys Interview me yahi puchenge
def calculate_salary(basic, bonus=5000):
    total = basic + bonus
    print(f"Total Salary: {total}")

calculate_salary(30000) # Bonus default lega
calculate_salary(30000, 10000) # Bonus tumne de diya

print("---")

# 5. Aaj ka Mini Practice
def final_intro(name, day, goal="Infosys"):
    print(f"Day {day} - {name} ka goal {goal} hai")

final_intro("Shakshi", 12)
final_intro("Shakshi", 12, "Google") # Goal change

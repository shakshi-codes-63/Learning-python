# Day 11 - Functions Intro
# Function kya hai? - Baar baar use hone wala code ek jagah likh do

# 1. Simple Function - Bina Arguments ke
def greet():
    print("Hello Shakshi!")
    print("Welcome to Day 11")

greet()  # Function ko call kiya

print("---")

# 2. Function with Argument
def greet_person(name):
    print(f"Hello {name}!")
    
greet_person("Shakshi")
greet_person("Anjali")

print("---")

# 3. Function with 2 Arguments
def add(a, b):
    print(f"{a} + {b} = {a+b}")

add(5, 3)
add(10, 20)

print("---")

# 4. Real Life Example - For your journey
def check_day_status(day):
    if day <= 10:
        print(f"Day {day} - Basics Complete ✅")
    elif day <= 15:
        print(f"Day {day} - Functions chal rahe hain 👉")
    else:
        print(f"Day {day} - Aage ka kaam baaki hai")

check_day_status(5)
check_day_status(11)  # Aaj ka din
check_day_status(18)

print("---")

# 5. Mini Task for Today
def intro():
    print("Name: Shakshi")
    print("Goal: Infosys / Wipro in 100 Days")
    print("Current Day: 11")

intro()

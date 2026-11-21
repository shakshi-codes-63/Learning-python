# Day 32 - Constructor (__init__)
# Author: shakshi-codes-63
print("--- Day 32 - Constructor ---")

# Constructor matlab - Jab Object banega, tabhi apne aap chalega
# Kal hume alag se introduce() call karna pada tha, aaj nahi karna padega

class Student:
    # Ye hai Constructor - __init__
    def __init__(self, name, course, city="Bareilly"):
        self.name = name
        self.course = course
        self.city = city
        print(f"Constructor chala! {self.name} ka admission ho gaya.")

    def show_details(self):
        print(f"Name: {self.name} | Course: {self.course} | City: {self.city}")

    def study(self, subject):
        print(f"{self.name} abhi {subject} padh rahi hai...")

# Object banate hi Constructor chal gaya - koi alag function call nahi kiya
print("\n--- Object 1 ---")
s1 = Student("Shakshi", "Python 70 Days")
s1.show_details()
s1.study("Constructor")

print("\n--- Object 2 ---")
s2 = Student("Priya", "Bharat BoudhIKS", "UP")
s2.show_details()
s2.study("Natyashastra")

# Extra Practice - Default Value wala Constructor
print("\n--- Tumhara Task ka Example ---")
class Car:
    def __init__(self, brand, color="Black"):
        self.brand = brand
        self.color = color
        print(f"{self.color} color ki {self.brand} ready hai!")

    def start(self):
        print(f"{self.brand} start ho gayi!")

c1 = Car("Swift")
c1.start()

c2 = Car("Thar", "Red")
c2.start()

print("\n--- Day 32 Complete ---")

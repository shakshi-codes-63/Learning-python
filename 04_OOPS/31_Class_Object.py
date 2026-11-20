# Day 31 - Class and Object (OOPs Start)
# Author: shakshi-codes-63
print("--- Day 31 - OOPs Start ---")

# Class matlab ek Blueprint / Design
class Student:
    # Method / Function inside class
    def __init__(self):
        print("Naya Student bana!")

    def introduce(self, name, course):
        self.name = name
        self.course = course
        print(f"Hi, Main {self.name} hun, {self.course} kar rahi hun.")

    def study(self, subject):
        print(f"{self.name} abhi {subject} padh rahi hai...")

# Object banana - Blueprint se ghar banana
print("\n--- Object 1 ---")
s1 = Student()  # Object 1
s1.introduce("Shakshi", "Python 70 Days")
s1.study("OOPs")

print("\n--- Object 2 ---")
s2 = Student()  # Object 2
s2.introduce("Priya", "Bharat BoudhIKS")
s2.study("Natyashastra")

# Extra Practice - Tumhara khud ka class
print("\n--- Tumhara Task ka Example ---")
class Car:
    def start(self):
        print("Car start ho gayi - Broom broom!")
    def stop(self):
        print("Car ruk gayi!")

my_car = Car()
my_car.start()
my_car.stop()

print("\n--- Day 31 Complete ---")

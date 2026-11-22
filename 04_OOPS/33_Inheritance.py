# Day 33 - Inheritance
# Author: shakshi-codes-63
print("--- Day 33 - Inheritance ---")

# Parent Class - Baap
class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        print(f"Person bana: {self.name}")

    def introduce(self):
        print(f"Main {self.name} hun, {self.city} se hun.")

    def eat(self):
        print(f"{self.name} khana kha raha hai...")

# Child Class - Beta, Person se sab kuch le lega
# Bracket me Parent ka naam likho - bas Inheritance ho gaya!
class Student(Person):
    def __init__(self, name, city, course):
        # super() matlab Parent ka Constructor call karo
        super().__init__(name, city)
        self.course = course
        print(f"Student bana: {self.course} ke liye!")

    # Naya function sirf Student ke paas hai
    def study(self, subject):
        print(f"{self.name} abhi {subject} padh raha hai...")

# Object banao
print("\n--- Object 1 (Student) ---")
s1 = Student("Shakshi", "Bareilly", "Python 70 Days")

# Parent wale function Child se call ho rahe hain - Yehi Inheritance hai!
s1.introduce()  # Person se aaya
s1.eat()        # Person se aaya
s1.study("Inheritance")  # Khud ka hai

print("\n--- Object 2 ---")
s2 = Student("Priya", "UP", "Bharat BoudhIKS")
s2.introduce()
s2.study("Natyashastra")

# Extra Practice - Tumhara khud ka example
print("\n--- Tumhara Task ka Example ---")
class Animal:
    def sound(self):
        print("Animal awaaz karta hai")

class Dog(Animal):  # Dog ne Animal se liya
    def sound(self):
        print("Dog bhow-bhow karta hai!")

class Cat(Animal):
    def bark(self):
        print("Cat meow-meow karti hai!")

d = Dog()
d.sound()

c = Cat()
c.sound()  # Parent wala chalega kyunki Cat ne khud ka nahi banaya
c.bark()

print("\n--- Day 33 Complete ---")

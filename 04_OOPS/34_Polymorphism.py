# Day 34 - Polymorphism (Poly = Many, Morph = Roop)
# Author: shakshi-codes-63
print("--- Day 34 - Polymorphism ---")
print("Ek hi naam, alag-alag kaam!")

# 1. Same function name, alag class me alag kaam
class Dog:
    def sound(self):
        print("Dog: Bhow Bhow!")

class Cat:
    def sound(self):
        print("Cat: Meow Meow!")

class Cow:
    def sound(self):
        print("Cow: Moo Moo!")

# Ek hi function sabke liye kaam kar raha hai
print("\n--- Polymorphism Example 1 ---")
animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()  # Ek hi line, teeno ka alag output

# 2. Method Overriding - Kal wala Inheritance + Aaj wala Polymorphism
print("\n--- Polymorphism Example 2 - Overriding ---")
class Person:
    def introduce(self):
        print("Main ek Person hun")

class Student(Person):
    # Same naam ka function, par naya kaam - Parent wala override ho gaya
    def introduce(self):
        print("Main Shakshi hun, Student hun!")

class Teacher(Person):
    def introduce(self):
        print("Main Teacher hun, padhati hun!")

p1 = Person()
p1.introduce()

s1 = Student()
s1.introduce()  # Student wala chalega, Person wala nahi

t1 = Teacher()
t1.introduce()  # Teacher wala chalega

# 3. In-built Polymorphism - len() sab pe chalta hai
print("\n--- Polymorphism Example 3 - len() ---")
print(len("Shakshi"))  # String pe
print(len([1, 2, 3, 4]))  # List pe
print(len({"name": "Shakshi", "age": 20}))  # Dict pe

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
class Shape:
    def area(self):
        print("Shape ka area?")

class Circle(Shape):
    def area(self):
        print("Circle ka area: pi * r * r")

class Square(Shape):
    def area(self):
        print("Square ka area: side * side")

c = Circle()
c.area()
s = Square()
s.area()

print("\n--- Day 34 Complete - OOPs Concepts Khatam! ---")

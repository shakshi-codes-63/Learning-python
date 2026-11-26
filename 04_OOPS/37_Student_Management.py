# Day 37 - OOPs Practice 3 - Student Management System
# Author: shakshi-codes-63
print("--- Day 37 - OOPs Practice: Student Management ---")

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = {}  # Subject : Marks

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        print(f"{self.name} ko {subject} me {marks} mile!")

    def get_total(self):
        return sum(self.marks.values())

    def get_average(self):
        if len(self.marks) == 0:
            return 0
        return self.get_total() / len(self.marks)

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A+ (Topper!)"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "Fail - Mehnat Karo!"

    def show_report_card(self):
        print(f"\n--- Report Card ---")
        print(f"Name: {self.name} | Roll No: {self.roll_no}")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Total: {self.get_total()}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Grade: {self.get_grade()}")

class School:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"Add hua: {student.name} (Roll: {student.roll_no})")

    def show_all_students(self):
        print(f"\n=== {self.name} ke Students ===")
        for s in self.students:
            print(f"Roll {s.roll_no} - {s.name}")

    def find_topper(self):
        topper = None
        highest = -1
        for s in self.students:
            avg = s.get_average()
            if avg > highest:
                highest = avg
                topper = s
        print(f"\n🏆 TOPPER: {topper.name} (Average: {highest:.2f})")

# School banao
print("\n--- School Start ---")
school = School("Shakshi Coding School")

# Students banao
s1 = Student("Shakshi", 63)
s1.add_marks("Python", 95)
s1.add_marks("OOPs", 90)
s1.add_marks("Math", 85)

s2 = Student("Priya", 12)
s2.add_marks("Python", 80)
s2.add_marks("OOPs", 75)
s2.add_marks("Math", 70)

s3 = Student("Rahul", 25)
s3.add_marks("Python", 98)
s3.add_marks("OOPs", 92)
s3.add_marks("Math", 99)

# School me add karo
school.add_student(s1)
school.add_student(s2)
school.add_student(s3)

# Report Cards dekho
s1.show_report_card()
s2.show_report_card()
s3.show_report_card()

school.show_all_students()
school.find_topper()

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
# Ek Employee class banao jisme salary se bonus calculate ho
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        bonus = self.salary * 0.10
        print(f"{self.name} ka Bonus: Rs. {bonus} | Total: Rs. {self.salary + bonus}")

e = Employee("Shakshi", 50000)
e.get_bonus()

print("\n--- Day 37 Complete ---")

# Day 36 - OOPs Practice 2 - Library Management
# Author: shakshi-codes-63
print("--- Day 36 - OOPs Practice: Library ---")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False  # Shuru me book library me hai

    def show(self):
        status = "Issued hai" if self.is_issued else "Available hai"
        print(f"Book: {self.title} | Author: {self.author} | Status: {status}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        print(f"{self.name} Library khul gayi!")

    def add_book(self, book):
        self.books.append(book)
        print(f"Add hui: {book.title}")

    def show_all_books(self):
        print(f"\n--- {self.name} ki saari Books ---")
        if len(self.books) == 0:
            print("Library khali hai!")
        for b in self.books:
            b.show()

    def issue_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                if b.is_issued == False:
                    b.is_issued = True
                    print(f"Mil gayi! '{b.title}' issue ho gayi.")
                    return
                else:
                    print(f"'{b.title}' pehle se hi issue hai.")
                    return
        print(f"'{title}' naam ki book library me nahi hai.")

    def return_book(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                b.is_issued = False
                print(f"'{b.title}' wapas aa gayi. Thank You!")
                return
        print(f"'{title}' humari library ki nahi hai.")

# Library banao
print("\n--- Library Start ---")
lib = Library("Shakshi")

# Books add karo
lib.add_book(Book("Python 70 Days", "Shakshi"))
lib.add_book(Book("Bharat BoudhIKS", "Priya"))
lib.add_book(Book("Natyashastra", "Bharat Muni"))

lib.show_all_books()

# Issue / Return ka khel
print("\n--- Issue / Return ---")
lib.issue_book("Python 70 Days")
lib.issue_book("Python 70 Days")  # Dobara try karo - fail hoga
lib.show_all_books()
lib.return_book("Python 70 Days")
lib.show_all_books()

# Extra Practice - Tumhara Task
print("\n--- Tumhara Task ka Example ---")
# Student Management - Kal wale Bank jaisa hi hai
class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def add_marks(self, marks):
        self.marks.append(marks)

    def show_result(self):
        total = sum(self.marks)
        print(f"{self.name} (Roll: {self.roll_no}) - Total: {total} - Avg: {total/len(self.marks)}")

s1 = Student("Shakshi", 63)
s1.add_marks(90)
s1.add_marks(95)
s1.show_result()

print("\n--- Day 36 Complete ---")

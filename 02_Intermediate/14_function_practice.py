# Day 14 - Function Practice

# 1. Simple Function - Hello bolna
def namaste(name):
    print(f"Namaste {name}!")
    
namaste("Shakshi")

# 2. Add karne wala function (Arguments + Return)
def add(a, b):
    return a + b

result = add(10, 20)
print(f"Add ka result: {result}")

# 3. Even/Odd check karna 
def check_even_odd(num):
    if num % 2 == 0:
        return "Even hai"
    else:
        return "Odd hai"

print(check_even_odd(7))
print(check_even_odd(10))

# 4. Factorial nikalna - Loop + Function
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

print(f"5 ka factorial: {factorial(5)}")

# 5. Practice Task 
def average_marks(marks_list):
    total = sum(marks_list)
    avg = total / len(marks_list)
    return avg

my_marks = [75, 80, 68, 90, 85]
print(f"Tumhara average: {average_marks(my_marks)}")

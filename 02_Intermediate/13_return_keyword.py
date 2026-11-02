# Day 13 - Return Keyword

def check_even_odd(num):
    if num % 2 == 0:
        return "Even hai"
    else:
        return "Odd hai"

# Function ko call karke uski return value pakad li
num = int(input("Ek number dalo: "))
result = check_even_odd(num)

print(f"Result: {result}")

# Extra Practice - Return ko aage use karna
def calculate_area(length, width):
    area = length * width
    return area

my_area = calculate_area(10, 5)
print(f"Ghar ka area hai: {my_area} sq ft")
print(f"Double area: {my_area * 2}")

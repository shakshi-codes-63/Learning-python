# Day 5 - Type Conversion - By Shakshi 

# 1. String to Integer
age_str = "19"
age_int = int(age_str)
print("My age is:", age_int)
print("Type is:", type(age_int))

# 2. Integer to String
my_age = 19
age_text = str(my_age)
print("My age in text is: " + age_text)

# 3. User input is always String, so convert it
print("\n--- User Input Conversion ---")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert string to int for addition
result = int(num1) + int(num2)
print("Addition result is:", result)
print("I am Shakshi, Day 5 complete!")

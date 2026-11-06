# Day 17 - Tuple and Set 

print("=== 1. TUPLE ===")
# Tuple: Data ko lock kar deta hai, change nahi hota. () me banta hai
student = ("Shakshi", 21, "MCA", 95.5)
print(f"Student Tuple: {student}")

# Q1. Tuple ka first aur last nikalna
print(f"Name: {student[0]}, Marks: {student[-1]}")

# Q2. Tuple change nahi hota - Error ayega agar try kiya
# student[1] = 22  # TypeError: 'tuple' object does not support item assignment

# Q3. Tuple unpacking 
name, age, course, marks = student
print(f"Unpack: Name={name}, Course={course}")

# Q4. Tuple ka use kyu? - Key ke liye safe hai
location = (27.18, 78.02) # Agra ke coordinates
print(f"Location: {location}")

print("\n=== 2. SET ===")
# Set: Duplicate nahi rakhta, order nahi hota. {} me banta hai
marks = {78, 82, 65, 88, 82, 90, 78}
print(f"Original Marks with duplicate: {marks}") # duplicate auto hat gaye

# Q5. Duplicate hatane ke liye Set ka use
list_with_dup = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list_with_dup))
print(f"Duplicate hatane ke baad: {unique_list}")

# Q6. Set ke important operations 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(f"Union: {set1 | set2}")        # Sab element: {1,2,3,4,5,6}
print(f"Intersection: {set1 & set2}") # Common: {3,4}
print(f"Difference: {set1 - set2}")   # Jo set1 me hai set2 me nahi: {1,2}

# Q7. Set me add aur remove
my_set = {10, 20}
my_set.add(30)
my_set.remove(20)
print(f"Set after add/remove: {my_set}")

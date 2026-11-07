# Day 18 - Dictionary

# 1. Dictionary kya hai? Key: Value ka pair
student = {
    "name": "Shakshi",
    "age": 19,
    "city": "Shamli",
    "course": "BA English"
}
print(student)

# 2. Value ko access karna
print(student["name"])  # Agra
print(student.get("age")) # 19 - ye safe tarika hai

# 3. Naya data add / update karna
student["phone"] = "98XXXXX" # naya add hoga
student["city"] = "Saharanpur" # update hoga
print(student)

# 4. Important Methods
print(student.keys())   # saari keys dega
print(student.values()) # saari values dega
print(student.items())  # key-value dono

# 5. Loop lagana Dictionary pe
for key, value in student.items():
    print(f"{key} -> {value}")

# 6. Ek key ko hatana
student.pop("age")
print(student)

# 7. Nested Dictionary 
users = {
    "user1": {"name": "Aman", "age": 22},
    "user2": {"name": "Shakshi", "age": 19}
}
print(users["user2"]["name"])

# MINI TASK for today
# Apna ek dictionary banao
my_profile = {}
my_profile["name"] = input("Naam: ")
my_profile["skill"] = "Content Writing"
print("Tumhara Profile:", my_profile)

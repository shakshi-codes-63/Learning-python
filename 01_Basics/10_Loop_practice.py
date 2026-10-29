# 🐍 Day 10 - Loop Practice | BA Student | Future Coder
# Shakshi 

print("--- Task 1: For Loop - 1 se 10 tak print ---")
for i in range(1, 11):
    print(i)

print("\n--- Task 2: While Loop - Even Numbers ---")
num = 2
while num <= 20:
    print(num, end=" ")
    num += 2

print("\n\n--- Task 3: If + Loop - Table Practice ---")
# User se table lo
n = int(input("\nKis number ka table chahiye? "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

print("\n--- Task 4: Break & Continue ---")
for i in range(1, 11):
    if i == 5:
        continue  # 5 ko skip kar do
    if i == 8:
        break     # 8 par ruk jao
    print(i, end=" ")

print("\n\n--- Task 5: Mini Challenge - Star Pattern ---")
for i in range(1, 6):
    print("*" * i)

print("\nDay 10 Done ✅")

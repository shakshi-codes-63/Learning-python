# Day 09 - Break and Continue

# 1. Break example - 5 aate hi loop band
for i in range(1, 11):
    if i == 5:
        print("5 mil gaya, ab loop band")
        break  # yaha loop khatam
    print(i)

print("---")

# 2. Continue example - 5 ko skip kar do
for i in range(1, 11):
    if i == 5:
        print("5 ko skip kar rahe hain")
        continue  # yaha 5 print nahi hoga, seedha 6 par
    print(i)

print("---")

# 3. Practical example - jaise tumhe negative number nahi chahiye
numbers = [2, 4, -1, 5, 3, -2, 10]

for n in numbers:
    if n < 0:
        continue  # negative hai toh ignore karo
    print(f"Positive number: {n}")

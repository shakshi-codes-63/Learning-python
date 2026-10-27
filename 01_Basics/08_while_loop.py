# Day 08 - While Loop

# 1. Basic - 1 se 5 tak print
print("1. Basic While Loop")
i = 1
while i <= 5:
    print(i)
    i = i + 1  # Ye line sabse important hai, isse hi loop badhega

print("\n")

# 2. 10 se 1 tak ulta print
print("2. Reverse Counting")
j = 10
while j >= 1:
    print(j)
    j = j - 1

print("\n")

# 3. User ka Table print karwana - Aaj ka main task
print("3. Table Task")
num = int(input("Koi number dalo: "))
k = 1
while k <= 10:
    print(f"{num} x {k} = {num * k}")
    k = k + 1

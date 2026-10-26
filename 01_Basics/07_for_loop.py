# Day 7 - For Loop - By Shakshi

# 1. Basic For Loop with range
print("--- 1. Basic Loop ---")
for i in range(5):
    print("Hello, Shakshi!", i)

# 2. For Loop with Start and End
print("\n--- 2. 1 to 10 Numbers ---")
for num in range(1, 11):
    print("Number is:", num)

# 3. User Input + For Loop - Your Name Print
print("\n--- 3. Name Print ---")
name = input("Enter your name: ")
times = int(input("How many times print? "))

for i in range(times):
    print(f"{i+1}. I am {name}")

print("\nI am Shakshi, Day 7 complete!")

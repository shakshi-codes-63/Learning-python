# Day 16 - List 
# **Data collection start**

# Q1. List ko reverse karo - bina reverse() ke (Most Asked)
def reverse_list(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print(reverse_list([1, 2, 3, 4, 5])) # Output: [5,4,3,2,1]

# Q2. Second Largest Element nikalo
def second_largest(arr):
    unique_arr = list(set(arr)) # duplicate hataya
    unique_arr.sort()
    return unique_arr[-2]

print(f"Second Largest: {second_largest([10, 20, 4, 45, 99])}") # 45

# Q3. Duplicate hatana
def remove_duplicate(arr):
    new_list = []
    for i in arr:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicate([1, 2, 2, 3, 4, 4, 5]))

# Q4. List me se Even aur Odd alag karo
def split_even_odd(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]
    return even, odd

even, odd = split_even_odd([1,2,3,4,5,6])
print(f"Even: {even}, Odd: {odd}")


# Q5. 2 list ko merge karo aur sort karo
list1 = [1, 3, 5]
list2 = [2, 4, 6]
merged = sorted(list1 + list2)
print(f"Merged Sorted: {merged}")

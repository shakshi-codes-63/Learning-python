# Day 19 - String Methods

# 1. Basic Setup
name = "  shakshi Rajput  "
print(f"Original: '{name}'")

# 2. Cleaning Methods - Sabse zyada use hote hain
print(name.strip())   # aage peeche ka space hatayega -> " Shakshi Rajput "
print(name.lstrip())  # left ka space
print(name.rstrip())  # right ka space

# 3. Case Methods
text = "hello WORLD"
print(text.upper())      # HELLO WORLD
print(text.lower())      # hello world
print(text.title())      # Hello World - Title ke liye best
print(text.capitalize()) # Hello world

# 4. Search and Check Methods
sentence = "I love Python, Python is easy"
print(sentence.find("Python"))    # pehli baar kaha aaya -> 7
print(sentence.count("Python"))   # kitni baar aaya -> 2
print(sentence.startswith("I"))   # True / False
print(sentence.endswith("easy"))  # True

# 5. Replace and Split - Content Writing me iska bahut use hai
print(sentence.replace("Python", "Content Writing"))
words = sentence.split() # list me tod dega
print(words)

# 6. Join Method (List ko String banana)
new_sentence = "-".join(words)
print(new_sentence) # I-love-Python,-Python-is-easy

# 7. Extra Useful Methods
email = "shakshi@gmail.com"
print(email.isspace()) # space hai kya? False
print("123".isdigit()) # number hai kya? True
print("abc".isalpha()) # sirf alphabet hai kya? True

# MINI TASK - Aaj ka Project
user_input = input("Apna naam likho (space ke saath): ")
clean_name = user_input.strip().title()
print(f"Hello, {clean_name}!")
print(f"Tumhare naam me {len(clean_name)} letters hain")

# Content Writer Wala Task
post = "   this is my first blog post about python   "
final_post = post.strip().title()
print(f"Final Blog Title: {final_post}")

# Day 21 - File Handling (Read)
# Folder: 03_Files

# Step 0 - Pehle ek file bana lete hain practice ke liye
# Ye code ek baar chalao to file ban jayegi
with open("my_notes.txt", "w") as f:
    f.write("Hello, I am Shakshi Sharma\n")
    f.write("I am learning Python\n")
    f.write("Day 21 - File Handling")

print("File ban gayi! Ab read karte hain...\n")

# Method 1 - Poori file ek baar me padhna (Sabse easy)
print("--- Method 1: read() ---")
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)

# Method 2 - Line by line padhna (Bahut use hota hai)
print("\n--- Method 2: readline() / for loop ---")
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip().title())  # Day 19 ka title() yaha use hua

# Method 3 - Saari lines ko List me lena (Day 16 ka List)
print("\n--- Method 3: readlines() ---")
with open("my_notes.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    print(f"Total lines: {len(lines)}")

# Mini Task for You
print("\n--- Aaj ka Task ---")
# Ek blog.txt file banao aur usko read karke word count karo
blog_content = "Python file handling is very easy and useful for content writers"
word_count = len(blog_content.split())
print(f"Blog words: {word_count}")

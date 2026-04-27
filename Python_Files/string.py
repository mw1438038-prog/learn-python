# ================================
# 🔤 PYTHON STRING PRACTICE
# ================================

# 🔹 1. User Input + f-String
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# f-string (dynamic string formatting)
message = f"Hello {name}, welcome! You are {age} years old."
print("\n--- Basic Message ---")
print(message)

# 🔹 2. New Line Example (\n)
print("\n--- New Line Example ---")
multi_line = f"Hello {name},\nWelcome to Python learning!\nEnjoy coding 🚀"
print(multi_line)


# 🔹 3. Multi-line Paragraph (Triple Quotes)
print("\n--- Multi-line Paragraph ---")
paragraph = """A warm welcome paragraph should be enthusiastic,
sincere, and personalized to the recipient.
It creates a positive impression."""
print(paragraph)


# 🔹 4. String Methods Practice
print("\n--- String Methods ---")
text = "   Brother is HOME and I am happy   "

# lower() → sab small letters
print("Lower:", text.lower())

# upper() → sab capital letters
print("Upper:", text.upper())

# strip() → start/end spaces remove
clean_text = text.strip()
print("Strip:", clean_text)

# split() → string ko list me todna
words = clean_text.split()
print("Split:", words)

# find() → word ki position
print("Find 'is':", clean_text.find("is"))

# replace() → word change karna
print("Replace 'is' with 'was':", clean_text.replace("is", "was"))

# startswith() → check start
print("Starts with 'Brother':", clean_text.startswith("Brother"))


# 🔹 5. Search in String (in keyword)
print("\n--- Search in String ---")
quote = """Python is easy to learn.
It is powerful and flexible."""

word = "Python"
print(f"Does '{word}' exist in quote? ->", word in quote)


# 🔹 6. Real Example: split + strip (User Input Cleaning)
print("\n--- Clean User Input (split + strip) ---")
names_input = input("Enter names (comma separated): ")

# split + strip using list comprehension
clean_names = [name.strip() for name in names_input.split("}")]

print("Clean Names List:", clean_names)


# 🔹 7. Extra Practice: Replace + Count
print("\n--- Extra Practice ---")
sentence = "Python is fun. Python is powerful."

# count() → kitni dafa word aya
print("Count 'Python':", sentence.count("Python"))

# replace() → text change
print("Replace Python with Java:", sentence.replace("Python", "Java"))
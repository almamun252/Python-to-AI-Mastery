# --- List Comprehension ---
# Genarally, we create a list using a for loop like this:
# squares = []
# for x in range(1, 6):
#     squares.append(x**2)

# Comprehension method (in a single line):
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares) # Output: [1, 4, 9, 16, 25]

# Condition-based List Comprehension (squares of even numbers only)
even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print("Even Squares:", even_squares) # Output: [4, 16]


# --- Dictionary Comprehension ---
words = ["python", "data", "ai"]
# Generally, we create a dictionary using a for loop like this:
# word_lengths = {}
# for word in words:
#     word_lengths[word] = len(word)

# Comprehension method (in a single line):
word_lengths = {word: len(word) for word in words}

print("Word Lengths:", word_lengths) 
# Output: {'python': 6, 'data': 4, 'ai': 2}
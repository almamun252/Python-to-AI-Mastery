# Function with default argument (greeting="Hello")
def greet_person(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Normal call (uses default argument)
greet_person("Karim") 
# Output: Hello, Karim!

# Call by providing both arguments
greet_person("Salam", "Good morning") 
# Output: Good morning, Salam!

# Call using Keyword arguments (Order can be changed without any issue)
greet_person(greeting="Hi there", name="Jalil") 
# Output: Hi there, Jalil!
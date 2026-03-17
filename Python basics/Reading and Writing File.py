# Writing to a file ( 'w' mode: new file will be created or existing file will be overwritten )
with open("abc.txt", "w") as file:
    file.write("Hello, Brother!\n")
    file.write("This is my first file handling code.\n")
print("File written successfully!")

# Appending to a file ( 'a' mode: existing file will be preserved and new data will be added at the end )
with open("abc.txt", "a") as file:
    file.write("Appending a new line.\n")

# Reading from a file ( 'r' mode: existing file will be read )
with open("abc.txt", "r") as file:
    content = file.read() # read all content at once
    print("\n--- File Content ---")
    print(content)
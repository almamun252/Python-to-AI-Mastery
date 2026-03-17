# List creation
my_list = [10, 20, 30, 40, 50, 60]

# Indexing (zero-based indexing)
print("First element:", my_list[0])       # Output: 10
print("Last element:", my_list[-1])       # Output: 60 (negative indexing works from the end)

# Slicing [start : stop : step]
print("First three elements:", my_list[0:3])  # Output: [10, 20, 30] (3 is the stop index)
print("Every second element:", my_list[::2])  # Output: [10, 30, 50] (skip every second element)
print("Reversed list:", my_list[::-1])        # Output: [60, 50, 40, 30, 20, 10]
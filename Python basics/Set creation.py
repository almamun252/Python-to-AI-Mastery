# Set creation and removing duplicates from a list
numbers_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique numbers:", unique_numbers) # Output: {1, 2, 3, 4, 5}

# Set operations
set_A = {1, 2, 3}
set_B = {3, 4, 5}

print("Intersection (Common):", set_A.intersection(set_B)) # Output: {3}
print("Union (All unique):", set_A.union(set_B))           # Output: {1, 2, 3, 4, 5}
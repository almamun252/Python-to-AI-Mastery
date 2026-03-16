# for loop with range()
print("Counting 1 to 5:")
for i in range(1, 6): # starts from 1, goes up to 5 (exclusive of 6)
    print(i)

# using enumerate() in a list
fruits = ["Apple", "Banana", "Mango"]
print("\nFruits list with index:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
    
# while loop
count = 3
print("\nCountdown starting:")
while count > 0:
    print(count)
    count -= 1
print("Go!")
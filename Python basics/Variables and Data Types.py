# --- ১. Text Type ---
name = "Rahim"            # String (str)

# --- ২. Numeric Types ---
age = 25                  # Integer (int)
height_cm = 175.5         # Float (float)
complex_num = 3 + 4j      # Complex (complex) 

# --- ৩. Boolean Type ---
is_student = True         # Boolean (bool) - True বা False

# --- ৪. Sequence Types (Ordered Collections) ---
my_list = ["Apple", "Banana", "Cherry"]  # List (list) - (Mutable)
my_tuple = ("Apple", "Banana", "Cherry") # Tuple (tuple) - (Immutable)
my_range = range(5)                      # Range (range) - (Immutable, Sequence of numbers)

# --- ৫. Mapping Type ---
my_dict = {"name": "Rahim", "age": 25}   # Dictionary (dict) - (Key-Value Pairs, Mutable)

# --- ৬. Set Types (Unique Elements) ---
my_set = {1, 2, 3, 3, 4}                 # Set (set) - (Unique, Unordered, Mutable)
my_frozenset = frozenset({1, 2, 3})      # Frozenset (frozenset) - (Unique, Unordered, Immutable)

# --- ৭. None Type (No Value) ---
empty_value = None                       # NoneType (None)

# --- ৮. Binary Types (Binary Data) ---
my_bytes = b"Hello"                      # Bytes (bytes)
my_bytearray = bytearray(5)              # Bytearray (bytearray)


# ==========================================
#         --- Type Checking ---
# ==========================================

print(type(name))           # Output: <class 'str'>
print(type(age))            # Output: <class 'int'> 
print(type(height_cm))      # Output: <class 'float'>
print(type(complex_num))    # Output: <class 'complex'>

print(type(is_student))     # Output: <class 'bool'>

print(type(my_list))        # Output: <class 'list'>
print(type(my_tuple))       # Output: <class 'tuple'>
print(type(my_range))       # Output: <class 'range'>

print(type(my_dict))        # Output: <class 'dict'>

print(type(my_set))         # Output: <class 'set'>
print(type(my_frozenset))   # Output: <class 'frozenset'>

print(type(empty_value))    # Output: <class 'NoneType'>

print(type(my_bytes))       # Output: <class 'bytes'>
print(type(my_bytearray))   # Output: <class 'bytearray'>
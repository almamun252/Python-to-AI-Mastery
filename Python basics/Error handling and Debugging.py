# This code demonstrates error handling in Python using try-except blocks.

def safe_division(num1, num2):
    try:
        print(f"Trying to divide {num1} by {num2}...")
        result = num1 / num2
        print(f"Success! Result: {result}")
        
    except ZeroDivisionError:
        # work for division by zero
        print("Error: You cannot divide a number by zero!")
        
    except TypeError:
        # work for invalid types (e.g., string instead of number)
        print("Error: Please provide numbers only.")
        
    finally:
        # work for all cases
        print("Execution of safe_division function finished.\n")

# call the function to test different scenarios
safe_division(10, 2)    # normal case
safe_division(10, 0)    # ZeroDivisionError
safe_division(10, "a")  # TypeError
import logging

# basic of logging
logging.basicConfig(
    filename='app.log',         # the file where logs will be saved
    level=logging.DEBUG,        # the level from which to start recording logs
    format='%(asctime)s - %(levelname)s - %(message)s' # the format of the log messages
)

# 5 level of logging
logging.debug("This is a debug message. (For developers only)")
logging.info("This is an info message. (System is running normally)")
logging.warning("This is a warning! (Something might go wrong)")
logging.error("This is an error! (A function failed)")
logging.critical("This is a CRITICAL message! (System crashed!)")

# an example function to demonstrate logging in action:
def divide_numbers(a, b):
    try:
        result = a / b
        logging.info(f"Successfully divided {a} by {b}. Result: {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Attempted to divide {a} by zero!")
        return None

# function calls to see logging in action
divide_numbers(10, 2)
divide_numbers(5, 0)

print("Check the log file, the messages have been saved!")
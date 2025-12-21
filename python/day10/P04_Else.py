"""
This case demonstrates the use of else in exception handling
"""

try:
    result = 5 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    print(f"The result is {result}")
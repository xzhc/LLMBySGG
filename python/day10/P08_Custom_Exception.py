"""
This case demonstrates custom exception handling in Python.
"""

class MyException(Exception):
    """Custom exception class."""
    def __init__(self, value):
        self.value = value

try:
    #Code that may raise an exception
    raise  MyException("This is an custom exception")
except MyException as e:
    #Code to handle the custom exception
    print(f'Custom Exception Caught: {e.value}')
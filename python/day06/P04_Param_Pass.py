"""
This case demonstrates the passing of function parameters
"""

def change_int (a):
    print(f"The memory address of the value before it is modified inside the function:{id(a)}")
    a = 20
    print(f"The memory address of the value after it is modified inside the function:{id(a)}")

change_int(10)
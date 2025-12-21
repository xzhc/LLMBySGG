"""
This case demonstrates global variables and local variables.
Variables defined in the global scope - global variables - act on the entire module
Variables defined in the local scope - local variables - act on the current function
"""

sum = 0 #this is a global variable

def add(num1, num2):
    sum = num1 + num2 #This is a local variable
    print("Value of local variable inside the functin: ", sum, id(sum))

add(10,20)

print("Global variable outside the function: ", sum, id(sum))
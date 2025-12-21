"""
This case demonstrates closures
Requirement:How to make variables defined in function A accessible to function B
"""

#Method1:Pass the variable in A to B as a parameter through nested function calls
# def func_a():
#     num = 10
#     func_b(num)
#
#
# def func_b(num):
#     print(num)
#
# func_a()

#Method2: closure

def func_a():
    num =10
    def func_b():
        print(num)
    return func_b

fb = func_a()
fb()
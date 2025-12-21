"""
This case demonstrates the nesting of functions
"""

def func_a():
    print('Before func_a executes')
    print('During func_a executes')
    print('After func_a executes')

def func_b():
    print('Before func_b executes')
    func_a()
    print('After func_b executes')

func_b()
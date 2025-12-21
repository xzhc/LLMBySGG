"""
This cade demonstrates enclosing  in Python
"""

def outer(a,b):
    def inner(x):
        return a * x + b
    return inner

inn = outer(1,2)
# print(inn(1))
print(inn.__closure__)
print(inn.__code__.co_freevars)
for cell in inn.__closure__:
    print(cell.cell_contents)
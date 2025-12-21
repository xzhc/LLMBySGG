"""
This case demonstrates the scope
Local scope --> Enclosing scope --> Global scope --> Built in scope
"""

#Built-in scope: Provided natively in python, accessible anywhere in all modules

a = int("10")
print(a)

# Global scope:Accessible through the current module
b = 20
print(b)

def outer():
    # Enclosing scope: Accessible within the closure function
    c = 10
    def inner():
        # Local scope: Only accessible within the current function
        d = 5
        print(a,b,c,d)
    return inner
inn = outer()
inn()


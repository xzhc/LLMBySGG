"""
This case demonstrates scopes in python
There are four main types of scopes in Python:
Local -> Enclosing -> Global -> Built-in
(Abbreviated as LEGB)
"""
a = 100 #Global scope variable
def outer():
    b = 200 #Enclosing scope variable
    def inner():
        c = 300 #Local scope variable
        print("First search in the local scope:", c)
        print("Then search in the enclosing scope:", b)
        print("Then search in the global scope:", a)
        print("Finally search in the built-in scope:", len([1, 2, 3]))
    inner()


outer()



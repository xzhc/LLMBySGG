"""
This case demonstrates attributes
"""

class Dog:
    home = 'earth'

    def __init__(self, name, age):
        print('222')
        self.name = name
        self.age = age

xd = Dog('xd', 1)
print(xd.home)
print(xd.age)
print(xd.age)

xd.color = 'black'
print(xd.color)
print('='*20)
bd = Dog('bd', 3)
print(bd.home)
print(bd.name)
print(bd.age)
# print(bd.color)

#Add a class attribute via ClassName.attribute
# bd.kemu = 'big dog'
# print(bd.kemu)
Dog.kemu = 'small dog'
print(Dog.kemu)
print(bd.kemu)
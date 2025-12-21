"""
This case demonstrates polymorphism
"""

class Bird:
    def __init__(self, name):
        self.name = name

class Fish:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, name):
        self.name = name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self, flag):
        ani = None
        match flag:
            case '1':
                ani = Bird('sparrow')
            case '2':
                ani = Fish('goldfish')
            case '3':
                ani = Dog('bulldog')
        return ani

    def feed(self, animal):
        print(f'{self.name} is feeding {animal.name}.')

xzh = Person('xzh', 24)
# ani = xzh.call('1')
# print(ani.name)
b1 = Bird('sparrow')
f1 = Fish('goldfish')
d1 = Dog('bulldog')
xzh.feed(f1)
xzh.feed(b1)
xzh.feed(d1)
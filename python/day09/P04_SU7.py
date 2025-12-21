"""
Implement the complex relationship of pingchuan's friends in an object-oriented manner
"""

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__bf = None

    @property
    def bf(self):
        return self.__bf

    @bf.setter
    def bf(self, bf):
        self.__bf = bf

    def __str__(self):
        return f'The {self.age}-year-old {self.name} is walking romantically with her boyfriend {self.__bf.name}'

class BoyFriend:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def buy_car(self, car):
        print(f'{self.name} bought a {car.color} {car.name} for his son')

class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

lhc = Student('LHC', 25)
xzh = BoyFriend('XZH', 26)
lhc.bf = xzh
print(str(lhc))

su7 =Car('SU7', 'WHITE')
xzh = Person('XZH', 26)
xzh.buy_car(su7)
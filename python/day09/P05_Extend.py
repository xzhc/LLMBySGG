"""
This case demonstrates inheritance
"""

class Person:
    #Class attribute
    home = 'earth'

    def __init__(self, name):
        #Instance attribute
        self.name = name

    def eat(self):
        print('eating')

class YelloRace(Person):
    color = 'yellow'

class WhiteRace(Person):
    color = 'white'

class BlackRace(Person):
    color = 'black'

xzh = YelloRace('xzh')
print(xzh.color)
print(xzh.home)
xzh.eat()
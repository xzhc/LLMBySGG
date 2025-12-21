"""
This case demonstrates restricting attributes and methods of an instance
"""

import types
class Person:
    __slots__ = ('name', 'age', 'eat')
    def __init__(self, name=None):
        self.name = name

def eat(self):
    print(f'{self.name} is eating.')
def drink(self):
    print(f'{self.name} is drinking.')


p = Person('xzh')
p.eat = types.MethodType(eat, p)

p.eat()

#Add instance attribute
"""
p.weight = 60
    ^^^^^^^^
AttributeError: 'Person' object has no attribute 'weight' and no __dict__ for setting new attributes
"""
# p.weight = 60
# print(p.weight)

#Add instance method
"""
AttributeError: 'Person' object has no attribute 'drink' and no __dict__ for setting new attributes
"""
p.drink = types.MethodType(drink, p)
p.drink()
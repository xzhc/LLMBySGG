"""
This case demonstrates the definition of a class and  access to members in the class
"""

class Person:
    """This is a person class"""
    home = 'home'
    def __init__(self):
        self.age = 18

    def eat(self):
        print('eating...')
    def drink(self):
        print('drinking...')


#Reference
print(Person.home)

print(Person.eat)
print(Person.drink)
# Person.drink()
print(Person.__doc__)

#Instantiation
xzh = Person()
print(xzh.age)
print(xzh.home)
xzh.eat()
xzh.drink()
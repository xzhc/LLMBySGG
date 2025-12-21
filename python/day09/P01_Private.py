"""
This case demonstrates encapsulation
"""
class Person:
    __home = 'earth'
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def __eat(self):
        print('eating')

    def eat_1(self):
        print('eating')
        print(self.__name)
        self.__eat()

# print(Person._Person__home)
# print(Person.home)

p = Person('John', 36)
# p.__eat()
p._Person__eat()
p.eat_1()
print(p._Person__home)
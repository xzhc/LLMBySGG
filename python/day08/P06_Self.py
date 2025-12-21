"""
This case demonstrates the usage of self
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eating...')

    def study(self):
        print('studying...')

    def eat_study(self):
        # Call other instance methods within an instance method
        self.eat()
        self.study()


xzh = Student('xzhang', 36)
xzh.eat_study()
"""
This cade demonstrates  multiple inheritance
"""
class Person():
    """Person class"""
    home = 'earth'

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('eating...')


class YellowRace(Person):
    """YellowRace class, inherits from Person"""
    color = 'yellow'
    def run(self):
        print('run...')

class Student(Person):
    """Student class, inherits from Person"""

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print('study...')

    def run(self):
        print('run...stu')

# class ChineseStudent(YellowRace,Student):
#     country = 'China'
class ChineseStudent(Student, YellowRace):
    country = 'China'

xzh = ChineseStudent('xzh', '100')

print(xzh.country)
print(xzh.color)
print(xzh.home)
xzh.eat()
xzh.study()
xzh.run()
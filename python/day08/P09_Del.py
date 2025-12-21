"""
This case demonstrates dynamically deleting attributes and methods
del object.attribute_name
delattr(obj, 'attribute_name')
"""

class Student():
    school = 'Stanford University'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat')


xzh = Student('xzh', 18)
xzh.eat()
# delattr(xzh, 'eat')
# xzh.eat()
# delattr(xzh, 'school')
print(xzh.school)
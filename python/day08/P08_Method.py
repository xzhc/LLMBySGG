"""
This case demonstrates methods
"""
#define a method outside the class
def drink(self):
    print(f" {self.name} is drinking...")

class Student:
    """This is a student class"""
    school = 'Stanford University'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance method
    def eat(self):
        print(self.name, self.age, self.school)

    #Class method
    @classmethod
    def get_info(cls, student):
        print(cls)
        print(cls.school)
        print(student.name)
        print(student.age)
        print(cls.__doc__)

    #add funciton to class as a class attribute
    drink1 = drink


student1 = Student('John', 20)
# student1.eat()
student1.get_info(student=student1)

# Student('xzh', 18).drink1()
student1.drink1()
import types
student1.drink = types.MethodType(drink, student1)
student1.drink()




#Static method
class MathUtil:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtil.add(1,2))
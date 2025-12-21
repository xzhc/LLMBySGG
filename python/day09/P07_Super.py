"""
This case demonstrates reusing attributes or methods from parent classes
"""
class Person:

    home = 'earth'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} is eating.')

class YellowPerson(Person):
    color = 'yellow'

    def run(self):
        print(f'{self.name} is running.')

class Student(Person):
    def __init__(self, name, age, grade):
        # Call methods in the parent class -Method 1: via super().parent_method_name
        super().__init__(name,age)
        self.grade = grade

    def study(self):
        print(f'{self.name} is studying.')

class ChineseStudent(Student, YellowPerson):
    country = 'China'

    def xuexi(self):
        super().eat()
        # Call methods in the parent class - Method 1: via ParentClassName.parent_method_name(self)
        # Person.eat(self)
        # Then exercise well
        super().run()
        super().study()
        print(super().home)


xzh = ChineseStudent(name='xzh', age=24, grade=90)
xzh.xuexi()
print(ChineseStudent.__mro__)
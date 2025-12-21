"""This case demonstrates method overriding"""

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('eat method in the parent class')

class ChineseStudent(Student):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    # def eat(self):
    #     print(f'{self.name} eats with chopsticks.')


xzh = ChineseStudent('xzh', 24, 90)

xzh.eat()
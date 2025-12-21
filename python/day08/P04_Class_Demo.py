"""
This case demonstrates the simple defenition of a class and the creation of  objects
"""
#Define a Student Class
class Student:
    """This is a Student class"""
    #Class attribute: shared by all instances of the class
    school = 'MIT'

    #A method that is automatically called when creating a students object(instance)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Instance method: the first parameter of the method is self, representing the current instance object
    #When calling the current method via object.method(), the current object itself is pass to the method
    def play_game(self):
        print(f'The {self.age}-year-old {self.name} is focusing on playing games')

    def study(self):
        print(f'The {self.age}-year-old {self.name} is studying off and on')

    def video(self):
        print(f'The {self.age}-year-old {self.name} is recording a video')

s1 = Student('xzh', 18)
s1.school="Stanford"
s1.play_game()
print(s1.school, s1.age, s1.name)

s2 = Student('lhc', 18)
s2.study()
s2.video()
print(s2.school)
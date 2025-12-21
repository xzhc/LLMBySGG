"""
This case demonstrates annotations related to encapsulation
"""
# @property Convert a method to attribute
# class Person:
#     def __init__(self, name):
#         self.name = name
#     @property
#     def eat(self):
#         print("eat")

# p = Person("xzh")
#By default, when calling an instance method, you must use object.method_name(),
# even if there are no parameters, the parentheses cannot be omitted
# p.eat()
#If the property() annotation is added to the method(converting the method to a property),
# then when calling the instance method, use object.method_name directly
# without adding parentless at the end
# p.eat

# Implement read-only properties via the @property annotation
# class Person:
#     def __init__(self, name):
#         self.__name = name
#
#     @property
#     def name(self):
#         return self.__name
#
# p = Person("xzh")
# print(p.name)
# # AttributeError: property 'name' of 'Person' object has no setter
# p.name = 'lhc'

# Implement read and write properties vua the @property and @name.setter annotaiton
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        #You can also set some interception conditions in the writing method to
        #standardize the writing of private attributes
        if value == 'xhz':
            print('xhz is dennied!')
        else:
            self.__name = value

person = Person("xzh")
print(person.name)
person.name = "lhc"
print(person.name)
person.name = "xhz"

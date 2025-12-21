"""
This case demonstrates the import of module
"""

#Global import -no alias
# import  P01_My_Add
# print(P01_My_Add.num)
# print(P01_My_Add.My_Add(10,20))

#Global import -with alias
# import P01_My_Add as md
# print(md.num)
# print(md.My_Add(10,20))

#Local import - from module_name import member1 [as alias1], member2 [as alias2], ...
#Only imported members can be called, unimported members are inaccessible
# from P03_My_Multi import multi
# print(multi(10,20))
# print(num)

#Local import - from module_name import member1 [as alias1], member2 [as alias2], ...
# For members with the same name, the later imported one will override the previous one
# from P01_My_Add import num
# from P03_My_Multi import num
# print(num)

#Local import - from module_name import member1 [as alias1], member2 [as alias2], ...
#Distinguish varibales from different modules via alias
# from  P01_My_Add import num as n1
# from P03_My_Multi import num as n2
# print(n1)
# print(n2)

#Local import - from module import *
#Import all members not starting with an underscore(_)
# from P03_My_Multi import *
# print(num)
# print(multi(1,2))
# print(_str1)

#Module import order
# import sys
# print(sys.path)
# sys.path.append("D:/")
# print(sys.path)

#Local import - from module import *
#__all__ restricts the importable members
# from P01_My_Add import *
# print(num)
# print(My_Add(10,20))
# print(num1)
# print(_str1)

#With global import, underscore-prefixed members and __all__ restriction do not take effect
# import P01_My_Add
# print(P01_My_Add._str1)
# print(P01_My_Add.num1)
# print(P01_My_Add.num)
# print(P01_My_Add.My_Add(10,20))

#Question: from decimal import Decimal imports the Decimal member from _decimal
# from P01_My_Add import add

# import P01_My_Add

# from P01_My_Add import *

# dir() function
# import math
# print(dir(math))
#
# class MyClass:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def method1(self):
#         pass
#
# obj = MyClass(10, 20)
# print(dir(obj))

num1 = 10
def add(a, b):
    pass

class MyClass:
    pass

print(dir())
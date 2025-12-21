"""
This case demonstrates decorators in Python
"""


#Without decorator, some functions may have incomplete functionality

# from  math import sqrt
#Calculate square root

# def func(n):
#     return sqrt(n)
# print(func(-4))

#Implement a decorator via closure to improve the square root function
# def decorator(func):
#     def inner(n):
#         n = abs(n)
#         res = func(n)
#         return res
#     return inner
#
# def func(n):
#     return sqrt(n)
# inn = decorator(func)
# print(inn(-4))

# Implement decorator functionality via decorator syntactic sugar (@)
# from math import sqrt
# def decorator(func):
#     def inner(n):
#         n = abs(n)
#         res = func(n)
#         return res
#     return inner
#
# @decorator
# def func(n):
#     return sqrt(n)
#
# print(func(-4))

#Multiple decorators - decorators syntactic sugar (@)
#First layer decoration -- add absolute value functionality
# def get_abs(f):
#     def inner(n):
#         n = abs(float(n))
#         res = f(n)
#         return res
#     return inner
# #Second layer decoration -- converting the result to integer
# def get_int(f):
#     def inner(n):
#         res = f(n)
#         res = int(res)
#         return res
#     return inner
#
# #Calculate square root
# @get_int
# @get_abs
# def func(n):
#     return sqrt(n)
#
# print(func('-4'))

#Multiple decorators - manual decoration
#First layer decoration -- add absolute value functionality
# def get_abs(f):
#     def inner(n):
#         n = abs(float(n))
#         res = f(n)
#         return res
#     return inner
# #Second layer decoration -- converting the result to integer
# def get_int(f):
#     def inner(n):
#         res = f(n)
#         res = int(res)
#         return res
#     return inner
#
# def func(n):
#     return sqrt(n)
#
# abs_in = get_abs(func)
# int_abs_in = get_int(abs_in)
# print(int_abs_in('-4'))

#Decorator with parameters
# from  math import sqrt
# def times(count):
#     #Decoration: first calculate absolute value, then calculate square root
#     def decorator(func):
#         def inner(n):
#             n = abs(n)
#             for i in range(count):
#                 n = func(n)
#             return n
#         return inner
#     return decorator
#
# @times(2)  #Equivalent to func = times(2)(func)
# def func(n):
#     return sqrt(n)
# print(func(-16))
# print(func(81))

#Class_based decorator
class DecoratorClass:
    def __init__(self, func):
        self.func = func

    def __call__(self, n):
        n = abs(n)
        res = self.func(n)
        return res

@DecoratorClass
def func(n):
    return n * n

# dec = DecoratorClass(func)
# print(dec.__call__(10))
print(func(10))
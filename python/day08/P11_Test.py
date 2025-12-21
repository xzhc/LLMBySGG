"""
动态添加属性
定义一个 Person 类，在类外动态地给 Person 类的一个对象添加一个 hobby 属性，值为 "reading"，并打印该属性。
"""
import types


class Person:
    pass

person = Person()
person.hobby = "reading"
print(person.hobby)

# 动态添加方法
# 定义一个 Circle 类，该类有一个 radius 属性。
# 在类外定义一个函数 calculate_area，功能是计算圆的面积（面积公式：\(S = π r^2），
# 然后将这个函数动态地添加为 Circle 类的一个对象的方法，并调用该方法计算半径为 5 的圆的面积。
# （提示：可使用 types.MethodType）

import math
def calculate_area(self):
    return math.pi * self.radius ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius

c = Circle(5)

c.calculate_area = types.MethodType(calculate_area, c)
print(c.calculate_area())
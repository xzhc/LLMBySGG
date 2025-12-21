"""
封装特性
定义一个 BankAccount 类，有一个私有属性 __balance（初始余额为 0），
提供一个 deposit 方法用于存钱，一个 withdraw 方法用于取钱，
取钱时如果余额不足则打印提示信息。
"""

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f'Deposited: {amount}, New Balance: {self.__balance}')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrew: {amount}, New Balance: {self.__balance}')
        else:
            print('Insufficient balance.')

"""
继承特性
定义一个 Animal 类，有一个 speak 方法打印 "I am an animal"。
再定义一个 Cat 类继承自 Animal 类，
并重写 speak 方法打印 "Meow"，创建 Cat 类的对象并调用 speak 方法。
"""
class Animal:
    def speak(self):
        print("I am an animal")
class Cat(Animal):
    def speak(self):
        print("Meow")
cat = Cat()
cat.speak()

"""
多态特性
定义一个 Shape 类，有一个抽象方法 area（方法体为空）。
再定义 Rectangle 类和 Circle 类继承自 Shape 类，分别实现 area 方法计算矩形面积（长 × 宽）和圆的面积（\(\pi r^2\)）。
创建 Rectangle 和 Circle 类的对象，将它们放入一个列表中，遍历列表并调用每个对象的 area 方法。
"""

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        import math
        return math.pi * (self.radius ** 2)

shapes = [Rectangle(4, 5), Circle(3)]
for shape in shapes:
    print(f'Area: {shape.area()}')
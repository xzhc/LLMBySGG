"""
函数定义与调用
定义一个函数 add_numbers，它接受两个整数参数 a 和 b，返回这两个数的和，并调用该函数计算 3 和 5 的和。
"""
def add_numbers(a, b):
    return a + b

sum = add_numbers(3,5)
print(sum)

"""
题目 2：默认参数
定义一个函数 greet，它接受一个字符串参数 name，并且有一个默认参数 message，默认值为 "Hello"，
函数功能是打印出问候语，如 "Hello, Alice"。调用该函数时，分别传入和不传入 message 参数进行测试。
"""

def greeting(name, message="Hello"):
    print(f"{message}, {name}")
greeting("Bob")
greeting("Bob","Byebye")

"""
可变参数
定义一个函数 sum_all，它接受任意数量的整数参数，返回所有参数的和。
例如调用 sum_all(1, 2, 3) 应返回 6，调用 sum_all(10, 20, 30, 40) 应返回 100。
"""

def sum_all(*args):
    total = 0
    for number in args:
        total += number
    return total
sum1 =sum_all(1, 2, 3)
sum2 =sum_all(10, 20, 30, 40)

print(sum1, sum2)

"""
函数的嵌套调用
定义两个函数，square 函数接受一个整数参数，返回该数的平方；cube 函数接受一个整数参数，
通过调用 square 函数返回该数的立方（立方 = 平方 × 该数）。调用 cube 函数计算 3 的立方。
"""

def square(number):
    return number * number
def cube(number):
    return square(number)*number

result = cube(3)
print(result)
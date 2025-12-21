"""
This cade demonstrates generators
"""

#Create a generator object - using a generator expression(tuple comprehension style)
# generator = (x for x in  range(5))
# print(generator)
#
# for x in generator:
#     print(x)

#Create a generator object - using a function
# def fibo():
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a + b
#
# f = fibo()
#
# print(type(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

#Create a generator object - using a function, get the function return value
# def feibo_ret():
#     a, b, count = 0, 1, 0
#     while count < 10:
#         yield b
#         a, b, count = b, a + b, count + 1
#     return 'done'
# f = feibo_ret()
#
# try:
#     while True:
#         print(next(f))
# except StopIteration as e:
#     print('Generator return value:', e.value)

#Send value to the generator as the result of the yield expression
#Case: Send a task ID via send() to make the generator execute two tasks alternately
def generator():
    task_id = 0
    int_value = 0
    char_value = 'A'
    while True:
        match task_id:
            case 0:
                task_id = yield int_value
                int_value += 1
            case 1:
                task_id = yield char_value
                char_value = chr(ord(char_value) + 1)
            case _:
                yield #return None
g = generator()
# print(next(g))
print(g.send(None))# 等价于 next(g)，启动生成器 → 输出# 0
print(g.send(0))
print(g.send(1))
print(g.send(0))
print(g.send(1))

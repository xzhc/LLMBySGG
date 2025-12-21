import math_operations
"""
创建一个简单的 Python 模块math_operations.py，其中定义两个函数add和multiply，
分别用于实现两个数的加法和乘法运算。
在另一个 Python 文件中导入该模块，并调用这两个函数计算3 + 5和3 * 5的结果。
"""
result_add = math_operations.add(3, 5)
result_multiply = math_operations.multiply(3, 5)
print(f'3 + 5 ={result_add}')
print(f'3 * 5 ={result_multiply}')

"""
使用生成器表达式创建一个生成器，生成 1 到 10 的偶数。
然后使用for循环遍历该生成器，打印每个偶数。
"""
even_numbers = (x for x in range(1, 11) if x % 2 == 0)
for number in even_numbers:
    print(number)

"""
创建一个迭代器类MyIterator，用于遍历一个给定列表的元素。
实现__iter__和__next__方法。使用该迭代器类遍历列表[10, 20, 30, 40]，并打印每个元素。
"""

class MyIterator():
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        else:
            value = self.data[self.index]
            self.index += 1
            return value

my_list = [10, 20, 30, 40]
my_iterator = MyIterator(my_list)
for number in my_iterator:
    print(number)
"""
编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，
如果转换失败，捕获 ValueError 异常，将异常信息记录到一个文本文件 error.log 中。
"""

# try:
#     num = int('123abc')
#     print(num)
# except ValueError as e:
#     with open('error.log', 'a', encoding='utf-8') as file:
#         file.write(str(e) + '\n')

"""
定义一个函数check_age，该函数接受一个年龄参数。
如果年龄小于 0，抛出一个自定义异常InvalidAgeError；如果年龄大于 120，抛出UnrealisticAgeError。
这两个自定义异常类都继承自Exception类。调用该函数并传入一个不合法的年龄值，捕获并处理异常。
"""
class InvalidAgeError(Exception):
    pass
class UnrealisticAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise InvalidAgeError('Age can not be negative')
    elif age > 120:
        raise UnrealisticAgeError('Age can not be greater than 120')

try:
    # check_age(-2)
    check_age(123)
except InvalidAgeError as e:
    print(e)
except UnrealisticAgeError as e:
    print(e)
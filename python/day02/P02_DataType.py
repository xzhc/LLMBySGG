"""
该案例演示数据类型
"""
#====================整数类型==============
#如果数字较大，可以用下划线优化显示效果，实际输出结果不会变化（Python3特性）
#num1 = 1_000_000_000_000
#print(num1)

# num1 = 10
# num2 = True
# print(num1)
# print(num2)


#type(参数)查看参数类型
#isinstance(num1, int)判断参数类型
#type不会认为子类是父类的一种类型，isinstance()会认为子类是父类的一种类型
# print(type(num1))
# print(type(num2))
# print(isinstance(num1, int))
# print(isinstance(num2, bool))
# print(isinstance(num2, int))
# print(type(num1) == type(num2))


#====================小整数池==================
# num1 = 7890
# num2 = 7890
# print(num1)
# print(num2)
#id()获取变量值在内存的地址
# print(id(num1))
# print(id(num2))

#=================浮点数========================
# num1 = 0.1
# num2 = 0.2
# 注意：在任何的编程语言中，浮点数类型都存在丢失精度的情况
# print(num1+num2)

# 为了解决浮点数丢失精度情况，可以借助python其它模块提供的功能
# from decimal import Decimal
# num1 = Decimal("0.1")
# num2 = Decimal("0.2")
# print(num1+num2);
#
# num4 = 3.14e7
# print(num4);

#=====================布尔型=======================
# num1 = True
# num2 = False
# print(num1, num2)
# print(type(num1), type(num2))
# # bool是int的子类型，可以和整数进行运算
# print(num1 + 10)
# # == 比较运算符   判断==左右两边的值是不是相等
# print(num1 == 1)
# print(num2 == 0)
# # is 判断左右两边是否指向内存中的同一个地址
# print(num1 is 1)
# print(num2 is 0)

#======================字符串=========================
# 字符串的表现形式      ''      ""          """   """
# str1 = 'hello'
# str2 = 'world'
# str3 = """hello
#     world """
# print(str1)
# print(str2)
# print(str3)

# str4 = "hell'o w'orld"
# print(str4)

# \在行尾作为续航符
# print("hello \
#       world")

# \\反斜杠符
# print("hello \\ hello")
#
# # \'单引号
# print("hello \' world")
# # \"双引号
# print("hello \"world")
# # \b退格
# print("hello \bworld")
# # \n 换行
# print("hello \n hello")
# # \t横向制表符
# print("hello \t hello \t hello")
# # \r回车，回到行首
# print("hellohe\rllo")

str1 ='hello world'
str2 = 'hello world'
print(id(str1), id(str2))
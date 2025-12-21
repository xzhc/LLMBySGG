"""
该案例演示了python的输出
"""
#==========1.普通输出=========
# print("hello world")
# print("hello" + "world" + "byebye")
# name = input("Please input your name: ")
# print("Your name is:" + name)
# print("Your name is:",name )

# print("hello world", end="\n")
# print("hello world", end="")

#============格式化输出==============
#（1）.字符串使用%占位
# num1 = 10
# num2 = 3.14
# str1 = "num1 =%d, num2 = %.3f" % (num1, num2)
# print(str1)

# (2).字符串.format()----不设置指定位置，按默认顺序
# num1 = 10
# num2 = 3.14
# num3 = False
# str = "num1={}, num2={}, num3={}".format(num1, num2, num3)
# （2）字符串.format()----设置指定位置，不能和方式1混合使用
# str = "num1={1} num2={0} num3={2}".format(num1, num2, num3)
# （2）字符串.format()----设置参数
# str = "num1={n1} num2={n3} num3={n2}".format(n1=num1, n3=num3, n2=num2)
# print(str)

#(3)数字格式化
# float1 = 31415.9
# str1 = "{:*^20,.2f}".format(float1)
# str2 = "{:*<20,.2f}".format(float1)
# str3 = "{:*>20,.2f}".format(float1)
# print(str1)
# print(str2)
# print(str3)

# # （4）使用大括号 {} 来转义大括号
# print("{0}对应的是{0}".format("hello"))
# print("{0}对应的位置是{{0}}".format("hello"))

# （5）f-字符串
num1 = 10
num2 = 3.14
str1 = "num1={}, num2={}".format(num1, num2)
str2 = f"num1={num1}, num2={num2}"
print(str1)
print(str2)

#要求：指定名字必须得相同
str3 = f"{num1=}, {num2=}"
print(str3)
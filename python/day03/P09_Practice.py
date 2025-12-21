"""
### 题目 1：分支语句
编写一个 Python 程序，输入一个整数，判断它是正数、负数还是零，并输出相应的结果。
"""
# num = int(input("请输入一个整数"))
# if num > 0:
#     print(f"{num}是正数")
# elif num == 0:
#     print(f"{num}是0")
# else:
#     print(f"{num}是负数")

"""
题目 2：循环语句
使用for循环打印出 1 到 10 的整数。
"""
# for i in range (1, 11):
#     print(i)

"""
题目 3：分支与循环结合
编写一个程序，从 1 循环到 10，当数字是偶数时打印 “偶数”，奇数时打印 “奇数”。
"""
# num = 1
# while num<=10:
#     if num %2 == 0:
#         print(f"{num}是偶数")
#     else:
#         print(f"{num}是奇数")
#     num += 1

"""
题目 4：循环控制
编写一个while循环，计算 1 到 100 的整数之和。
"""
num = 1
sum = 0
while num <= 100:
    sum += num
    num += 1
print(sum)
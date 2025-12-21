"""
该案例演示了运算符
"""

# ===============算术运算符=================
# num1 = 10
# num2 = 4
# # 加
# print(num1 + num2)
# # 减或取负
# print(num1 - num2)
# # 乘
# print(num1 * num2)
# #除
# print(num1 / num2)
# # 整除，除后向下取整
# print((num1 // num2))
# # 模，返回除法的余数
# print(num1 % num2)
# #幂
# print(num2 ** 3)

# ================赋值运算符=============
# num1 = 10
# +=加法赋值
# num1 += 5;
# -=减法赋值
# num1 -= 5
# *=乘法赋值
# num1 *= 2
# /=除法赋值
# num1 /= 5
# //=整除赋值
# num1 //= 4
# %=模赋值
# num1 %=4
# **=幂赋值
# num1 **= 2
# :=	海象运算符，在表达式中同时进行赋值和返回赋值的值。Python3.8 版本新增
# print((num2 := num1 * 2) > num1)
# print(num2)

#================比较运算符====================
# num1 = 10
# num2 = 20
# # == 相等，比较二者的值
# print(num1 == num2)
# # != 不相等
# print(num1 != num2)
# # > 大于
# print(num1 > num2)
# # < 小于
# print(num1 < num2)
# # >=大于等于
# print(num1 >= num2)
# # <=小于等于
# print(num1 <= num2)

#====================逻辑运算符=================
# and	与，描述的是并且的关系，参与运算的两个数同时true，表达式返回true            x and y，若x为False返回x的值，否则返回y的值
# or	或，描述的是或者的关系，参与运算的两个数只要有一个为true，表达式返回true     x or y，若x为True返回x的值，否则返回y的值
# not	非，not x，若x为True返回False，若x为False返回True

# b1 = False
# b2 = True
# print(b1 and b2)
# print(b1 or b2)
# print(not b1)
# print(not b2)

# print(5 and  8)
# print(0 and 8)
# print(5 or 8)
# print(0 or 8)

#=================位运算符===================

#正数的位运算
# num1 = 17
# num2 = 13

#全1则1
# print(f"正数与运算：{num1} & {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2: 08b}")
# print(f"{num1 & num2 :3} : {num1 & num2 :08b}")
# print()

#有1则1
# print(f"正数或运算：{num1} | {num2}")
# print(f"{num1:3}: {num1:08b}")
# print(f"{num2:3}: {num2:08b}")
# print(f"{num1 | num2 :3}: {num1 |num2:08b}")

#不同则1
# print(f"正数异或运算：{num1} ^ {num2}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num2:3} : {num2:08b}")
# print(f"{num1 ^ num2 :3b} : {num1 ^ num2 :08b}")

#取反
# print(f"非运算： ~{num1}")
# print(f"{num1:3}原码：{num1:08b}")
# print(f"{num1:3}取反：{(1 << 8) - 1 ^ num1:08b}, 得到结果的补码")
# print(f"{~num1:3}原码：{~num1:08b},计算出结果的源码")

#负数的位运算
"""
当负数参与位运算时，Python（以及绝大多数编程语言）遵循一个绝对的核心规则：
核心规则：一切皆基于“补码”
计算机不认识负号，它只认识补码。 所以在进行任何位运算（&, |, ^, <<, >>）之前，必须先把负数想象成它的补码形式，算完后再变回十进制。
但在 Python 中，有一个非常特殊的点需要注意：Python 的整数是“无限长”的。
这意味着：
正数左边有无穷多个 0（...00000101）
负数左边有无穷多个 1（...11111011）<-- 这点最关键！
"""
# num1 = 17
# num2 = 13
# num3 = -12

# num4 = 4
# print(num4 << 1)

# print(f"负数参与的与运算：{num3} & {num1}")
# print(f"{num3:3}原码：{num3:08b}")
# print(f"{num3:3}反码：{(( 1 << 8) -1) + num3:08b}")
# print(f"{num3:3}补码：{(( 1 << 8))  + num3:08b}")
# print(f"{num1 & num3:3}补码：{num1&num3:08b}, 得到结果")
#
#
# print(f"有负数的或运算: {num3} | {num1}")
# print(f"{num3:3}原码 : {num3:08b}")
# print(f"{num3:3}反码 : {(1 << 8) - 1 + num3:08b}")
# print(f"{num3:3}补码 : {(1 << 8) + num3:08b}")
# print(f"{num1:3}补码 : {num1:08b}")
# print(f"{num1 | num3:3}补码 : {(1 << 8) + (num1 | num3):08b}，得到结果的补码")
# print(f"{num1 | num3}原码 : {num1 | num3:08b}，计算出结果的原码")

# 按位左移。右移运算
# num1 = 17
# num2 = -12
# offset = 1
# print(f"左移运算：{num1} << {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 << offset:3} : {num1 << offset:08b}")

# offset = 3
# print(f"右移运算: {num1} >> {offset}")
# print(f"{num1:3} : {num1:08b}")
# print(f"{num1 >> offset:3} : {num1 >> offset:08b}")

# offset = 3
# print(f"右移运算: {num2} >> {offset}")
# print(f"{num2:3}原码\t\t: {num2:08b}")
# print(f"{num2:3}反码\t\t: {(1 << 8) - 1 + num2:08b}")
# print(f"{num2:3}补码\t\t: {(1 << 8) + num2:08b}")
# print(f"{num2:3}补码>>{offset}\t: {(((1 << 8) + num2) >> offset) | (0xff >> 5 << 5):08b}，得到结果的补码")
# print(f"{num2 >> offset:3}\t\t\t: {num2 >> offset:08b}，计算出原码")

#===================成员运算符==================
# num1 = 10
# num2 = 20
# numbers = [10,20,30,40,50]
# print(num1 in numbers)
# print(num2 not in numbers)


#==================身份运算符=====================
# m = 20
# n = 20
# q = 30
# print(m is  n) # True 判断m和n在内存中是否指向同一个地址
# print(m is q)
# print(n is not q)
# # id() 用于获取对象在内存中的地址
# print(id(m)==id(n))

# print('*' * 20)
# -------------is和==的区别---------------
# == —— 比较“值”是否相等
# 作用：比较两个对象的内容或值是否相同。
# 底层调用：调用对象的 __eq__() 方法。
# 适用于所有可比较类型（如数字、字符串、列表、字典等）。
# is —— 比较“身份”是否相同（即是否指向同一个对象）
# 作用：比较两个变量是否引用同一个对象（内存地址是否相同）。
# 本质：检查 id(obj1) == id(obj2)。
# 常用于判断是否为 None、True、False 等单例对象
# a = [1,2,3]
# b = a
# a[:] 是列表切片，它会创建一个新的列表对象，内容与 a 相同（浅拷贝）。
# 然后把新列表赋值给 b。
# 所以现在 b 不再指向原来的 a 对象，而是指向一个副本
# b = a[:]
# print(b is a)
# print(b == a)

# import sys;print(sys.path) #没有问题

# import sys
# for i in sys.path:
#     print(i) #没有问题
#
# import sys;for i in sys.path:;print(i) # 报错

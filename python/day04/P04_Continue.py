"""
    该案例演示了continue和break和pass关键字
"""
# 案例：打印0-9，跳过偶数。
# continue关键词

# for i in range(10):
#     if i % 2 == 0:
#         #跳过当前循环块中的剩余语句，继续进行下一轮循环。一般写在if判断中。
#         continue
#     print(i)

# break关键词
# for i in range(10):
#     if i % 2 == 1:
#         #跳出当前for或while的循环体，一般写在if判断中
#         break
#     print(i)

# 案例：求0-9每个数自己幂自己的加和，如果大于10000000则循环终止。
# sum = 0
# for i in range(0,10):
#     sum = sum + i ** i
#     if sum > 10000000:
#         break
# print(sum, i)


"""
pass是空语句，是为了保持程序结构的完整性。
pass不做任何事情，一般用做占位语句。
例如：在一个循环中，如果循环体为空，语法会提示报错，
这个时候我们就可以使用pass占位
"""
# pass关键字  --- 占位
# for i in range(10):
#     pass

# 循环 + else
# target = 3
#
# for i in [1,2,3,4,5,6,7,8,9]:
#     if i == target:
#         print(f"当前要找的{target}在列表中")
#         break
# else:
#     print(f"当前列表中没有要找的{target}")

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print("%d等于%d*%d" %(n, x, n / x))
            break
    else:
        print("%d是质数" %n)
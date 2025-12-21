"""
该案例演示了元组的常用操作
"""

#创建元组
tuple1 = (100, 200, 300, 400, 500)
# print(tuple1)
# #如果元组中只有一个元素，那么在元素的后面也需要需要,
# tuple2 = (100,)
# list1 = [ i for i in range(10) ]
# print(list1)
# #使用生成器表达式创建元组
# tuple3 = tuple( i * 2 for i in range(10) )
# print(tuple3)
# print(tuple3, type(tuple3))

#访问元组
# print(tuple1[0])
# print(tuple1[0:-2])

#元组相加
# tuple2 = ("a", "b", "c", "d", "e")
# print(tuple1 + tuple2)

#元组相乘
# print(tuple1 * 2)

#检查成员在元组中吗
# print(100 in tuple1)
# print(1000 in tuple1)

#获取元组长度
# print(len(tuple1))

#求元组中的最大值、最小值、和
# print(max(tuple1))
# print(min(tuple1))
# print(sum(tuple1))

#遍历元组
# for item in tuple1:
#     print(item)
# for i in range(len(tuple1)):
#     print(tuple1[i])

# for i, item in enumerate(tuple1):
    # print(i, item)

#元组的不可变性
# print(tuple1,id(tuple1))
# tuple1 = tuple1 + (1, 2, 3, 4, 5)
# print(tuple1, id(tuple1))
# TypeError: 'tuple' object does not support item assignment
# tuple1[0] = 10
# print(tuple1, id(tuple1))

#如果元组中元素是可变数据类型，其嵌套项可以被修改
tuple2 = (100, 200, 300, [1,2,3])
tuple2[3].append(4)
print(tuple2)
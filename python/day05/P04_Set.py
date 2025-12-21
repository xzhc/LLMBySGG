"""
该案例演示Set基本操作
"""
# Set1 = {1,2,3}
# Set2 = set([range(10)])
#如果创建空Set需要用Set()而不是{}，后者创建的是一个dict
# Set3 = set()
# print(Set1, type(Set1))
# print(Set2, type(Set2))
# print(Set3, type(Set3))


#添加和删除元素
# Set1 = { i * 2 for i in range(10) }
# Set1 = {100, 200, 300, 400, 500}
#add element
# Set1.add(21)
#delete element
# Set1.remove(21)
# print(Set1)
# select element randomly
# print(Set1.pop())
# print(Set1)


#check  element whether it in set
set1 = {1, 2, 3, 4, 5}
# print(1 in set1)
# print(2 not in set1)

# get the length of set
# print(len(set1))

# get the max, min and sum in set
# print(max(set1))
# print(min(set1))
# print(sum(set1))

#Set's elements can not repeat
# set1.add(1)
# set1.add(1)
# print(set1)

# 遍历
for item in set1:
    print(item)
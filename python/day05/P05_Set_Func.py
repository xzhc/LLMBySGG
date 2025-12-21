"""
该案例演示了set集合常用的函数
"""

# set1 = set([100, 200, 300, 400, 500])
#add element x  set.add(x)
# set1.add(600)
#set update(x) add elements x can be list 、tuple、 string and dict (Iterable object)
# set1.update([600, 700])

#set.union(x) return a new set after adding element, x can be list 、tuple、 string and dict (Iterable object)
# set2 = set([600, 700, 800, 900, 1000])
# set3 = set1.union(set2)
# print(set1, set2, set3, id(set1), id(set2), id(set3))

#set.remove(x) remove x from set, report errors if x not exists
# set1.remove(100)
# print(set1)
# Traceback (most recent call last):
#   File "F:\Tech\SoftwareEnginner\LLMBySGG\python\day05\P05_Set_Func.py", line 19, in <module>
#     set1.remove(100)
#     ~~~~~~~~~~~^^^^^
# KeyError: 100
# set1.remove(100)

#set.dsicard(x) remove x from set, do not report errors even x not exists
# set1.discard(100)
# set1.discard(600)

#set.pop() get a element randomly from set, it will appear errors if x not exists
# print(set1.pop())

#set.clear() clear the set
# set1.clear()

#set.difference(x1, ...) Compute the difference between set1 and x1, and return a new set
set2 = set([400, 500, 600])
# print(set1.difference(set2))
# print(set2.difference(set1))

# set.difference_update(x1, ...) compute difference between set1 and x1
# set1.difference_update(set2)
# print(set1)
# set2.difference_update(set1)
# print(set2)

#set.intersection(x1, ...) Compute the intersection of set1 and x1, and return a new set
# print(set1.intersection(set2))
# print(set2.intersection(set1))

#set.intersection_update(x1, ...) compute the intersection of set1 and x1
# set1.intersection_update(set2)
# print(set1)

#set1 & set2 two sets compute intersection
# print(set1 & set2)

#set1 | set2 compute the union of the two sets
# print(set1 | set2)

#set1 - set2 Compute the difference of the two sets
# print(set1 - set2)
# print(set2 - set1)

#determine if the two sets are disjoint
# print(set1.isdisjoint(set2))

#determine if set1 is a subset of set2
# set1 = {300,400}
# set2 = {300,400,600}
# print(set1.issubset(set2))

#determine if set2 is a subset of set1
# print(set2.issubset(set1))

# get the unique element from two sets and return a new set
# set1 = {300, 400, 600}
# set2 = {300, 400, 500}
# # print(set1.symmetric_difference(set2))
# #get the unique element from two sets
# set1.symmetric_difference_update(set2)
# print(set1)

#copy sets
# set1 = {100,200,300,400}
# set2 = set1.copy()
# print(set2, id(set2))
# print(set1, id(set1))

# len(set)	返回集合元素个数
# max(set)	求集合中元素的最大值
# min(set)	求集合中元素的最小值
# sum(set)	求集合中元素的加和

set1 = set([400, 500, 600])
print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
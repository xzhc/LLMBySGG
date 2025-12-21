"""
现有集合 set1 = {1, 2, 3, 4, 5} 和 set2 = {3, 4, 5, 6, 7} 。

1. 求这两个集合的并集。
2. 求这两个集合的交集。
3. 从 set1 中移除元素 3
"""
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(set1.union(set2))
# print(set1.intersection(set2))
# set1.remove(3)
# print(set1)

"""
字典 person = {'name': 'Alice', 'age': 25, 'city': 'New York'} 。
1. 获取字典中 'age' 对应的值。
2. 向字典中添加一个键值对 'job': 'Engineer' 。
3. 删除字典中 'city' 这个键值对。
"""
# person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# print(person["age"])
# person["job"] = "Engineer"
# print(person)
# del person["city"]
# print(person)

"""
创建一个集合，包含数字 1 到 5 。再创建一个字典，键为集合中的数字，值为该数字的平方。
"""

num_set = {i for i in range(1, 6)}
num_dict = {num: num ** 2 for num in num_set}
print(num_set)
print(num_dict)
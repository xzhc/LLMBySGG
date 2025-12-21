"""
This case further explains anonymous functions
"""

#list1 The collection to be processed
#func The processing logic for elements in the collection

def my_map(list1, func):
    for i, item in enumerate(list1):
        # func(item)
        list1[i] = func(item)
    return list1

list1 = [1, 2, 3]
print(my_map(list1, lambda x: x * 2))
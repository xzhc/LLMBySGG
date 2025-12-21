"""
This cade demonstrates iterators
"""

#Demonstrate that most container types can be traversed with a for loop
#and we refer to them as iterable types(Iterable)
# for elem in [1, 2, 3, 4]:
    # print(elem)

# for elem in (1, 2, 3, 4):
#     print(elem)

# for key in {'name':'Tom', 'age':20}:
    # print(key)

# for char in 'Python':
#     print(char)
import os
# with open('myfile.txt', 'w') as f:
#     f.write('h\ne\nl\nl\no\n')
# for line in open('myfile.txt', 'r'):
#     print(line, end='')

# os.remove('myfile.txt')


# from collections.abc import Iterable
# #Check whether a type is iterable
# print(isinstance([], Iterable))
# print(isinstance((),Iterable))
# print(isinstance({},Iterable))
# print(isinstance(set(),Iterable))
# print(isinstance('hello',Iterable))
# print(isinstance(123,Iterable))

# from collections.abc import Iterator
# #Check whether a type is an iterator
# print(isinstance((), Iterator))
# print(isinstance(set(), Iterator))
# print(isinstance({}, Iterator))
# print(isinstance('100', Iterator))
# print(isinstance((x for x in range(10)), Iterator))
# print(isinstance(iter([]), Iterator))

# Create an iterator object from a container manually
#
# print(type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# for item in iterator:
#     print(item)

#Custom Iterator - implement the function to reverse elements in a container
class Reverse:
    #data represents the data to be iterated over
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    #An iterator must implement __iter__() method that returns the iterator object itself
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.data[self.index]

rev = Reverse([1, 2, 3, 4, 5])
# for item in rev:
#     print(item)
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))
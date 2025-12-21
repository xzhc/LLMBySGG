"""This case demonstrates shallow and deep copy"""

#Shallow Copy - [:],list(),copy()
# list1 = [1, 2, [3, 5], 4]
# list2 = list1.copy()
#
# #Modify immutable type data in the list
# list1[0] = 10
# #Modify mutable type data in the list
# list1[2].append(6)
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)


#Deep Copy - copy.deepcopy()
# import copy
# list1 = [1, 2, [3, 5], 4]
# list2 = copy.deepcopy(list1)
#
# list1[0] = 10
# list1[2].append(6)
# print(id(list1), id(list1[0]), id(list1[1]), id(list1[2]), id(list1[3]), list1)
# print(id(list2), id(list2[0]), id(list2[1]), id(list2[2]), id(list2[3]), list2)

#Special cases of copying
#(1) Non-container types(e.g., number, string and other 'atomic' type objects) are immutable types, so shallow copy and deep copy have the same effect.
import copy
# var1 = 123
# var2 = copy.copy(var1)
# var3 = copy.deepcopy(var1)
# print(id(var1), id(var2), id(var3), var1, var2, var3)
#(2)Tuple variables containing only atomic (immutable) type objects,cannot  be deep copied,shallow copy and deep copied.
# tuple1 = (1, 2, 3, 4)
# tuple2 = copy.copy(tuple1)
# tuple3 = copy.deepcopy(tuple1)
# print(id(tuple1), id(tuple2), id(tuple3), tuple1, tuple2, tuple3)
tup1 = (1, 2, 3, [4,5])
tup2 = copy.deepcopy(tup1)
tup1[3].append(6)
print(id(tup1), tup1)
print(id(tup2), tup2)
"""
Exercise on modifying element in a list through functions
Requirement:The function needs to process the list without modifying the original list
Example:
    There is a list, list[1,2,3,[100,200,300]]
    Define a function to append a new element 400 to the sublist in the list
    ===>list[1,2,3,[100,200,300,400]]
"""
from day06.P04_Param_Pass import change_int

list1 = [1,2,3,[100,200,300]]
def change_list(m_list):
    """
    This function demonstrates append
    :param m_list:
    :return:
    """
    print(id(m_list))
    m_list[3].append(400)
    print(m_list)
    print(id(m_list))

change_list(list1)


#Shallow copy

import copy
# list2 = copy.copy(list1)
# list2.append(400)
# list2[3].append(500)
# print(list1,list2)
# print(id(list1[3]),id(list2[3]))

#deep copy
# list2 = copy.deepcopy(list1)
# list2.append(400)
# list2[3].append(500)
# print(list1,list2)
# print(id(list1[3]),id(list2[3]))

help(change_list)
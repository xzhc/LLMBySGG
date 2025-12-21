"""
This case demonstrates anonymous functions
"""

#Requirement:Implement a simple calculator for +,-,*,/ operations of two numbers
# def open1(num1,num2):
#     return num1+num2
# def open2(num1,num2):
#     return num1-num2
# def open3(num1,num2):
#     return num1*num2
# def open4(num1,num2):
#     return num1/num2

#Define a calculation function receives two numbers involved in the operation
# and call the relevant operation method to perform the calculation
# def cal(num1, num2, op):
#     return op(num1, num2)
#
# print(cal(20,10,lambda x,y: x + y))
# print(cal(20,10,lambda x,y: x - y))
# print(cal(20,10,lambda x,y: x * y))
# print(cal(20,10,lambda x,y: x / y))

#There are three students with names and ages, sort them by age
student_list = [{"name": "zhang3", "age": 36},
                {"name": "li4", "age": 14},
                {"name": "wang5", "age": 27}]
# def getKey(student):
#     return student["age"]
# student_list.sort(key=getKey)
student_list.sort(key=lambda student: student["age"])
print(student_list)
# print(getKey(student_list[0]))


#The map() function process each element in the sequence one by one
# list1 = [1,3,5,7,9]
# print(list(map(lambda item: item*item, list1)))

#The filter() function filters elements in the sequence
list1 = [0,-1,3,-7,9]
print(list(filter(lambda item: item < 0, list1)))

#The reduce() function accumulates elements in the sequence
from functools import reduce
list1 = [1,2,3,4,5]
print(reduce(lambda x,y: x*y, list1))


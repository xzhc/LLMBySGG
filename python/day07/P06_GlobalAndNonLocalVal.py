"""
This case demonstrates the global and nonlocal keywords
"""
# var1 = 10
# def func():
#     #Assignment via += operation will throw an error, as the local variable is considered undefined
#     var1 += 10
#     print(var1)
# func()

# var1 = 10
# def func():
#     #Declaration:Use the global variable var1 in the current local scope
#     global var1
#     var1 = 20
#     print(f"var1 in local scope: {var1, id(var1)}")
# func()
# print(f"var1 in global scope: {var1, id(var1)}")

# list1 = [1,2,3]
# def func1():
#     # list1[0] = 100
#     list1 = [2,3,4]
#     print(f"list1 in local scope = {list1, id(list1)}")
# func1()
# print(f"list1 in global scope = {list1, id(list1)}")


def outer():
    var1 = 10
    def inner():
        nonlocal var1
        var1 = 20
        print(f"var1 in local scope = {var1, id(var1)}")
    inner()
    print(f"var1 in global scope = {var1, id(var1)}")
outer()
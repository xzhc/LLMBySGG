"""
This case demonstrates the porameters of a function
Requirement:First print a 2x3 grid of asterisks(), then print a 1x6 grid of asterisks().
"""

#Do not extract functions
# num = 2
# while num > 0:
#     print("*" * 3)
#     num = num - 1
# print("="* 20)
# num = 1
# while num > 0:
#     print("*" * 6)
#     num = num - 1

#Extract a function
# def print_star_1():
#     num = 2
#     while num > 0:
#         print("*" * 3)
#         num =  num - 1
#
# def print_star_2():
#     num = 1
#     while num > 0:
#         print("*" * 6)
#         num = num - 1
#
# print_star_1()
# print("=" * 20)
# print_star_2()

#Extract a function (add parameters)
def print_star(row, col):
    while row > 0:
        print("*" * col)
        row -= 1
print_star(2, 3)
print('=' * 20)
print_star(1, 6)
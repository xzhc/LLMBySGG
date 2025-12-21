"""
This case demonstrates the recursion of functions
Case:Calculate the factorial of an integer n
5! = 5 * 4 * 3 * 2 * 1
"""

#Without using recursion
# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res
#
# print(factorial(5))

#Using recursion
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
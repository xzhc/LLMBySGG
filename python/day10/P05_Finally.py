"""
This case demonstrates the use of finally in exception handling
"""

try:
    result = 5 / 2
except ZeroDivisionError as e:
    print(e)
else:
    print(result)
finally:
    print('finally')

print('End')
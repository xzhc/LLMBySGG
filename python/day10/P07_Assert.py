"""
This case demonstrates
"""
from logging import exception


def int_add(x,y):
    # if not (isinstance(x, int) and isinstance(y, int)):
    #     raise TypeError('Incorrect parameter type.')
    assert isinstance(x, int) and isinstance(y, int), 'Incorrect parameter type.'
    return x+y

print(int_add(1,'2'))
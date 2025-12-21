"""
This case demonstrates  raising exceptions with the raise statement
"""

def add(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise TypeError('Incorrect parameter type.')

try:
    #print(add(1, 2))
    print(add(1, '2'))

except TypeError as e:
    print(f'Error: {e}')
except Exception as e:
    print(f'Unexcepted Error: {e}')
print('End')
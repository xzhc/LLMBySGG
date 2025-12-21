"""
This case demonstrates exception types
"""
try:
    result = 3/ 0
    print('An exception has occurred.')
except NameError as e:
    print(e)
except (RuntimeError, TypeError) as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except:
    print('Unexcepted error.')

print('End')
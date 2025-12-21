"""
This case demonstrates exception propagation
"""

try:
    try:
        try:
            result = 3 / 0
        except NameError as e:
            print("Inner NameError:", e)
    # except ZeroDivisionError as e:
    #     print("Middle ZeroDivisionError:", e)
    except TypeError as e:
        print("Middle TypeError:", e)
except Exception as e:
    print("Outer Exception:", e)

def m1():
    m2()

def m2():
    m3()
def m3():
    print(3/0)

m1()
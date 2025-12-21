"""
This case demonstrates return of function
"""

def func():
    pass
    return

print(func())

def func2():
    for i in range(100):
        if i == 5:
            # continue
            # break
            return
        print(i)

    print("for-loop is over")

print(func2())


def sum(num1, num2):
    return num1 + num2

print(sum(2, 3))

def func3(a,b,c):
    print(a,b,c)
    return (a,b,c), [a,b,c]

result = func3(1, 2, 3)
print(result)
print(type(result))
"""
使用multiprocessing模块创建两个进程，
一个进程打印从 1 到 5 的数字，
另一个进程打印从 6 到 10 的数字。
"""

# def print_number1():
#     for i in range(1, 6):
#         print(f'Process1:{i}')
#
# def print_number2():
#     for i in range(6, 11):
#         print(f'Process2:{i}')
#
# if __name__ == '__main__':
#     import multiprocessing
#     p1 = multiprocessing.Process(target=print_number1)
#     p2 = multiprocessing.Process(target=print_number2)
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


"""
使用threading模块创建两个线程，
一个线程打印 10 次 "Hello"，另一个线程打印 10 次 "World"。
"""

def print_hello():
    for i in range(10):
        print('Hello')

def print_world():
    for i in range(10):
        print('World')

if __name__ == '__main__':
    import threading
    t1 = threading.Thread(target=print_hello)
    t2 = threading.Thread(target=print_world)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
"""
This case demonstrates that variables are not shared between process
"""

import multiprocessing
import os

# Add 10 elements to the list
def func(list1):
    for i in range(10):
        list1.append(i)
        print(f'Current process id: {os.getpid()}, list1: {list1}')

if __name__ == '__main__':
    # Create a list
    list1 = []
    # Create two child processes
    p1 = multiprocessing.Process(target=func, args=(list1,))
    p2 = multiprocessing.Process(target=func, args=(list1,))
    # Start the child process
    p1.start()
    p2.start()
    # Wait for the child process to finish
    p1.join()
    p2.join()
    print('done',os.getpid(),list1)
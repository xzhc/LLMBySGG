"""
This case demonstrates sharing data between processes using a Queue
"""
import multiprocessing
import os
import time
import random

# Put data to the Queue (Producer)
def func1(queue):
    while True:
        num = random.randint(1, 50)
        queue.put(num)
        print(f'Process ID: {os.getpid()}, put {num} to the queue')
        time.sleep(0.5)

# Get data from the Queue (Consumer)
def func2(queue):
    while True:
        num = queue.get()
        print(f'Process ID: {os.getpid()}, get {num} from the queue')
        time.sleep(0.5)

if __name__ == '__main__':
    # Create a Queue
    queue = multiprocessing.Queue(10)
    # # Create a child process to put data to the Queue
    p1 = multiprocessing.Process(target=func1, args=(queue,))
    # Create a child process to get data from the Queue
    p2 = multiprocessing.Process(target=func2, args=(queue,))
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
    print('done')


    #The active block below use a Manager Queue with a Pool
    # queue = multiprocessing.Manager().Queue(50)
    # pool = multiprocessing.Pool(2)
    # pool.apply_async(func1, (queue,))
    # pool.apply_async(func2, (queue,))
    # pool.close()
    # # pool.join()
    # print('done')
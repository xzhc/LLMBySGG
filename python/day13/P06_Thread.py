"""
This case demonstrates the creation of thread objects
"""
import threading
import time

#Alternately print 00000 and 11111
def func():
    flag = 0
    while True:
        print(threading.current_thread().name, f'{flag}'* 5)
        flag = flag ^ 1
        time.sleep(0.5)

if __name__ == '__main__':
    # Create a thread object
    t1 = threading.Thread(target=func)
    # Create a thread object
    t2 = threading.Thread(target=func)
    # Start the thread
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('done')
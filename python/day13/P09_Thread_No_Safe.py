"""
This example demonstrates a thread safety issuse
"""
import threading
import time
def func():
    global g_num
    for _ in range(10):
        #1. read and calculate
        temp = g_num + 1
        # time.sleep(0.3)# If you uncomment this, the error becomes obvious!
        #2. write
        g_num = temp
        print(f"Current thread{threading.current_thread().name}:{g_num}")

if __name__ == '__main__':
    g_num = 0

    threads = [threading.Thread(target=func, name='Thread-'+str(i)) for i in range(10)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'Current thread{threading.current_thread().name}:{g_num}')
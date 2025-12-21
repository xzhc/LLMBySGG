"""
This example demonstrates a thread-safety issue.
"""
import time
import threading
def func1():
    global ticket_num
    while True:
        #Acquire lock
        lock.acquire()
        if ticket_num <= 0:
            #Release the lock
            lock.release()
            break
        time.sleep(5)
        ticket_num -= 1
        lock.release()
        print(f'{threading.current_thread().name} sold 1 ticket, {ticket_num} remaining')


if __name__ == '__main__':
    ticket_num = 100
    lock = threading.Lock()
    threads = [threading.Thread(target=func1, name='window' + str(i)) for  i in range(1,4)]
    [t.start() for t in threads]
    [t.join() for t in threads]
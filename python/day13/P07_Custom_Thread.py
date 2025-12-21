"""
This example demonstrates a custom thread class to create thread objects
"""

import threading
import time
"""
Python 3.13 (and possibly future versions) and happens because the threading.
Thread constructor now enforces that the group argument must be None (it's reserved for future use).
"""
class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name) # pass name as keyword argument
    def run(self):
        flag = 0
        while True:
            print(self.name, f'{flag}' * 5)
            flag = flag ^ 1
            time.sleep(0.5)

if __name__ == '__main__':
    # Create a thread object
    t1 = Worker('Thread-1')
    t2 = Worker('Thread-2')
    # Start the thread
    t1.start()
    t2.start()
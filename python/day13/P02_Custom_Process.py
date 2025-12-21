"""
This file demonstrates a custom process
"""

import multiprocessing
import os
class Worker(multiprocessing.Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(self)
        print(f'Current process ID: {os.getpid()}, Name: {self.name}, Parent process ID:{os.getppid()}')

if __name__ == '__main__':
    #create a procss
    for i in range(5):
        p = Worker(name=f'Process-{i}')
        p.start()
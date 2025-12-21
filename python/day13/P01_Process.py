"""
This case demonstrates reading and writing files via multiprocessing
"""

import time
import  multiprocessing
# Write data to a file
def write_file():
    with open('test.txt', 'a') as f:
        while True:
            f.write('hello world\n')
            #Manually flush the buffer
            f.flush()
            time.sleep(0.5)

#Read data from a file
def read_file():
    with open('test.txt', 'r') as f:
        while True:
            time.sleep(0.5)
            line = f.readline()
            print( line)

if __name__ == '__main__':
    # Create a child processes to write data to the file
    p1 = multiprocessing.Process(target=write_file)
    # Create a child processes to read data from the file
    p2 = multiprocessing.Process(target=read_file)
    p1.start()
    p2.start()
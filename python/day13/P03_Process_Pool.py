"""
This case demonstrates process pool in python
"""

import multiprocessing
import time

def square(x):
    time.sleep(1)
    return x * x

if __name__ == '__main__':
    #Create a process pool for parallel computation
    with multiprocessing.Pool(processes=4) as pool:
        #Use the map method to compute square of numbers
        results = pool.map(square, [1,2,3,4,5])
        print(results)

        #Asynchronous computation
        with multiprocessing.Pool(processes=4) as pool:
            async_result = pool.apply_async(square, (10,))
            print(async_result.get())




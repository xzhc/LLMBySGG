"""
This example demonstrates the Thread Pool
"""

import concurrent.futures

def func(tname):
    global word

    #Iterate over the word
    for i, char in enumerate(word):
        word[i] = chr(ord(char) ^ 1)
        print(f'{tname}:{word}\n', end='')

    return word

if __name__ == '__main__':
    # Initial encrypted string (as a list of characters)
    word = list("idmmn!vnsme")
    # Create a thread pool
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # Submit the task to the thread pool
        future1 = executor.submit(func, 'Thread-1')
        future2 = executor.submit(func, 'Thread-2')
        future3 = executor.submit(func, 'Thread-3')
        # Get the result

        word = future1.result()
        word = future2.result()
        word = future3.result()
        print("".join(word))
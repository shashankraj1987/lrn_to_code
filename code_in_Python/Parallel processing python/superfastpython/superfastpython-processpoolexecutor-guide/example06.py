# SuperFastPython.com
# example of calling map on a process pool with two iterables
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(value1, value2):
    # sleep for less than a second
    sleep(random())
    return (value1, value2)

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit all tasks
        for result in executor.map(task, ['1', '2', '3'], ['a', 'b', 'c']):
            print(result)

if __name__ == '__main__':
    main()

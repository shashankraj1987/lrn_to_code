# SuperFastPython.com
# example of the map and wait pattern for the ProcessPoolExecutor
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    return name

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # execute tasks concurrently and process results in order
        for result in executor.map(task, range(10)):
            # retrieve the result
            print(result)

if __name__ == '__main__':
    main()

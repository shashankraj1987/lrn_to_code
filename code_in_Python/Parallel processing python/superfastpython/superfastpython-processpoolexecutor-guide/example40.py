# SuperFastPython.com
# example of calling map with a function call
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(value):
    # sleep for less than a second
    sleep(random())
    return value

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit all tasks
        for result in executor.map(task(), range(5)):
            print(result)

if __name__ == '__main__':
    main()
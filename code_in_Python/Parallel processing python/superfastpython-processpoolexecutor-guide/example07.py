# SuperFastPython.com
# example of calling map on the process pool and not iterating the results
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(value):
    # sleep for less than a second
    sleep(random())
    print(f'Done: {value}')
    return value

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit all tasks
        executor.map(task, range(5))
    print('All done!')

if __name__ == '__main__':
    main()

# SuperFastPython.com
# example of an exception in a process pool initializer function
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# function for initializing the worker process
def initializer_worker():
    # throws an exception
    raise Exception('Something bad happened!', flush=True)

# a mock task that sleeps for a random amount of time less than one second
def task(identifier):
    sleep(random())
    # get the unique name
    return identifier

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor(max_workers=2, initializer=initializer_worker) as executor:
        # execute tasks
        for result in executor.map(task, range(10)):
            print(result)

if __name__ == '__main__':
    main()

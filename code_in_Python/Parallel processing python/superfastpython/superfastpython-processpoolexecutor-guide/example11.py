# SuperFastPython.com
# example of the submit and use multiple callbacks for the ProcessPoolExecutor
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    return name

# custom callback function called on tasks when they complete
def custom_callback1(future):
    # retrieve the result
    print(f'Callback 1: {future.result()}')

# custom callback function called on tasks when they complete
def custom_callback2(future):
    # retrieve the result
    print(f'Callback 2: {future.result()}')

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # register the callbacks on all tasks
        for future in futures:
            future.add_done_callback(custom_callback1)
            future.add_done_callback(custom_callback2)
        # wait for tasks to complete...

if __name__ == '__main__':
    main()

# SuperFastPython.com
# example of the submit and use a callback pattern for the ProcessPoolExecutor
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    return name

# custom callback function called on tasks when they complete
def custom_callback(future):
    # retrieve the result
    print(future.result())

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # register the callback on all tasks
        for future in futures:
            future.add_done_callback(custom_callback)
        # wait for tasks to complete...

if __name__ == '__main__':
    main()

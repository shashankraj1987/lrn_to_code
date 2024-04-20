# SuperFastPython.com
# example of the submit and use sequentially pattern for the ProcessPoolExecutor
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
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # process task results in the order they were submitted
        for future in futures:
            # retrieve the result
            print(future.result())

if __name__ == '__main__':
    main()

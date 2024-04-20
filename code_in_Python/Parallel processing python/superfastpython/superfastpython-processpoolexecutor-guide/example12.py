# SuperFastPython.com
# example of the submit and wait for all pattern for the ProcessPoolExecutor
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait

# custom task that will sleep for a variable amount of time
def task(name):
    # sleep for less than a second
    sleep(random())
    # display the result
    print(name)

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        # submit tasks and collect futures
        futures = [executor.submit(task, i) for i in range(10)]
        # wait for all tasks to complete
        wait(futures)
    print('All tasks are done!')

if __name__ == '__main__':
    main()

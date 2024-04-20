# SuperFastPython.com
# example of not having a check for the main top-level environment
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a variable amount of time
def task(value):
    # sleep for less than a second
    sleep(random())
    return value

# start the process pool
with ProcessPoolExecutor() as executor:
    # submit all tasks
    for result in executor.map(task, range(5)):
        print(result)

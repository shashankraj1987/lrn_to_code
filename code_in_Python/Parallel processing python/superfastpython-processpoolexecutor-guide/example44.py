# SuperFastPython.com
# example of not flushing output when call print() from tasks in new processes
from time import sleep
from random import random
from concurrent.futures import ProcessPoolExecutor

# custom task that will sleep for a moment
def task(value):
    sleep(value)
    print(f'Done: {value}')

# entry point
def main():
    # start the process pool
    with ProcessPoolExecutor() as executor:
        executor.map(task, range(5))
    print('All done!')

if __name__ == '__main__':
    main()

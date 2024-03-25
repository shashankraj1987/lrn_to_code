# SuperFastPython.com
# set a timeout when getting results from a future
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import TimeoutError

# mock task that will sleep for a moment
def work():
    sleep(1)
    return "all done"

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # start one process
        future = executor.submit(work)
        # get the result from the task, wait for task to complete
        try:
            result = future.result(timeout=0.5)
            print(f'Got Result: {result}')
        except TimeoutError:
            print('Gave up waiting for a result')

if __name__ == '__main__':
    main()

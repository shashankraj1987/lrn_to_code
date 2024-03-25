# SuperFastPython.com
# get the result from a completed future task
from time import sleep
from concurrent.futures import ProcessPoolExecutor

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
        result = future.result()
        print(f'Got Result: {result}')

if __name__ == '__main__':
    main()

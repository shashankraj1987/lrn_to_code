# SuperFastPython.com
# check the status of a Future object for task executed by a process pool
from time import sleep
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import wait

# mock task that will sleep for a moment
def work():
    sleep(0.5)

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # start one process
        future = executor.submit(work)
        # confirm that the task is running
        running = future.running()
        done = future.done()
        print(f'Future running={running}, done={done}')
        # wait for the task to complete
        wait([future])
        # confirm that the task is done
        running = future.running()
        done = future.done()
        print(f'Future running={running}, done={done}')

if __name__ == '__main__':
    main()

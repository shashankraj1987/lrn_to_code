# SuperFastPython.com
# example of the wrong signature on the callback function
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# callback function to call when a task is completed
def custom_callback():
    print('Custom callback was called', flush=True)

# mock task that will sleep for a moment
def work():
    sleep(1)
    return 'Task is done'

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # execute the task
        future = executor.submit(work)
        # add the custom callback
        future.add_done_callback(custom_callback)
        # get the result
        result = future.result()
        print(result)

if __name__ == '__main__':
    main()

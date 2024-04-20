# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# mock task that will sleep for a moment
def work():
    sleep(1)
    try:
        raise Exception('Something bad happened!')
    except Exception:
        return 'Unable to get the result'
    return "never gets here"

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # execute our task
        future = executor.submit(work)
        # get the result from the task
        result = future.result()
        print(result)

if __name__ == '__main__':
    main()

# SuperFastPython.com
# example of handling an exception raised within a task
from time import sleep
from concurrent.futures import ProcessPoolExecutor

# mock task that will sleep for a moment
def work(value):
    sleep(1)
    raise Exception('Something bad happened!')
    return f'Never gets here {value}'

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # execute our task
        for result in executor.map(work, [1]):
            print(result)

if __name__ == '__main__':
    main()

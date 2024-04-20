# SuperFastPython.com
# configure and report the default number of worker processes
from concurrent.futures import ProcessPoolExecutor

# entry point
def main():
    # create a process pool with a large number of worker processes
    pool = ProcessPoolExecutor(60)
    # report the number of worker processes
    print(pool._max_workers)

if __name__ == '__main__':
    main()

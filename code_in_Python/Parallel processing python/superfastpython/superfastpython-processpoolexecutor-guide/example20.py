# SuperFastPython.com
# example of setting the process start context
from multiprocessing import get_context
from concurrent.futures import ProcessPoolExecutor

# entry point
def main():
    # create a start process context
    context = get_context('fork')
    # create a process pool
    with ProcessPoolExecutor(mp_context=context) as executor:
        # report the context used
        print(executor._mp_context)

if __name__ == '__main__':
    main()

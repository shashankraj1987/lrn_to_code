# SuperFastPython.com
# example of checking the process start context
from concurrent.futures import ProcessPoolExecutor

# entry point
def main():
    # create a process pool
    with ProcessPoolExecutor() as executor:
        # report the context used
        print(executor._mp_context)

if __name__ == '__main__':
    main()
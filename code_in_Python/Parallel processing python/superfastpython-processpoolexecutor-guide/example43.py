# SuperFastPython.com
# example of an argument that does not pickle
from concurrent.futures import ProcessPoolExecutor

# write to a file
def work(file):
    file.write('hi there')
    return "All done!"

# entry point
def main():
    # submit the task
    with open('tmp.txt', 'w') as file:
        # start the process pool
        with ProcessPoolExecutor() as executor:
            # submit the task
            future = executor.submit(work, file)
            # get the result
            result = future.result()
            print(result)

if __name__ == '__main__':
    main()

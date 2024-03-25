# SuperFastPython.com
# example of a parallel for loop with the Thread class
from threading import Thread

# execute a task
def task(value):
    # add your work here...
    # ...
    # all done
    [x**2 for x in range(value)]
    # print(f'.done {value}')

# protect the entry point
if __name__ == '__main__':
    # create all tasks
    print("Thread Started")
    threads = [Thread(target=task, args=(i,)) for i in range(20000)]
    # start all threads
    for thread in threads:
        thread.start()
    # wait for all threads to complete
    for thread in threads:
        thread.join()
    # report that all tasks are completed
    print('Done')

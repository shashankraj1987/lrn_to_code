import asyncio
from asyncio import sleep
import numpy as np


async def func_sleep(tmr: int) -> bool:
    sleep_timer = np.random.random()*tmr
    print("Will Sleep for ", sleep_timer)
    try:
        await sleep(sleep_timer)
    except Exception as e:
        print(e)
        return False
    else:
        return True


async def basic_main():
    # Functions will be run, one by one. Error can be handled manually, slow process.
    print(" ********** Inside main coroutine ********** ")
    task1 = func_sleep(np.random.randint(0, 5))
    task2 = func_sleep(np.random.randint(0, 5))
    await task1
    await task2
    print("Main Coroutine finished.")


async def async_with_gather():
    # Functions will run all at once.
    # Errors will not be handled, fast process.
    print(" ********** Using Gather ********** ")
    await asyncio.gather(*(func_sleep(x) for x in range(10)))
    print("Main Coroutine finished.")


async def async_task_grp():
    print(" ********** Using Task Group ********** ")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for x in range(10):
            task = tg.create_task(func_sleep(x))
            tasks.append(task)

    results = [task.result() for task in tasks]
    for x in results:
        print("Result received", x)


if __name__ == "__main__":
    # Note: We need to run this in a new event loop as the first function will finish in the main event loop.
    # Then second will start and first will not be awaited.
    # The other option would be to create a function which will wrap the other functions, in async
    # Then run that function.

    loop = asyncio.new_event_loop()

    loop.run_until_complete(basic_main())
    loop.run_until_complete(async_with_gather())
    loop.run_until_complete(async_task_grp())

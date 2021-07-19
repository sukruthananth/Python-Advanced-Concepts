import asyncio
import time
async def first_function():
    print('First function has started')
    await asyncio.sleep(1)
    print('First is still running')
    await asyncio.sleep(1)
    print('first done')
    return 'wow'

async def second_function():
    print('second has started')
    await asyncio.sleep(0.5)
    print('still second')
    await asyncio.sleep(1)
    print('second done')
    return 'second'

async def main():
    task1 = asyncio.create_task(first_function())
    task2 = asyncio.create_task(second_function())

    value1 = await task2
    # val2 = await task2
    # print(value1, val2)

asyncio.run(main())
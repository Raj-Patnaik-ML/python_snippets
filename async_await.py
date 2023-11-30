import asyncio
import time


async def task1(name):
    await asyncio.sleep(1)
    return 'Hi {}, task 1 done'.format(name)


async def task2(name):
    await asyncio.sleep(2)
    return 'Hi {}, task 2 done'.format(name)


async def main():
    # Method 1
    sc_task1 = asyncio.create_task(task1('name'))
    sc_task2 = asyncio.create_task(task2('name'))
    res1 = await sc_task1
    res2 = await sc_task2
    print(res1, res2, sep='\n')

    # Method 2
    # x = task1('1')
    # y = task2('2')
    # task_result_list = await asyncio.gather(x, y)
    # print(*task_result_list, sep='\n')

t1 = time.time()
print('Time Start: {}'.format(t1))
asyncio.run(main(), debug=True)
# main()
t2 = time.time()
print('Time End: {}'.format(t2))
print('\nTime Taken: {}'.format(t2 - t1))

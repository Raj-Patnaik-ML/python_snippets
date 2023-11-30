import asyncio
import threading
import time


def fetch_data_from_api(arg1, result):
    time.sleep(2)
    result['data'] = arg1


def normal_function():
    # Do some synchronous work here
    print("Normal function is doing something...")
    result = dict()
    t1 = threading.Thread(target=fetch_data_from_api, args=('new data', result))
    t1.start()
    # Continue with synchronous work
    print("Normal function is done with concurrant data: ", end='')
    # get result

    t1.join()
    print(result['data'])


# Call the normal function
normal_function()

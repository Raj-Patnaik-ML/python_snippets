import threading
import time


def th_func1():
    print('Th 1 start')
    print('Th 1 sleep start...')
    with threading.Lock():
        time.sleep(1)

    print('Th 1 sleep done')
    print('Th 1 end')


def th_func2():
    print('Th 2 start')
    print('Th 2 sleep start...')
    with threading.Lock():
        time.sleep(1)
    print('Th 2 sleep done')
    print('Th 2 end')


if __name__ == '__main__':
    print('Main start')
    t1 = threading.Thread(target=th_func1, daemon=True)
    t1.start()

    t2 = threading.Thread(target=th_func2, daemon=True)
    t2.start()

    t2.join()
    t1.join()
    print('Main end')

import threading
import time


def th_func1(result):
    print('Th 1 start')
    print('Th 1 Sleep...')
    time.sleep(3)
    print('Th 1 Sleep done')
    print('Th 1 end')


def th_func2(result):
    print('Th 2 start')
    # print('Th 2 Sleep...')
    # time.sleep(1)
    # print('Th 2 Sleep done')
    while result[2] < 90:
        # call the api
        # res = get_request(url)
        # sleep(1)
        # result[2] = res
        # django_cache = res
        pass
    print('doing operation')
    print('Th 2 end')


if __name__ == '__main__':
    parser_result = {
        1: None,
        2: None
    }
    print('Main start')
    t1 = threading.Thread(target=th_func1, args=(parser_result,), daemon=True)
    t1.start()

    t2 = threading.Thread(target=th_func2, args=(parser_result,), daemon=True)
    t2.start()

    # t2.join()
    # t1.join()
    print('Main end')

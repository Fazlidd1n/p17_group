import multiprocessing
import os
import time


def a(num):
    time.sleep(2)
    print(f"{num} {os.getpid()}")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=a, args=(2,))
    p2 = multiprocessing.Process(target=a, args=(10,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

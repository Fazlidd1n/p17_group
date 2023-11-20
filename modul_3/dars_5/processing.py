import multiprocessing
import os
import time


def a(num):
    time.sleep(2)
    print(f"{num} {os.getgid()}")


# with multiprocessing.Pool(8) as p:
#     p.map(a, [1, 2, 3, 4, 5, 6, 7, 8])

# p1 = multiprocessing.Process(target=a,args=(2,))
# p2 = multiprocessing.Process(target=a,args=(10,))

if __name__ == '__main__':
    with multiprocessing.Pool(100) as p:
        p.map(a, range(1,100))

    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

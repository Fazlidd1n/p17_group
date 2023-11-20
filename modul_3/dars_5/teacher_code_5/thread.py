# import time
#
#
# def a():
#     time.sleep(1)
#
# start = time.time()
# for i in range(10):
#     a()
# print(time.time() - start)


# import threading
# import time
#
#
# def a():
#
#     time.sleep(5)
#     print("a")
# def b():
#
#     time.sleep(6)
#     print("b")
#
# start = time.time()
# # a()
# # b()
# t1 = threading.Thread(target=a)
# t2 = threading.Thread(target=b)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(time.time() - start)
# import os
# import threading
# import time
#
#
# def a(num1):
#     time.sleep(2)
#     print(os.getpid())
#
#
# start = time.time()
# l = [1,2,3]
# threads = []
# for i in l:
#     t = threading.Thread(target=a , args=(i,))
#     t.start()
#     threads.append(t)
#
# for i in threads:
#     i.join()
# print(time.time() - start)





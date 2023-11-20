# async - asyncio
# import time, asyncio


# async def task1():
#     print("task1 start")
#     await asyncio.sleep(1)
#     print("task1 finish")
#
#
# async def task2():
#     print("task2 start")
#     await asyncio.sleep(1)
#     print("task2 finish")
#
#
# async def main():
#     task_1 = asyncio.create_task(task1())
#     task_2 = asyncio.create_task(task2())
#     await task_1
#     await task_2
#     print("main start")
#     await asyncio.sleep(1)
#     print("main finish")
#
#
# start = time.time()
# asyncio.run(main())
# print(time.time() - start)


import time, asyncio, requests
# async def send():
#     urls = [
#         'https://www.example.com',
#         'https://www.google.com',
#         'https://www.github.com'
#     ]
#     s=[]
#     for url in urls:
#         s.append(requests.get(url).text)
#     for i in s:
#         print(len(i))
#
# start = time.time()
# asyncio.run(send())
# print(time.time()-start)


# import aiofiles
#
# async def main():
#     async with aiofiles.open("users.txt",mode="w") as f:
#         data = await f.write("fasfnjndndf")
# asyncio.run(main())


# async def range(n):
#     c=0
#     while c<n:
#         yield c
#         c+=1
#
# async def main():
#     async for i in range(10):
#         print(i,end=" ")
# asyncio.run(main())
#
#
# import aiohttp
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         data = await session.get("https://www.example.com")
#         print(data.text)

# async - asyncio

# main thread
# import time
#
#
# def a():
#     time.sleep(1)
# def b():
#     time.sleep(2)
#
# def c():
#     time.sleep(1)
# a()
# b()
# c()

# import time
# import asyncio
#
# async def task1():
#     print("task1 start")
#     await asyncio.sleep(2)
#     print("task1 finish")
#
# async def task2():
#     print("task2 start")
#     await asyncio.sleep(1)
#     print("task2 finish")
#
# async def main():
#     task1_var = asyncio.create_task(task1())
#     task2_var = asyncio.create_task(task2())
    # await task1_var
    # await task2_var
#     print("function start")
#     await asyncio.sleep(1)
#     print("function finish")
#
# start = time.time()
# asyncio.run(main())
# print(time.time() - start)
# import asyncio
# import time
#
# import requests
#
#
# def response(url):
#     data = requests.get(url)
#     return data.text
#
# start = time.time()
# print(len(response("https://www.example.com")))
# print(len(response("https://www.google.com")))
# print(len(response("https://www.github.com")))
# print(time.time()- start)
#


"""
async def main():
    urls = [
        'https://www.example.com',
        'https://www.google.com',
        'https://www.github.com'
    ]
    l = []
    for i in urls:
        l.append(asyncio.create_task(response(i)))
    for i in l:
        res = await i
        print(len(res))

start = time.time()
asyncio.run(main())
print(time.time()- start)
"""
# import asyncio
# import json
#
# import aiofiles
#
# async def main():
#     async with aiofiles.open("text.txt", "r") as f:
#         data = await f.read()
#     return data
# if __name__ == '__main__':
#     print(asyncio.run(main()))


# import asyncio
#
# async def range(n):
#     c = 0
#     while c< n:
#         yield c
#         c += 1
#
# async def main():
#     async for i in range(10):
#         print(i)
# asyncio.run(main())


# import asyncio
#
# import aiohttp
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         data = await session.get("https://www.example.com")
#         print(data.text)
#
# asyncio.run(main())
import asyncio
import json

import aiofiles


async def main():
    async with aiofiles.open("test.json" , "w") as f:
        data = json.dumps([1,2,3] , indent=3)
        await f.write(data)

asyncio.run(main())
























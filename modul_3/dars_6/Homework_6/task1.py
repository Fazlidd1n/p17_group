# import asyncio
# import json
# import time
# import requests
#
# async def send(url: str):
#     with open(url + ".json", "w") as f:
#         url = requests.get("https://jsonplaceholder.typicode.com/" + url)
#         json.dump(url.json(), f, indent=3)
#         print(f"{url} save ✅")
#         # f.write(data)
#
#
#
# async def rangee(l:list):
#     for i in l:
#         yield i
#
# async def main():
#     data = ["todos", "users", "photos", "albums", "posts", "comments"]
#     async for url in rangee(data):
#         time.sleep(1)
#         await send(url)
# start = time.time()
# asyncio.run(main())
# print(time.time() - start)

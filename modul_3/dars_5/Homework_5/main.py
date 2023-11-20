# multiprocessing
# import json, requests, multiprocessing, time
#
#
# def save_data(li: str):
#     link = "https://jsonplaceholder.typicode.com/"
#     data = requests.get(link + li)
#     with open(li + ".json", "w") as f:
#         json.dump(data.json(), f, indent=3)
#         print(f"{li} save ✅")

# start = time.time()
# a = ["todos", "users", "photos", "albums", "posts", "comments"]
# for i in a:
#     save_data(i)
# print(time.time() - start)
#
# if __name__ == '__main__':
#     start = time.time()
#     with multiprocessing.Pool(6) as p:
#         p.map(save_data, ["todos", "users", "photos", "albums", "posts", "comments"])
#     print(time.time() - start)






# threading
# import requests,time,json,threading
#
# def create_json(li, ):
#     link = "https://jsonplaceholder.typicode.com/"
#     data = requests.get(link + li)
#     with open(li + ".json", 'w') as f:
#         json.dump(data.json(), f, indent=3)
#     print(li,"save ✅")
#
# a = ["todos", "users", "photos", "albums", "posts", "comments"]
# theads = []
# start = time.time()
# for i in a:
#     # create_json(i)
#     t = threading.Thread(target=create_json, args=(i,))
#     t.start()
#     theads.append(t)
#
# for i in theads:
#     i.join()
# print(time.time() - start)

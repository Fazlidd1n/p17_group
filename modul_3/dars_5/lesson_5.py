import json

import requests

#
# """
# get
# put
# patch
# delete
# post1
# """
#
#
data = requests.get("https://jsonplaceholder.typicode.com/users")

with open("users.json", "w") as f:
    l = []
    for i in data.json():
        l.append(i)
    json.dump(l, f, indent=3)

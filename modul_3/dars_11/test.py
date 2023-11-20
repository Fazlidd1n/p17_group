# pathlib , join
import pathlib
from os.path import join
import os

# BASE_PATH = pathlib.Path(__file__).parent.parent.parent

# with open(f"{BASE_PATH}/module_3/exam/exam_test.py")
# print(join(BASE_PATH,"module_3","exam","exam_test.py"))
# dir_list = ["p17_group","exam"]
# path = pathlib.Path(join(BASE_PATH,*dir_list))
# print(path.parts)
# print(os.chdir(".."))
# print(os.listdir())

s1 = 0
s2 = 0
BASE_PATH = pathlib.Path(__file__).parent.parent.parent
for i in os.listdir(BASE_PATH):
    path = BASE_PATH.joinpath(i)
    if BASE_PATH.is_dir() and not i.startswith("."):
        s1 += 1
    if BASE_PATH.is_file():
        s2 += 1
print(f"papka : {s1}")
print(f"fayl : {s2}")


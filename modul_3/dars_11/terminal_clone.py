import os
import pathlib
from zipfile import ZipFile

Bath_Path = pathlib.Path(__file__).parent.parent.parent
os.chdir(Bath_Path)
while True:
    command_value = input(f"{os.getcwd()} $ ").split()
    if command_value[0] == "cd":
        os.chdir(command_value[1])

    if command_value[0] == "mkdir":
        os.mkdir(command_value[1])

    if command_value[0] == "ls":
        for i in os.listdir():
            if not i.startswith("."):
                print(i, end="  ")
        print()

    if command_value[0] == "zip":
        with ZipFile(command_value[1], "w") as zip:
            for i in os.listdir(Bath_Path.joinpath(command_value[2])):
                zip.write(f"{command_value[2]}/{i}")

    # if command_value[0] == "unzip":
    #     with ZipFile(command_value[1], "r") as zip:
    #         print("Extracting all the files now ...")
    #         zip.extractall()
    #         print("Done ✅")

    if command_value[0] == "exit":
        break
